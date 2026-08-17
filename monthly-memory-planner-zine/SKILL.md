---
name: monthly-memory-planner-zine
description: Generate prompts and finished raster images for editorial monthly journal calendar collages, memory-dump planners, scrapbook calendar pages, black-border social posts, clipped paper calendars, handwritten annotations, small photo grids, stickers, product/event notes, and diary-like lifestyle recap layouts. Use when the user gives a month, season, mood, photos, memories, products, events, or reference images and wants a visual monthly planner / journal zine rather than a sparse single-anchor paper poster.
---

# Monthly Memory Planner Zine

Turn the user's month, memories, photos, product/event notes, or mood into:

1. a final image-generation prompt, and
2. a generated raster image made from that prompt.

Use the `imagegen` skill for generation or editing. Prefer local CLI/API/pptoken only when the user explicitly asks for that path.

## Style Thesis

Create vertical calendar-journal posters that feel like a social-media memory dump, planner page, or boutique campaign calendar photographed/scanned as a flat zine object. This skill borrows `gc-minimal-zine-poster-v0-1`'s prompt-compiler discipline, but replaces the single tiny anchor with a controlled calendar grid, multiple small photo cells, hand notes, sticker marks, and tactile paper layout.

## Reference-Derived Structure

Use these rules as the core visual grammar:

- **Frame:** vertical phone-poster, usually 3:5 or 4:5. Often a centered white/cream paper calendar sits inside a black screenshot-like margin or over a blurred lifestyle photo background.
- **Main object:** one month-view calendar, memory grid, or journal page. It may be a clean UI-like calendar, printed paper sheet, spiral notebook page, clipped board, rug-backed card, or scrapbook layer.
- **Grid logic:** use 5-7 columns and 4-6 rows; cells can hold date numbers, tiny photos, polaroids, product cutouts, hand notes, doodles, icons, or empty whitespace. Lines should be thin and slightly imperfect.
- **Photo logic:** use small square/rectangular lifestyle photos: food, cat, sea, trees, city walks, outfit mirror shot, cafe cup, gifts, shopping item, album cover, wall texture, blue sky, dog, flowers. Keep them varied but organized.
- **Typography:** mix one large serif/italic month title, small sans weekday labels, monospaced/typewriter captions, and casual handwritten notes. Text should be short and visual; do not rely on long exact readability.
- **Marks:** circles around dates, arrows, sticky notes, paper clips, starbursts, tape, stickers, stamp marks, handwritten underlines, tiny icon drawings, and clipped product photos.
- **Texture:** flat scan/photo of paper, subtle grain, washed whites, faint shadow, slight blur, phone screenshot crop, black outer border, paper fibers, thin grid lines.
- **Color:** mostly cream, white, black, gray, faded photo colors. Use one accent system per image: cobalt/blue, red, tomato/coral, lime green, dusty blue, burgundy, or yellow.

## Prompt Compiler

Write the final image prompt as four compact paragraphs:

1. **Canvas and page object:** frame ratio, black border or full paper, page type, month title, grid/page placement.
2. **Calendar/journal content:** number of cells or collage structure, kinds of photos/cutouts, notes, icons, doodles, and where the attention lands.
3. **Typography and accent color:** title style, weekday/date style, handwritten/typed notes, chosen accent hue and how it appears.
4. **Material and constraints:** scanned paper, phone screenshot/poster feel, texture, hard avoids.

Make text requests concrete but short. If the user gives exact labels, include only the most important words; image models distort long handwriting and small calendar text.

## Variation Engine

Choose one option from each axis before writing the prompt.

### Layout

- **clean-month-grid:** centered clean calendar grid with small photos in selected dates and lots of open cells
- **journal-dump-scatter:** no full grid; floating photo squares and repeated typewriter phrase on cream paper
- **paper-on-photo:** white calendar sheet over a blurred monochrome or muted outdoor photo background
- **clipboard-planner:** calendar page clipped by a bright red binder clip, visible black margin
- **spiral-notebook:** top spiral binding, planner grid printed on textured notebook paper
- **fashion-shopping-calendar:** sparse shopping/date planner with product cutouts and red handwritten notes
- **handdrawn-campaign-calendar:** rough pencil/marker grid with doodles, starbursts, release/event blocks
- **scrapbook-month-recap:** calendar grid partially covered by polaroids, receipts, cake, camera, drinks, and handwritten notes
- **ornate-rug-card:** rounded calendar card centered over patterned rug/textile background

### Page Density

- airy: 70%-85% quiet paper, few photos, sparse notes
- balanced: 40%-60% calendar/grid filled, clear breathing room
- dense: many cells filled, stickers and handwritten notes, still readable as a calendar
- cropped-detail: zoomed-in corner of a larger calendar, black margin or background visible

### Typography Mode

- large elegant serif month title
- bold clean sans month title
- italic serif `Month Journal`
- handwritten title plus small printed weekdays
- rough marker campaign title
- typewriter phrase repeated across the sheet
- minimal thin white overlay calendar on photo

### Accent System

- cobalt-blue label bars and captions
- red handwritten notes and circles
- tomato-red binder clip or header
- lime-green sticky note
- dusty-blue polaroid/card accents
- burgundy holiday handwriting
- yellow lantern/product note accent
- mostly monochrome with one small accent mark

### Content Motifs

- sea, birds, blue sky, shoreline
- cat, food, cafe cup, pizza, dessert
- shopping item, bag, shoes, jacket, matcha
- concert/album/release schedule
- pop-up planner and marketplace notes
- family time, cake, camera, receipts
- city walk, tree shadows, balcony, outdoor path
- product campaign calendar with shipping/promo dates

## Generation Workflow

1. Parse the user's month, theme, photos, or memory list into a month title, mood, and 5-12 visual memory cells.
2. Choose a recipe from the Variation Engine. If reference images are provided, preserve their layout family, density, typography, and accent system before inventing content.
3. Compile the four-paragraph prompt. Explicitly state `vertical calendar journal poster`, `thin grid`, `small lifestyle photo cells`, `handwritten notes`, and `flat scanned paper` unless the selected layout intentionally omits a full grid.
4. Generate the raster image. Save final workspace outputs under `output/imagegen/monthly-memory-planner-zine/`.
5. Inspect the output. Regenerate once if it becomes a generic scrapbook, clean digital calendar UI, illegible clutter, stock-photo collage, or a sparse single-object poster.

## Text Guidance

Use short, imageable text:

- Month titles: `November Journal`, `July Dump`, `September 2025`, `December`, `October 2025`
- Short captions: `ABOUT BLUE`, `BLANK DAY`, `PAY DAY`, `FAMILY'S DAY`, `KEEP SWIPING`, `Notes:`
- Hand notes: keep to 2-6 words where possible.
- For bilingual or non-Latin notes, request visual handwritten snippets rather than exact long paragraphs.

Do not ask the model to render a fully accurate functional calendar unless the user explicitly requires accuracy. Prioritize aesthetic calendar-journal feeling over exact day/date correctness.

## Hard Avoids

Avoid glossy app UI, perfect vector calendar, corporate schedule template, generic Canva poster, dense unreadable text walls, full-bleed scenic illustration, cinematic depth, 3D render, neon cyberpunk, cute mascot focus, anime poster, luxury ad layout, hard product ad CTA, clean white webpage, and too many unrelated accent colors.

## Output Format

```markdown
**生成图**

![Monthly memory planner zine image](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Recipe: [layout / density / typography / accent / motifs]
- [one short note on how the user's month or memories were translated]
```

## Quality Gate

Before finalizing, check:

- Does it read as a monthly journal/planner page, not a generic collage?
- Is there a clear calendar grid, memory grid, or deliberate journal dump structure?
- Are photo cells small, varied, and placed with editorial rhythm?
- Does typography mix month title, weekday/date labels, and handwritten/typed notes?
- Is there one dominant accent system rather than many competing colors?
- Does the page have paper/scan/phone-post texture, not clean vector UI?
- Are black margins, clipping, notebook binding, or background layers used only when they support the selected recipe?
- Is the image visually coherent at mobile thumbnail size?
- Did the prompt avoid long exact text, glossy UI, corporate calendar templates, 3D, anime, and commercial ad hierarchy?
