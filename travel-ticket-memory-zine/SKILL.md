---
name: 旅途票据
description: "【旅途票据 / travel-ticket-memory-zine】 Generate prompts and finished raster images for rounded travel-memory ticket cards, city photo pass cards, diary ticket grids, location archive cards, and soft souvenir photo zines. Use when the user provides a place, trip, season, daily memory, reference photo, photo set, mood, or short phrase and wants a vertical card with a large rounded photo window, solid color ticket-stub information panel, semicircle bottom notch, barcode-like marks, bold place typography, date/index microcopy, soft shadows, muted palette, or a 3x3 collection of coordinated memory cards. Also use when the user asks to fuse gc-minimal-zine-poster negative space with photo-ticket or barcode-card visual structure."
---

# Travel Ticket Memory Zine

Turn the user's theme, place, reference image, photo set, or memory into:

1. a final image-generation prompt, and
2. a finished raster image in a soft travel-ticket memory-card style.

Fuse Minimal Zine discipline with a reusable ticket-card object: one photo window, one information panel, rounded card corners, shallow paper/plastic relief, a bottom semicircle notch, barcode-like marks, compact place/date typography, and controlled background color.

## Reference Routing

- Treat supplied images as subject, palette, or layout references unless the user explicitly asks for literal editing.
- Inspect local references before prompt writing. Extract photo subject, dominant palette, card proportions, text hierarchy, notch shape, barcode placement, background color, shadow depth, and whether the request wants a single card or a grid.
- Do not reproduce visible real barcodes, personal identifiers, serials, watermarks, or copied text from reference images unless the user explicitly supplies exact in-image copy to preserve.
- Do not hard-code `GUI ZHOU`, dates, or serials from the reference. Use user-supplied place/date/copy, or invent short fictional non-identifying copy.
- Read [references/style-grammar.md](references/style-grammar.md) when reverse-engineering a reference, preserving card structure, or fixing drift.
- Read [references/prompt-recipes.md](references/prompt-recipes.md) when selecting card layout, palette, typography, or batch variation.

## Core Identity

Preserve these signals:

- Portrait 3:4, 4:5, or 3:5 raster image; single centered card or 3x3 card grid.
- Muted full-page color background matching the card panel: sage green, gray, dusty blue, warm clay, rose red, dark olive, taupe, or smoke brown.
- Rounded card with a top photo window occupying roughly 58%-70% of the card and a bottom ticket-stub information panel occupying roughly 30%-42%.
- Bottom center semicircle notch cut into the card edge, visible as a soft physical indentation.
- Tiny top seam or perforation ticks between photo and info panel when useful.
- Bold compact uppercase place title, short date or month, small `NO.` index, and barcode-like vertical stripes or scan marks.
- Soft drop shadow, shallow relief, matte card surface, no glossy product mockup.
- The photo area should look like an everyday memory photo: trees, old walls, fish tank, fireworks, city blossoms, roof tiles, street detail, rain glass, window, mountain, cafe, seaside, or user-provided subject.

## Minimal Zine Fusion

Carry from `gc-minimal-zine-poster-v0-1`:

- one restrained attention system
- large calm background field around the object
- matte paper or card texture
- subtle scan noise, old print softness, and low-to-medium contrast
- one clear color identity per card
- sparse text and archive-like microcopy

Change the object logic:

- Replace the tiny zine anchor with a larger ticket-card object.
- Let the card itself be the main specimen; do not scatter unrelated stickers.
- Use a photo-memory window instead of abstract object specimens.
- Use barcode-like marks and serial codes as fictional design texture, not real data.

## Layout Engine

Choose one family before compiling:

- single-memory-ticket: one large centered ticket card on a matching muted background.
- gallery-nine: a 3x3 grid of small memory-ticket cards, each on a different muted color block.
- diptych-ticket: two companion cards side by side or stacked with related memories.
- full-bleed-card-study: one oversized cropped card with its notch and barcode panel emphasized.
- seasonal-pass: one card designed around a month or season palette.
- photo-led-ticket: photo window dominates and panel is quieter; use when the user's image subject matters.
- type-led-ticket: place/date typography and barcode texture dominate; photo window is minimal or abstract.

Use one family only. Do not combine a nine-grid, oversized hero card, and dense scrapbook extras in one image.

## Photo And Subject Engine

Translate the user's content into one photo-memory subject:

- city or place: skyline fragment, old roof, alley wall, trees, bridge, apartment facade, station, window, cafe, street light.
- nature: tree canopy, blossom branches, mountain fog, water surface, beach, rain leaves, sunlight through green.
- festival or night: fireworks, sparklers, lanterns, wet street light, night window, glowing smoke.
- aquarium or interior: fish tank, glass condensation, soft reflections, warm domestic color.
- abstract phrase: choose one everyday photo subject that could plausibly have been found in a travel diary.
- supplied photo: preserve the primary subject and palette in the photo window unless the user asks for mood-only reinterpretation.

Keep the photo simple and memory-like. Avoid cinematic spectacle, stock-photo perfection, or busy travel advertisement composition.

## Typography And Metadata

- Use user-supplied place/title/date exactly when provided.
- If no title is provided, invent a short uppercase place or memory label of 1-3 words such as `MIST CITY`, `TREE LIGHT`, `OLD ROOF`, `FISH WINDOW`, or `NIGHT SPARK`.
- Use a compact bold sans for the main title, often two stacked words.
- Use a small date-like line only when supplied or when fictional diary metadata is appropriate for a memory card. Keep it short, for example `2026 - 06`, `AUGUST`, or `NO.70186`.
- Use barcode-like vertical stripes and short fictional alphanumeric codes as graphic texture. Do not call them scannable or factual.
- Keep total readable text short. Avoid long captions, addresses, prices, phone numbers, URLs, or copied reference text.

## Color Engine

Select one dominant card/background palette:

- muted sage: trees, leaves, summer, fish tank, quiet city greenery.
- dusty blue: blossoms, winter sky, glass building, pale morning.
- smoke gray: old roofs, bare trees, stone walls, rain, archive mood.
- warm clay: goldfish, old walls, indoor warmth, food, sunset.
- rose red: fireworks, sparklers, festival smoke, neon warmth.
- deep olive: sun-through-leaves, forest, humid summer, shadowed green.
- smoke brown: night fireworks, old houses, muted memory.

The card panel and page background may share the same hue family, but use a slight value difference so the card edge and shadow remain visible. Use photo colors naturally; do not add rainbow accents unless the subject is fireworks or fish.

## Prompt Compiler

Write the final prompt as five compact paragraphs:

1. Canvas, background color, card count, card placement, card scale, and physical surface.
2. Ticket-card anatomy: rounded corners, photo window, information panel, semicircle notch, seam/perforation ticks, barcode area, shadow.
3. Photo subject, preservation of reference image or chosen memory subject, photo crop, palette, and mood.
4. Typography and metadata: exact title/date/index/code treatment, font voice, and text limits.
5. Minimal-zine texture and hard avoids: no real brand, no real barcode data, no CTA, no UI, no glossy mockup, no long copy, no copied text.

Compile only visible renderable details. Do not mention source paths, reverse-engineering, or analysis in the final prompt.

## Generation

- Generate the image by default; stop at prompt-only only when explicitly requested.
- Prefer the built-in image generation capability.
- When built-in generation is unavailable and server fallback has already been approved, run:

    python3 scripts/server_image_gen.py \
      --prompt-file output/imagegen/<slug>.prompt.txt \
      --out output/imagegen/<slug>.png \
      --size 1024x1536 \
      --quality high

- The fallback reads provider configuration and `OPENAI_API_KEY` from the environment or Codex config, calls the OpenAI-compatible image endpoint, requests `b64_json`, and writes the decoded image locally. Never print or hard-code secrets.
- Store the exact final prompt beside the image. Never overwrite existing outputs; use a new descriptive slug.
- Inspect once. Regenerate with one targeted correction if the card notch disappears, typography dominates, photo becomes a commercial ad, the barcode becomes a real-looking scannable code, the card becomes app UI, or the result loses the ticket-card anatomy.

## Hard Avoids

Always avoid:

- real brands, real barcodes, real QR codes, URLs, phone numbers, addresses, prices, CTAs
- copying reference text, serials, or visible personal identifiers
- glossy credit-card mockup, plastic bank card, app UI card, mobile wallet pass, SaaS panels
- dense scrapbook, sticker overload, Polaroid pile, torn collage clutter
- commercial travel poster, tourism ad, logo lockup, promotional headline
- cinematic dramatic lighting, 3D render, hard shadow, neon cyberpunk
- cute cartoon, anime, kawaii ticket, toy-like illustration
- long readable paragraphs or too many metadata lines

## Output Format

Return the generated image, exact final prompt, and:

- Layout: selected family
- Photo subject: source or invented memory subject
- Palette: dominant card/background palette
- Typography: title/date/index/barcode treatment
- one short interpretation note

## Quality Gate

Before finalizing, check:

- Is the result clearly a rounded travel-memory ticket card or coordinated ticket-card grid?
- Does the photo window occupy the top portion and the information panel occupy the bottom portion?
- Is the bottom semicircle notch visible?
- Are the title, date/index, and barcode-like marks subordinate but legible enough?
- Is the barcode clearly decorative and not a real scannable code?
- Does the palette follow one muted card/background system?
- Does the image preserve minimal-zine restraint: calm background, soft paper/card texture, no ad clutter?
- Did the prompt avoid copying reference text unless explicitly supplied?
- Did you generate and inspect the final raster image?
