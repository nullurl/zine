---
name: 分析诗学海报
description: Generate prompts and finished raster images for sparse analytical diagram zines and poetic poster studies. Use when the user provides a short phrase, thought, memory, poem, observation, time/space concept, reference image, or diagram-like brief and wants a huge cream-paper or off-white field, one small analytical cluster, thin axis lines, arrows, coordinates, scientific labels, a poetic Chinese note, restrained blue/red/gold accents, paper grain, and a generated bitmap image.
---

# Analytical Skyline Poetry Zine

Turn the user's phrase, thought, memory, concept, or reference set into:

1. a final image-generation prompt, and
2. a finished vertical raster poster.

Fuse Minimal Zine negative-space discipline with a scientific-poetic diagram: pale paper, thin axes, small labeled anchors, floating arrows, and one precise accent color.

## Reference Routing

- Treat supplied images as visual-grammar or subject references unless the user explicitly asks for a literal edit.
- Analyze references locally: extract blank-space ratio, axis geometry, line weight, anchor scale, label density, accent color, and placement of the poetic note.
- Do not reproduce private names, exact copied text, watermarks, or distinctive labels unless the user explicitly supplies them as intended text.
- Do not upload private local references to an untrusted third-party endpoint. The bundled server fallback is text-only.
- Read [references/style-grammar.md](references/style-grammar.md) when reverse-engineering a reference image or correcting style drift.
- Read [references/prompt-recipes.md](references/prompt-recipes.md) when choosing a layout, axis system, or accent strategy.

## Core Identity

Preserve these signals:

- Portrait 3:4 or 4:5 frame with a cream, warm-white, or pale gray paper field.
- 80%-95% of the canvas should remain quiet paper.
- One analytical cluster sits near the center or lower-middle, never edge-hugging.
- The cluster can be a single diagram, specimen, silhouette, head study, bird sequence, compass, timeline, flow field, or object study.
- Thin crosshairs, axes, dots, tick marks, arrows, coordinates, and tiny legends may surround the anchor.
- Small Chinese poetic lines sit below or beside the diagram.
- Type is restrained: small serif, typewriter, monospaced, or fine printed labels.
- Accent color is sparse but precise: blue, red, magenta, gold, or cyan as a line, highlight, point, or tiny object.
- Mood is quiet, analytical, poetic, archival, speculative, and slightly scientific.

## Fusion With Minimal Zine

Carry forward:

- huge negative space
- one attention cluster
- paper texture and matte scan feel
- one clear accent color
- sparse text and editorial restraint

Change the geometry:

- Replace the tiny isolated specimen with an analytical diagram, but keep it small relative to the page.
- Allow thin lines, arrows, and labels, but do not turn the image into a busy data chart.
- Keep the poetic note secondary to the diagram.

## Layout Engine

Choose one family before compiling:

- central-axis: one anchor on a crosshair or axis system, with open field all around.
- horizon-line: a thin horizontal or vertical diagram line with small figures or marks along it.
- flow-field: arrows, curves, or forces swirl around one small subject.
- split-study: two related forms or states with a measured gap between them.
- head-map: a profile or head silhouette filled with diagrams, notes, or cloud-like data.
- specimen-array: a single subject plus a few small analytic insets or labels.

Use one family only.

## Color Trend Enhancement

Use this only when the user asks for brighter color, richer color, preserved source color, a named palette mood, or when the draft would otherwise become too gray, beige, dark, or flat. Preserve this skill's layout grammar first; color is an enhancement layer, not a replacement for structure.

Pick one dominant palette and optionally one small adjacent accent. Assign colors to visible roles such as paper field, photo grade, ink, label, material, shadow, highlight, or motion accent. Do not combine more than two palettes unless the user explicitly asks for chaotic or maximal color.

- forest green: #92AD76, #B6CCAA, #E3EBDD, #71906A, #435F45. Use for botanical, tropical, moss, spring, garden, healing, or green-reverie briefs.
- purple luxury: #7B5FA4, #A487C6, #D8C9EE, #9A8AB6, #5B376D. Use for dreamy, ritual, night floral, velvet, memory, or quiet-luxury briefs.
- vintage mocha: #885949, #C87949, #E6BC8C, #D9D2C8, #203A35. Use for cafe, archive, editorial, old-photo, paper, or warm city briefs.
- earth warm brown: #A5673D, #C89A6B, #E8D6C3, #7B5A42, #3D2C22. Use for handmade, soil, leather, textile, relic, desert, or autumn briefs.
- deep sea blue: #0F2E48, #1E4F73, #5C87B2, #AFC5DA, #E6F0F8. Use for ocean, rain, night water, cloud-sea, distance, or cinematic calm.
- mist blue gray: #9FB0C3, #C9D3DF, #EEF2F6, #75879A, #31485D. Use for rain, fog, glass, winter, quiet architecture, or analytical moods.
- sunset orange: #FF9A42, #FFC185, #FFE9D3, #C66A31, #7B3D1E. Use for warm light, cafe lamps, islands, evening, energy, or celebratory accents.
- cream soft pink: #F6D7DE, #FBE9EE, #FFF7F8, #E9C6D1, #C39BAA. Use for bright journaling, tender memory, blossoms, soft albums, or feminine notes.
- sea-salt blue: #A8D8EA, #D8EDF5, #F8FCFD, #7FB8CF, #5A8097. Use for airy coastal, island, pool, travel, summer, or brighter-water requests.
- desert elegant white: #F7F4EE, #E7DED1, #D1C6B8, #A99F91, #736F66. Use as a clean bright base when the image needs lift without saturation.

When brightening a dark output, increase paper/background luminance with desert elegant white, sea-salt blue, or cream soft pink before increasing saturation. When preserving a reference image, keep its main hues first, then harmonize them with the closest palette above.

## Prompt Compiler

Write the final prompt as five compact paragraphs:

1. Canvas, paper field, blank-space ratio, and flat scan/photo feel.
2. Layout family, anchor size, axis lines, arrows, coordinates, and analytical structure.
3. Typography: tiny labels, poetic Chinese note, optional short English line, and exact accent color.
4. Texture, print defects, line softness, paper fibers, and low-contrast reproduction.
5. Mood and hard avoids.

Compile only visible renderable details. Never mention source paths, reverse-engineering, or reference-image analysis in the final prompt.

## Text Policy

- If the user supplies exact text, use it sparingly and only if short.
- If no exact text is supplied, invent a short Chinese poetic line or analytical phrase.
- Keep label text minimal and mostly decorative.
- Do not ask the image model to render paragraphs or dense prose.

## Generation

- Generate the image by default; stop at prompt-only only when explicitly requested.
- Prefer the built-in image generation capability.
- When built-in generation is unavailable and server fallback has already been approved, run:

    python3 scripts/server_image_gen.py \
      --prompt-file output/imagegen/<slug>.prompt.txt \
      --out output/imagegen/<slug>.png \
      --size 1024x1536 \
      --quality high

- The fallback reads provider configuration and OPENAI_API_KEY from the environment or Codex config, calls the OpenAI-compatible image endpoint, requests b64_json, and writes the decoded image locally. Never print or hard-code secrets.
- Store the exact final prompt beside the image. Never overwrite existing outputs; use a new descriptive slug.
- Inspect once. Regenerate with one targeted correction if the diagram becomes too dense, the paper field shrinks, the labels dominate, or the accent disappears.

## Hard Avoids

Always avoid:

- full-page infographic, data dashboard, or scientific plate overload
- dense text blocks, long paragraphs, tiny illegible captions everywhere
- glossy mockup, 3D render, cinematic lighting, hard shadows, or neon
- scrapbook clutter, stickers, collage piles, UI cards, or brand-ad styling
- multiple bright accent colors
- leaving too little paper field around the analytical cluster

## Output Format

Return the generated image, exact final prompt, and:

- Layout: selected family
- Accent: chosen color and material form
- Text: short poem or note strategy
- one short interpretation note

## Quality Gate

Before finalizing, check:

- Is 80%-95% of the canvas quiet paper?
- Is there one small analytical cluster rather than a busy chart?
- Are axes, arrows, coordinates, or labels thin and restrained?
- Is the poetic note short and secondary?
- Is there only one clear accent color?
- Does the image avoid infographic overload, UI, neon, and glossy rendering?
- Did you generate and inspect the final raster image?
