---
name: 旅行档案拼贴
description: "【旅行档案拼贴 / travel-archive-collage-zine】 Generate travel archive collage zine prompts and matching raster images from photos or scene briefs. Use when the user provides a city, travel, street, notebook, map, diary, memory, window, bicycle, waterfront, architecture, or urban photo and wants an aged-paper editorial collage with photo fragments, hand-drawn map/notebook elements, Chinese brush-calligraphy typography, handwritten calligraphic microtext, tape, grid lines, dark framed cards, and nostalgic archive texture."
---

# Travel Archive Collage Zine

Transform a travel photo, city scene, diary idea, or memory brief into both:

1. a final image-generation prompt, and
2. a generated raster image made from that prompt.

Use this as a fusion of `gc-minimal-zine-poster-v0-1` and tactile urban travel archives: keep the old paper, sparse editorial restraint, print defects, and one strong accent strategy, but allow layered photo cards, notebook maps, Chinese brush calligraphy, and physical collage construction.

## Reverse-Engineered Image Structure

The references form two related layout grammars.

### Split Memory Layout

- Tall vertical travel page.
- Top half: realistic warm travel photo, usually waterfront, skyline, old city, architecture, sky, or vehicle edge.
- Bottom half: top-down hands holding an open diary, map, ticket scrapbook, or illustrated travel notebook on dark textile.
- The seam is a clean horizontal cut. The upper panel is documentary; the lower panel is tactile and object-based.
- Use readable travel clues: city map, folded paper, stickers, receipts, stamps, labels, small souvenirs, hand marks, worn page edges.

### Archive Card Layout

- Mostly horizontal cards or a tall vertical stack of horizontal cards.
- Background: aged beige paper, dark blue fabric, grid paper, translucent city photo, or blurred window reflection.
- Foreground: one or more framed rectangular print cards with heavy black border, off-white mat, taped corners, binder holes, staples, clips, paper strips, or small tags.
- Inside each card: ghosted urban photo, wall texture, bicycle silhouette, abstract building shadow, map crop, or textured memory window.
- Typography: large expressive Chinese brush calligraphy as the main visual anchor, plus handwritten calligraphic vertical or horizontal body text blocks, side labels, punctuation, and archive tags. Avoid clean printed font behavior.
- Accent: burnt orange/copper/yellow ochre tape, title strokes, tags, dots, or stripe marks. Keep the rest muted.

## Prompt Compiler

Write final prompts as five compact paragraphs in this order.

1. **Canvas and paper system**
   - Specify vertical 3:5 poster unless the user explicitly asks for horizontal.
   - Define the selected layout: split memory, single archive card, two-card editorial spread, stacked archive wall, or horizontal textural title sheet.
   - Specify aged matte paper, scan texture, visible fibers, old folds, stains, scratches, and low-to-medium contrast.

2. **Photo and memory material**
   - Convert the user's scene into one grounded memory source: city waterfront photo, open map notebook, window reflection, bicycle against wall, street facade, train platform, hotel card, ticket, receipt, or diary spread.
   - If a reference photo is supplied, preserve its main geometry and mood but allow collage transformation.
   - Mention tangible objects: hands, folded map, sticker, receipt, label, fabric, tape, binder ring, paper tag, or frame.

3. **Collage construction**
   - State the exact arrangement and scale: top/bottom split, centered framed card, left text column plus right image frame, vertical stack of 3-4 cards, or full-page ghost photo with border.
   - Add physical marks: black mat frame, off-white border, masking tape, copper dots, staples, tabs, stripe tape, grid lines, punched holes, faint crop marks, or torn paper.
   - Keep the design editorial and sparse enough to breathe; do not fill every gap.

4. **Brush-calligraphy typography and accent color**
   - Use large rough Chinese brush calligraphy or handwritten calligraphic title as a major compositional object. If exact text is not supplied, invent a very short poetic Chinese title of 2-6 characters or a brief broken phrase.
   - Make all visible Chinese lettering feel written by brush, ink pen, or calligraphic hand: pressure variation, dry-brush edges, ink bleed, uneven baseline, connected strokes, and imperfect paper absorption.
   - Add microtext blocks as tiny handwritten calligraphic Chinese notes, vertical side labels, date/weather/location, or illegible archive marks. Microtext may be semi-legible, but it should not become clean printed body copy.
   - Choose one warm accent: burnt orange, copper brown, yellow ochre, rust red, or aged gold. Let it occupy about 1%-5% of the page through tape, calligraphy, tags, dots, or stripes.

5. **Mood and hard avoids**
   - Specify nostalgic travel memory, handmade diary, scanned archive, quiet indie zine, imperfect print.
   - Avoid glossy mockup, clean UI, commercial poster, brand logo, CTA, cute stickers, anime, neon, 3D, cinematic lighting, perfect readable long text, standard Songti/Heiti/sans-serif printed Chinese fonts, overly clean vector graphics, and maximal scrapbook clutter.

## Visual Rules

- Use real physical paper logic: cards sit on paper, tape crosses edges, frames have thickness, text aligns to margins, and grid lines recede into texture.
- Keep one dominant image anchor or one dominant card stack. Do not make a random mood board of unrelated fragments.
- Let Chinese calligraphy behave as image, not as ordinary caption. It can overlap photo windows, sit inside black frames, or dominate a blank paper field.
- Treat Chinese text as brush-written material by default. Use xingshu/caoshu-like rhythm, dry-brush fiber, ink pooling, broken strokes, imperfect alignment, and hand pressure changes. Do not prompt for neat digital Songti, Heiti, sans-serif, UI, caption, or book-body typography.
- Microtext should read as handwritten calligraphic texture at thumbnail scale. Do not depend on long readable copy for meaning.
- Use a muted base palette: aged ivory, gray-blue, charcoal, faded black, dark fabric navy, pale green-gray, tea stain, and warm paper beige.
- Use only one main warm accent family per output. It may be saturated but should feel printed, taped, stamped, or brushed.
- Preserve `gc-minimal-zine-poster-v0-1` discipline: quiet mood, paper surface, intentional negative space, old print defects, and no commercial hero-poster hierarchy.
- Unlike minimal-zine, the subject cluster may occupy 45%-85% of the page when using card stacks. The negative space should appear inside margins, columns, and paper gaps rather than as an almost empty page.

## Variation Engine

Choose one option from each axis before writing the prompt. Always include **Calligraphy Font Style** in the recipe; it is mandatory, not decorative.

### Layout Family

- **split-photo-notebook:** upper travel photo, lower hands holding open map diary
- **single-black-frame:** one large dark-bordered memory card on aged paper
- **left-text-right-card:** pale grid page with text columns on left and framed photo/card on right
- **stacked-archive-wall:** 3-4 horizontal cards pinned vertically over a translucent city background
- **ghost-photo-poster:** full-page faded urban photo with calligraphy and small archive labels
- **textural-title-sheet:** mostly blank aged paper with scratches, loose line drawings, centered brush title, and tiny body text

### Memory Anchor

- waterfront city skyline
- open map notebook with hands
- bicycle silhouette on weathered wall
- blurred building through window glass
- street facade shadow
- ticket, receipt, stamp, or label cluster
- old map spread with stickers
- dark textile under paper artifacts

### Typographic System

- oversized white rough-brush Chinese title
- burnt-orange dry-brush Chinese title
- pale ink calligraphy over ghost photo
- vertical handwritten calligraphy side title with tiny author/date
- small handwritten calligraphic Chinese note columns
- mixed brush microtext, calligraphic labels, and punctuation marks

### Calligraphy Font Style

- xingshu-style flowing brush lettering with connected strokes
- caoshu-style abstracted brush marks for large titles
- dry-brush archive calligraphy with broken edges
- pale ink handwritten notes with uneven pressure
- copper-brown stamped brush lettering on tape or tags
- rough white ink brush lettering over black photo mats

### Physical Detail

- black photo mat frame
- masking tape tabs
- copper binder dots and loop clips
- orange stripe tape
- off-white border mat
- faint square grid
- torn label patch
- fold marks and scratches

### Accent Set

- burnt orange tape and title strokes
- copper brown tags and binder dots
- yellow ochre brush title
- rust red stamps and stickers
- muted blue-gray field with warm paper labels

## Photo Parsing

When given a reference image, identify:

- whether it fits better as a top photo, ghost photo card, map notebook, or background reflection
- the main place clue: skyline, water, building, street object, bicycle, window, map, hands, or fabric
- the emotional temperature: golden travel, urban melancholy, diary intimacy, night archive, or transit memory
- 3-5 dominant colors and the strongest warm accent candidate
- a short Chinese calligraphic title idea and optional small English/Chinese location note
- which exact shapes must survive: horizon, church spire, boat edge, bicycle basket, window grid, map fold, hands, card frame, or text column

If the user supplies several images, either build a stacked archive wall or choose the strongest single memory anchor. For a series, keep card proportions and accent color consistent.

## Example Prompt Fragments

Use these as structure references, not fixed templates.

```text
Vertical 3:5 travel archive collage zine, split-photo-notebook layout: the upper half is a warm realistic waterfront city photograph with blue sky, rippled water, old buildings, a church spire, and a boat edge; the lower half is a top-down view of two hands holding an open folded city map diary on dark navy fabric, with stickers, receipts, stamps, and worn paper edges.
```

```text
Single-black-frame layout on aged grid paper: a dark-bordered rectangular memory card sits right of center, containing a faded ghost photo of a bicycle silhouette against a blue-gray wall, scratched scan texture, pale cream dry-brush Chinese calligraphy crossing the image with visible ink bleed and broken stroke edges, a small ochre vertical tag on the right with handwritten calligraphic marks, and tiny illegible handwritten archive notes near the top edge.
```

```text
Stacked archive wall: three horizontal zine cards pinned vertically over a translucent blurred city-window background, each card uses black mat borders, beige paper margins, copper binder dots, orange tape tabs, rough Chinese brush-calligraphy titles, tiny handwritten calligraphic prose columns, grid lines, scratches, and one warm burnt-orange accent system.
```

## Workflow

1. Parse the user's photo or brief into memory anchor, mood, title, palette, and tactile materials.
2. Choose a layout family, memory anchor, typographic system, calligraphy font style, physical detail set, and accent set.
3. Compile the final prompt using the five-paragraph Prompt Compiler.
4. Generate the image by default unless the user explicitly asks for prompt-only.
5. Inspect the result and regenerate once if:
   - the output is a clean digital poster rather than scanned paper collage,
   - the warm accent disappears or becomes multicolor clutter,
   - the Chinese title is not a visible brush-calligraphy compositional anchor,
   - visible Chinese text looks like a clean digital font, Songti, Heiti, sans-serif, UI text, or ordinary printed caption instead of calligraphy,
   - the cards, tape, frames, or notebook materials are missing,
   - the image becomes a commercial travel ad or dense scrapbook.

## Output Format

````markdown
**生成图**

![Travel Archive Collage Zine poster](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Recipe: [layout / memory anchor / typography / calligraphy font style / physical detail / accent]
- Title: [short Chinese title or supplied title]
- [one short note about how the source photo or brief was transformed]
````

## Quality Gate

Before finalizing, verify:

- The page reads as an aged-paper zine, archive card, diary, or travel collage.
- The structure is one of the defined layout families.
- A main photo, map, notebook, city object, or ghost image anchor is clear.
- Chinese brush calligraphy or vertical handwritten calligraphic Chinese title is prominent.
- Visible Chinese text uses calligraphic brush/handwritten forms, not clean printed fonts.
- The recipe explicitly names a calligraphy font style such as xingshu, caoshu, dry-brush, pale ink handwriting, or stamped brush lettering.
- Microtext, tags, tape, frames, grid lines, or binder details are present.
- The warm accent is visible but controlled.
- Paper fibers, folds, scratches, scan noise, and print wear are visible.
- The result avoids glossy mockup, clean UI, commercial ad, logo, CTA, neon, 3D, anime, and chaotic scrapbook clutter.
