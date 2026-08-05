---
name: 影像诗迹
description: Generate prompts and finished raster images for dual-panel photo and line-trace poetry zines. Use when the user provides a theme, place, object, memory, Chinese sentence, city scene, garden view, lake, bridge, animal, flower, night light, travel photo, or reference images and wants a vertical poster with a colored matte-paper upper panel, pale line drawing traced from the subject, centered Chinese poetic title and date, and a lower photographic panel fused with Minimal Zine negative-space discipline.
---

# Photo Trace Poetry Zine

Turn the user's theme, photograph, place, object, or reference set into:

1. a final image-generation prompt, and
2. a finished vertical raster poster.

Fuse Minimal Zine paper discipline with a two-register editorial system: a quiet drawn study on colored paper above and a related photographic scene below.

## Reference Routing

- Treat supplied images as visual-grammar or subject references unless the user explicitly asks for a literal edit.
- Analyze local references locally: extract split ratio, paper color, line-art subject, title placement, date style, photo crop, lighting, palette, and edge alignment.
- Do not reproduce visible brands, exact signs, addresses, logos, watermarks, faces, private text, or distinctive copied text from references.
- Do not upload private local references to an untrusted third-party endpoint. The bundled server fallback is text-only.
- Read [references/style-grammar.md](references/style-grammar.md) when reverse-engineering references or correcting style drift.
- Read [references/prompt-recipes.md](references/prompt-recipes.md) when choosing a layout, title, subject translation, or batch variation.

## Core Identity

Preserve these signals:

- Portrait 3:4 or 4:5 poster with a clean horizontal split.
- Upper 42%-55% is matte colored paper: blue-gray, moss green, ochre, muted sky blue, warm orange, charcoal, or kraft.
- Lower 45%-58% is a full-width photographic panel related to the same subject.
- Upper panel contains thin off-white line art that abstracts or traces the lower photo subject.
- A centered Chinese poetic title sits near the top of the upper panel, with a small date such as `28 July 2026` below.
- Line drawing can be architectural elevation, botanical sketch, animal outline, street scene, boat, bridge, skyline, rain lamp, or object study.
- Lower photo feels real, quiet, local, and slightly cinematic, but not glossy advertising.
- Matte paper grain, mild print wear, soft line misregistration, and a restrained editorial mood.

## Fusion With Minimal Zine

Carry forward:

- decisive negative space in the upper paper panel
- restrained typography
- one coherent attention structure
- paper texture and old-print softness
- poetic, memory-like emotional temperature

Change the geometry:

- Replace the tiny isolated anchor with a two-register comparison: drawing above, photo below.
- Allow the photo to occupy nearly half the poster.
- Use the colored paper field as the main quiet space rather than a white paper field.
- Keep the split precise and editorial; do not turn it into a scrapbook, postcard, or social template.

## Layout Engine

Choose one family before compiling:

- subject-trace: line art directly mirrors the lower photo subject.
- architectural-memory: bridge, pavilion, tower, city, corridor, temple, or street is traced as a clean elevation above the photo.
- water-and-animal: ducks, koi, boats, fish, lake surfaces, or river scenes with thin waterline drawing above.
- botanical-sky: flowers, branches, trees, grasses, or clouds traced over a pale colored paper sky.
- night-lamp: dark upper paper, lamp/tree/rain linework, and lower night photograph with warm light.
- object-poem: cats, statues, fruit, signs, drawings, letters, toys, or small found objects treated as an illustrated study above a photo.

Use one family only.

## Title System

- Use a Chinese poetic title by default, 6-12 Chinese characters when possible.
- If the user supplies an exact title, use it.
- If the user gives only a theme, invent a concise Chinese title that describes a moment, not an advertisement.
- Add one small date line below the title. Use the supplied date if present; otherwise use a neutral fictional date only when useful.
- Keep all other text minimal. Do not ask the image model to render paragraphs.

## Color Engine

Choose the upper paper color from the subject:

- old stone, rain, statues, or quiet city: blue-gray or charcoal green.
- lake, bridge, plants, fish, or garden: moss green, deep teal, or muted pond green.
- autumn, sunset, fruit, warm memory: ochre, kraft, clay, or muted orange.
- spring sky, magnolia, boats, clear day: soft blue.
- night snow or lamps: dark brown-black or graphite.

The lower photo may keep natural color. The upper line art should be off-white, ivory, or pale ink. Do not use neon or rainbow palettes.

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

1. Canvas, split ratio, upper paper color, lower photo panel, and overall scan/editorial feel.
2. Upper panel: line-art subject, title, date, line weight, paper grain, and blank-space behavior.
3. Lower panel: photographic subject, framing, lighting, color, and relationship to the drawing.
4. Typography, palette, texture, print wear, and title/date limits.
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
- Inspect once. Regenerate with one targeted correction if the split disappears, the upper drawing becomes a busy illustration, the title dominates, the photo becomes a collage, or the result becomes an ad template.

## Hard Avoids

Always avoid:

- full-bleed photo with text pasted directly on top
- postcard frame, Instagram story template, UI cards, app mockups, or dashboard panels
- scrapbook stickers, tape overload, Polaroid stacks, tickets, lace, or random stationery
- glossy 3D paper mockup, hard drop shadows, dramatic perspective, luxury campaign lighting
- commercial headline hierarchy, CTA, logo lockup, pricing, packaging, or brand ad feeling
- cartoon, anime, cute mascot style, neon cyberpunk, fantasy poster drama
- too much text, long readable copy, copied signs, watermarks, social handles, or private identifiers
- line art that is too thick, vector-clean, or unrelated to the photo
- photo that ignores the upper drawing subject

## Output Format

Return the generated image, exact final prompt, and:

- Layout: selected family
- Upper panel: paper color, title, line-art subject
- Lower panel: photographic subject
- one short interpretation note

## Quality Gate

Before finalizing, check:

- Is there a clear horizontal split between colored paper and photo?
- Does the upper panel preserve generous negative space?
- Is the line drawing thin, pale, and related to the lower photo?
- Is the title Chinese, centered, and restrained?
- Is the date small and secondary?
- Does the lower photo feel real and quiet rather than commercial?
- Is the palette controlled and derived from the subject?
- Does the result avoid UI, scrapbook, postcard, glossy mockup, and ad styling?
- Did you generate and inspect the final raster image?
