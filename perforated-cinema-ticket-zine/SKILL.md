---
name: perforated-cinema-ticket-zine
description: Generate prompts and finished raster images for perforated black-and-white cinema-ticket zines, playbill cards, and film-program posters. Use when the user provides a film title, play, dramatic theme, memory, reference image, or short brief and wants a black-void poster with a white punch-ticket card, die-cut scalloped edges, dense monochrome illustration, bilingual ticket metadata, an optional repeat strip, halftone grain, and a generated bitmap image.
---

# Perforated Cinema Ticket Zine

Turn the user's theme, title, memory, play, or reference set into:

1. a final image-generation prompt, and
2. a finished vertical raster poster.

Fuse Minimal Zine's single-cluster discipline with a punched-ticket stage: black void, white ticket card, scalloped perforations, theatrical illustration, ticket metadata, and one optional spot accent.

## Reference Routing

- Treat supplied images as visual-grammar or subject references unless the user explicitly asks for a literal edit.
- Analyze references locally: extract background color, card proportion, perforation rhythm, title scale, illustration style, metadata rows, repeat-strip behavior, and accent usage.
- Do not reproduce visible logos, exact private text, addresses, watermarks, signatures, or distinctive copied phrases from references.
- Do not upload private local references to an untrusted third-party endpoint. The bundled server fallback is text-only.
- Read [references/style-grammar.md](references/style-grammar.md) when reverse-engineering a reference image or correcting style drift.
- Read [references/prompt-recipes.md](references/prompt-recipes.md) when choosing a layout, title system, or metadata pattern.

## Core Identity

Preserve these signals:

- Portrait 3:4 or 4:5 poster with a deep black background and one dominant white ticket card.
- The ticket card has punched scallops or half-moon perforations along the top and bottom edges.
- One main illustration panel sits in the upper half or center of the card.
- The lower half holds title, Chinese title, genre line, and ticket-like metadata rows.
- Optional narrow repeat strip on the right shows smaller copies of the same ticket.
- Typography is bold, high-contrast, and poster-like: slab serif, condensed serif, distressed display, or heavy grotesk.
- The illustration is graphic, theatrical, and print-like: stage scene, room, figure, creature, object tableau, symbol system, or surreal film still.
- Palette is mostly black and white, with at most one controlled accent color such as red, yellow, pink, or cream.
- Mood is retro cinema, playbill, program card, speculative fiction, dramatic, collectible, and slightly uncanny.

## Fusion With Minimal Zine

Carry forward:

- one primary cluster
- strong negative space
- short title hierarchy
- print grain, halftone, and paper wear
- controlled accent strategy

Change the geometry:

- Replace the quiet cream field with a black void around the ticket card.
- Make the ticket card itself the object, not just a poster pasted on top of a page.
- Use repeat strips, punch holes, and metadata blocks as part of the composition, not as decoration.

## Layout Engine

Choose one family before compiling:

- single-ticket: one centered white ticket card, no side strip, strong black surround.
- ticket-strip: one large card plus a narrow repeated strip on the right.
- double-bill: two stacked tickets or one tall card with two program sections.
- accent-card: monochrome ticket with one spot color panel, stamp, or title burst.
- poster-plus-stub: large ticket card on the left, smaller stub or mini card beside it.

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

1. Canvas, black void background, ticket-card scale, and overall print process.
2. Layout family, perforated edges, illustration panel, and card proportion.
3. Typography system: main title, Chinese title, genre line, and short metadata rows.
4. Palette, spot accent if any, halftone grain, photocopy wear, and die-cut feel.
5. Mood and hard avoids.

Compile only visible renderable details. Never mention source paths, reverse-engineering, or reference-image analysis in the final prompt.

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
- Inspect once. Regenerate with one targeted correction if the card loses its perforated edge, the repeat strip disappears, the type becomes too clean, or the result turns into a modern UI mockup.

## Hard Avoids

Always avoid:

- glossy ad render, app UI card, social template, or dashboard layout
- full-bleed color scene with text pasted on top
- decorative scrapbook clutter, Polaroids, tape overload, lace, ribbons, or unrelated stickers
- cinematic 3D lighting, luxury mockup shadows, depth-of-field bokeh, or polished poster stock look
- cute cartoon, anime, neon cyberpunk, colorful collage chaos, or fantasy-game splash art
- long paragraphs, watermarks, exact copied poster text, social handles, or private identifiers
- losing the black-void contrast or turning the ticket into a flat white page

## Output Format

Return the generated image, exact final prompt, and:

- Layout: selected family
- Typography: title system and metadata
- Palette: monochrome base and spot accent if any
- one short interpretation note

## Quality Gate

Before finalizing, check:

- Is the background mostly black void?
- Is there one dominant ticket card with punched scalloped edges?
- Is the illustration panel graphic and theatrical?
- Are the title and ticket metadata short, bold, and legible enough?
- Does the repeat strip appear when requested?
- Is the palette mostly black and white with at most one spot color?
- Does the image avoid UI, glossy mockup, scrapbook clutter, neon, and cinematic 3D styling?
- Did you generate and inspect the final raster image?
