---
name: 书摘分享卡
description: "【书摘分享卡 / book-excerpt-share-zine】 Turn a supplied book excerpt, quotation, reading note, or photographed page into a finished shareable card or carousel with exact deterministic text and trustworthy attribution. Analyze concrete entities, actions, time, place, senses, argument tension, and verified source evidence before routing among botanical, nocturne, weather, urban, domestic, archival, cartographic, sound, ink, geometric, ghost-print, film, material, scientific, storybook, editorial, or cobalt minimal-zine styles. Use when excerpt visuals should arise from the passage rather than defaulting to open books, sea, divers, bodies, or generic emotional symbols."
---

# Book Excerpt Share Zine

## Overview

Turn a passage into a credible reading artifact built on the `gc-minimal-zine-poster-v0-1` material grammar. Preserve bibliographic truth and mobile readability while deriving visual subject, action, layout, and print process from the passage itself.

## Core Contract

- Preserve the supplied excerpt exactly unless the user requests editing or abridgment.
- Never invent title, author, translator, edition, publisher, chapter, page, cover, logo, endorsement, era, or location.
- Analyze the passage before choosing a recipe. Never route from a single keyword or assumed genre.
- Select one primary motif, zero to two supporting motifs, one dominant style family, and one layout.
- Prefer source-grounded objects, places, systems, species, materials, and actions over a generic person or stock emotional metaphor.
- Keep required text out of generated backgrounds and compose it afterward with deterministic typography.
- Preserve a tactile, sparse, flat printed identity while allowing the visual cluster and color plan to adapt to the selected semantic style.
- Move to a carousel before making the excerpt small. Readability overrides decorative density.
- Avoid commercial book-ad hierarchy, CTAs, fake covers, glossy mockups, full-bleed stock scenes, and dense unrelated collage.

## Workflow

1. Establish the source record.
   - Separate excerpt, book title, author, translator, edition/publisher, chapter/page, and reader note.
   - Keep quotation and reader commentary distinct. Mark omissions with an ellipsis and never splice distant sentences invisibly.
   - Omit unknown metadata rather than guessing.

2. Build the semantic evidence map.
   - Read [references/semantic-routing.md](references/semantic-routing.md).
   - Extract literal entities, actions, time/light, senses, space/scale, argument tension, and verified source evidence.
   - Rank motifs from the passage; select one primary motif and at most two supporting motifs.
   - Report `Evidence map: [primary] / [supporting] / [action or argument relation]` and `Source status: [confirmed / omitted]`.

3. Select style and layout.
   - Read [references/gc-grammar.md](references/gc-grammar.md) for the material foundation and prompt compiler.
   - Read [references/layouts.md](references/layouts.md) for excerpt recipes and format behavior.
   - Match the evidence map to one style family and one layout ID. Report `Style: [family] / Layout: [id] / Palette: [ink plan]`.
   - Read [references/cobalt-breath.md](references/cobalt-breath.md) only when water/breath/depth is dominant, a supplied reference has that identity, or the user explicitly requests it.

4. Fit the delivery format.
   - Default to `4:5`; use `3:5` for the pure GC poster proportion.
   - Use `9:16` for stories and `1:1` only for short quotations.
   - Use 2-6 cards for longer passages. Continue without repetition and place full confirmed source details on the final card.

5. Compile the background prompt.
   - Write four compact paragraphs: canvas/negative space; primary motif and action/argument; style/palette/material; mood and hard avoids.
   - State why the selected layout expresses the passage's action or argument.
   - Reserve the reading area and require `no letters, no words, no logos, no watermark, no fabricated book cover`.
   - Do not add an open book, anonymous person, ocean, diver, bubbles, or rescue scene unless selected from evidence.

6. Generate and typeset.
   - Generate or construct the text-free background and inspect it at thumbnail size.
   - Add the excerpt and confirmed metadata as exact deterministic layers with preserved punctuation and paragraph boundaries.
   - Use no more than two type families and three weights. Keep normal Chinese letter spacing at `0`.
   - Make HTML output self-contained with inline styles and embedded or public image sources.

7. Verify and deliver.
   - Check every card for missing or duplicated text, false metadata, clipped lines, weak contrast, unsupported imagery, and repeated compositions.
   - Regenerate when the output ignores the primary motif or uses a familiar visual cliché unsupported by the passage.

## Text Architecture

- Excerpt: primary readable block with moderate line length and generous leading.
- Source line: `《书名》｜作者`; append translator only when supplied.
- Detail line: edition, publisher, chapter, or page only when confirmed and useful.
- Reader note: label explicitly as `读后记`、`我的批注` or equivalent.
- Accent phrase: one supplied phrase may be highlighted without altering the quotation.

## Variant Rules

When multiple designs are requested, vary at least three of these four dimensions:

1. primary subject family
2. composition/layout system
3. reproduction process or material texture
4. palette logic

Do not create variants by moving the same vignette or changing only the ink hue.

## Output

Return the evidence-map line, style/layout/palette line, source-status line, finished card or ordered carousel, exact card-by-card text map, confirmed attribution, aspect ratio, short sharing caption, alt text, and final background prompt when image generation was used.

## Quality Gate

- Can every major visual element be traced to the passage, verified source evidence, or an explicitly requested reference style?
- Is one primary motif visibly dominant with no more than two supporting motifs?
- Does the layout express the passage's action or argument instead of functioning as decoration?
- Is every attribution field confirmed and every excerpt character exact and readable at mobile size?
- Does the GC tactile print identity remain visible without forcing every result into the same paper-and-cobalt composition?
- Does the result avoid fabricated metadata, fake covers, commercial hierarchy, AI lettering, and unrelated imagery?
- If sea/body/fear/courage appears, was it weighed against all other evidence instead of automatically producing a diver or rescue scene?
