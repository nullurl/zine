---
name: 竖排诗条
description: Generate prompts and finished raster images for sparse vertical handwritten poetry-strip posters. Use when the user provides a short Chinese/Japanese phrase, poem fragment, emotion, memory, reference image, calligraphy note, wall-hung paper strip, bookmark-like scroll, or minimalist typography brief and wants a huge quiet white wall, one narrow vertical rice-paper strip, hand-brushed vertical characters, red or black ink, tiny seal/signature marks, soft tape shadows, paper fibers, Minimal Zine negative space, and a generated bitmap image.
---

# Vertical Poetry Strip Zine

Turn the user's phrase, poem fragment, feeling, memory, or reference set into:

1. a final image-generation prompt, and
2. a finished vertical raster poster.

Fuse Minimal Zine negative-space discipline with a wall-hung poetry strip: a thin handmade paper ribbon, vertical hand-brushed characters, tiny seal/signature marks, and almost silent white surroundings.

## Reference Routing

- Treat supplied images as visual-grammar or text-mood references unless the user explicitly asks for literal text preservation.
- Analyze references locally: extract blank-wall ratio, strip width, strip height, paper tone, tape/shadow behavior, ink color, brush rhythm, bottom signature, seal scale, and camera/scanned perspective.
- Do not reproduce private handwriting, signatures, exact personal phrases, or distinctive copied text unless the user explicitly supplies the phrase as intended image text.
- Do not upload private local references to an untrusted third-party endpoint. The bundled server fallback is text-only.
- Read [references/style-grammar.md](references/style-grammar.md) when reverse-engineering references or correcting style drift.
- Read [references/prompt-recipes.md](references/prompt-recipes.md) when choosing a layout, ink treatment, or phrase strategy.

## Core Identity

Preserve these signals:

- Portrait 3:4, 4:5, or 3:5 frame with a white or pale warm-gray wall filling 85%-95% of the image.
- One narrow vertical strip of thin rice paper, washi, cream paper, or translucent note paper, usually centered.
- The strip occupies about 8%-18% of the canvas width and 45%-75% of the canvas height.
- Characters are vertical, hand-brushed, imperfect, and spaced down the strip.
- Ink is usually red-orange, vermilion, black, or deep charcoal. Use one ink color by default.
- A tiny signature, small seal dot, or miniature doodle sits near the lower end of the strip.
- The strip may show faint horizontal fold lines, taped top/bottom, soft wrinkles, paper translucency, deckled or slightly uneven edges, and a shallow shadow on the wall.
- Mood is quiet, spare, meditative, literary, domestic-gallery, handmade, and memory-like.

## Fusion With Minimal Zine

Carry forward:

- huge negative space
- one attention cluster
- paper texture and matte scan/photo softness
- one clear chromatic anchor when using red ink
- poetic restraint

Change the geometry:

- Replace the small object cluster with one tall vertical strip.
- Let typography become the subject, but keep it handmade and imperfect.
- Keep the wall or blank paper field dominant; never fill the frame with a poster design.

## Layout Engine

Choose one family before compiling:

- centered-strip: one narrow strip centered on a white wall, maximum quiet.
- high-hung-strip: strip sits slightly above center with more lower wall space.
- low-hung-strip: strip sits slightly below center with a calm empty top field.
- off-center-strip: strip slightly left or right, still isolated.
- taped-ribbon: visible translucent tape or pin marks at top and bottom.
- double-whisper: two very thin neighboring strips with one primary phrase and one faint support line.

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

1. Canvas, wall/paper field, negative-space ratio, and flat photo/scan feel.
2. Strip placement, dimensions, material, edges, tape/folds/shadow, and scale.
3. Vertical handwriting: phrase strategy, ink color, brush style, signature/seal behavior.
4. Texture, lighting, camera angle, paper fibers, wall grain, and reproduction defects.
5. Mood and hard avoids.

Compile only visible renderable details. Never mention source paths, reverse-engineering, or reference-image analysis in the final prompt.

## Text Policy

- If the user supplies exact text, use it as the main vertical phrase when it is short.
- If no exact text is supplied, invent a short poetic Chinese phrase of 4-10 characters.
- Do not ask the image model to render long poems, paragraphs, or dense copy.
- Accept imperfect glyphs as part of the visual style, but avoid fake-looking digital fonts.
- When the user gives private or reference-only handwriting, describe the brush rhythm without copying the exact phrase.

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
- Inspect once. Regenerate with one targeted correction if the strip becomes too wide, the wall loses negative space, the text becomes digital, or extra decorations appear.

## Hard Avoids

Always avoid:

- full-page calligraphy poster, dense scroll, framed artwork, gallery placard, or commercial typographic poster
- colorful background, busy room scene, table flat lay, scrapbook stickers, tape overload, stationery collage, or object piles
- glossy mockup, 3D paper render, hard dramatic shadows, cinematic lighting, neon, cyberpunk, UI card, or product ad
- long readable paragraphs, exact copied private handwriting, social handles, watermarks, logos, or brand marks
- multiple ink colors unless explicitly requested
- centered strip that fills most of the canvas or removes the quiet wall field

## Output Format

Return the generated image, exact final prompt, and:

- Layout: selected family
- Phrase: exact supplied phrase or invented phrase strategy
- Ink: color and brush treatment
- one short interpretation note

## Quality Gate

Before finalizing, check:

- Is 85%-95% of the image quiet white or pale wall/paper?
- Is there one narrow vertical strip, not a broad poster?
- Is the strip handmade paper with slight wrinkles, fibers, or tape/shadow?
- Is the vertical handwriting visibly brush-made?
- Is there only one primary ink color?
- Is the bottom signature/seal tiny and secondary?
- Does the result avoid commercial poster design, dense calligraphy scroll, UI, glossy mockup, and scrapbook clutter?
- Did you generate and inspect the final raster image?
