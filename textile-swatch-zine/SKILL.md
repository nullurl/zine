---
name: 织物样本
description: "【织物样本 / textile-swatch-zine】 Generate prompts and finished raster images for tactile textile and material swatch zines, fabric sample boards, yarn studies, paper or leather archives, dye tests, woven structure ledgers, and quiet bespoke material dossiers. Use when the user provides a theme, place, season, product-free material direction, reference image, or mood and wants a vertical fibrous-paper composition with a 2x3 or 3x2 grid of translucent frosted sample cards, real textile swatches, tiny labels, generous blank space, soft scan lighting, one controlled color accent, or explicit preservation of a reference image's original color palette."
---

# Textile Swatch Zine v0.2

Turn the user's theme, material brief, mood, or reference set into:

1. a final image-generation prompt, and
2. a finished portrait raster swatch-board image.

Fuse Minimal Zine negative-space discipline with a bespoke material archive: textile samples, yarn cards, paper chips, leather or dye swatches, small index type, shallow physical depth, and explicit reference-image color preservation.

## Reference Routing

- Treat supplied images as visual-grammar or subject references unless the user explicitly requests a literal edit.
- Analyze local references locally: extract paper tone, grid rhythm, card translucency, material types, tactile edges, shadow depth, type scale, blank-space share, and accent color.
- If the user asks to preserve color, treat the reference palette as a core material signal rather than neutralizing it.
- For color-preserving requests, keep the dominant hues visible in at least one swatch card or thread/dye chip.
- Do not reproduce visible brands, logos, supplier names, product SKUs, personal identifiers, watermarks, or distinctive copied text from references.
- Do not upload private local references to an untrusted third-party endpoint. The bundled server fallback is text-only.
- Read references/style-grammar.md when reverse-engineering a reference or correcting style drift.
- Read references/prompt-recipes.md when choosing a layout, material family, title treatment, or batch variation.

## Core Identity

Preserve these signals:

- Portrait 2:3 or 3:4 composition on off-white, warm gray, pale cool gray, or ivory fibrous paper.
- A compact upper or central swatch system with wide lower blank space.
- A 2x3, 3x2, or asymmetric six-cell arrangement of translucent frosted sample cards.
- Three to five physically believable material specimens: coarse wool, boucle yarn, rib knit, satin, linen, raw silk, handmade paper, leather, dyed cotton, or thread bundles.
- One or two cells may be index cards with material names, season words, numbers, or short sample notes.
- Slightly rounded card corners, shallow shadows, matte surface, flat scanned or overhead product-archive view.
- Tiny modern sans, typewriter, or sample-index typography; no long paragraphs.
- One controlled high-chroma or medium-chroma accent, usually inside one swatch or a small printed mark.
- If the user wants the source image's color preserved, let that palette dominate one or more cards instead of reducing it to a tiny accent.
- Calm material-library mood: bespoke sample book, studio archive, fabric ledger, not retail catalog.

## Fusion With Minimal Zine

Carry forward:

- paper as the primary visual field
- generous negative space
- one restrained attention system
- short text with typographic materiality
- one chromatic anchor, or a preserved source palette when the user requests color retention
- old paper fiber, print softness, scan noise, and low-to-medium contrast

Change the object logic:

- Replace the isolated tiny specimen with a small material-board system.
- Let texture and sample thickness carry the image, not photography or illustration.
- Use frosted translucent cards instead of scrapbook ephemera or vellum portfolio sheets.
- Keep labels tiny and archival; do not make a commercial headline or UI card grid.
- For color-preserving reference images, keep the source hues legible and continuous rather than flattening them to beige or grayscale.

## Layout Engine

Choose one family before compiling:

- balanced-six: a 2x3 grid with four material cards, one text card, and one small accent or index card.
- material-ledger: samples on the left and compact label/index cells on the right, like a studio material record.
- single-hero-swatch: one larger tactile swatch with four smaller surrounding cards and large blank space below.
- thread-route: yarn tails, thread strands, or stitched lines create a subtle reading path between sample cards.
- dye-study: one fabric or paper material repeated in three to five tonal swatches with one vivid dye accent.
- construction-grid: different weave, knit, pile, and satin structures from the same palette in a precise grid.
- color-preserved-reference: one or two cards hold the reference image's dominant hues while the rest echo them in lighter, darker, or neutral support tones.

Use one family only. Do not combine every sample type, thread route, dye chart, and hero panel in one image.

## Material Engine

Translate the user's theme into a coherent material set:

- place: choose fibers, paper, leather, or dye colors that could belong to that place.
- season: choose temperature, fiber weight, and tactile finish before choosing decoration.
- mood: use texture contrast such as matte/shine, fuzzy/smooth, dense/open weave.
- product or brand idea: abstract into material language; avoid logos, packaging, and advertising.
- abstract phrase: convert into a material archive title plus three to five touchable samples.
- image reference: preserve dominant colors first, then translate them into matching textile, paper, or thread materials.

Keep every sample touchable and specific. Mention edges, pile, ribs, weave, folds, thread tails, lifted corners, embossing, or subtle fray.

## Typography

- Invent one short title of 2-5 words when the user supplies no exact text.
- Add one tiny subtitle, date-like code, or material index only when useful.
- Use modern sans, typewriter, small serif, or stamped sample-label type.
- Text belongs on cards, margins, or tiny tags; it must remain subordinate to material.
- Do not ask the image model to render long copy, full recipes, supplier data, price tags, or dense label sheets.

## Color Engine

Start from paper neutrals: ivory, warm gray, oatmeal, cool pale gray, charcoal, or unbleached cotton. Choose one accent:

- ice blue satin or thread for cool modern material boards
- vivid moss or botanical green for living or tropical themes
- tomato red stitch, tab, or dye chip for editorial tension
- cobalt ink label or tiny thread for minimal-zine energy
- saffron, lemon, or marigold fiber for warm-season memory
- black wool, graphite paper, or ink for high-contrast material study
- preserved reference palette: when the user supplies an image with clear color, keep that color family visible as the main system instead of demoting it to a tiny accent.

The accent should occupy about 1%-8% of the page or one clear sample cell. Avoid rainbow palettes, retail color fans, and uniformly beige/brown boards unless explicitly requested.

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

1. Canvas, paper surface, portrait ratio, negative-space share, scan or overhead lighting.
2. Layout family, grid position, card count, translucent/frosted card behavior, blank-space placement.
3. Material samples: exact fibers, textures, edges, thickness, thread tails, folds, and one accent sample, or a preserved reference palette when color retention is requested.
4. Typography: exact short title, tiny labels, index marks, font voice, and text limits.
5. Texture, mood, physical depth, and hard avoids: no brands, UI, retail catalog, glossy mockup, clutter, or long text.

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
- Inspect once. Regenerate with one targeted correction if the swatches look flat and fake, the cards become UI panels, the material texture is not visible, the page is too dark, the label text dominates, or the result becomes a retail catalog.
- If the user asked to preserve color and the palette collapses to neutral tones, regenerate once with stronger color-preservation language and a larger colored swatch area.

## Hard Avoids

Always avoid:

- ecommerce color-card fan, Pantone chart, paint sample catalog, or shopping grid
- digital dashboard, app UI, website mockup, social-media template, or rounded SaaS cards
- glossy 3D render, hard drop shadows, dramatic perspective, plastic glass panels
- fashion campaign, luxury brand lockup, logo, CTA, price tag, barcode-heavy packaging
- dense scrapbook stickers, botanical collage, Polaroid stack, ticket lace overload
- full-bleed fabric photo with text pasted over it
- cartoon, anime, cute classroom craft, neon cyberpunk, metallic spectacle
- long readable paragraphs, supplier addresses, usernames, copied reference text, watermarks, signatures
- too many colors, muddy low-light palette, or a one-note beige/brown board with no accent
- material samples that look like flat vector rectangles instead of tactile specimens

## Output Format

Return the generated image, exact final prompt, and:

- Layout: selected family
- Materials: primary samples and accent
- Typography: title and label treatment
- one short interpretation note

## Quality Gate

Before finalizing, check:

- Is the result a portrait tactile material swatch board?
- Does the composition preserve generous paper space, especially below the card system?
- Are there three to five distinct real material textures?
- Are sample cards translucent or frosted without becoming UI panels?
- Does one layout family clearly organize the page?
- Is one accent color controlled and visible?
- Is type tiny, archival, and subordinate?
- Are shadows shallow and matte, with no glossy mockup effect?
- Does the image avoid brands, copied text, retail catalogs, UI, and dense scrapbook styling?
- Did you generate and inspect the final raster image?
