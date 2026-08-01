---
name: neon-botanical-annotation-zine
description: Generate prompts and finished raster images for dark botanical photo zines, neon-annotated flower field notes, Y2K garden overlays, night plant editorials, pixel botanical labels, cyber scrapbook plant pages, and poetic photographed flora with graphic annotations. Use when the user provides plant photos, flower names, a garden/night/street scene, a mood, a memory, reference images, or asks for flowers/plants with cyan, magenta, white, dotted, numbered, framed, pixel, script, color-chip, UI-like, or field-note annotations fused with Minimal Zine negative-space discipline and a generated bitmap image.
---

# Neon Botanical Annotation Zine

Turn the user's plant, place, mood, memory, or reference set into:

1. a final image-generation prompt, and
2. a finished raster image of a botanical photograph with graphic annotation layers.

Fuse Minimal Zine restraint with early-digital botanical note graphics: dark real plant photography, one flower or plant as the anchor, neon cyan/magenta/white marks, thin frames, dotted matrices, arrows, pixel line drawings, script labels, small numbers, and floating color chips.

## Reference Routing

- Treat supplied images as visual-grammar or subject references unless the user explicitly requests a literal edit.
- Analyze local references locally: extract flower scale, dark exposure, photo depth, overlay color, mark vocabulary, text amount, frame geometry, dot rhythm, and negative-space zones.
- Do not reproduce visible brands, exact captions, exact article text, watermarks, signatures, social handles, license plates, or recognizable private people from references.
- Do not upload private local references to an untrusted third-party endpoint. The bundled server fallback is text-only.
- Read references/style-grammar.md when reverse-engineering references or correcting style drift.
- Read references/prompt-recipes.md when choosing an overlay system, title, palette, or batch variation.

## Core Identity

Preserve these signals:

- A real photographic plant anchor: lily, hollyhock, daisy, chamomile, vine, grass, bottle in grass, wildflower, or small garden detail.
- Dark or low-exposure botanical setting by default: dusk garden, shaded street plant, night grass, black background, or underexposed green foliage.
- One readable attention route: flower first, annotations second, background third.
- Digital overlay layer that looks printed or composited over the photo: cyan squares, magenta circles, white frames, dotted grids, pixel flower icons, arrows, star marks, small numbers, translucent circles, or color chips.
- Sparse text: one short plant name, title, season word, or tiny note; never long copy.
- Low-to-medium contrast photo texture with film grain, slight blur, scan softness, or screen capture softness.
- One or two neon accent colors only. Default pairs: cyan + magenta, white + red, pale blue + white, or green chip palette.
- A poetic, handmade-electronic mood: field note, amateur garden diary, early web graphic overlay, not a clean app UI.

## Fusion With Minimal Zine

Carry forward:

- generous negative space, here as dark foliage, sky, shadow, or quiet photo field
- one small-to-medium visual cluster with a clear anchor
- short type and restrained mark density
- one visible high-chroma accent strategy
- scan/print/film softness and imperfect registration
- diary-like, editorial, memory-like tone

Change the surface:

- Replace aged paper with dark photographic space when the reference grammar calls for it.
- Replace paper fragments with digital annotation fragments.
- Let the flower or plant remain photographic, not vector-only.
- Keep overlays graphic and intentional; do not make a full UI dashboard or social template.

## Layout Engine

Choose one family before compiling:

- flower-callout: one large flower or stem with arrow lines, script plant name, and a few dot/circle markers.
- numbered-neon-field: magenta numbered circles, cyan squares, and star marks form a route through a dark plant photo.
- framed-specimen: a thin white rectangular frame isolates the flower cluster with translucent circles and one short caption.
- pixel-botany: a pixel-art line drawing of the plant sits beside the real flower, with small dots and one label.
- night-bouquet-labels: flowers emerge from black or deep green space with delicate script labels and pale blue dots.
- color-chip-garden: a garden or object-in-grass photo gets a translucent palette panel, color codes, thin frames, and minimal title.
- sky-note-flower: one silhouetted flower against bright sky with music notes, dots, tiny stars, or a small inset card.

Use one layout family only. Do not combine all overlay types in every image.

## Subject Engine

Translate the user's input:

- flower name: use it as the photographic anchor and title if short.
- mood or memory: choose a believable plant and one annotation metaphor.
- street scene: use one foreground flower or vine, with the street softened behind it.
- garden detail: choose one specimen and make the rest recede into dark green.
- abstract phrase: invent a small title and visual note system rather than illustrating the phrase literally.
- reference set: use its overlay grammar, not exact captions or exact composition.

Prefer one plant species or one visual family. Avoid unrelated flower collages unless the user asks for a set.

## Typography

- Invent one short title of 1-4 words when the user supplies no exact text.
- Use script, serif, small monospaced, pixel text, or tiny field-note type.
- Text can sit on curves, callout lines, label cards, or under a frame.
- Keep exact readable text short. Long supplied prose becomes semantic mood unless the user explicitly requires it.
- Never copy visible reference captions such as plant names, slogans, poems, or sentence fragments unless the user supplies that exact text as the requested copy.

## Color Engine

Start from dark green, black, muted blue, shadow brown, or sky blue photo fields. Choose one accent system:

- cyan + magenta for street-flower or Y2K annotation
- white + red for lily or field-study graphics
- pale blue + white for dark bouquet labels
- lime-green circles + white frame for grass and daisies
- cream + powder blue for bright sky summer notes
- hot pink dots + white pixel text for night lilies

Keep neon accents to about 2%-12% of the image. Let the flower color remain natural and stronger than the annotations unless the user asks for graphic dominance.

## Prompt Compiler

Write the final prompt as six compact paragraphs:

1. Canvas, photo setting, ratio, lighting, negative-space zone, and camera feel.
2. Plant anchor: species or visual form, scale, position, focus, and background depth.
3. Overlay layout family: mark types, positions, route, frame, dots, numbers, arrows, or inset.
4. Typography: exact short title or label, font voice, text placement, and text limits.
5. Palette, film/screen texture, softness, grain, glow level, and registration imperfections.
6. Mood and hard avoids: no clean UI, no social template, no copied reference text, no brand, no overdecorated sticker sheet.

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
- Inspect once. Regenerate with one targeted correction if the image becomes a clean botanical scrapbook, loses the photographic anchor, turns into a UI mockup, overlays become too dense, text becomes long, or neon marks are absent.

## Hard Avoids

Always avoid:

- clean app UI, dashboard, web mockup, social post template, or product ad
- polished botanical scrapbook, paper sticker collage, or wedding stationery
- full vector illustration with no real photographic plant
- cinematic fantasy flower scene with no annotation layer
- excessive neon, rainbow stickers, emoji, cute cartoon, anime, or kawaii graphics
- long readable prose, copied reference captions, exact brand labels, usernames, watermarks, signatures
- identifiable private people, license plates, storefront names, or personal data from reference photos
- glossy 3D overlays, heavy glow, lens flare spectacle, or cyberpunk city styling
- dense information graphic that overwhelms the flower
- minimal poster so sparse that the digital annotation grammar disappears

## Output Format

Return the generated image, exact final prompt, and:

- Layout: selected family
- Anchor: plant or flower subject
- Overlay: mark system and accent colors
- Typography: title and label treatment
- one short interpretation note

## Quality Gate

Before finalizing, check:

- Is there a real photographic botanical anchor?
- Does the image preserve a dark or quiet photo field as negative space?
- Are annotation marks visible and deliberate?
- Is one overlay family clearly selected?
- Are accent colors restrained to one system?
- Is text short and original?
- Does the result avoid copied reference captions, brands, UI templates, and identifiable people?
- Are overlays integrated into a zine/editorial photo mood rather than a generic phone app?
- Did you generate and inspect the final raster image?
