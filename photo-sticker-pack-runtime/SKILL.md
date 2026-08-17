---
name: 照片贴纸包
description: "【照片贴纸包 / photo-sticker-pack-runtime】 Use when a user asks to turn an uploaded or local photo into exactly eight personalized classic blue-and-white line-art stickers, reaction stickers, photo-derived decals, a recolorable SVG sticker pack, a downloadable offline sticker HTML page, or optional macOS desktop stickers, including single-sticker regeneration or post-generation color switching."
---

# Photo Sticker Pack

Create an eight-sticker pack without pre-generation preference questions. Deliver a completed gallery only after all eight items validate; a terminal item failure instead gets an explicitly incomplete candidate preview.

## First-run guidance

Keep onboarding progressive. On the first photo request, start automatically and send only three useful progress milestones: `已识别主角，正在规划 8 张贴纸`, `正在生成贴纸：N / 8`, and `正在整理透明 PNG、SVG 和画廊`. Never introduce StickerDesk before the user selects or asks for desktop stickers; ordinary generation, recoloring, PNG, SVG, and gallery use need no helper.

After completion, lead with the gallery link and one sentence: click a sticker to peel and download PNG, and use the upper-right blue dot to change color. Mention the optional Mac desktop mode only after this core action. When a user asks to enable desktop stickers on macOS, use `desktop-helper/install.sh` with an explicit destination under their user Applications directory, request any required external-write or app-launch approval, and then report the confirmed installed path. Do not make users run the compiler command manually when the installer can do it.

## Resolve resources and state

Set `SKILL_DIR` to the absolute directory that contains this loaded `SKILL.md`; never infer it from the current working directory. Resolve every asset, reference, and script from it, for example `STYLE_REFERENCE="$SKILL_DIR/assets/style-reference.webp"` and `POSTPROCESS="$SKILL_DIR/scripts/postprocess_sticker.py"`. Create an absolute `PACK_DIR` outside the Skill folder as `sticker-pack-YYYYMMDD-HHMMSS/`.

Read `$SKILL_DIR/references/style-guide.md` before prompts, `$SKILL_DIR/references/content-planning.md` before planning, and `$SKILL_DIR/references/manifest-schema.md` before resuming. Use `$STYLE_REFERENCE` as style-only input; never copy its people, words, or brand.

`manifest_utils.py` is an import module, not a CLI. Import only its existing functions: `new_manifest`, `load_manifest`, `save_manifest`, and `validate_manifest`. Persist each transition atomically by saving to a sibling temporary manifest with `save_manifest`, then replacing `manifest.json` with `os.replace`; do this after every state change.

Set `CANDIDATE_DIR="${PACK_DIR}.candidate"` and `BACKUP_DIR="${PACK_DIR}.backup"` as sibling directories on the same filesystem as `$PACK_DIR`. The candidate is an independent full pack mirror with its own `manifest.json` and the same canonical relative `raw/`, `work/`, `vectors/`, and `stickers/` layout. Never process into the actual pack while a candidate is running.

Run `python3 "$SKILL_DIR/scripts/resume_utils.py" "$PACK_DIR" --allow-new` before creating directories or scheduling any generation. The helper returns `fresh/items=[]` only when root, candidate, and backup state are genuinely absent. Any existing but unresolved state returns `recovery required`; do not create, mirror, overwrite, or generate in that case. An existing valid candidate or root returns `resume` and one decision per row: `skip`, `chroma`, `gate`, `process`, `finalize`, `fail`, or `generate`. Treat fresh creation, state-aware resume, and requested regeneration as distinct flows. Always derive every write target from item id and kind with the canonical helper; never trust stored artifact paths as write destinations. Reject path traversal, aliases, hardlinks (including an outside link count), and symlinked components instead of repairing them in place.

Before creating or mirroring anything, recover an interrupted swap when the helper reports it. If PACK_DIR missing + BACKUP exists, restore backup with `os.replace(BACKUP_DIR, PACK_DIR)`. If PACK_DIR and BACKUP both exist, validate PACK_DIR; retain it only if valid, otherwise move aside the invalid root and restore backup. Always rerun `resume_utils.py PACK_DIR` after any backup or transaction recovery and use the newly selected root/candidate; never reuse a pre-recovery result. Next, if `$CANDIDATE_DIR/manifest.json` exists, resume it before creating/mirroring anything: preserve its complete rows and process only missing or failed rows. Until its first successful promotion, the candidate manifest is authoritative; after promotion, the root manifest is authoritative.

Bridge the fresh result into executable work before entering the item loop. On `fresh/items=[]`, inspect and plan the photo, create `$CANDIDATE_DIR`, build all eight rows with `new_manifest`, atomically save the new candidate manifest through a sibling temporary plus `os.replace`, then rerun `resume_utils.py PACK_DIR` without `--allow-new`. Require `state="resume"` and consume exactly eight returned decisions from that second result. For an initial `resume` result, likewise require and consume exactly eight returned decisions. Never enter the per-item action loop with the empty fresh list. Only `generate` or a successful `reserve_retry` reservation may call `image_gen`.

## Plan and create manifest

1. Inspect the supplied photo and select the visual protagonist automatically. Record only visible hairstyle, face shape, glasses, clothing silhouette, expression, and unambiguous accessories. Do not infer identity, age, ethnicity, health, or other sensitive traits.
2. Plan exactly eight items in this order: three `character_accessory`, two `character_accessory_text`, two `accessory_text`, and one `character_expression`. Normalize and make every action, action+accessory combination, and text caption distinct. For every text item, name the visible cue, turn it into a situational reaction, mood, or action consequence, then reject literal object labels and reserve integrated negative space beside the art for at most two caption lines. Use English-only captions of 2–4 concise uppercase words by default. Change language only when the user explicitly requests another language.
3. For a first-ever pack, follow the fresh bridge above: create the manifest with `new_manifest(SOURCE_PATH, subject, items)` in `$CANDIDATE_DIR/manifest.json`, atomically persist it, rerun the helper, and use its eight decisions. For a resume, replacement, or single-item regeneration, byte-copy the whole existing pack into `$CANDIDATE_DIR` with no symlinks, including its manifest and canonical relative artifacts; keep valid non-target rows complete and set only the requested/missing/failed candidate rows to work again. Store the source path only; do not copy the original user photo into either pack. Leave the actual root pack and manifest untouched while candidate work runs.

## Run high-quality fast mode

Use high-quality fast mode by default. Keep all eight stickers as independent 1024×1024 generations; never generate a contact sheet or crop several stickers from one generated canvas. Preserve the same `quality_gate.py` acceptance criteria as the safe item-wise flow.

Set `CACHE_DIR` to a hidden sibling such as `$(dirname "$PACK_DIR")/.photo-sticker-cache`. When the manifest source photo still exists locally, probe and restore the content-addressed raw-art cache before generation:

```bash
python3 "$SKILL_DIR/scripts/cache_utils.py" restore "$CANDIDATE_DIR" \
  --style-reference "$STYLE_REFERENCE" --cache-dir "$CACHE_DIR" --ids 1,2,3,4,5,6,7,8
```

The cache key includes source-photo bytes, the style reference, visible subject features, kind, action, accessory, expression, and text-free visual prompt, but deliberately excludes the caption. This lets a caption-only revision reuse the same art and rerun local typography. Treat a missing source, invalid entry, or cache error as a miss; the cache is non-authoritative and must never enter the candidate or promoted pack. Store only normalized raw art after a quality-gate pass.

For cache misses whose resume decision is `generate`, persist every selected row as `generating` through the single manifest coordinator, then dispatch at most eight independent full-resolution `image_gen` calls in one bounded concurrent tool-call batch. Every sticker keeps its own 1024×1024 generation, item prompt, and ordered source/style references; concurrency must not change prompts or combine canvases. As each call returns, copy its result to that row's canonical staging path, and never let parallel workers write `manifest.json`; the single manifest coordinator owns every status transition and atomic save. Preserve successful results immediately. If a transport or service limit affects part of the batch, retry only the failed calls in the largest supported concurrent batch and never regenerate a successful item. Fall back to serial calls only when the runtime cannot issue concurrent tool calls.

After the generation batch, or whenever several cache-restored/raw-ready items exist, run the bounded local pipeline:

```bash
python3 "$SKILL_DIR/scripts/fast_pipeline.py" "$CANDIDATE_DIR" \
  --ids "$READY_IDS" --workers 4 \
  --chroma-script "${CODEX_HOME:-$HOME/.codex}/skills/.system/imagegen/scripts/remove_chroma_key.py" \
  --cache-dir "$CACHE_DIR" --style-reference "$STYLE_REFERENCE"
```

`fast_pipeline.py` uses bounded worker processes that do not require macOS system semaphores for isolated item artifacts, then the single manifest coordinator commits `generating -> generated -> processed -> complete` in order. It performs chroma removal with an automatic edge-contract retry, exact-palette normalization, the generation-time quality gate, caption composition, PNG/SVG export, and final item verification. A worker failure never advances its row. Feed a quality failure into the existing one-retry reservation contract. Keep retry and crash recovery on the safe item-wise flow below; `fast_pipeline.py` rejects rows whose shared retry budget is active or spent.

After the initial batch is processed, collect generation and quality failures, reserve all eligible retries first with `reserve_retry`, and retain every successful reservation token. Send only those authorized items in one concurrent retry batch using the simplified retry prompts. Never regenerate a successful item. The retry Image Gen calls may be concurrent, but chroma removal, `mark_retry_raw_ready`, quality gating, terminal failure recording, and manifest transitions remain on the safe item-wise flow below.

## Generate, stage, and key one item

Use this safe item-wise flow for retry and crash recovery, or as the fallback when batching is unavailable. For each candidate item, execute the normalization and operation returned by `resume_utils.decision_transition`: `skip` changes nothing; `chroma` normalizes to `generating`, keys the staged image, and remains `generating`; `gate` normalizes to `generating`, runs `quality_gate.py`, and alone advances a valid raw file to `generated`; `process` normalizes to `generated` and postprocesses/vectorizes; `finalize` normalizes to `processed` and verifies; `fail` atomically normalizes a retry-exhausted row to `failed` and performs no operation; `generate` sets `generating` and calls the initial `image_gen`. Atomically save each non-null normalization before its operation and each success status afterward. After `generate` or `chroma`, rerun the helper and consume the next decision, so a valid raw file still in `generating` resumes as `gate`, never `process`. Use the relevant kind-specific prompt variant from the style guide, always with text-free generated art.

Only `generate` or a successful `reserve_retry` reservation may call `image_gen`; `skip`, `chroma`, `gate`, `process`, `finalize`, and `fail` cannot generate. If the retry budget was reserved but no valid staged or raw artifact survived a crash, the helper returns `fail`, never a fresh `generate` decision.

Use the built-in `image_gen` tool once for an item's first attempt; never use an image-generation API or CLI fallback. When both references have local paths, include them in this order:

```text
referenced_image_paths: [SOURCE_PHOTO, STYLE_REFERENCE]
```

If the source is a recent conversation image without a local path, use `num_last_images_to_include` only when it is the smallest count that includes every required target. Never mix `referenced_image_paths` and `num_last_images_to_include`. If the source and style references cannot both be included under that contract, report the source-reference blocker and do not silently generate an unpersonalized item.

After the tool call, use `resume_utils.staged_relative_path(row)` to derive a distinct staging file such as `CANDIDATE_STAGED="$CANDIDATE_DIR/work/01-character-accessory-imagegen-staged.png"`; do not write it in place to the candidate raw asset. Derive `CANDIDATE_RAW`, both mask targets, `CANDIDATE_SVG`, and `CANDIDATE_PNG` from the row id/kind with `artifact_contract.canonical_write_paths`, never from mutable manifest strings. Keep `$CANDIDATE_STAGED` until the candidate raw output succeeds, then it may be removed.

```bash
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/imagegen/scripts/remove_chroma_key.py" \
  --input "$CANDIDATE_STAGED" --out "$CANDIDATE_RAW" --auto-key border --soft-matte \
  --transparent-threshold 12 --opaque-threshold 220 --despill --force
```

Inspect `$CANDIDATE_RAW` for alpha, transparent corners, plausible coverage, and a green fringe. If a fringe remains, rerun from the unchanged `$CANDIDATE_STAGED` to `$CANDIDATE_RAW` with `--edge-contract 1 --force`. Immediately after the final chroma removal, deterministically flatten visible source art to the exact cobalt-and-white palette while preserving alpha, then run the generation-time-only quality gate:

```bash
python3 "$SKILL_DIR/scripts/normalize_raw_palette.py" --input "$CANDIDATE_RAW" --output "$CANDIDATE_RAW"
python3 "$SKILL_DIR/scripts/quality_gate.py" --input "$CANDIDATE_RAW"
```

The gate prints one deterministic JSON report, exits `0` only when it passes, and exits `1` on a quality failure; it is required before the candidate can transition `generating -> generated`. Do not add this V2 raw-palette gate to `validate_pack.py`: old V1 raw art may contain orange and must remain usable. Generation and quality failures share one retry budget. Before either retry path, call `resume_utils.reserve_retry(CANDIDATE_MANIFEST, row_id, failure, reasons)`. The helper serializes callers with a candidate-scoped retry lock stored as a persistent sibling outside the candidate, so it is crash-reusable but never copied into or promoted with the pack. While holding that non-symlink, non-hardlink lock, it reloads and validates the authoritative manifest, checks `retry_count < 1` plus canonical path and candidate-only safety, and records the exact canonical retry quarantine paths plus a strong unguessable reservation token in structured metadata. It then atomically increments `retry_count` to 1, marks the row `failed`, and persists the explicit reservation phase `invalidation_in_progress` before quarantining. While in that phase it quarantines the old canonical raw and staged artifacts. Only after both invalidations succeed does it atomically advance the phase to `authorized`, mark the row `generating`, and return `True`; only that `True` result authorizes one built-in `image_gen` retry. After `True`, reload the saved row and retain its reservation token as the retry owner's capability. An invalidation failure atomically records `{"retry_invalidation":["unsafe_artifact"]}`, consumes the shared budget, marks the row `failed`, returns `False`, and does not authorize Image Gen. A process interruption leaves the durable in-progress phase fail-closed: interrupted invalidation resumes as `fail`, even if neither or only one stale artifact was moved, and repeated reservation cannot authorize another call. A quality retry uses the **simplified retry** style-guide frame and preserves the protagonist, kind, and visible identity cues with a face/upper-body subject or one simple accessory silhouette, fewer contours, cobalt and white only, uniform stroke weight, no flyaway hairs, no tiny fabric folds, no shading, no texture, no hatching, and no fine whiskers.

If a duplicate or losing `reserve_retry` encounters an existing reservation, its `False` means no authorization and no state mutation; it must not call `image_gen` or report a retry outcome. (The first caller's unsafe invalidation can still persist the required terminal `retry_invalidation` state.) Only the token owner may report an actual reserved retry failure: call `resume_utils.fail_reserved_retry(CANDIDATE_MANIFEST, row_id, token, failure, reasons)` with failure `generation` and reason `tool_failure` or `chroma_failure`, or failure `quality_gate` with the gate's ordered reasons. The dedicated helper reloads under the same lock, requires the exact id, active phase, count, and reservation token, and atomically terminalizes once. A wrong, stale, cross-item, or replayed token returns `False` without mutation. A crash/resume `fail` decision may use the persisted active token with this API when recording a known actual retry failure; never use a duplicate reservation call to terminalize it. A crash after reservation is deliberately at-most-once: the persisted count is already 1, so an `invalidation_in_progress` row or an `authorized` row with no genuinely new valid staged result resumes as `fail` and must not recall Image Gen. An `authorized` reserved valid retry stage takes precedence over a stale raw and resumes as `chroma`. After retry chroma succeeds, `resume_utils.mark_retry_raw_ready(CANDIDATE_MANIFEST, row_id)` is mandatory after retry chroma: it reloads the authoritative active reservation under the same lock, verifies the canonical retry raw, persists phase `raw_ready`, and removes the retry quarantines and staged image through only the recorded quarantine paths. It also removes the empty `.retry-quarantine` directory after verifying that it is the exact real in-candidate directory and contains no unexpected residue. Removing the stage alone is never a progress signal. Rerun the resume helper only after `mark_retry_raw_ready` returns `True`; `raw_ready` plus valid raw returns `gate`, even if a crash left the stage present, while `raw_ready` without valid raw returns `fail`. A crash before the phase advance leaves `authorized` plus the stage and safely repeats `chroma`. Only after a quality-gate pass may the candidate transition `generating -> generated`, clear `error`, and atomically save the candidate manifest.

If initial image generation fails, use `reserve_retry` with failure `generation` and reason `tool_failure`; only a `True` result permits one simpler-pose retry preserving the protagonist, kind, visible cues, and style. If that reserved generation, chroma, or quality attempt later fails, only its token owner calls `fail_reserved_retry`; a duplicate `reserve_retry` merely returns `False` and cannot revoke the owner. On terminal failure continue by running `build_gallery.py` on the candidate to publish a candidate-only incomplete preview: its payload is `complete=false`, failed or missing cards are labeled, and there is no ZIP. Return that `index.html` explicitly as an **incomplete preview**, with failed ids/errors and the resume path. A candidate generation or processing failure must not alter any actual canonical output or completed actual row.

## Process and validate

Do not run repository unit tests during ordinary pack creation. Runtime acceptance is the per-item `quality_gate.py`, final `validate_pack.py`, and successful `build_gallery.py` collision/derivative build. Run repository tests only when Skill source files changed in the current task; prefer targeted affected tests, and reserve the full suite for a release-level change rather than every generated pack.

Run all project scripts by their absolute resolved paths, never assuming a working directory:

```bash
python3 "$POSTPROCESS" --input "$CANDIDATE_RAW" --ink-mask "$CANDIDATE_INK_MASK" --white-mask "$CANDIDATE_WHITE_MASK" --png "$CANDIDATE_PNG" --caption "$CAPTION"
python3 "$SKILL_DIR/scripts/vectorize_sticker.py" --white-mask "$CANDIDATE_WHITE_MASK" --ink-mask "$CANDIDATE_INK_MASK" --output "$CANDIDATE_SVG"
```

Set a candidate row `generated -> processed` only after its masks, 1024×1024 default-blue PNG, SVG, and its `path` or `mask` representation all exist in candidate canonical paths; atomically save its candidate manifest. The SVG master must have separate fixed `#FFFFFF` and `currentColor` layers (paths or lossless masks), never a flattened generated bitmap.

After verifying the target candidate fields and artifacts, set `processed -> complete` and atomically save. The required state path is `planned -> generating -> generated -> processed -> complete`; a terminal item may instead become `failed`. `validate_pack.py` requires every candidate item to be `complete`, so run it only after all eight candidate items are marked complete:

```bash
python3 "$SKILL_DIR/scripts/validate_pack.py" "$CANDIDATE_DIR"
```

After the candidate validates, atomically set its candidate manifest pack `status="complete"`. Let the gallery builder stage and atomically replace `$CANDIDATE_DIR/index.html` and `$CANDIDATE_DIR/stickers-default-blue.zip` through unpredictable, exclusive same-directory temporary files and rollback backups. Do not pre-delete existing derivatives. Then build fresh shared derivatives in the candidate:

```bash
python3 "$SKILL_DIR/scripts/build_gallery.py" "$CANDIDATE_DIR" --template "$SKILL_DIR/assets/gallery-template.html"
```

Require fresh `$CANDIDATE_DIR/index.html` and `$CANDIDATE_DIR/stickers-default-blue.zip` to exist, with all builder-created temporary files cleaned. If candidate gallery/ZIP creation fails, leave the root untouched and keep the candidate resumable; on its next candidate-first startup, detect valid complete items and pack status, rebuild only derivatives, and do not call `image_gen`, chroma processing, postprocess, or vectorization.

The gallery must preserve the clean white-paper presentation from the reference: use a deterministic asymmetric composition with large, medium, and small visual anchors; size and position each preview from a content-aware crop of its visible alpha bounds rather than its 1024px square export canvas; keep slight varied rotations; run a rotated bounding-box collision check over the true preview aspect ratios and enforce a minimum whitespace gap before rendering; and apply a subtle alpha-silhouette shadow to every resting sticker. Do not add cards, frames, labels, or per-sticker download buttons. Keep color controls collapsed to one minimal collapsed blue dot in the upper-right; reveal the other preset color circles and the circular custom-color control only on hover, keyboard focus, or touch activation, update the dot to the selected ink, and show no visible bulk-download control. Clicking the sticker itself runs an offline Three.js edge-origin peel on a subdivided mesh: continuous vertex deformation moves a curl front through the sticker, recomputed normals light the front and paper-colored back independently, and lift-shadow, persistent gray residue, and detach-and-disappear stay synchronized before downloading its full 1024px transparent PNG exactly once. Once download succeeds, hide the peeled sticker for the rest of the current page session, leave its low-contrast gray imprint at the original position, and restore all stickers only on page reload; never spring the sticker back into place. Inline the pinned local Three.js runtime so `file://` galleries never depend on a CDN. Keep the local WebGL canvas centered on the clicked sticker's `getBoundingClientRect()` center and set its CSS display width and height equal to the Three.js scene size; never leave the canvas at the browser's default `300×150` display size. Select the peel origin from the nearest clicked edge, lock repeated clicks during motion, expose `aria-busy`, dispose every WebGL resource after the animation, fall back to a direct download if WebGL fails, and bypass the animation under `prefers-reduced-motion`.

The color flyout also contains one compact, opt-in desktop-mode circle. The default remains direct PNG download. Desktop mode is enabled only when the user selects it and the gallery is opened from `file://`; it sends the manifest-backed item id, pack path, and selected color through `photosticker://add`. Invoke that external protocol synchronously inside the original sticker click before any promise, timer, texture load, or peel animation consumes browser user activation; the visual peel may continue afterward. If the gallery is hosted or desktop delivery is unavailable, preserve the normal download path.

## Optional macOS desktop helper

The bundled `desktop-helper/` is an optional macOS desktop helper, not a dependency of pack generation. The core HTML, PNG, and SVG outputs remain fully usable without it. During ordinary generation, never require the helper, never install or launch it, and never block gallery delivery because it is absent. Its source and one-command builder ship inside the same Skill so a GitHub user does not need a second repository.

Build it only when the user explicitly asks to enable or test desktop stickers:

```bash
"$SKILL_DIR/desktop-helper/build.sh" --output "/absolute/output/StickerDesk.app"
```

For the guided one-command install, prefer:

```bash
"$SKILL_DIR/desktop-helper/install.sh" \
  --destination "$HOME/Applications/StickerDesk.app"
```

The helper must keep desktop stickers behind the desktop icons by default. Because Finder owns mouse input at that level, provide an explicit menu-bar edit mode that temporarily lifts every sticker to a clickable layer; only in edit mode may users drag, resize, rotate, right-click, or remove ordinary desktop-level stickers, and finishing edit mode returns them behind the icons. Preserve positions across restarts and retain a per-sticker always-on-top toggle. It may accept only the exact `photosticker://add` contract; resolve the supplied pack locally, reject symlinks and path traversal, then load only a completed 1–8 item whose PNG path is declared by that pack's valid `manifest.json`. Never accept an arbitrary image path or network URL. Recolor locally from the default cobalt master so switching colors never calls Image Gen.

Only after candidate validation and fresh derivatives succeed, require no retry quarantine directory or files before promotion, and therefore no retry quarantine files before promotion; the crash-reusable lock remains outside the candidate and is never bundled. Then commit the candidate as one sibling-directory transaction. For a first-ever pack, use `os.replace(CANDIDATE_DIR, PACK_DIR)`; if its post-promotion verification fails, move that failed new root back to `$CANDIDATE_DIR` and report it as resumable. For an existing root pack, ensure BACKUP is absent or recovered, then use `os.replace(PACK_DIR, BACKUP_DIR)` followed by `os.replace(CANDIDATE_DIR, PACK_DIR)`. If the second rename, root validation, final manifest/status verification, or root derivative check fails, move aside the failed new root if present (back to `$CANDIDATE_DIR`) and use `os.replace(BACKUP_DIR, PACK_DIR)` to roll back. Keep BACKUP until promoted PACK_DIR validates; only then remove the known backup. Verify the promoted root with `validate_pack.py`, pack status `complete`, and fresh/present `index.html` and default ZIP with temp absent. This replaces the full directory at once, so non-target files remain byte-identical from the candidate copy and old/new target files can never mix.

If candidate generation, processing, validation, or derivative construction fails, build and return the candidate incomplete preview whenever its manifest is valid, report its resumable state, and do not change the root.

## Return paths

When the promoted root validates, has pack status `complete`, and its fresh `$PACK_DIR/index.html` and ZIP exist, return clickable absolute links to that `index.html` and `$PACK_DIR`, with a short retry summary. For an incomplete first-ever run, return `$CANDIDATE_DIR/index.html` labeled **incomplete preview**, `$CANDIDATE_DIR`, and exact failed IDs/errors; confirm that no ZIP exists. When an old valid root exists, return its root path plus the candidate incomplete-preview and resume paths as appropriate, but never present stale root HTML as the new result. Do not link to a nonexistent gallery or ZIP and do not claim completion.

## Single-sticker regeneration and recoloring

For a single-sticker regeneration, clone the root into a candidate and replace only the requested id's staged/raw/mask/SVG/PNG chain there. Revalidate the whole candidate, rebuild its shared derivatives, and transact the complete candidate directory; preserve the other seven artifacts byte-for-byte.

For color-only requests, do not call `image_gen` and do not change composition. Reuse SVG masters in the gallery: change only `currentColor` for ink, flat fills, and text. Keep `#FFFFFF` fixed for subject white areas and the die-cut border; default ink is `#2E429B`.
