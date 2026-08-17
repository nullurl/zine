---
name: 诗分享卡
description: "【诗分享卡 / poetry-share-zine】 Turn a supplied Chinese or multilingual poem into a finished shareable poetry poster or carousel with exact deterministic typography and poem-derived raster imagery. Analyze literal entities, action, time, weather, sensory cues, space, emotional tension, and formal rhythm before routing among botanical, nocturne, weather, urban, domestic, archival, cartographic, sound, ink, geometric, ghost-print, film, material, storybook, concrete-type, or cobalt minimal-zine styles. Use for poetry cards that must reflect the poem's own imagery instead of defaulting to sea, divers, bodies, or generic emotional symbolism."
---

# Poetry Share Zine

## Overview

Turn poetry into a readable sharing artifact built on the `gc-minimal-zine-poster-v0-1` material grammar. Derive subject, action, composition, color, and print process from the supplied poem, then add the exact poem as a deterministic typography layer.

## Core Contract

- Preserve supplied wording, punctuation, stanza breaks, title, author, and translator. Do not silently rewrite or invent them.
- Analyze the poem before choosing a recipe. Never route from a single keyword.
- Select one primary motif, zero to two supporting motifs, one dominant style family, and one layout.
- Prefer poem-specific objects, species, places, weather, gestures, and verbs over generic people or emotional symbols.
- Treat aged paper, deliberate negative space, controlled visual anchors, tactile print texture, and flat reproduction as the GC foundation. The visual cluster may expand when the selected semantic style needs it, but the poem must remain readable.
- Keep required lettering out of generated backgrounds. Add exact text afterward with SVG, HTML/canvas, Pillow, or another deterministic renderer.
- Use one saturated hue or one tightly controlled duotone by default. A poem may justify a restrained two-ink contrast when the semantic opposition depends on it.
- Use one dominant recipe per card set. Do not combine every style family into one composition.
- Avoid logos, fake publication marks, CTAs, AI-generated pseudo-text, glossy mockups, and unrelated decorative collage.

## Workflow

1. Normalize content.
   - Separate title, poem body, author, translator, source note, and optional sharing caption.
   - Preserve deliberate line and stanza breaks. Create new verse only when explicitly requested.

2. Build the semantic image map.
   - Read [references/semantic-routing.md](references/semantic-routing.md).
   - Extract literal entities, action vectors, time/light, senses, space/scale, emotional tension, and formal cues.
   - Rank motifs from textual evidence; select one primary motif and at most two supporting motifs.
   - Report `Image map: [primary] / [supporting] / [action relation]`.

3. Select style and layout.
   - Read [references/gc-grammar.md](references/gc-grammar.md) for the material foundation and prompt compiler.
   - Read [references/layouts.md](references/layouts.md) for recipe families and format behavior.
   - Match the image map to one style family and one layout ID. Report `Style: [family] / Layout: [id] / Palette: [ink plan]`.
   - Read [references/cobalt-breath.md](references/cobalt-breath.md) only when water/breath/depth is the dominant relation, the supplied reference clearly has that identity, or the user explicitly requests cobalt-breath.

4. Fit the delivery format.
   - Default to `4:5` for social sharing; use `3:5` for the pure GC poster proportion.
   - Use `9:16` for stories and `1:1` for two to five short lines.
   - Split long poems into 2-6 cards before reducing body text below comfortable mobile size.

5. Compile the background prompt.
   - Write four compact paragraphs: canvas/negative space; primary motif and action; style/palette/material; mood and hard avoids.
   - State why the selected layout expresses the poem's action or formal rhythm.
   - Reserve the text-safe area explicitly and require `no letters, no words, no logo, no watermark`.
   - Name concrete entities from the poem. Do not substitute a lone figure, ocean, diver, bubbles, or rescue scene unless the image map selected them.

6. Generate and typeset.
   - Generate or construct the text-free background and inspect it at thumbnail size.
   - Add the poem as an exact deterministic layer. Preserve stanza rhythm and prevent orphan punctuation.
   - Use no more than two type families and three weights. Keep normal Chinese letter spacing at `0`.
   - Make HTML output self-contained with inline styles and embedded or public image sources.

7. Verify and deliver.
   - Inspect thumbnail and full-size views for wrong characters, clipping, overlap, weak contrast, excess decoration, and visual clichés.
   - Regenerate when the background ignores the primary motif, introduces unsupported imagery, or repeats a previous composition with only a color change.

## Text Architecture

- Main poem: normally 3-10 short lines per card.
- Title: small or medium; omit when not supplied.
- Attribution: `作者` or `作者｜译者`; never infer missing data.
- Weighted phrase: at most one short supplied phrase may become the type-led anchor.
- Microcopy: optional supplied date, place, weather, or note; keep it secondary.

## Variant Rules

When multiple designs are requested, vary at least three of these four dimensions:

1. primary motif family
2. composition/layout system
3. reproduction process or material texture
4. palette logic

Do not make several variants by moving the same cobalt vignette or changing only the accent color.

## Output

Return the image-map line, exact style/layout/palette line, finished image or ordered carousel, exact card text, aspect ratio, short sharing caption, alt text, and final background prompt when image generation was used.

## Quality Gate

- Can every major visual element be traced to a supplied word, action, sensory cue, formal pattern, or requested reference style?
- Is one primary motif visibly dominant with no more than two supporting motifs?
- Does the style family express the poem's action or tension rather than merely decorate it?
- Is the GC tactile paper/print identity visible without forcing every result into the same beige-and-cobalt composition?
- Is every required character exact, readable, and rhythmically faithful?
- Does the card work at mobile size without clipping, overlap, fake metadata, or AI lettering artifacts?
- If sea/body/fear/courage appears, was it weighed against all other evidence instead of automatically producing a diver or rescue scene?
