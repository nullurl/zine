---
name: textile-swatch-zine
description: Generate prompts and finished raster images for tactile textile and material swatch zines, fabric sample boards, yarn studies, paper or leather archives, dye tests, woven structure ledgers, and quiet bespoke material dossiers. Use when the user provides a theme, place, season, product-free material direction, reference image, or mood and wants a vertical fibrous-paper composition with a 2x3 or 3x2 grid of translucent frosted sample cards, real textile swatches, tiny labels, generous blank space, soft scan lighting, and one controlled color accent.
---

# Textile Swatch Zine

Turn the user's theme, material brief, mood, or reference set into:

1. a final image-generation prompt, and
2. a finished portrait raster swatch-board image.

Fuse Minimal Zine negative-space discipline with a bespoke material archive: textile samples, yarn cards, paper chips, leather or dye swatches, small index type, and shallow physical depth.

## Reference Routing

- Treat supplied images as visual-grammar or subject references unless the user explicitly requests a literal edit.
- Analyze local references locally: extract paper tone, grid rhythm, card translucency, material types, tactile edges, shadow depth, type scale, blank-space share, and accent color.
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
- Calm material-library mood: bespoke sample book, studio archive, fabric ledger, not retail catalog.

## Fusion With Minimal Zine

Carry forward:

- paper as the primary visual field
- generous negative space
- one restrained attention system
- short text with typographic materiality
- one chromatic anchor
- old paper fiber, print softness, scan noise, and low-to-medium contrast

Change the object logic:

- Replace the isolated tiny specimen with a small material-board system.
- Let texture and sample thickness carry the image, not photography or illustration.
- Use frosted translucent cards instead of scrapbook ephemera or vellum portfolio sheets.
- Keep labels tiny and archival; do not make a commercial headline or UI card grid.

## Layout Engine

Choose one family before compiling:

- balanced-six: a 2x3 grid with four material cards, one text card, and one small accent or index card.
- material-ledger: samples on the left and compact label/index cells on the right, like a studio material record.
- single-hero-swatch: one larger tactile swatch with four smaller surrounding cards and large blank space below.
- thread-route: yarn tails, thread strands, or stitched lines create a subtle reading path between sample cards.
- dye-study: one fabric or paper material repeated in three to five tonal swatches with one vivid dye accent.
- construction-grid: different weave, knit, pile, and satin structures from the same palette in a precise grid.

Use one family only. Do not combine every sample type, thread route, dye chart, and hero panel in one image.

## Material Engine

Translate the user's theme into a coherent material set:

- place: choose fibers, paper, leather, or dye colors that could belong to that place.
- season: choose temperature, fiber weight, and tactile finish before choosing decoration.
- mood: use texture contrast such as matte/shine, fuzzy/smooth, dense/open weave.
- product or brand idea: abstract into material language; avoid logos, packaging, and advertising.
- abstract phrase: convert into a material archive title plus three to five touchable samples.

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

The accent should occupy about 1%-8% of the page or one clear sample cell. Avoid rainbow palettes, retail color fans, and uniformly beige/brown boards unless explicitly requested.

## Prompt Compiler

Write the final prompt as five compact paragraphs:

1. Canvas, paper surface, portrait ratio, negative-space share, scan or overhead lighting.
2. Layout family, grid position, card count, translucent/frosted card behavior, blank-space placement.
3. Material samples: exact fibers, textures, edges, thickness, thread tails, folds, and one accent sample.
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
