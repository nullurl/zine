---
name: shadow-lotus-assemblage-zine
description: "Generate prompts and finished raster images for dark devotional Buddha-and-lotus assemblage zines. Use when the user provides a theme, phrase, memory, reference image, scripture-like line, botanical subject, statue, shrine, meditation mood, or abstract poster brief and wants a layered black/olive collage poster with oversized grayscale sculpture, lotus or leaf materials, translucent paper/vellum overlays, vertical Chinese calligraphy, seal marks, smoke or gold traces, and Minimal Zine-style controlled composition."
---

# Shadow Lotus Assemblage Zine

Turn the user's theme, phrase, memory, subject, or reference set into:

1. a final image-generation prompt, and
2. a finished vertical raster poster.

Fuse Minimal Zine's disciplined "background / material / glyph / subject" structure with dark devotional collage: black-green textured fields, cropped grayscale Buddha or statue fragments, lotus and leaf matter, translucent paper layers, vertical scripture-like typography, seals, smoke, ribbon, and small warm metallic accents.

## Reference Routing

- Treat supplied images as visual-grammar or subject references unless the user explicitly asks for a literal edit.
- Analyze local references locally: extract layer order, background tone, subject scale, crop, lotus/leaf placement, calligraphy density, seal position, geometry panels, and accent color.
- Do not reproduce visible brands, logos, watermarks, private text, exact religious inscriptions, or distinctive copied phrases from references.
- Do not upload private local references to an untrusted third-party endpoint. The bundled server fallback is text-only.
- Read [references/style-grammar.md](references/style-grammar.md) when reverse-engineering a reference or correcting style drift.
- Read [references/prompt-recipes.md](references/prompt-recipes.md) when choosing a composition family or translating an abstract theme.

## Core Identity

Preserve these signals:

- Portrait 3:4 or 4:5 poster with a dark ink field: black, smoky olive, deep green, charcoal, or aged bronze-black.
- Layer order stays legible: background texture, translucent material layers, glyph/type layer, then one dominant statue or lotus subject.
- Main subject is usually an oversized grayscale Buddha face, stone head, bronze statue crop, sculpture hand, or shrine fragment, often cut off by an edge.
- Secondary material is lotus flower, lotus leaf, withered leaf, pale botanical scrap, vellum panel, torn paper, smoke ribbon, thin gold line, or red seal.
- Typography is short: vertical Chinese calligraphy, scripture-like columns, small serif labels, stamped seals, or scattered glyph fragments.
- Color stays restrained: grayscale stone plus black/green ground, with one warm accent such as cinnabar red, dull gold, coral, pale lotus pink, or aged cream.
- Texture is matte and tactile: paper fibers, print grain, smoky blur, ink bleed, translucent vellum, old photocopy softness, soft dust, and worn edges.
- Mood is quiet, devotional, mysterious, archival, ceremonial, and poetic rather than commercial or decorative.

## Fusion With Minimal Zine

Carry forward:

- one clear attention system
- large controlled empty or low-detail fields
- short text treated as material
- matte scanned-paper finish
- restrained accent logic
- abstract composition awareness from "background / material / glyph / subject" diagrams

Change the geometry:

- Replace tiny paper specimens with a large sacred or sculptural body.
- Let the cluster become layered and shadowed, but keep hierarchy clean.
- Let vertical typography behave like drifting glyph material, not a headline.
- Use translucent panels and symbolic overlays when needed, but avoid infographic labels.

## Layout Engine

Choose one family before compiling:

- edge-statue: oversized grayscale statue face cropped along one side, lotus and glyphs floating around it.
- central-shrine: centered dark shrine-like assemblage with statue, flower, seals, and vellum layers.
- lotus-orbit: lotus or leaf cluster becomes the focal point, statue fragment recedes behind it.
- vellum-scripture: translucent panels and vertical calligraphy dominate, with a ghosted sculpture below.
- red-panel-ritual: one dark red or cinnabar translucent geometric panel cuts across the composition.
- diagram-fusion: abstract block/circle/arrow structure from the reference diagrams is translated into poetic layers without labels.
- smoke-ribbon: smoke, ribbon, or gold thread draws the eye through statue, flower, and small text.

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

1. Canvas, dark background tone, layer logic, and flat scanned-poster surface.
2. Main subject, crop, scale, material quality, and relation to the frame.
3. Secondary lotus/leaf/vellum/smoke materials and exact layout family.
4. Typography, seal marks, accent color, and print defects.
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

- The fallback reads provider configuration and `OPENAI_API_KEY` from the environment or Codex config, calls the OpenAI-compatible image endpoint, requests `b64_json`, and writes the decoded image locally. Never print or hard-code secrets.
- Store the exact final prompt beside the image. Never overwrite existing outputs; use a new descriptive slug.
- Inspect once. Regenerate with one targeted correction if the poster becomes too bright, too clean, too religiously literal, too scrapbook-like, too commercial, or if the statue/lotus hierarchy collapses.

## Hard Avoids

Always avoid:

- clean infographic labels such as "background", "material", "glyph", or "subject"
- bright UI, app screens, dashboard styling, social media templates, or presentation slides
- glossy luxury ad lighting, 3D render, hard shadows, heavy mockup perspective, or cinematic depth of field
- neon cyberpunk, cute cartoon, anime, kawaii scrapbook, stickers, lace, or busy journaling decoration
- full-color realistic temple tourism scenes or stock-photo spirituality
- long readable scripture paragraphs, copied sacred text, exact seals, brand marks, watermarks, or private identifiers
- too many colors, rainbow gradients, flat one-note black poster with no material depth, or a large commercial headline

## Output Format

Return the generated image, exact final prompt, and:

- Layout: selected family
- Layers: background, material, glyph, subject
- Accent: selected color and form
- one short interpretation note

## Quality Gate

Before finalizing, check:

- Is the canvas vertical and dark, with visible paper or print texture?
- Is the "background / material / glyph / subject" hierarchy readable without labels?
- Is there one dominant statue, lotus, or shrine-like focal system?
- Are lotus/leaf/vellum/smoke materials integrated rather than decorative clutter?
- Is typography short, vertical, and secondary to the image structure?
- Is there one restrained warm accent that remains visible at thumbnail scale?
- Does the image avoid clean infographics, commercial ads, glossy mockups, neon cyberpunk, cute scrapbook, and long text?
- Did you generate and inspect the final raster image?
