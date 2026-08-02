---
name: gilded-ripple-poetry-zine
description: Generate prompts and finished raster images for ornate vintage water-and-coast poetry zines. Use when the user provides a theme, sentence, river, lake, ocean, windmill, boat, flower, bird, dusk, travel memory, reference image, or poetic title and wants a cream-paper editorial poster with decorative calligraphic English title, bold serif subtitle band, Chinese vertical or corner title, central risograph illustration panel, aqua water, sage typography, golden glimmer, aged print grain, and a generated bitmap image.
---

# Gilded Ripple Poetry Zine

Turn the user's theme, phrase, memory, place, or reference set into:

1. a final image-generation prompt, and
2. a finished vertical raster poster.

Fuse Minimal Zine paper discipline with ornamental vintage water-poetry posters: cream paper, old print grain, decorative title typography, a central illustrated water panel, Chinese editorial marks, and one warm glimmer accent.

## Reference Routing

- Treat supplied images as visual-grammar or subject references unless the user explicitly asks for a literal edit.
- Analyze references locally: extract paper tone, central panel ratio, ornate title placement, Chinese title placement, water palette, gold accent behavior, border/rule motifs, illustration style, and text density.
- Do not reproduce visible logos, exact private text, addresses, watermarks, signatures, or distinctive copied phrases from references.
- Do not upload private local references to an untrusted third-party endpoint. The bundled server fallback is text-only.
- Read [references/style-grammar.md](references/style-grammar.md) when reverse-engineering a reference image or correcting style drift.
- Read [references/prompt-recipes.md](references/prompt-recipes.md) when choosing a layout, title system, or subject translation.

## Core Identity

Preserve these signals:

- Portrait 3:4 or 4:5 cream/off-white aged paper poster, flat scanned or letterpress-print view.
- Top area has a large ornate English calligraphic or engraved-style title.
- A bold all-caps serif subtitle band sits near the title or below the central panel.
- The central illustration panel occupies about 35%-55% of the canvas, usually rectangular with soft print edges.
- Subject language favors water, ripple, river, coast, pond, cloud sea, geese, fish, windmill, boats, flowers, reeds, shells, dusk, or golden reflections.
- Chinese typography appears as a vertical left-side title, a bottom-right title block, or small editorial annotations.
- Microtext, dotted rules, oval labels, registration marks, tiny copyright-like metadata, and ornamental separators add structure.
- Palette: cream paper, sage/olive/dark green type, aqua/blue/teal water, soft ochre or golden-orange highlights, black-brown print grain.
- Mood: poetic, vintage, literary, watery, slightly nostalgic, editorial, hand-finished.

## Fusion With Minimal Zine

Carry forward:

- paper-first composition
- controlled palette and one clear accent logic
- material typography rather than digital UI type
- matte scan texture, old paper fibers, ink bleed, and mild misregistration
- poetic restraint

Change the geometry:

- Replace huge empty minimal fields with a more text-rich ornamental poster system.
- Keep decoration organized by rules, bands, panels, and margins; do not let it become a sticker scrapbook.
- Let the central water illustration be the main image, not a tiny specimen.

## Layout Engine

Choose one family before compiling:

- ripple-title: ornate title top, central water panel, bold subtitle below, vertical Chinese title at left.
- dusk-coast: horizon/windmill/coast panel, golden sun accent, large bottom-right Chinese title.
- bird-water: geese, cranes, or gulls glide across blue water with reeds and tiny side annotations.
- fish-cloud-sea: fish silhouettes, cloud sea, and wave panels arranged as a poetic imaginary map.
- floral-pond: flowers, lotus, reeds, or wet garden panel with decorative botanical marginalia.
- oval-label-poster: central panel plus oval label, dotted rules, small seals, and condensed serif metadata.

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

1. Canvas, aged paper, poster proportions, and overall vintage print process.
2. Layout family, central illustration panel, subject, panel scale, and water/coast treatment.
3. Typography system: ornate English title, serif subtitle band, Chinese title/annotations, microtext limits.
4. Palette, gold glimmer accent, paper grain, risograph/letterpress defects, borders, dotted rules, labels.
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
- Inspect once. Regenerate with one targeted correction if the result becomes too dark, too clean, too commercial, unreadably crowded, or loses the central water panel.

## Hard Avoids

Always avoid:

- clean modern travel ad, commercial campaign, product poster, CTA, price, logo lockup, or social media template
- full-bleed cinematic scene with text pasted on top
- glossy 3D paper mockup, hard drop shadow, dramatic perspective, luxury lighting, or UI cards
- cute cartoon, anime, kawaii stickers, cyberpunk neon, fantasy-game poster drama
- chaotic scrapbook clutter, Polaroid piles, random tape overload, lace, ribbons, or stationery dump
- long readable paragraphs, copied private text, watermarks, social handles, exact brand marks, or exact reference-title copying
- muddy monochrome, dark low-key palette, or missing aqua/gold water contrast

## Output Format

Return the generated image, exact final prompt, and:

- Layout: selected family
- Typography: English title, subtitle band, Chinese placement
- Palette: paper, water, type, and glimmer accent
- one short interpretation note

## Quality Gate

Before finalizing, check:

- Is the poster cream-paper, vintage, and flat-scanned?
- Is there a central water/coast/pond illustration panel?
- Does the top title feel ornate and calligraphic or engraved?
- Is there a bold serif subtitle band and short Chinese typography?
- Are microtext and decorative rules present but controlled?
- Are aqua/blue water, sage/olive type, and warm gold glimmer visible?
- Does the image avoid modern ad layout, glossy mockup, neon, cartoon, UI, and scrapbook clutter?
- Did you generate and inspect the final raster image?
