---
name: monochrome-archive-stationery-zine
description: "Generate monochrome archival stationery zine board prompts and matching raster images. Use when the user gives a theme, brand mood, object, phrase, reference image, publication idea, music/art/fashion/architecture concept, or visual brief and wants a black-ground display of grayscale printed matter: envelopes, tickets, letterheads, labels, book covers, folded leaflets, invoices, barcodes, microtypography, Swiss/modernist editorial grids, archival paper texture, and restrained experimental typography."
---

# Monochrome Archive Stationery Zine

Turn the user's content into both:

1. a final image-generation prompt, and
2. a generated raster image made from that prompt.

## Source Grammar

This style fuses Minimal Zine Poster v0.1's restraint with a different object system: not a single quiet paper poster, but a photographed/scanned black-board arrangement of printed artifacts. The references share these stable traits:

- **Frame:** vertical phone-poster canvas, usually 3:4 or 3:5, with a deep black background and one or two darker black rectangular fields.
- **Objects:** off-white, grey, or charcoal printed matter arranged as stationery systems: letterheads, envelopes, cards, labels, tickets, sleeves, folded brochures, book covers, invoices, barcode strips, photo cards, and specimen sheets.
- **Composition:** asymmetrical clusters with large dead space; objects are aligned by invisible grid edges, stacked, overlapped, or separated into upper/lower boards.
- **Scale:** 2-8 artifacts per canvas. One dominant object or pair establishes the hierarchy, while small cards, strips, spines, or micro-panels add archival rhythm.
- **Typography:** Swiss grotesk, condensed sans, typewriter/OCR, serif book titles, vertical labels, large cropped initials, bilingual overlays, tables, dates, item numbers, and dense microtext blocks.
- **Material:** matte paper, grey chipboard, photocopy grain, dust, scan noise, stamped marks, fold lines, perforations, punched holes, string closures, torn tape, barcode ink, and soft shadows.
- **Color:** default near-monochrome black, white, warm grey, and cool grey. Optional one restrained industrial accent such as safety orange tape, blue stamp, red registration mark, or tiny cream label; never make the image colorful.
- **Mood:** archival, institutional, quiet, precise, editorial, design-school, gallery identity, small press, art-book, invoice, catalog, or mail-room.

## Mode Policy

Use **Standard Mode** for all generation. Compile only renderable visual instructions into the final prompt. If the user asks for "same structure", "reverse prompt", or supplies references, extract composition logic and material treatment; do not copy exact brand names, readable addresses, copyrighted layouts, or personal information from the references unless the user explicitly provides text to use.

## Standard Prompt Compiler

Write the final prompt as four compact paragraphs in this order:

1. **Canvas and Display Field**
   - State the vertical frame, black background, flat scanned/catalog presentation, and amount of empty space.
   - Specify whether there is one large black field, two offset black fields, or a full matte black background.

2. **Artifact System and Layout**
   - Convert the user's theme into a set of printed objects.
   - State object count, dominant artifact, secondary artifacts, stacking, overlap, gaps, alignment, and position.
   - Use concrete object language: envelope, ticket strip, letterhead, business card, receipt, book spine, CD sleeve, label, folded leaflet, calendar card, punched specimen, invoice, catalog spread.

3. **Typography, Marks, and Material Detail**
   - Define type behavior: oversized cropped word, vertical side label, tiny archive caption, barcode, tabular date, invoice columns, multilingual text, ghosted logo, or dense microtext.
   - Define reproduction effects: xerox grain, halftone, paper fibers, low-contrast ink, embossed blind type, rough edges, perforation holes, folds, tape, string, stamp, scan dust, slight misregistration.

4. **Tonal Logic and Hard Avoids**
   - State monochrome grey palette and any one optional accent, with approximate share.
   - Define the mood and negative constraints.

Keep prompts concrete and imageable. Avoid long aesthetic essays.

## First-Principles Fields

Every prompt must answer:

1. **What is the display surface?**
   - deep black archival background; photographed or scanned flat lay; matte, no glossy mockup.

2. **How much is empty?**
   - 45%-75% black negative space. The cluster should not fill the frame like a commercial collage.

3. **What printed artifacts carry the concept?**
   - choose 2-8 artifacts. Tie them to the user's subject through labels, captions, coded marks, or object choice.

4. **What is the hierarchy?**
   - one dominant paper piece, one supporting strip/card/panel, and optional small archival fragments.

5. **How does type behave?**
   - typography is part of the image, not just readable information. Let text rotate, crop, stack, become a block, run vertically, sit in tables, or dissolve into microtext.

6. **What material process makes it authentic?**
   - paper grain, ink absorption, fold shadows, print wear, scan noise, barcode blur, punched holes, tape wrinkles, embossed text, or perforated edges.

7. **What is the color logic?**
   - near-monochrome by default. If color is useful, use one small utilitarian accent only: orange label/tape, blue stamp, red mark, or muted off-white card. Keep it under 3% of the canvas.

8. **What should be avoided?**
   - no bright multi-color collage, cute stickers, scrapbook clutter, brand ad, logo lockup, CTA, glossy product photography, 3D render, cinematic lighting, realistic office desk, hands, plants, coffee, lifestyle props, neon, gradients, or clean web UI.

## Variation Engine

Choose one option from each axis before writing the prompt.

### Layout Family

- **stationery-cascade:** overlapping letterhead, envelope, card, and invoice cluster
- **ticket-strip-system:** long horizontal strips with tiny captions, dates, and repeated marks
- **two-board-archive:** upper and lower black fields, each holding separate artifact systems
- **book-object-row:** covers, spines, page block, and edition marks arranged like a catalog
- **folded-leaflet-float:** one folded brochure at an angle plus strict side label
- **label-stack:** repeated textile/product labels, one inverted or offset
- **specimen-card-grid:** cards, photo crops, punched holes, and measurement marks
- **identity-system-flatlay:** envelope, business card, letterhead, stamp, address block, and oversized initials
- **poster-quartet:** 3-4 independent typographic posters placed with large gaps
- **single-artifact-monolith:** one large sheet or envelope dominating the frame with one small companion

### Artifact Inventory

- letterhead and envelope
- folded brochure or leaflet
- receipt, invoice, or order form
- ticket strip or admission band
- book cover, book spine, or catalog page
- CD sleeve, record insert, or barcode panel
- textile label or care tag
- business card and stamp block
- calendar card or date grid
- punched specimen sheet
- grayscale photo crop or xerox image window
- torn tape, string closure, or paper tab

### Typography Mode

- oversized cropped sans word
- tiny upper-corner institutional captions
- vertical spine/side label
- typewriter/OCR inventory text
- dense justified microtext block
- bilingual overlay with one heavy headline
- serif title paired with grotesk metadata
- barcode plus numeric code
- rotated or inverted label
- blind-embossed low-contrast lettering

### Graphic Mark Mode

- black circle punch or circular void
- barcode or QR-like linear mark
- dotted perforation row
- ruled table grid
- thin measurement ticks
- geometric registration corners
- photocopied landscape or architecture crop
- moire/halftone texture block
- tape strip or folded paper seam
- stamp square or postal box

### Material Mode

- grey chipboard grain
- warm off-white stationery
- xeroxed white paper
- charcoal book cloth
- translucent vellum overlay
- thermal receipt paper
- rough recycled card
- glossy-but-flattened CD sleeve
- wrinkled tape
- embossed heavy stock

## Standard Prompt Shape

Use this exact shape:

```text
Vertical 3:4 or 3:5 monochrome archival zine board on a deep matte black background, flat scanned/catalog flat-lay view, [45%-75%] black negative space, [layout family] positioned [placement], no outer frame.

For [user theme], arrange [artifact count] printed artifacts: [dominant artifact] as the main mass, plus [secondary artifacts]. Describe exact stacking, overlap, alignment, cut corners, folds, punched holes, strips, cards, or spines.

Use [typography mode] with invented short text based on the theme, tiny archive metadata, dates, codes, barcode/table/grid marks, and [graphic mark mode]. Materials show [material mode], xerox grain, paper fibers, scan dust, low-contrast ink, soft contact shadows, slight misregistration.

Near-monochrome palette of black, charcoal, white, warm grey, and cool grey; optional [accent color/form] occupying under 3% of the canvas. Quiet institutional art-book mood. Avoid colorful collage, clean ad design, logo lockups, CTAs, lifestyle props, 3D render, glossy mockup, neon, gradients, cute illustration, and full-bleed scene.
```

## Workflow

1. Parse the user's brief.
   - Identify subject, mood, exact text if supplied, object domain, and whether reference images are structural or content references.
   - If no text is supplied, invent short artifact text: 1 title, 1 date/code, and 1-2 metadata fragments.

2. Select a recipe.
   - Pick layout family, artifact inventory, typography mode, graphic mark mode, material mode, and optional accent.
   - Change layout materially between batch outputs. Do not only swap words.

3. Write the final prompt.
   - Use the Standard Prompt Shape.
   - Keep exact in-image text short. Image models distort long text; use microtext as texture when needed.
   - Use invented names and addresses unless the user supplies approved copy.

4. Generate the image.
   - Use image generation by default.
   - If the user asks for prompt-only, return only the prompt and recipe.
   - If the image becomes too colorful, too clean, too commercial, or too full, regenerate once with stronger monochrome, black negative space, and archival material wording.

5. Return the image and prompt.

## Negative Constraints

Always avoid:

- copying visible brand systems from references unless explicitly requested and permitted
- readable personal addresses, phone numbers, emails, or private order details from reference images
- commercial product advertisement hierarchy
- luxury mockup lighting, desk props, hands, plants, coffee, or lifestyle staging
- colorful scrapbook, stickers, washi-tape decoration, cute zine collage, anime, or kawaii style
- glossy 3D renders, perspective-heavy mockups, cinematic shadows, depth of field, neon, gradients
- full-bleed photography or scenic poster layout
- clean digital UI whitespace instead of printed paper surfaces
- too many colors or more than one accent hue
- long perfectly readable paragraph text

## Output Format

````markdown
**生成图**

![Monochrome archival stationery zine board](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Mode: Standard
- Recipe: [layout / artifacts / typography / graphic mark / material / accent]
- [one short note about how the user's theme became printed artifacts]
````

If generated images render directly without a file path, show the image normally and still include the final prompt.

## Quality Gate

Before finalizing, check:

- Did the prompt use a black-ground archival board rather than a white poster?
- Is there 45%-75% black negative space?
- Are there 2-8 printed artifacts with a clear hierarchy?
- Does the arrangement use grid alignment, overlap, or deliberate gaps?
- Are typography, metadata, marks, and microtext integrated into the artifacts?
- Is the palette near-monochrome, with at most one small utilitarian accent under 3%?
- Are paper grain, scan noise, soft shadows, fold lines, or print wear visible?
- Does the image avoid commercial ad, lifestyle flat-lay, glossy mockup, 3D render, neon, and cute collage aesthetics?
- If references were supplied, did the prompt borrow structure and material grammar without copying private or brand-specific text?
- Did you actually generate the image unless the user asked for prompt-only?

## Example Requests

- "用 $monochrome-archive-stationery-zine 做一张关于建筑边界的黑白档案文具图"
- "根据这张参考图，反推一条同结构的 prompt，不要生成图"
- "把我的乐队专辑概念做成灰度 CD sleeve + barcode + ticket strip 的 zine board"
