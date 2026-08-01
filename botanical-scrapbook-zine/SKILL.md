---
name: botanical-scrapbook-zine
description: Generate prompts and finished raster images for sunlit botanical scrapbook zines, garden memory pages, nature diaries, seasonal photo journals, handmade collage posters, plant field notes, open ring-albums, and keepsake-tin collages. Use when the user provides a theme, memory, poem, place, season, plant, garden photographs, or visual references and wants a vertical off-white paper composition with generous negative space, natural snapshot fragments, clipped type, handwritten notes, Polaroids, ledger paper, lace or tickets, and restrained green-led color.
---

# Botanical Scrapbook Zine

Turn the user's theme, memory, text, or references into both:

1. a final image-generation prompt, and
2. a generated vertical raster collage.

Fuse minimal-zine attention discipline with a tactile botanical photo diary. Keep the page airy and editorial even when it contains several physical fragments.

## Reference Routing

- Treat supplied images as visual-grammar or subject references unless the user explicitly requests a literal edit.
- Analyze local references locally. Extract canvas ratio, empty-paper share, photo rhythm, paper layers, type materials, accent marks, and emotional temperature.
- Do not reproduce exact photographs, personal identifiers, watermarks, visible quotations, or distinctive layouts from a reference set.
- Do not upload private local references to an untrusted third-party endpoint. The bundled server fallback is text-only.
- Read references/style-grammar.md when reverse-engineering references or correcting style drift.
- Read references/prompt-recipes.md when the theme is abstract, a batch needs variation, or the physical container is unclear.

## Core Identity

Preserve these signals:

- Tall vertical 2:3 or 3:5 composition on warm white, cloudy ivory, or pale gray fibrous paper.
- Roughly 35%-65% visible paper, with one primary collage zone and clear breathing room.
- Three to seven related natural photographs from one walk, garden, season, or memory thread.
- Sunlit foliage, flowers, water, paths, open books, hands, found objects, or quiet landscape details photographed like personal snapshots rather than stock imagery.
- Mixed photo formats: borderless crops, narrow vertical strips, Polaroids, contact sheets, framed prints, or a single partial-bleed photo edge.
- Tactile secondary layers such as notebook paper, kraft folder, clipped prose strips, handwritten note, receipt, barcode, tag, paper clip, lace, ribbon, or botanical specimen.
- Mixed but controlled typography: one short phrase in serif/typewriter print, one cut-paper or ransom-letter title, and optional handwriting.
- One plant-led palette plus one small graphic accent: leaf green with butter yellow, cyan, cobalt, vermilion, or black.
- Flat scanned-paper or photographed-flat-lay appearance with soft daylight, paper tooth, slight print wear, and modest analog imperfection.
- Tender, youthful, observant mood: a personal page assembled after a walk, not a commercial campaign.

## Fusion With Minimal Zine

Carry forward:

- paper and negative space as active composition
- one dominant attention route
- short text instead of long copy
- restrained color hierarchy
- scan noise, old-print defects, halftone, and imperfect alignment
- quiet editorial mood

Expand the grammar:

- Let photographs occupy 25%-55% of the canvas rather than one tiny specimen.
- Use three to seven coherent images, not unrelated mood-board imagery.
- Permit tactile overlap, but keep no more than two dense material zones.
- Let saturated natural green live inside photographs; reserve the added accent for a few squares, letters, drops, stars, or quotation marks.
- Use scrapbook artifacts only when they support the memory thread.

## Layout Engine

Choose one family before writing the prompt:

- split-sunlight: one large natural photo fills 40%-55% of one side; the other side is open paper with two or three clipped fragments.
- drifting-clippings: three to five unframed photos drift vertically through a large paper field with wide gaps.
- central-polaroid-stack: one hand-held or object photograph anchors a compact stack of Polaroids, ruled paper, and type strips.
- botanical-ledger: a kraft folder, ledger, or index page holds photos, field-note fragments, and one clipped quote.
- open-ring-album: an open two-page notebook or ring album occupies the lower half while annotations float above.
- keepsake-tin: an open shallow silver tin contains photos and ephemera against a softly blurred place background.
- sound-and-leaf: sparse music notation or waveform-like lines cross the paper between botanical photographs.

Use one family only. Do not combine the tin, binder, music, lace, tickets, and Polaroids in every image.

## Memory Thread

Choose one anchor and two to six supports from the same believable outing:

- anchor: sunlit canopy, flowering shrub, forest path, open book on grass, hand holding a plant fragment, pond reflection, or place-defining garden view
- support: leaf close-up, white flower cluster, tree shadow, water ripple, grass detail, shoe-level path view, notebook, ribbon, earphones, ticket, or small found object

Keep season, daylight, film response, vegetation, and point of view coherent. Use one imperfect snapshot or motion-blurred fragment for lived-in rhythm.

## Material Hierarchy

Use three levels:

1. Primary: natural photographs.
2. Secondary: one paper system such as Polaroid, notebook, kraft folder, contact strip, or clipped prose.
3. Tertiary: two to five tiny marks such as stars, color squares, arrows, rain drops, quotation marks, index numbers, paper clip, lace edge, or barcode.

Do not let tertiary marks become a sticker sheet. Keep edges tactile but shadows shallow.

## Typography

- Invent one original short phrase of 2-7 words when the user supplies no exact text.
- Use at most three type voices: serif/typewriter strip, rough cut-paper letters, and small handwriting.
- Render no more than one short sentence plus one title and one tiny note.
- Break type across separate paper strips when it helps the page rhythm.
- Keep text subordinate to photographs; no giant commercial headline.
- Treat long supplied prose as semantic inspiration unless the user explicitly needs it reproduced.
- Never copy lyrics, quotations, signatures, usernames, or personal text visible only in reference images.

## Color Engine

Start with photographic greens and neutral paper. Choose one added accent:

- butter-yellow four-point glints for sunlight
- pale olive squares for indexing
- cyan line drops or circles for rain and water
- cobalt or forest-green cut letters for a stronger title
- restrained vermilion arrows for route or emphasis
- black halftone eye, arrows, notes, or music as a graphic counterweight

The added accent should occupy about 1%-5% of the canvas. Avoid rainbow sticker palettes and uniformly saturated photography.

## Prompt Compiler

Write the final prompt as six compact paragraphs:

1. Canvas and paper: vertical ratio, paper tone, visible-paper share, lighting, scan or flat-lay treatment.
2. Attention geometry: chosen layout family, primary collage zone, breathing space, reading route.
3. Photo memory: anchor, supporting photographs, count, crop formats, shared time/place/film response.
4. Material layers: selected secondary paper system, overlap order, physical artifacts, shallow shadows.
5. Typography and accent: exact short title, optional note, type materials, exact accent hue and marks.
6. Texture, mood, and avoids: paper fibers, photo softness, print defects, emotional temperature, explicit anti-identity.

Compile only renderable details. Do not mention source paths, analysis, or the reference images in the final prompt.

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
- Store the exact final prompt beside the image. Never overwrite an existing output; choose a new descriptive slug.
- Inspect the result once. Regenerate with one targeted correction if the page becomes dense, the photographs look unrelated, the paper disappears, the text dominates, or the output resembles an advertisement or UI.

## Hard Avoids

Always avoid:

- full-bleed stock landscape with no paper field
- unrelated generic mood-board photos
- dense maximal scrapbook with every artifact type
- digital card grid, app UI, dashboard, website mockup, or social template
- glossy 3D collage, heavy drop shadows, deep perspective, or floating paper spectacle
- commercial headline, logo, CTA, product placement, or influencer-ad styling
- kawaii stickers, emoji, cartoon, anime, or childish classroom craft
- neon rainbow palette, excessive beige, or dark desaturated gloom
- perfectly clean vector layout with no material variation
- long readable paragraphs, copied lyrics, reference-image quotes, usernames, watermarks, or signatures
- duplicate photographs pretending to be separate moments

## Output Format

Return the generated image, the exact final prompt, and:

- Layout: selected layout family
- Memory thread: anchor and support images
- Materials: secondary system, tertiary marks, and accent
- one short interpretation note

## Quality Gate

Before finalizing, check:

- Is the result a vertical botanical paper diary rather than a generic poster?
- Does visible paper occupy roughly 35%-65% of the canvas?
- Is there one readable attention route and no more than two dense zones?
- Do three to seven photos belong to the same walk, season, light, and film response?
- Is one photograph clearly primary?
- Are paper artifacts materially varied but hierarchically controlled?
- Is the title short, original, and subordinate?
- Is one accent color visible without becoming a sticker palette?
- Are botanical greens luminous and natural rather than muddy or neon?
- Does the image avoid copied text, brands, UI, stock mood board, and commercial layout?
- Did you generate and inspect the final raster image?
