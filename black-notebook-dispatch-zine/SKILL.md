---
name: black-notebook-dispatch-zine
description: "Generate prompts and finished raster images for monochrome open-notebook dispatch zines. Use when the user gives a theme, sentence, object, mood, article idea, photo, or content brief and wants a black-tabletop editorial notebook collage with a tilted white zine spread, handwritten Chinese annotations, large gray numeric index, xerox branch photo panel, label stickers, safety pin or paperclip details, dotted white pen, and sparse archive-field-note energy."
---

# Black Notebook Dispatch Zine

Turn the user's content into both:

1. a final image-generation prompt, and
2. a generated raster image made from that prompt.

## Source Grammar

Use this visual grammar as the style core:

- **Scene:** matte black tabletop or black void background with very high negative space.
- **Main object:** one open white notebook, folded zine, or loose paper spread, lying slightly angled in the lower or central field.
- **Page system:** white pages with black and gray print, small handwritten Chinese notes, curved annotation arrows, boxed callouts, and one large pale gray numeric index such as `1234567`.
- **Photo panel:** a bordered black-and-white xerox or photocopy panel of bare tree branches, winter shrubs, wires, or another sparse field-photo fragment.
- **Label system:** one large outlined sticker or label frame over the photo with a bold short Chinese headline, plus one tiny blue time pill such as `05:00:00` when a small color accent is useful.
- **Pin and tool:** a safety pin, paperclip, taped tag, or small pinned label near the top or side of the notebook; a white pen with black dots placed above or beside the spread.
- **Mood:** monochrome editorial dispatch, field-note evidence, quiet handmade zine, private observation, black-and-white stationery archive.

## Mode Policy

Use **Standard Mode** for all generation. Compile only the visual details that should become pixels. Do not include analysis prose, source filenames, or process notes inside the final image prompt.

## Standard Mode Prompt Compiler

Every prompt must describe a single finished still image, not a template or UI. Use the fields below in order.

### First-Principles Fields

1. **Canvas and Surface**
   - Vertical 3:5 poster or square editorial product shot.
   - Matte black tabletop or black paper background.
   - Orthographic or gentle overhead camera; no dramatic perspective.
   - The notebook occupies roughly 35%-60% of the frame, leaving large black negative space.

2. **Notebook Geometry**
   - Open white notebook, folded zine, or two-page paper spread.
   - Slight clockwise or counterclockwise tilt.
   - Pages are clean but tactile: paper fibers, soft shadows, tiny creases, subtle scan wear.
   - The spread should feel placed by hand, not digitally composited.

3. **Information Architecture**
   - Large pale gray numeric index, usually `1234567`, running across the top, right edge, or page center.
   - Curved arrows connect some numbers to handwritten note clusters.
   - Small printed boxes, dotted guides, stamp-like captions, and microtext create a field-note system.
   - Chinese handwriting should be visually present; keep important phrases short.

4. **Image Anchor**
   - Place one bordered black-and-white xerox photo panel on the lower page or crossing the gutter.
   - Convert the user's theme into a sparse photo fragment: bare branches, plant shadow, street wires, window reflection, document crop, object silhouette, empty chair, rain marks, or another quiet evidence-like subject.
   - Treat the panel with photocopy grain, low contrast, halftone, scan streaks, and slightly imperfect borders.

5. **Label and Accent**
   - Add one large outlined label/sticker frame over or near the photo panel.
   - Put a bold short Chinese headline inside the label, for example `临场发挥`, `现场记录`, `未寄出的信`, or a user-supplied phrase.
   - Use almost no color. A tiny muted blue time pill or sticker may appear as the only color accent, occupying less than 1% of the image.

6. **Pinned Detail and Pen**
   - Add a small safety pin, paperclip, taped label, or pinned note near the upper page or left side.
   - Add one white pen with black polka dots above the notebook or along one side.
   - These props should support scale and tactility; they must not become the main subject.

7. **Reproduction Texture**
   - Matte black background, soft diffuse light, low-to-medium contrast.
   - Paper fibers, xerox softness, gray ink, imperfect registration, hand-drawn arrow irregularity.
   - Realistic tactile still-life, but flat and editorial rather than glossy product photography.

8. **Emotional Temperature**
   - Quiet, private, investigative, diary-like, archival, slightly poetic.
   - The viewer should feel a found notebook dispatch before reading any exact text.

9. **Hard Avoids**
   - Avoid colorful scrapbook, cute stickers, commercial ad layout, UI, glossy mockup, neon, 3D render, cinematic spotlight, heavy depth of field, fashion editorial drama, dense unrelated collage, clean digital poster, perfect typesetting, or long readable paragraphs.

### Standard Prompt Shape

Write the final prompt as four compact paragraphs:

1. canvas, black surface, notebook size, camera angle, negative space
2. page architecture, numeric index, handwritten Chinese annotations, arrows
3. xerox photo panel, label headline, tiny blue time sticker, pin or paperclip, dotted white pen
4. material texture, mood, lighting, and avoid-list

Prefer precise visible instructions over abstract style words. If the user supplies no text, invent one short Chinese headline and one tiny time code.

## Variation Engine

Before writing the prompt, choose one option from each axis. For multiple images, vary at least three axes per image.

### Layout Family

- **right-index-spread:** notebook centered low; `1234567` runs vertically on the right page.
- **top-number-dispatch:** numbers stretch across the top; notes cascade downward.
- **lower-photo-ledger:** xerox photo dominates the lower page; label frame sits across it.
- **pinned-left-card:** small pinned label on the left page; photo panel on the right page.
- **gutter-crossing-panel:** photo and label cross the notebook fold.
- **pen-above-table:** white dotted pen floats above the spread in black negative space.

### Photo Fragment

- bare tree branches
- tangled winter shrubs
- telephone wires against white sky
- rain-streaked window
- cropped empty chair
- small document evidence photo
- plant shadow on paper
- blurred street corner photocopy

### Typography Mode

- large pale numeric index plus tiny handwriting
- boxed Chinese headline over photo
- curved arrows from numbers to notes
- stamp-like captions and dotted guide marks
- handwritten marginalia around the gutter
- sparse label stickers with one bold phrase

### Prop Mode

- safety pin through a tiny tag
- silver paperclip at page edge
- taped label with soft shadow
- dotted white pen above the notebook
- dotted white pen along the right side
- small binder clip cropped at an edge

### Accent Mode

- tiny muted blue time pill
- tiny blue inventory sticker
- no color, pure black/white/gray
- one pale blue registration mark

### Mood Mode

- field dispatch
- private diary
- winter archive
- late-night annotation
- quiet investigation
- unfinished manuscript
- classroom afterthought
- rain-day evidence

## Workflow

1. Determine mode.
   - Use Standard Mode.

2. Parse the user's content.
   - Identify the core subject, mood, exact text if supplied, and any reference image role.
   - For a complex idea, reduce it to one evidence-like photo fragment and one short Chinese label.
   - If no text is supplied, invent a concise Chinese headline of 2-6 characters plus optional tiny time code.

3. Select a variation recipe.
   - Pick layout, photo fragment, typography mode, prop mode, accent mode, and mood.
   - Keep the scene sparse. If the page becomes crowded, reduce microtext first.

4. Write the final image prompt.
   - Use the four-paragraph Standard Prompt Shape.
   - Include exact in-image text only for the short label, numeric index, and tiny time code.
   - Specify the notebook angle, page placement, photo panel position, and prop placement.

5. Generate the image.
   - Use the built-in image generation capability by default.
   - Do not stop after prompt-only unless the user explicitly asks for prompt-only.
   - If the result becomes a colorful scrapbook, glossy mockup, or clean digital poster, tighten the monochrome black-tabletop and tactile notebook language and regenerate once.

6. Return the image and prompt.

## Negative Constraints

Always avoid:

- full-bleed scene instead of tabletop notebook still-life
- colorful scrapbook, cute stickers, washi-tape overload, kawaii marks, anime style
- commercial headline hierarchy, product ad, logo, CTA, magazine cover polish
- clean UI, website mockup, app screen, vector infographic
- glossy product mockup, hard spotlight, dramatic cinematic lighting
- 3D rendering, CGI, neon, cyberpunk, excessive depth of field
- perfect digital typography, long clean readable paragraphs, generic lorem ipsum blocks
- many unrelated photos, flowers, tickets, or decorative stationery items
- color accents larger than a tiny blue label or mark unless the user explicitly asks

## Output Format

````markdown
**生成图**

![Black Notebook Dispatch Zine image](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Mode: Standard
- Recipe: [layout / photo fragment / typography / prop / accent / mood]
- [one short note about how the user's content became the notebook dispatch]
````

If generated images render directly without a file path, show the image normally and still include the final prompt.

## Quality Gate

Before finalizing, check:

- Did the prompt create a black tabletop or black-background still-life?
- Is there one open white notebook, folded zine, or loose two-page spread?
- Does the notebook sit slightly angled with large black negative space?
- Are large pale gray numbers such as `1234567` visible?
- Are handwritten Chinese notes, arrows, boxes, or label stickers part of the page system?
- Is there one bordered black-and-white xerox photo panel?
- Does the photo panel contain a sparse evidence-like fragment rather than a full scene?
- Is there a bold short Chinese headline in an outlined label frame?
- Is the blue accent tiny, or absent when pure monochrome is selected?
- Is there a safety pin, paperclip, tape detail, or dotted white pen for tactile scale?
- Does the image feel like a private archival notebook dispatch, not a digital poster?
- Did the prompt avoid colorful scrapbook, commercial, UI, glossy, 3D, neon, and dense collage aesthetics?
- Did you actually generate the image?

## Example Requests

- "用 $black-notebook-dispatch-zine 做一张关于雨夜观察的图"
- "Use $black-notebook-dispatch-zine to turn this sentence into a monochrome field notebook poster: 未寄出的信"
- "用 $black-notebook-dispatch-zine 根据这张照片生成黑底笔记本拼贴"
