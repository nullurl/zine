---
name: 织物样本V3
description: "【织物样本V3 / textile-swatch-zine-v0-3】 Generate prompts and finished raster images for tactile textile and material swatch zines, soft graphic label boards, paper or leather archives, dye tests, woven structure ledgers, and quiet bespoke material dossiers. Use when the user provides a theme, place, season, product-free material direction, reference image, or mood and wants a vertical fibrous-paper composition with a 2x3 or 3x2 grid of translucent frosted sample cards, rounded label tabs, film-strip or ticket-like fragments, tiny labels, generous blank space, soft scan lighting, one controlled color accent, or explicit preservation of a reference image's original color palette or geometry."
---

# Textile Swatch Zine v0.3

Turn the user's theme, material brief, mood, or reference set into:

1. a final image-generation prompt, and
2. a finished portrait raster swatch-board image.

Fuse Minimal Zine negative-space discipline with a bespoke material archive: textile samples, paper chips, leather or dye swatches, frosted label cards, rounded tabs, film-strip fragments, tiny index type, shallow physical depth, and reference-image palette or geometry preservation.

## Reference Routing

- Treat supplied images as visual-grammar or subject references unless the user explicitly requests a literal edit.
- Analyze local references locally: extract paper tone, grid rhythm, card translucency, geometry families (rounded rectangle, pill, ticket, frame, bracket, perforated strip, circle, arrow), material types, tactile edges, shadow depth, type scale, blank-space share, and accent color.
- If the user asks to preserve color, treat the reference palette as a core material signal rather than neutralizing it.
- If the user asks to preserve style, also preserve the reference's shape language: rounded panels, punched circles, perforated rails, corner brackets, tags, and soft diagram-like spacing.
- For color-preserving requests, keep the dominant hues visible in at least one swatch card, chip, or label strip.
- Do not reproduce visible brands, logos, supplier names, product SKUs, personal identifiers, watermarks, or distinctive copied text from references.
- Do not upload private local references to an untrusted third-party endpoint. The bundled server fallback is text-only.
- Read [references/style-grammar.md](references/style-grammar.md) when reverse-engineering a reference or correcting style drift.
- Read [references/prompt-recipes.md](references/prompt-recipes.md) when choosing a layout, material family, title treatment, or batch variation.

## Core Identity

Preserve these signals:

- Portrait 2:3 or 3:4 composition on bright fibrous paper, pearl white, warm gray, pale cool gray, ivory, or sea-glass mint paper.
- A compact upper or central swatch system with wide lower blank space.
- A 2x3, 3x2, or asymmetric six-cell arrangement of translucent frosted sample cards, label slips, or soft diagram cards.
- Three to five physically believable material specimens or tactile chips: coarse wool, boucle yarn, rib knit, satin, linen, raw silk, handmade paper, leather, dyed cotton, thread bundles, vellum-like label strips, perforated tabs, or paper-cut chips.
- One or two cells may be index cards with material names, season words, numbers, or short sample notes.
- Slightly rounded corners, shallow shadows, matte surface, flat scanned or overhead product-archive view.
- Tiny modern sans, typewriter, or sample-index typography, or no text when geometry already reads as the label system.
- One controlled high-chroma or medium-chroma accent, or a preserved pastel reference palette when the user asks for color retention.
- Calm material-library mood: bespoke sample book, studio archive, fabric ledger, or soft notation sheet, not retail catalog and not UI.

## Fusion With Minimal Zine

Carry forward:

- paper as the primary visual field
- generous negative space
- one restrained attention system
- short text with typographic materiality
- one chromatic anchor, or a preserved source palette when the user requests color retention
- old paper fiber, print softness, scan noise, low-to-medium contrast, and a quiet editorial tone

Change the object logic:

- Replace the isolated tiny object with a small material-board or label-board system.
- Let texture, sample thickness, and cut-paper geometry carry the image, not photography or illustration alone.
- Use frosted translucent cards, rounded tabs, perforated strips, film-frame windows, circles, arrows, and corner brackets when the reference leans graphical.
- Keep labels tiny and archival; do not make a commercial headline or UI card grid.
- For color-preserving reference images, keep the source hues legible and continuous rather than flattening them to beige or grayscale.
- If the reference is more diagrammatic than textile-heavy, let the page become a paper-cut notation board with tactile materials as supporting evidence.

## Layout Engine

Choose one family before compiling:

- balanced-six: a 2x3 grid with four material cards, one text card, and one small accent or index card.
- material-ledger: samples on the left and compact label/index cells on the right, like a studio material record.
- single-hero-swatch: one larger tactile swatch with four smaller surrounding cards and large blank space below.
- thread-route: yarn tails, thread strands, or stitched lines create a subtle reading path between sample cards.
- dye-study: one fabric or paper material repeated in three to five tonal swatches with one vivid dye accent.
- construction-grid: different weave, knit, pile, and satin structures from the same palette in a precise grid.
- graphic-label-board: rounded cards, tabs, circles, arrows, dotted rails, perforated edges, and small swatch chips arranged like a calm index sheet.
- color-preserved-reference: one or two cards hold the reference image's dominant hues while the rest echo them in lighter, darker, or neutral support tones.

Use one family only. Do not combine every sample type, thread route, dye chart, label rail, and hero panel in one image.

## Material Engine

Translate the user's theme into a coherent material set:

- place: choose fibers, paper, leather, or dye colors that could belong to that place.
- season: choose temperature, fiber weight, and tactile finish before choosing decoration.
- mood: use texture contrast such as matte/shine, fuzzy/smooth, dense/open weave.
- product or brand idea: abstract into material language; avoid logos, packaging, and advertising.
- abstract phrase: convert into a material archive title plus three to five touchable samples.
- image reference: preserve dominant colors first, then translate them into matching textile, paper, thread, label, or chip materials.
- graphic reference: preserve spacing, rounded corners, punched holes, perforation rows, dotted lines, tag notches, and film-frame edges in paper form.

Keep every sample touchable and specific. Mention edges, pile, ribs, weave, folds, thread tails, lifted corners, embossing, perforation, or subtle fray.

## Typography

- Invent one short title of 2-5 words when the user supplies no exact text and the composition benefits from type.
- Add one tiny subtitle, date-like code, or material index only when useful.
- Use modern sans, typewriter, small serif, or stamped sample-label type.
- Text belongs on cards, margins, or tiny tags; it must remain subordinate to material and geometry.
- Do not ask the image model to render long copy, full recipes, supplier data, price tags, or dense label sheets.
- When the reference is shape-led, text can disappear entirely and be replaced by tiny counters, dots, ticks, or simple marks.

## Color Engine

Start from paper neutrals: pearl white, warm gray, oatmeal, cool pale gray, sea-glass mint, muted celadon, charcoal, or unbleached cotton. Choose one accent:

- ice blue satin or thread for cool modern material boards
- vivid moss or botanical green for living or tropical themes
- tomato red stitch, tab, or dye chip for editorial tension
- cobalt ink label or tiny thread for minimal-zine energy
- saffron, lemon, or marigold fiber for warm-season memory
- black wool, graphite paper, or ink for high-contrast material study
- preserved reference palette: when the user supplies an image with clear color, keep that color family visible as the main system instead of demoting it to a tiny accent
- sea-glass mint or pearl gray: when the reference favors soft graphical shapes, airy white space, and misty green-gray cards

The accent should occupy about 1%-8% of the page or one clear sample cell. Avoid rainbow palettes, retail color fans, and uniformly beige or brown boards unless explicitly requested.

## Prompt Compiler

Write the final prompt as five compact paragraphs:

1. Canvas, paper surface, portrait ratio, negative-space share, scan or overhead lighting.
2. Layout family, grid position, card count, translucent/frosted card behavior, blank-space placement.
3. Material samples: exact fibers, textures, edges, thickness, thread tails, folds, and one accent sample, or a preserved reference palette and label geometry when color retention is requested.
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

- The fallback reads provider configuration and `OPENAI_API_KEY` from the environment or Codex config, calls the OpenAI-compatible image endpoint, requests `b64_json`, and writes the decoded image locally. Never print or hard-code secrets.
- Store the exact final prompt beside the image. Never overwrite existing outputs; use a new descriptive slug.
- Inspect once. Regenerate with one targeted correction if the swatches look flat and fake, the cards become UI panels, the material texture is not visible, the page is too dark, the label text dominates, or the result becomes a retail catalog.
- If the user asked to preserve color and the palette collapses to neutral tones, regenerate once with stronger color-preservation language and a larger colored swatch area.
- If the reference was shape-led and the result loses the rounded tabs, perforations, or dotted rails, regenerate with stronger geometry-preservation language.

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
- too many colors, muddy low-light palette, or a one-note beige or brown board with no accent
- material samples that look like flat vector rectangles instead of tactile specimens

## Output Format

Return the generated image, exact final prompt, and:

- Layout: selected family
- Materials: primary samples and accent
- Typography: title and label treatment
- one short interpretation note

## Quality Gate

Before finalizing, check:

- Is the result a portrait tactile material swatch board or label board?
- Does the composition preserve generous paper space, especially below the card system?
- Are there three to five distinct real material textures or tactile chips?
- Are sample cards translucent or frosted without becoming UI panels?
- Does one layout family clearly organize the page?
- Is one accent color controlled and visible?
- Is type tiny, archival, and subordinate?
- Are shadows shallow and matte, with no glossy mockup effect?
- Does the image avoid brands, copied text, retail catalogs, UI, and dense scrapbook decoration?
- If the reference was graphic, do the rounded tabs, dots, perforations, and label rails still read clearly?
- Did you generate and inspect the final raster image?
