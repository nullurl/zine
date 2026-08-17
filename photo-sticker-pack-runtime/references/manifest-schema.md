# Manifest Schema

`manifest.json` is version 1 and the only resume state. Import `new_manifest`, `load_manifest`, `save_manifest`, and `validate_manifest` from `manifest_utils.py`; it is not a command-line program. Save every change atomically: call `save_manifest` on a sibling temporary path, then use `os.replace` to replace `manifest.json`.

| Field | Rule |
| --- | --- |
| `version` | Must be `1` |
| `default_color` | Must be `#2E429B` |
| `status` | Pack status: `planned`, `generating`, `generated`, `processed`, `complete`, or `failed` |
| `source_path` | Original photo path only; never copy the photo into the pack |
| `subject` | Visible-feature profile used consistently for all character items |
| `items` | Exactly eight ordered item objects |

Each item has `id`, `kind`, `action`, `accessory`, `expression`, `caption`, and `prompt`; the manifest helper adds deterministic `raw_path`, `ink_mask_path`, `white_mask_path`, `svg_path`, and `png_path` from its id and kind. All output paths are relative to the pack directory. It also adds `status`, `representation`, `retry_count`, and `error`.

All five stored paths are assertions, not authority. For every read or write, derive the canonical path again from item `id` and `kind`; require an exact match, reject aliases/case-fold collisions/resolved-file collisions/cross-item hardlinks, reject any existing regular artifact whose link count is not exactly one (including an untracked outside hardlink), and reject every symlinked path component. The deterministic pre-chroma staging path is `work/NN-kind-imagegen-staged.png`.

`representation` is `path` for a vector-path SVG, `mask` for a lossless recolorable mask SVG, or `null` before vectorization. `retry_count` records the one shared Image Gen retry across generation and quality failures. `error` is a human-readable failure string or `null`.

## Item state transitions

The successful per-item path is `planned -> generating -> generated -> processed -> complete`. Set `generating` and atomically save immediately before the built-in tool call. Chroma removal leaves the row in `generating`; set `generated` only after the canonical valid raw also passes the generation-time quality gate, then clear `error`. Set `processed` only after masks, canonical SVG, canonical 1024×1024 PNG, and `representation` exist. Set `complete` only after its fields and artifacts have been checked.

In high-quality fast mode, the coordinator may normalize up to eight initial `generate` rows in one atomic manifest save and issue their independent full-resolution tool calls in one concurrent batch. Artifact workers never write `manifest.json`. Successful calls are staged once and never repeated; only failed calls may be retried in the largest supported concurrent batch. After bounded local workers finish, the coordinator reloads the authoritative manifest and persists `generated`, `processed`, and `complete` in order for each successful row. A failed worker leaves its row at the last safe state. The coordinator may reserve several eligible one-time retries before sending the authorized Image Gen calls together, but each retry keeps its own token and uses the item-wise chroma, raw-ready, gate, and terminal state transitions below.

The optional content-addressed raw-art cache is outside the candidate and pack. Its key covers the source bytes, style bytes, visible subject features, and text-free visual brief, but not `caption`. Only a valid normalized raw image that passes the generation-time quality gate may be stored. A cache restore writes a byte copy to the canonical candidate raw path; the normal `gate -> process -> finalize` path then revalidates it. Cache state is never manifest authority.

Generation and quality failures share one retry budget. Call `resume_utils.reserve_retry` before either retry: it accepts failure `generation` (reason `tool_failure` or `chroma_failure`) or `quality_gate` (the gate's ordered reasons). A candidate-scoped retry lock serializes the authoritative manifest reload and all reservation writes. The regular single-link lock is a persistent sibling outside the candidate, making it crash-reusable without ever bundling or promoting it. Under the lock, the helper validates candidate-only canonical path/symlink/hardlink safety and saves the exact recorded quarantine paths plus a strong unguessable reservation token as structured reservation metadata. It then atomically increments `retry_count` to 1, sets status `failed`, and records the explicit retry-reservation phase `invalidation_in_progress` before quarantining. While in that phase it quarantines the old canonical raw and staged artifacts. After both invalidations succeed it atomically advances the phase to `authorized`, sets status `generating`, and only then returns `True`; the successful caller reloads and retains the persisted token. An invalidation failure atomically keeps count 1 and status `failed`, records `{"retry_invalidation":["unsafe_artifact"]}`, returns `False`, and does not authorize Image Gen. A crash during either quarantine preserves the fail-closed in-progress marker: interrupted invalidation resumes as `fail` whether all, some, or none of the stale artifacts remain. Once the budget is spent, later reservation calls return `False` with no authorization and no state mutation. Only `generate` or a successful `reserve_retry` reservation may call `image_gen`.

For crash recovery, an `authorized` reserved valid retry stage takes precedence over a stale raw and resumes as `chroma`. This exception requires the explicit active-reservation tuple `status="generating"`, `retry_count==1`, and exact retry-reservation JSON with phase `authorized`, failure `generation` or `quality_gate`, nonempty reasons, and recorded quarantine paths. Without that tuple, raw retains normal precedence, so an arbitrary first-attempt stage cannot loop. The `invalidation_in_progress` phase is terminal recovery and takes precedence over every surviving or partially invalidated artifact. With no genuinely new valid staged result, an `authorized` spent reservation resumes as `fail` and cannot call Image Gen again.

Calling `resume_utils.mark_retry_raw_ready(CANDIDATE_MANIFEST, row_id)` is mandatory after retry chroma. Under the same candidate-scoped retry lock, it reloads the manifest, requires the exact active `authorized` reservation, verifies the canonical retry raw, securely removes the retry quarantines and staged image using only the recorded quarantine paths, and persists phase `raw_ready`. It then removes the empty `.retry-quarantine` directory only after proving it is the exact real in-candidate directory with no unexpected residue. Removing the stage alone is not a progress transition. After the helper returns `True`, rerun resume: `raw_ready` plus valid raw returns `gate` even if the stage remains after an interruption; `raw_ready` without valid raw returns `fail`. A crash before the phase advance leaves `authorized` plus the stage, so chroma removal is idempotently repeated before the mandatory helper call. Reject an unexpected, nonempty, symlinked, or hardlinked cleanup target and fail closed.

Only the token owner may terminalize an actual reserved generation, chroma, or quality failure. Call `resume_utils.fail_reserved_retry(CANDIDATE_MANIFEST, row_id, token, failure, reasons)`; it reloads under the same lock and requires the exact item id, active `authorized` or `raw_ready` phase, count 1, and reservation token. It atomically writes terminal failure once. Wrong, stale, cross-item, and replayed tokens return `False` without mutation. A crash/resume `fail` decision may terminalize a known actual retry failure with the verified persisted token and phase, never with a duplicate reservation call. Require no retry quarantine directory or files before promotion, and therefore no retry quarantine files before promotion; the persistent lock stays outside the candidate and therefore cannot enter the promoted pack.

`validate_pack.py` requires every item to be `complete`; run it as the all-eight final check, then and only then set the pack status to `complete`. A `failed` or incomplete item means the pack remains incomplete and must not be represented as a completed gallery or ZIP.

## Resume and replacement

Run `resume_utils.py PACK_DIR --allow-new` before creating a new timestamped directory. `fresh/items=[]` is legal only when the root, candidate, backup, and all three manifest paths are absent. If any of those paths exists but is missing required state, symlinked, nonregular, unreadable, malformed, or awaiting backup/transaction recovery, the helper exits with `recovery required`; it must never downgrade that state to fresh. Candidate manifest precedence is deterministic for a `resume` result.

On `fresh/items=[]`, create the candidate directory and all eight planned rows with `new_manifest`, atomically save the new candidate manifest through a sibling temporary and `os.replace`, then rerun `resume_utils.py PACK_DIR` without `--allow-new`. Require the second result to be `resume` and consume exactly eight returned decisions before entering the action loop. If backup or transaction recovery changes which root/candidate exists, always rerun the helper after any backup or transaction recovery and discard the earlier result. Only `generate` or a successful `reserve_retry` reservation may call `image_gen`.

For every existing row use this state table; inspect recoverable canonical artifacts even when the stored status is `planned` or `failed`:

| Valid recoverable state | Decision |
| --- | --- |
| Status `complete` plus valid matching SVG+PNG | `skip` |
| Any other status plus valid matching SVG+PNG | `finalize` |
| Valid transparent canonical raw PNG with status `generating`, `planned`, or `failed` | `gate` |
| Valid transparent canonical raw PNG with status `generated`, `processed`, or `complete` | `process` |
| Valid 1024x1024 RGB/RGBA imagegen stage with opaque flat key-green corners/border and nontrivial non-key subject coverage | `chroma` |
| No valid prerequisite and `retry_count < 1` | `generate` |
| No valid prerequisite and retry budget already spent | `fail` |

An invalid advanced artifact falls back to the next valid prerequisite in that order. The helper is read-only and never overwrites a valid actual root.

Execute each decision with this exact normalization table. Atomically save a non-null normalization before the operation and the success status afterward:

| Decision | Normalize status | Operation | Success status |
| --- | --- | --- | --- |
| `skip` | no status change | no operation | no status change |
| `chroma` | `generating` | `remove_chroma_key` | `generating` |
| `gate` | `generating` | generation-time quality gate | `generated` |
| `fail` | `failed` | no operation | no status change |
| `process` | `generated` | postprocess and vectorize | `processed` |
| `finalize` | `processed` | verify | `complete` |
| `generate` | `generating` | `image_gen` | `generating` |

Build a sibling candidate-pack mirror before every first run, resume, or replacement. The candidate has its own manifest and identical relative output paths; it must use byte copies, never symlinks. If an existing candidate manifest is present, resume it before mirroring again and preserve its complete rows. Otherwise, byte-copy the existing root pack, or create a new candidate manifest for a first run. Make only candidate-state changes until the public validator accepts the complete candidate.

After candidate validation, atomically set candidate pack status to `complete`, then let `build_gallery.py` validate and stage new HTML/ZIP siblings in unpredictable exclusive temporary files before atomically replacing candidate derivatives. Never pre-delete `index.html` or `stickers-default-blue.zip`; a staging or validation failure preserves their prior bytes. Require both final derivatives to exist and all builder-created temporary files to be cleaned before promotion. A derivative failure leaves the root unchanged and the complete candidate resumable; the next candidate-first invocation rebuilds only derivatives.

Replace the whole root directory as one same-filesystem transaction only after the complete candidate and fresh derivatives are ready. For an existing root, move it to a sibling backup directory, promote the candidate directory, validate the promoted root, verify pack status and final derivatives, then remove the backup. If a rename or post-promotion verification fails, move aside the failed promoted root and restore the backup. If candidate work fails, leave every existing root output and completed row unchanged.

Load the existing manifest before resuming and follow the helper decision instead of status alone. If a processing step fails, leave the prior valid SVG and PNG untouched and set the affected candidate item to `failed` with its error. Build a candidate-only incomplete `index.html` with missing cards and `complete=false`, remove no published-root derivative, and create no ZIP.

For one requested item, regenerate only that item, then revalidate all eight. Preserve all non-target raw files, masks, SVGs, PNGs, and their bytes unchanged. Rebuild only shared derivatives that must change: `stickers-default-blue.zip` and `index.html`.
