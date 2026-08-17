---
name: 钴蓝气息引用
description: "【钴蓝气息引用 / cobalt-breath-quote-zine】 Generate prompts and finished raster images for sparse cobalt-duotone quote, poetry, and reflective prose zines on warm fibrous paper. Use when the user wants a 3:4 editorial card with large aged-paper negative space, exact Chinese text, a single torn or brush-masked blue halftone vignette, sea/breath/diving/writing/growth metaphors, tiny archival microtype, or a conceptual relation between one person and one object, landscape, or action, inspired by gc-minimal-zine-poster-v0-1."
---

# Cobalt Breath Quote Zine

## Overview

Turn a poem, quotation, book excerpt, reflective note, or supplied photo into a quiet 3:4 paper zine. Build one existential visual metaphor in cobalt duotone, preserve a broad warm paper field, and add all required text as an exact deterministic layer.

## Mandatory Recipe Lock

Apply this lock before making any aesthetic choice.

1. Read [references/structure.md](references/structure.md).
2. Select exactly one canonical layout ID from its `Layout Families` section:
   - `upper-text-lower-sea-strip`
   - `upper-text-lower-organic-pool`
   - `left-specimen-right-passage`
   - `left-passage-tall-water-window`
   - `upper-passage-lower-letter-sea`
   - `source-fragment-depth-axis`
   - `split-metaphor-relation`
3. Use the selected geometry literally. Never invent, rename, or substitute a recipe such as `ripple-title`, `centered-strip`, `scroll`, `gallery`, or `calligraphy-poster`.
4. For sea, breath, bubbles, diving, swimming, body, depth, fear, courage, writing, rescue, floating, or drowning content, the image anchor must be one cobalt-only organic vignette. It must not become a clean rectangular image panel, a hanging paper strip, a framed artwork, or a full scene.
5. Report the exact ID as `Recipe: cobalt-breath-quote-zine / Layout: [canonical-layout-id]` before the prompt or image.

## Core Rules

- Use a vertical `3:4` canvas by default; preserve the reference proportion of `1080x1440` when dimensions matter.
- Keep 55%-78% of the canvas as warm yellow-gray fibrous paper.
- Use one cobalt/ultramarine duotone vignette occupying about 18%-35% of the canvas. Keep its boundary irregular, feathered, torn, or brush-printed.
- Use one primary metaphor: a person plus sea, breath, depth, weight, writing, rescue, drift, or one meaningful object.
- Keep the palette nearly two-color: warm paper, gray-blue text, and one saturated cobalt family. Do not add a contrasting accent hue.
- Use halftone dots, xerox softness, risograph grain, missing ink, overprint, faded edges, and embedded paper fibers.
- Keep important text out of generated backgrounds. Typeset exact quotation, attribution, translation, and notes afterward.
- Avoid full-bleed photography, clean rectangular photo cards, hanging rice-paper strips, red seals, ornate headings, glossy mockups, cinematic realism, commercial hierarchy, decorative collage, and invented metadata.

## Workflow

1. Establish the content record.
   - Separate main text, title, author, translator, source, reader note, and optional microcopy.
   - Preserve wording and punctuation. Omit unknown metadata rather than guessing.
   - If the user requests original writing, label it as original and do not fabricate a source.

2. Apply the Mandatory Recipe Lock, then choose one metaphor relation and one cobalt print treatment.

3. Fit the content.
   - Keep the main text block around 10%-24% of the canvas.
   - Use 4-8 short lines or one compact paragraph per card.
   - Split long material into a consistent carousel before shrinking the type.

4. Compile the background prompt in four compact paragraphs.
   - Canvas: 3:4 warm paper, fiber density, negative-space percentage, flat scan.
   - Geometry: text-safe zone plus exact vignette shape, location, and size.
   - Metaphor: one person/object/landscape relation and its cobalt halftone treatment.
   - Reproduction and avoids: risograph/xerox defects, tiny registration marks, mood, and `no letters, no words, no logos, no watermark`.

5. Generate and compose.
   - Generate or construct the text-free background.
   - Preserve the recognizable subject and pose when a source photo is supplied.
   - Add exact text with HTML/SVG/canvas/Pillow or another deterministic renderer.
   - Use no more than two type families and three weights; keep normal Chinese letter spacing at 0.

6. Verify and deliver.
   - Inspect the card at thumbnail and full size.
   - Regenerate once if the warm paper field, organic blue vignette, halftone texture, or conceptual relation is missing.
   - Check every character, source line, and translation for accuracy and separation.

## Text Architecture

- Main quotation or poem: muted gray-blue Song/Ming-style or restrained humanist type.
- Source line: smaller and lighter, preceded by a short rule when useful.
- Optional translation: clearly separated below the source text and never invented.
- Microtype: faint English archive words, depth/breath/time notation, crosshairs, tiny plus marks, or a short measurement label.
- Do not use a large headline; the text should read as a kept passage, not an advertisement.

## Output

Return the exact canonical recipe/layout line, finished image or ordered carousel, exact card text, selected metaphor/texture treatment, short sharing caption, alt text, and final background prompt when image generation was used.

## Quality Gate

- Does the image read first as warm fibrous paper with a cobalt printed fragment?
- Is 55%-78% of the canvas quiet and is the vignette roughly 18%-35%?
- Does the vignette have an organic brush/torn boundary rather than a clean card edge?
- Is there one legible conceptual relation rather than a generic sea photograph?
- Are text, attribution, and translation exact and readable at mobile size?
- Are cobalt halftone, xerox loss, paper fibers, and faint archive marks visible?
- Does the result avoid full-bleed scenes, multicolor accents, fake metadata, clean UI cards, glossy depth, and commercial design?
- Is the reported layout one of the seven canonical IDs, with no invented recipe name or fallback to a hanging scroll, gallery panel, decorative calligraphy, or red seal?
