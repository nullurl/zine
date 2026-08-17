---
name: folded-daily-archive-zine
description: "Generate prompts and finished raster images for folded-paper daily archive zines. Use when the user gives an ordinary object, street moment, drink, notebook, travel note, garden light, city light, small memory, photo, mood, sentence, or content brief and wants a sparse cream folded-paper poster with visible grid fold creases, one or several small rectangular everyday photos, black Swiss-style sans typography, archive number/date labels, tiny captions, large negative space, and quiet daily-life documentation."
---

# Folded Daily Archive Zine

Turn the user's content into both:

1. a final image-generation prompt, and
2. a generated raster image made from that prompt.

## Source Grammar

Use this visual grammar as the style core:

- **Surface:** off-white or warm cream poster paper with visible vertical and horizontal fold creases, subtle wrinkles, scuffs, soft dents, and slightly rounded or worn paper edges.
- **Grid:** implicit folded-paper grid, usually 3 columns by 4 rows or 3 by 3, created by crease lines rather than drawn rules.
- **Image system:** one small rectangular photo, or a sparse set of 3-5 small photos, each showing an ordinary real moment: milk tea, street object, garden light, city lights, travel notebook, paper stamps, leaves, lamp, sidewalk detail.
- **Typography:** small black sans-serif text, left-aligned, clean but not corporate; bold uppercase title only when useful; tiny archive number/date; short lowercase captions.
- **Text motifs:** `MY DAILY ARCHIVE`, `2024`, `archive no. 0524`, `simple things. real moments. kept on paper.`, plus subject captions like `MILK TEA`, `CITY LIGHTS`, `STREET OBJECT`.
- **Composition:** lots of empty cream paper; image and caption cluster sits near the upper center, mid-center, left third, or in a loose multi-photo grid; footer labels sit in bottom corners.
- **Mood:** quiet everyday archive, paper-kept memory, ordinary days worth keeping, minimal zine poster, personal record.

## Mode Policy

Use **Standard Mode** for all generation. Compile only the visual details that should become pixels. Do not include analysis prose, source filenames, or process notes inside the final image prompt.

## Standard Mode Prompt Compiler

Every prompt must describe a single finished poster image, not a UI, website, or digital template.

### First-Principles Fields

1. **Canvas and Folded Paper**
   - Vertical 3:5 poster by default.
   - Full-frame off-white folded paper, with visible crease grid and tactile wrinkles.
   - No decorative border; the paper itself fills the frame.
   - Keep 70%-90% calm paper negative space for single-photo layouts; keep 55%-75% negative space for multi-photo layouts.

2. **Attention Geometry**
   - Place one small photo cluster in a deliberate position: upper center, central column, left third, lower-left, or a sparse 2-column/3-column archive spread.
   - Avoid edge-hugging unless placing tiny footer archive text.
   - Let fold intersections pass through or near the photo, making the poster feel physically folded.

3. **Everyday Photo Anchor**
   - Convert the user's theme into one ordinary photographable subject.
   - Suitable anchors: takeaway cup, street sign/object, garden leaves with small lamp glow, city lamps at dusk, travel notebook, stamped paper, meal, window, chair, receipt, stationery, sidewalk plant, bag, tiny personal object.
   - Render the photo as a real small rectangular print with slight grain and natural color; it should feel like a phone snapshot kept on paper.

4. **Archive Typography**
   - Use black sans-serif type only; no decorative fonts.
   - Main subject caption: one short uppercase phrase, 1-3 words.
   - Subtitle: two short lines, lowercase or sentence case, quiet and observational.
   - Optional bold title block: `MY DAILY ARCHIVE` in the upper left.
   - Footer: `2024` and `archive no. 0524` or a user-supplied date/number.
   - Side note or lower-right motto: `simple things. real moments. kept on paper.`

5. **Color Logic**
   - Paper stays warm cream, gray-white, or slightly yellowed.
   - Typography stays black or dark charcoal.
   - Color exists mainly inside the photo: green leaves, amber tea, blue evening sky, yellow street sign, warm lamp.
   - Do not add separate graphic color blocks or high-chroma poster accents.

6. **Reproduction Texture**
   - Paper fibers, fold shadows, crease highlights, small tears, soft dents, dust, and scanned-poster grain.
   - Photo edges are clean rectangles, not Polaroid frames unless user asks.
   - Lighting is diffuse and flat, like a photographed folded zine sheet.

7. **Emotional Temperature**
   - Quiet, simple, personal, ordinary, archived, still, modest, real.
   - The viewer should feel a mundane moment saved carefully, not a designed campaign.

8. **Hard Avoids**
   - Avoid collage overload, stickers, tape, handwriting, scrapbook, colorful zine chaos, glossy mockup, UI, magazine layout, commercial ad, large decorative typography, torn-paper pile, 3D render, cinematic lighting, neon, cartoon, or long text blocks.

### Standard Prompt Shape

Write the final Standard Mode prompt as four compact paragraphs:

1. canvas, off-white folded paper, crease grid, negative space, camera/scan feel
2. everyday photo anchor, photo size/position, subject treatment
3. typography system, exact short captions, archive number/date, motto/footer placement
4. paper/photo texture, mood, lighting, and avoid-list

Prefer concrete placement and text instructions. If the user supplies no text, invent one uppercase subject label, a two-line observational subtitle, and an archive number.

## Variation Engine

Before writing the prompt, choose one option from each axis. For multiple images, vary at least three axes per image.

### Layout Family

- **single-center-photo:** one small photo centered slightly above the middle, caption underneath.
- **upper-left-title-photo:** bold `MY DAILY ARCHIVE` in upper left, photo below or to the right.
- **lower-footer-balance:** photo in upper center, archive number bottom left, motto bottom right.
- **multi-photo-archive:** 3-5 small photos distributed across the folded grid with captions under each.
- **left-column-record:** title and small copy on left, one larger photo in left or center column.
- **quiet-right-photo:** photo in upper-right or mid-right with wide blank left paper.
- **travel-page-feature:** photo of notebook/stamps or paper record, caption block beneath.
- **object-specimen-sheet:** one ordinary object photo treated like a daily specimen.

### Photo Subject

- milk tea or takeaway drink
- street object or yellow sign
- garden glow or leaves
- city lights at dusk
- travel notes and stamps
- open notebook page
- sidewalk plant
- cup on table
- small receipt or ticket
- window or lamp
- paper object
- quiet snack or meal

### Typography Mode

- bold archive title in upper left
- subject label and two-line subtitle
- bottom-left date and archive number
- lower-right motto
- tiny scattered labels only
- multi-photo caption set
- clean lowercase observational copy

### Fold Texture

- 3-by-4 fold grid
- 3-by-3 fold grid
- strong horizontal center crease
- subtle vertical center crease
- wrinkled corner and paper scuffs
- soft worn edge and dents
- photographed folded sheet shadows

### Photo Treatment

- crisp phone snapshot
- slightly faded print
- warm indoor snapshot
- dusk blue photo
- green garden photo
- paper/document photo
- close-up object crop
- small archive print

### Mood Mode

- daily archive
- ordinary day
- simple things
- kept on paper
- evening slows down
- comfort in a cup
- ready to go
- worth keeping
- quiet green
- travel notes

## Workflow

1. Determine mode.
   - Use Standard Mode.

2. Parse the user's content.
   - Identify the ordinary subject, mood, exact text if supplied, and any reference image role.
   - Convert abstract ideas into one everyday photo anchor rather than an illustrated metaphor.
   - If no text is supplied, invent a short subject label, two-line subtitle, motto, and archive number.

3. Select a variation recipe.
   - Pick layout, photo subject, typography mode, fold texture, photo treatment, and mood.
   - Keep the composition sparse. If the poster feels empty, strengthen the fold texture or typography placement before adding decorative elements.
   - For batches, alternate between single-photo and multi-photo archive layouts.

4. Write the final image prompt.
   - Use the four-paragraph Standard Prompt Shape.
   - Specify exact photo count, photo position, caption placement, fold grid, footer labels, and motto.
   - Keep exact in-image text short and plausible.

5. Generate the image.
   - Use the built-in image generation capability by default.
   - Do not stop after prompt-only unless the user explicitly asks for prompt-only.
   - If the result becomes a scrapbook, glossy design mockup, or colorful commercial poster, tighten the folded paper, sparse black typography, small photo, and archive constraints and regenerate once.

6. Return the image and prompt.

## Negative Constraints

Always avoid:

- scrapbook collage, stickers, tape, handwritten notes, torn-paper piles, decorative stationery overload
- commercial ad, brand campaign, logo/CTA, magazine cover, poster headline hierarchy
- clean UI, app screen, website mockup, digital template
- glossy product mockup, 3D render, cinematic lighting, hard shadows, dramatic depth of field
- neon, cyberpunk, high-chroma gradients, colorful graphic blocks
- cute cartoon, anime, kawaii illustration, fashion editorial drama
- full-bleed photo background instead of folded paper
- too many photos, long text, perfectly typeset paragraph blocks

## Output Format

````markdown
**生成图**

![Folded Daily Archive Zine image](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Mode: Standard
- Recipe: [layout / photo subject / typography / fold texture / photo treatment / mood]
- [one short note about how the user's content became the daily archive poster]
````

If generated images render directly without a file path, show the image normally and still include the final prompt.

## Quality Gate

Before finalizing, check:

- Did the prompt create full-frame off-white folded paper with visible crease grid?
- Does the poster preserve large negative space?
- Is there one small everyday photo, or a sparse set of 3-5 photos?
- Is the subject ordinary and photographable rather than symbolic or illustrated?
- Is typography black, sans-serif, sparse, and left-aligned?
- Are short captions, date, archive number, or motto included?
- Does the image feel like a personal daily archive kept on paper?
- Did the prompt avoid stickers, handwriting, scrapbook, UI, commercial ad, glossy mockup, 3D, neon, and full-bleed photo aesthetics?
- Did you actually generate the image?

## Example Requests

- "用 $folded-daily-archive-zine 做一张关于奶茶的日常档案图"
- "Use $folded-daily-archive-zine to turn 'city lights' into a folded daily archive poster."
- "用 $folded-daily-archive-zine 根据这张街头物件照片生成极简折痕纸海报"
