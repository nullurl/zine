---
name: 手写便签
description: "【手写便签 / handwritten-paper-note-zine】 Generate handwritten paper-note zine poster prompts and matching raster images. Use when the user gives a theme, sentence, mood, event, memory, photo, object, exhibition, brand note, or poetic brief and wants a quiet off-white paper poster with naive handwritten typography, sparse doodle lines, small photo inserts, crayon or marker accents, delicate editorial metadata, and large airy negative space."
---

# Handwritten Paper Note Zine

Turn the user's content into both:

1. a final image-generation prompt, and
2. a generated raster image made from that prompt.

## Source Grammar

This style fuses Minimal Zine Poster v0.1's sparse paper discipline with a hand-authored note system. The references share these stable traits:

- **Surface:** off-white, cream, pale grey, or lightly speckled paper; flat scanned poster view; no dark background, frame, glossy mockup, or heavy shadow.
- **Space:** 65%-90% quiet paper. The composition often feels underfilled, with a few handwritten islands and one loose visual anchor.
- **Writing:** naive hand lettering, shaky uppercase, scribbled words, underlines, crossed-out phrases, circled words, tiny serif/grotesk event metadata, bilingual fragments, and deliberately uneven spacing.
- **Drawing:** simple black-line doodles, stick figures, walking people, hands, vases, flowers, paths, fan outlines, border boxes, arrows, and small symbolic marks.
- **Image anchor:** one small grayscale or faded color photo crop, a childlike floral crayon drawing, a thin-line scene, or a hand-drawn conceptual diagram.
- **Color:** mostly black ink on warm paper. Optional childlike accent lines in blue, red, teal, green, yellow, or olive, usually marker/crayon and slightly imperfect.
- **Mood:** diary-like, workshop flyer, studio sale note, personal manifesto, small festival poster, field note, memory page, poetic school handout, casual gallery announcement.

## Mode Policy

Use **Standard Mode** for all generation. Compile only concrete visual details into the final prompt. If the user supplies reference images, borrow structure and material grammar; do not copy private contact details, real addresses, logos, or brand text unless the user explicitly provides approved text.

## Standard Prompt Compiler

Write the final prompt as four compact paragraphs in this order:

1. **Canvas and Paper**
   - State vertical paper format, off-white surface, scan texture, and negative space.
   - Specify whether the page is plain, speckled, letterhead-like, poster-like, or notebook-like.

2. **Handwritten Structure**
   - Convert the user's theme into one main handwritten phrase and 3-7 smaller note fragments.
   - State where these text islands sit: top letterhead, center headline, margin notes, bottom caption, scattered corners, or around a photo.

3. **Visual Anchor and Marks**
   - Define one anchor: crayon flowers, small framed photo, loose line drawing, walking figures, hand-drawn path map, vase pair, simple object, or large rough handwritten word.
   - Define mark behavior: underlines, circled words, crossed-out line, thin rule, hand border, arrows, tiny doodle, or colored path lines.

4. **Material, Color, Mood, Avoids**
   - State ink, crayon/marker, paper grain, scan dust, blur, low contrast, and accent colors.
   - Add the mood and hard avoid-list.

Keep exact text short. Let some microtext become texture rather than perfect copy.

## First-Principles Fields

Every Standard Mode prompt must answer:

1. **What is the paper surface?**
   - vertical off-white or cream paper, matte, lightly aged, scanned flat.

2. **How empty is the page?**
   - 65%-90% open paper. The composition must breathe.

3. **What is handwritten?**
   - at least one rough handwritten title or phrase; optional small handwritten side notes, underlines, or crossed-out words.

4. **What is typeset?**
   - use tiny printed metadata sparingly: event date, venue line, address-like fictional line, festival label, page code, or serif caption.

5. **What visual anchor carries the theme?**
   - one photo crop, naive drawing, crayon flower cluster, line diagram, stick figure, object outline, or hand-framed memory image.

6. **What is the mark system?**
   - use childlike but intentional lines: borders, brackets, underlines, circles, arrows, paths, or thin horizon lines.

7. **What is the color logic?**
   - black ink plus restrained hand-color accents. Color can be sparse multi-accent if it reads like crayon/marker, not graphic design.

8. **What should be avoided?**
   - no polished branding, perfect vector lettering, digital UI, glossy magazine layout, dense scrapbook, cute sticker pack, anime, realistic illustration, commercial CTA, or complex scene.

## Variation Engine

Choose one option from each axis before writing the prompt.

### Layout Family

- **letterhead-drawing:** formal tiny header at top, large naive drawing in the middle
- **walking-line-map:** small figures, colored path lines, and scattered text fragments
- **studio-sale-note:** tiny printed event metadata, rough central handwritten headline, bottom paragraph
- **photo-with-hand-notes:** small photo rectangle with hand border and notes around it
- **festival-flyer-hands:** grayscale photo plus large hand-drawn headline and doodled hands
- **bilingual-air-grid:** sparse English/Chinese or English/Japanese text floating on a loose grid
- **speckled-micro-poster:** mostly empty speckled paper with tiny centered text columns
- **crayon-flower-letter:** institutional header plus childlike colorful flower drawing
- **manifesto-margin-page:** handwritten thoughts scattered in corners around one blank or photo box
- **single-scribble-word:** oversized repeated scribble word overlays a quiet photo or empty paper

### Anchor Type

- crayon flower bouquet
- small grayscale photo
- faded color snapshot
- stick-figure walkers
- hand-drawn vase or object pair
- rough handwritten word stack
- simple hand or pencil drawing
- thin colored path lines
- centered text constellation
- empty hand-drawn frame

### Typography Mode

- shaky uppercase handwriting
- childlike loose script
- rough charcoal scribble letters
- underlined handwritten phrase
- crossed-out printed schedule
- tiny serif gallery metadata
- small grotesk event caption
- bilingual sparse word grid
- margin note fragments
- handwritten paragraph over a photo

### Mark Mode

- uneven hand border
- circled keyword
- crossed-out line
- long thin underline
- colored walking path
- simple arrow or pointer
- doodled hands
- tiny flower or music note
- loose diagram ticks
- horizon line

### Texture Mode

- warm aged paper
- speckled recycled paper
- photocopied poster grain
- pencil pressure variation
- wax crayon bloom
- marker bleed
- faded snapshot softness
- low-contrast xerox photo
- scan dust and paper fibers
- slight ink smudge

### Mood Mode

- quiet optimism
- settling down
- studio afternoon
- change and movement
- small festival
- handwritten announcement
- fragile memory
- casual workshop
- school-notebook poetry
- intimate public notice

## Color Engine

- Default to black ink on off-white paper with 1-3 restrained handmade accent colors.
- Use accents as crayon or marker marks, not clean graphic blocks: red flower, blue path, green stem, yellow bloom, olive text, teal underline, or tan diagonal path.
- Color may occupy 1%-12% of the canvas depending on the anchor. Larger color areas should look naive and soft, not polished.
- If the user asks for monochrome, use black ink and grey photo only.
- Do not use saturated digital gradients, neon, glossy color fields, or corporate palette systems.

## Standard Prompt Shape

Use this exact shape:

```text
Vertical 3:5 off-white paper-note zine poster, flat scanned matte paper surface with subtle fibers and dust, [65%-90%] quiet negative space, [layout family] composition, no border, no mockup, no dark background.

For [user theme], create [main phrase] as [typography mode], placed [position]. Add [3-7] small note fragments as tiny printed metadata, margin handwriting, bilingual words, dates, captions, or underlined lines, with deliberately uneven spacing.

Use one visual anchor: [anchor type], placed [position and size]. Add [mark mode] and handmade details such as shaky lines, pencil pressure variation, marker bleed, crayon bloom, circled words, crossed-out phrase, hand border, or a thin path line.

Palette: warm paper, black ink, muted graphite, plus [accent colors/forms] as handmade crayon/marker accents. Quiet diary-like editorial mood, poetic studio flyer feeling. Avoid polished branding, perfect vector type, commercial CTA, glossy magazine layout, dense scrapbook, cute stickers, anime, realistic full scene, 3D render, neon, gradients, and clean digital UI.
```

## Workflow

1. Parse the user's brief.
   - Identify the core subject, mood, exact text if supplied, and whether any reference photo should become the anchor.
   - If no text is supplied, invent one short handwritten phrase and a few tiny metadata fragments.

2. Select a recipe.
   - Pick layout family, anchor type, typography mode, mark mode, texture mode, mood mode, and color recipe.
   - For batches, vary composition families. Do not repeatedly use only centered headline plus bottom caption.

3. Write the final prompt.
   - Use the Standard Prompt Shape.
   - Specify placement, empty space, hand-made marks, paper texture, and accent colors.
   - Keep in-image text brief. Use invented names, addresses, and dates unless user supplies exact copy.

4. Generate the image.
   - Use image generation by default.
   - If the user asks for prompt-only, return only the prompt and recipe.
   - If the result is too polished, too colorful, too dense, or too commercial, regenerate once with stronger "naive hand lettering, scanned off-white paper, large empty space" wording.

5. Return the image and prompt.

## Negative Constraints

Always avoid:

- copying real hotel, festival, brand, address, logo, phone, email, or private details from references unless the user explicitly supplies approved text
- polished brand identity systems, luxury ads, product campaigns, CTAs, or clean poster templates
- perfect vector handwriting, smooth calligraphy, typography that looks like a font pretending to be handwriting
- glossy magazine photography, cinematic lighting, heavy shadow, 3D mockup, desktop scene, lifestyle props
- dense scrapbook collage, sticker overload, washi tape decoration, cute cartoon, anime, kawaii illustration
- full-bleed scenic illustration, complex background, or realistic narrative scene
- neon, gradients, high-contrast digital colors, UI panels, or corporate palette blocks
- long perfectly readable paragraph text

## Output Format

````markdown
**生成图**

![Handwritten paper-note zine poster](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Mode: Standard
- Recipe: [layout / anchor / typography / mark / texture / color / mood]
- [one short note about how the user's theme became a handwritten paper-note poster]
````

If generated images render directly without a file path, show the image normally and still include the final prompt.

## Quality Gate

Before finalizing, check:

- Did the prompt produce off-white or cream paper, not a black archival board?
- Does 65%-90% of the page remain quiet paper?
- Is there at least one rough handwritten phrase?
- Are tiny printed metadata or caption fragments used sparingly?
- Is there one clear visual anchor such as photo, doodle, crayon flower, stick figure, or diagram?
- Do hand-made marks feel naive but intentional?
- Are color accents handmade crayon/marker/pencil marks rather than polished graphic blocks?
- Does the composition avoid commercial poster hierarchy and glossy mockup aesthetics?
- If references were supplied, did it borrow structure without copying private or brand-specific text?
- Did you actually generate the image unless the user asked for prompt-only?

## Example Requests

- "用 $handwritten-paper-note-zine 做一张关于搬家和重新开始的手写纸面海报"
- "根据这张参考图反推同结构 prompt，不要生成图"
- "把我的活动做成 studio sale note 风格，米白纸、手写标题、小字信息"
