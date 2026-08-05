---
name: 日常叠影
description: Generate prompts and finished raster images for layered everyday lifestyle photo collages, window-cafe memory boards, room-and-table moodboards, fan-object diary spreads, botanical drink snapshots, and soft overlay zines. Use when the user provides a place, room, cafe, flower, drink, toy, book, character-merch mood, daily memory, reference image, or phrase and wants a horizontal or portrait photo collage with one blurred/full-scene background, many rectangular photo tiles, white wireframe overlays, arrows, tiny icons, scattered poetic text, muted natural color, and Minimal Zine restraint.
---

# Everyday Overlay Photo Zine

Turn a daily memory, room, cafe, object set, reference image, or phrase into:

1. a final image-generation prompt, and
2. a finished raster image in a layered lifestyle photo-collage style.

Fuse Minimal Zine restraint with a contemporary personal moodboard: photographic background, overlapping snapshots, white outline boxes, small arrows/icons, and tender text fragments.

## Reference Routing

- Treat supplied images as visual-grammar or mood references unless the user explicitly requests literal editing.
- Inspect references locally. Extract background scene, photo tile count, tile scale, white line overlays, icon style, text density, blur depth, palette, and subject thread.
- Do not copy visible real usernames, watermarks, brand marks, lyrics, copyrighted character art, personal faces, or exact reference text unless the user explicitly supplies it as intended copy.
- If the reference contains fan merch or anime images, abstract it into fictional character goods, printed cards, acrylic standees, plush toys, badges, notebooks, or illustrated ephemera.
- Read [references/style-grammar.md](references/style-grammar.md) when reverse-engineering the reference look or correcting style drift.
- Read [references/prompt-recipes.md](references/prompt-recipes.md) when selecting a layout family, subject thread, overlay system, or text policy.

## Core Identity

Preserve these signals:

- horizontal 4:3, 16:10, or 3:2 collage by default; portrait only when requested.
- one full-background lifestyle photograph: cafe table, window seat, balcony, garden, room, train/bus interior, rainy glass, tiled wall, or wooded light.
- five to twelve overlapping photo tiles arranged across the scene, not a rigid grid.
- everyday subjects: flowers, drinks, desserts, books, open magazines, plush toys, figurines, stationery, phone, window light, plants, chairs, transit, small collectibles.
- thin white rectangular outlines, corner frames, arrows, dotted shapes, clover/star/tear/music-note icons, and faint line geometry.
- short poetic text fragments in white or pale gray, sometimes vertical, sometimes cursive, serif, or small sans.
- soft blur behind some layers, mild vignetting, natural shadow, muted greens/browns/cream/gray, and warm daylight or moody indoor light.
- personal diary mood, not a commercial template or product ad.

## Minimal Zine Fusion

Carry forward from `gc-minimal-zine-poster-v0-1`:

- one restrained attention system
- quiet text fragments
- controlled color and texture
- old-print or scan softness
- editorial memory atmosphere

Change the geometry:

- replace the tiny paper anchor with a layered photographic moodboard.
- allow the background photo to fill the canvas while overlays provide structure.
- keep visual clutter intentional: several photo tiles are allowed, but every tile must belong to one memory thread.
- use white linework as the zine-like organizing device.

## Layout Engine

Choose one family before compiling:

- `window-cafe-board`: window or cafe table background, drink/flower/book tiles, white outline boxes.
- `room-fan-diary`: blurred bedroom or desk background, fictional character goods, toys, cards, stickers, and vertical text.
- `garden-light-collage`: dark green garden or forest background, flower tiles, drinks, books, and sunlight patches.
- `tabletop-summer-board`: tiled wall or cafe chair background, desserts, soda, plush toys, and pale blue/green accents.
- `transit-memory-board`: train/bus/window background, umbrella, flowers, notebook, drink, and moving-light blur.
- `quiet-gray-room-board`: concrete/cafe interior, grayscale shadows, flowers, pastry, cup, and sparse white typography.

Use one family only. Do not mix every possible object category into one image.

## Subject Thread

Build each image around one believable day:

- primary scene: one background place and lighting condition.
- primary object: one standout flower, drink, book, plush, figure, dessert, or window.
- supporting objects: four to eight related snapshots from the same outing, room, collection, or season.
- overlay marks: three to seven line elements, not a full UI interface.
- text: one short phrase plus optional tiny fragments.

Keep the tile content coherent. Avoid unrelated generic moodboard scraps.

## Typography System

- Use exact user-supplied words only when intended for the image.
- If no text is supplied, invent short non-factual poetic fragments such as `ordinary light`, `memories take you back`, `happy and ordinary`, or `summer fashion`.
- Keep text short, atmospheric, and secondary.
- Allow a mix of small serif, cursive, vertical CJK-like notes, and tiny sans labels, but keep it airy.
- Do not render long paragraphs, URLs, real usernames, dates, sponsors, prices, or copied reference captions.

## Color Engine

Choose one palette:

- forest window: deep green, dark wood, cream white, glass gray.
- cafe milk: warm brown, cream, muted green drink, soft white flower.
- summer tile: pale blue tile, cream wall, mint drink, plush pastel accents.
- moody gray: charcoal, concrete gray, white lily, coffee brown.
- garden shadow: dark olive, yellow flower, black rail, warm table.
- soft fan room: blurred warm beige, pink flower, blue toy accents, white type.

Color may be richer than Minimal Zine, but keep the whole image coherent and slightly muted.

## Prompt Compiler

Write the final prompt as six compact paragraphs:

1. canvas ratio, background scene, lighting, blur, and overall palette
2. selected layout family, tile count, tile placement rhythm, and background/tile hierarchy
3. subject thread: primary object, supporting objects, and how tiles relate to one memory
4. white overlay system: outline boxes, arrows, icons, line thickness, and placement
5. typography: exact allowed text or invented short fragments, font voices, density, and avoids
6. texture, mood, Minimal Zine fusion, and hard avoids

Compile only visible renderable details. Do not mention source paths, reverse-engineering, or analysis in the final prompt.

## Generation

- Generate the image by default; stop at prompt-only only when explicitly requested.
- Prefer the built-in image generation capability.
- When built-in generation is unavailable and server fallback has already been approved, run:

    python3 scripts/server_image_gen.py \
      --prompt-file output/imagegen/<slug>.prompt.txt \
      --out output/imagegen/<slug>.png \
      --size 1536x1024 \
      --quality high

- The fallback reads provider configuration and `OPENAI_API_KEY` from the environment or Codex config, calls the OpenAI-compatible image endpoint, requests `b64_json`, and writes the decoded image locally. Never print or hard-code secrets.
- Store the exact final prompt beside the image. Never overwrite an existing output; choose a new descriptive slug.
- Inspect once. Regenerate with one targeted correction if the output becomes a rigid grid, loses the background scene, copies reference text, becomes an app UI, or turns into a commercial ad.

## Hard Avoids

Always avoid:

- copied usernames, watermarks, exact fan art, copyrighted character likenesses, brand logos, URLs, prices, sponsors, or personal identifiers
- commercial ad layout, CTA, product-promo campaign, social media template, or influencer marketing style
- app UI, dashboard panels, website mockup, or clean digital card grid
- unrelated image scraps, chaotic sticker overload, or every object category at once
- glossy 3D collage, hard shadows, cutout spectacle, neon, or rainbow palette
- long readable paragraphs, lyrics, copied captions, real dates, or fake contact details
- photorealistic human faces as the main subject unless explicitly supplied and permitted

## Output Format

Return the generated image, exact final prompt, and:

- Layout: selected family
- Subject thread: background, primary object, supporting objects
- Overlay system: line boxes, arrows, icons, text fragments
- Palette: dominant color direction
- one short interpretation note

## Quality Gate

Before finalizing, check:

- Is there one coherent lifestyle background scene?
- Are there five to twelve photo tiles, not a rigid grid?
- Do all tiles belong to the same day, room, cafe, or memory thread?
- Are white outline boxes/arrows/icons visible but not UI-like?
- Is text short, atmospheric, and free of copied identifiers?
- Does the image keep a personal diary/collage mood rather than a commercial template?
- Does color stay coherent and slightly muted?
- Did you generate and inspect the final raster image?
