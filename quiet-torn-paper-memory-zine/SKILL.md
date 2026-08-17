---
name: 静撕纸记忆
description: "【静撕纸记忆 / quiet-torn-paper-memory-zine】 Generate quiet torn-paper memory zine prompts and matching raster images from a user photo, object, meal, flower, pet, landscape, phrase, mood, or visual brief. Use when the user wants large aged-paper negative space, small torn photo fragments, translucent rice-paper tape, deckled paper edges, soft faded object photography, tiny serif captions, delicate orbit lines, dot/star registration marks, archival diary labels, calm beige paper texture, or reverse-engineered prompt structures based on gc-minimal-zine-poster-v0-1 with tactile memory-collage materials."
---

# Quiet Torn Paper Memory Zine

## Overview

Transform the user's content into a compact image-generation prompt, then generate a raster image unless the user explicitly requests prompt-only. This style keeps the sparse paper-poster discipline of `gc-minimal-zine-poster-v0-1`, but shifts the anchor treatment toward torn photo scraps, translucent tape, soft still-life fragments, and quiet diary-like labels.

## Source DNA

Use this reverse-engineered identity:

- **Canvas:** tall vertical 9:16, 4:7, or 3:5 phone-poster; flat scanned paper; no mockup, no tabletop perspective.
- **Paper field:** warm ivory, oatmeal, pale cream, or light gray handmade paper with fibers, specks, scratches, faint stains, soft edge aging, and diffuse scan lighting.
- **Negative space:** 70%-90% quiet paper. The layout should feel spacious, slow, and contemplative.
- **Image anchor:** one small object, photo, or scene fragment: canal at dusk, green apple, close pet face, quiet meal, flower branch, crescent scrap, seashell, bread, vase flower, ceramic flowers. Use one main anchor plus optional tiny secondary photo.
- **Material treatment:** torn/deckled photo paper, uneven square or oval cutout, translucent rice-paper tape, vellum patch, softened photo grain, muted natural color, frayed shadow just enough to show layers while staying flat.
- **Line system:** one or two fine gray curves, dotted path segments, thin vertical rules, tiny circles, star-cross marks, small black dots, minimal measurement-like ticks.
- **Typography:** tiny serif or typewriter captions with wide tracking: "GREEN MORNING", "DUSK CANAL / 03", "A quiet bloom remembers the rain." Keep text sparse and poetic.
- **Mood:** still, intimate, archival, hand-kept, slow morning, quiet meal, found object, faded memory, soft museum note.

Do not use commercial poster hierarchy, saturated color blocks, dense scrapbook clutter, RGB glitch, or polished product advertising. The subject should look physically attached to the paper, not composited as a clean UI asset.

## Workflow

1. Parse the input.
   - If a source image is supplied, preserve the subject and convert it into a small torn-photo or paper-specimen anchor.
   - If only text is supplied, choose one everyday object or memory fragment that can embody the theme.
   - Extract mood, exact text, season, time of day, material, and desired aspect ratio if provided.

2. Choose a recipe.
   - Select one layout family, one anchor material, one line-mark system, and one caption mode.
   - Vary geometry between generations: oval cutout, square scrap, dual photo, bottom-left specimen, upper-right fragment, etc.
   - Keep the number of physical elements low. Remove decoration before adding more.

3. Compile the final prompt.
   - Use the Prompt Compiler field order.
   - Specify paper tone, negative-space percentage, anchor scale and position, torn edge/tape treatment, line marks, tiny captions, print defects, and hard avoids.
   - Keep text short because image models distort long copy.

4. Generate the image.
   - Use built-in image generation by default.
   - If the result is too clean, too glossy, or too full, regenerate once with stronger aged-paper, small-anchor, torn-edge, and sparse-caption wording.
   - If the subject anchor is too tiny to recognize, regenerate once with it occupying about 10%-22% of the canvas.

5. Return the image, prompt, and selected recipe.

## Prompt Compiler

Write final prompts as four compact paragraphs:

1. **Canvas and paper:** vertical ratio, handmade paper tone, scan texture, negative-space percentage, flat lighting.
2. **Memory anchor:** subject, photo/object treatment, torn shape, size, placement, tape/vellum layer, optional secondary scrap.
3. **Marks and typography:** fine curves, dotted paths, star marks, rules, tiny serif captions, archive code, line weight and placement.
4. **Mood and avoids:** emotional temperature, print/scanning texture, and hard negative constraints.

Use this skeleton:

```text
[Canvas and paper paragraph]

[Memory anchor paragraph]

[Marks and typography paragraph]

[Mood and avoid-list paragraph]
```

## Variation Engine

Pick one layout family and one anchor material.

Layout families:

- **dual-torn-photo-memory:** two torn rectangular photo scraps overlap near lower-middle or center-left; one taller scene and one smaller detail; subtle tape behind.
- **single-object-center:** one softly photographed object sits around center or lower-middle on a translucent paper patch; tiny secondary monochrome photo in a corner.
- **oval-found-face:** one oval or circular torn crop placed upper-right; playful or uncanny close subject; sparse poem at left; small stamp-like detail lower-right.
- **quiet-meal-plate:** one food dish on a torn paper patch, centered low; small ingredient photo and utensil stamp as secondary elements.
- **flower-archive-pair:** one main floral photo scrap with a tiny echo scrap; botanical stamp or black specimen drawing nearby; dated vertical label.
- **tiny-night-fragment:** small dark square scrap with crescent or night detail in upper-right; huge empty paper; minimal caption and moon-orbit line.
- **sea-found-object:** shell or beach object on torn paper, small sea photo scrap lower-right, bird silhouette and tide-note captions.
- **handmade-bread-study:** bread or handmade object in lower-left photo scrap, wheat/photo card upper-right, tool stamp, tape strips.
- **paper-vase-bloom:** vase or single flower on layered torn paper in right-middle; second small botanical card lower-left; scissors or tool stamp optional.
- **ceramic-studies-cluster:** small cluster of ceramic/flower objects in lower-right with vellum patches; mostly empty upper field.

Anchor materials:

- muted color torn photograph
- faded monochrome mini photo
- soft object cutout on translucent paper
- deckled square paper specimen
- oval/circle rough photo crop
- rice-paper tape strip
- vellum overlay patch
- black ink object stamp

Caption modes:

- two-line poem in tiny serif
- uppercase archive label with slash number
- spaced small title words
- vertical date and weather note
- nearly textless with one catalog caption
- three separate micro labels around the page

Line-mark systems:

- long fine gray orbit curve
- short dotted path segment
- vertical measurement rule with tiny circles
- small four-point star marks
- scattered black ink dots
- faint circular construction line
- thin horizontal rule under a caption

## Reverse Prompt Patterns

Use these references for reverse-prompting similar images. Adapt subject, text, and placement.

- **Dusk canal scraps:** warm ivory paper, two overlapping torn canal photos near lower-left center, sunset reflections in muted peach and charcoal, translucent tape above, tiny serif poem at right, thin gray rules and a loose curved line, label "DUSK CANAL / 03".
- **Green apple morning:** pale handmade paper, single soft green apple centered on a translucent torn patch, tiny leaf stamp upper-right, small faded orchard photo lower-left, sparse labels "GREEN MORNING", "A QUIET BITE", "SLOW GROWING", long gray curve.
- **Found pet face:** oatmeal paper, oval torn close-up pet face in upper-right, translucent tape on edge, small ghost face stamp lower-right, tiny poem at left, star marks and dotted line fragments.
- **Quiet meal:** cream paper, one food dish on a rough translucent base centered low, tiny wheat photo lower-left, chopstick or utensil ink stamp lower-right, captions "A QUIET MEAL", "SLOWLY, SAVORED", "WARM TABLE".
- **Rain bloom archive:** large floral photo scrap upper-left/middle with smaller echo scrap behind, black botanical line stamp to the right, vertical date label, poem near center, small star marks and dotted rules.
- **Crescent fragment:** mostly empty aged paper, tiny black torn square with crescent in upper-right, rice-paper tape on one side, thin circular orbit line, caption "Night begins with a thin line", catalog "CRESCENT / 04".
- **Tide notes:** shell on pale torn paper center-left, small ocean horizon photo lower-right taped with a scrap, bird silhouette, tide labels, large sweeping curve.
- **Bread and mornings:** bread photo scrap lower-left with broad translucent tape, wheat card upper-right, knife/scissors stamp, captions "BREAD & MORNING", "MADE BY HAND", "SIMPLE THINGS".

## Color and Texture Rules

- Keep the palette low-chroma: ivory, oatmeal, gray ink, charcoal, faded sage, muted pink, dusty peach, weathered brown, soft sea gray.
- Avoid one strong color block. Color should live inside the photo/object, not dominate the page.
- Use soft matte shadows only to reveal physical layering. The poster must still read as flat scanned paper.
- Torn edges should be visible: deckled fibers, uneven ragged borders, small paper thickness, worn photo grain.
- Tape and vellum must be translucent, fibrous, and low contrast, never glossy plastic.

## Typography

- Use tiny serif, typewriter, or monospaced text with wide tracking.
- Keep captions short: one title, one poetic line, one archive code, or 2-3 scattered labels.
- Allow imperfect readability for micro labels, but keep main phrase legible.
- Avoid big headline hierarchy, commercial slogans, logos, CTAs, long paragraphs, and decorative script.

## Negative Constraints

Always avoid:

- dense scrapbook or junk journal clutter
- bright saturated poster colors, neon, RGB glitch, cyberpunk
- commercial product ad, brand campaign, logo lockup, CTA
- glossy tape, strong cast shadows, 3D paper mockup, desk perspective
- cute cartoon, sticker pack, anime, vector illustration
- full-bleed photo scene or centered large hero image
- modern clean UI white, clinical minimalism, plain blank digital background
- long clean readable text blocks

## Output Format

````markdown
**生成图**

![Quiet torn-paper memory zine image](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Recipe: [layout family / anchor material / caption mode / line-mark system]
- Source interpretation: [one short note]
````

If the user asks for reverse prompting only, omit image generation and return the analyzed structure plus the final prompt.

## Quality Gate

Before finalizing, check:

- Does the image use the four-paragraph Prompt Compiler?
- Does 70%-90% of the canvas read as warm aged paper?
- Is there one clear memory anchor plus at most one or two tiny supporting scraps?
- Are torn edges, tape, vellum, or paper layers physically visible but subtle?
- Are line marks and dots sparse, fine, and archival rather than decorative clutter?
- Is typography tiny, serif/typewriter-like, and poetic?
- Does the image avoid commercial hierarchy, saturated color blocks, glossy mockups, dense scrapbook, cartoons, and full-bleed photography?
