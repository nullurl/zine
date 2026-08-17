---
name: 植物纸拼贴
description: "【植物纸拼贴 / botanical-paper-collage-zine】 Generate botanical paper-collage zine prompts and matching raster images. Use when the user gives a theme, object, mood, phrase, plant/photo reference, or article idea and wants a quiet vertical poster with muted recycled paper, translucent rectangular overlays, soft-focus framed botanical photography, botanical stamp silhouettes, woodgrain or ripple relief textures, sparse lowercase words, and tactile editorial archive styling."
---

# Botanical Paper Collage Zine

Turn the user's content into both:

1. a final image-generation prompt, and
2. a generated raster image made from that prompt.

## Source Grammar

Use this visual grammar as the identity:

- vertical botanical paper poster, 3:5 or 4:5, flat scanned view
- muted sage, blue-grey, cream, off-white, olive, graphite, recycled-paper palette
- layered translucent rectangles, vellum sheets, cream cards, soft-edged paper panels
- one framed soft-focus botanical photo as the main anchor, usually with a white border
- secondary botanical marks: stamp silhouettes, pressed-leaf prints, fern panels, flower or branch print blocks
- texture anchors: woodgrain strip, ripple relief, circular tree-ring form, embossed botanical paper pattern
- sparse lowercase rounded sans words floating over panels or photos, such as `warm`, `freedom`, `unrestrained`
- visible paper fibers, scratches, dust, stains, scan grain, low-contrast ink, quiet editorial spacing

Do not turn the style into a normal scrapbook page. The image should feel like a restrained archive sheet assembled from paper, plant memory, and soft print texture.

## Mode Policy

Use **Standard Mode** for all generation. Use the Standard Mode Prompt Compiler below to convert the user's content into a compact, imageable, high-fidelity prompt.

Use prompt-only output only when the user explicitly asks for prompt-only.

## Standard Mode Prompt Compiler

Default generation should compile only the parts that become visible pixels.

### First-Principles Fields

Every prompt must answer these rendering questions in this order:

1. **Canvas:** What is the frame and paper base?
   - tall vertical 3:5 or 4:5 poster; flat orthographic scanned-paper surface; no mockup; no perspective.

2. **Paper Field:** What large quiet surface dominates the image?
   - 55%-75% muted paper field; sage green, blue-grey, or warm off-white; visible fibers, dust, worn stains, scratches, softened print noise.

3. **Layer Geometry:** How do the paper overlays sit?
   - 3-6 overlapping translucent rectangles or cream cards; edges slightly softened; vertical and horizontal offsets; no busy sticker pile.

4. **Botanical Photo Anchor:** What is the main imageable subject?
   - convert the user's theme into one soft-focus botanical photo crop, plant detail, flower stem, leaf cluster, seed pod, fern, branch, or plant-shadow fragment; place it in a thin white or cream frame.

5. **Secondary Botanical Marks:** What printed plant elements support the photo?
   - choose one or two: flat botanical stamp silhouette, pressed leaf print, cyanotype-like plant block, graphite flower outline, faded fern panel, branch rubbing, translucent specimen shadow.

6. **Relief Texture Anchor:** What non-photo texture adds tactile structure?
   - choose one: horizontal woodgrain strip, ripple-water relief block, circular tree-ring form, embossed floral paper panel, relief-printed bark band, soft contour-line plate.

7. **Typography System:** How does text behave?
   - use 1-4 short lowercase words in rounded sans or plain grotesk; white, pale cream, graphite, or faded grey; words float, overlap a panel edge, sit over a photo, or drift in the paper field; keep text sparse.

8. **Color Logic:** How restrained is the palette?
   - low saturation overall; one calm palette, not a bright accent system. Use muted sage, olive, blue-grey, cream, smoke grey, graphite, and faded botanical green. Avoid neon or saturated commercial color.

9. **Reproduction Texture:** What process binds it together?
   - matte absorbent paper, scan grain, faint halftone, photocopy softness, translucent ink, worn print edges, no hard shadow.

10. **Emotional Temperature:** What should the viewer feel first?
   - quiet, natural calm, botanical archive, memory collage, soft editorial zine, tactile handmade stationery, unhurried.

11. **Hard Avoids:** What must not appear?
   - black background, neon, glossy mockup, dense scrapbook, stickers, cute cartoon, commercial ad, full realistic scene, UI, maximal typography, hard 3D shadows.

### Standard Prompt Shape

Write the final Standard Mode prompt as four compact paragraphs:

1. canvas + paper field + overall palette + texture
2. layer geometry + botanical photo anchor + placement
3. secondary botanical marks + relief texture anchor + typography
4. flat scan mood + reproduction defects + avoid-list

Prefer concrete placement and material words over broad art-direction adjectives. Keep prompt length medium; image models need visible constraints more than analysis.

## Variation Engine

Before writing the prompt, choose one option from each axis. Vary structure, not only colors or words.

### Layout Family

- **centered-photo-stack:** framed botanical photo centered over translucent paper rectangles
- **left-archive-column:** narrow botanical photo column on the left, large paper field on the right
- **upper-float-panel:** small framed plant photo in the upper third, texture band below it
- **low-card-stack:** overlapping cream and sage cards in the lower half, empty upper paper field
- **wide-relief-band:** horizontal woodgrain or ripple strip crossing the poster behind the photo
- **ring-and-specimen:** circular tree-ring texture paired with a small botanical photo frame
- **print-panel-grid:** loose grid of 3-4 paper panels with one photo and one botanical stamp block
- **word-led-calm:** sparse lowercase words become the quiet anchor, with plant image secondary

### Botanical Photo Anchor

- soft-focus leaf close-up
- small flower stem in a white frame
- fern or grass silhouette photo
- blurred branch against pale light
- seed pod or dried plant specimen
- translucent plant-shadow photo
- cropped garden texture
- pale botanical macro fragment

### Secondary Print Mark

- faded fern stamp
- pressed leaf silhouette
- cyanotype-like flower block
- graphite botanical line drawing
- mossy green plant rubbing
- branch shadow print
- small archival specimen label mark
- low-contrast floral emboss pattern

### Relief Texture

- horizontal woodgrain strip
- circular tree-ring plate
- ripple relief band
- bark-rubbing rectangle
- embossed botanical paper patch
- contour-line print panel
- faint handmade paper watermark
- worn photocopy texture window

### Typography Mode

- one large lowercase word floating over photo
- three small lowercase words scattered across panels
- pale word partly clipped by a rectangle edge
- white word over muted green paper
- graphite micro-caption near photo border
- quiet title plus tiny date-like marks
- almost textless, one soft word only
- words aligned vertically along a card edge

### Palette Mode

- sage paper, cream cards, graphite type, faded olive print
- blue-grey paper, off-white frame, smoke grey type, pale green plant
- warm recycled paper, muted sage panels, cream type, graphite marks
- washed olive field, cream photo frame, blue-grey overlay, dark grey microtext
- off-white paper, green-grey vellum, faded cyanotype plant block, graphite relief
- pale eucalyptus, chalk white overlays, low-contrast charcoal, dusty cream

## Workflow

1. Parse the user's content.
   - Identify the core subject, mood, exact words if supplied, and any reference image role.
   - If the user supplies a non-botanical theme, translate it into a botanical metaphor or plant-memory fragment.
   - If no text is supplied, invent 1-4 short lowercase words. Prefer quiet words such as `warm`, `freedom`, `soft`, `unrestrained`, `afterlight`, `root`, `field`, `memory`, or concise Chinese words if the user writes in Chinese.

2. Select a recipe.
   - Choose layout, botanical photo anchor, secondary print mark, relief texture, typography mode, and palette mode from the Variation Engine.
   - Keep the number of visible parts restrained. One photo, one relief texture, one or two botanical print marks, and sparse text are usually enough.

3. Write the final image prompt.
   - Use the Standard Prompt Shape.
   - Specify exact placement, approximate scale, paper color, number of translucent panels, and in-image words.
   - Keep typography short because image models distort long text.
   - Never describe a bright high-chroma accent unless the user explicitly asks for one.

4. Generate the image.
   - Use the available image generation capability by default.
   - Do not stop after prompt-only unless the user asks for prompt-only.
   - If the result becomes a generic plant photo, dense scrapbook, or commercial botanical poster, tighten the prompt and regenerate once.

5. Return the image and prompt.

## Negative Constraints

Always avoid:

- black or dark dramatic background
- neon, cyberpunk, high-chroma gradients, loud accent blocks
- glossy paper mockup, angled perspective, heavy drop shadows, 3D depth
- dense scrapbook, many stickers, washi-tape clutter, cute journaling decoration
- commercial ad layout, logo, CTA, brand campaign, product packaging
- full realistic landscape or full-bleed botanical photo scene
- anime, kawaii cartoon, fashion editorial drama, luxury perfume poster
- clean digital UI, app screen, website layout
- long readable text paragraphs, big headline hierarchy, maximal typography
- oversharpened stock photo realism

## Output Format

````markdown
**生成图**

![Botanical Paper Collage Zine style poster](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Mode: Standard
- Recipe: [layout / photo anchor / print mark / relief texture / typography / palette]
- [one short note about the content interpretation]
````

If generated images render directly without a file path, show the image normally and still include the final prompt.

## Quality Gate

Before finalizing, check:

- Did the run use the Standard Mode Prompt Compiler?
- Did the run choose a variation recipe across layout, photo anchor, print mark, relief texture, typography, and palette?
- Is the image a vertical flat scanned paper poster?
- Does the background read as muted sage, blue-grey, cream, or recycled paper?
- Are translucent rectangles or cream cards visibly layered?
- Is there one framed soft-focus botanical photo anchor?
- Are botanical stamp, pressed-leaf, or print marks present but restrained?
- Is a woodgrain, ripple, tree-ring, emboss, or relief texture visible?
- Are lowercase words sparse and integrated into the paper layout?
- Does the palette remain low-saturation and tactile?
- Did the prompt avoid black background, neon, glossy mockup, dense scrapbook, cute cartoon, commercial ad, full realistic scene, and UI aesthetics?
- Did you actually generate the image?

## Example Requests

- "用 $botanical-paper-collage-zine 做一张关于自由的植物纸张拼贴海报"
- "Use $botanical-paper-collage-zine to turn the word warm into a muted botanical collage poster."
- "用这张花草照片做一张同风格 zine poster"
- "Use $botanical-paper-collage-zine prompt-only for a quiet archive sheet about spring rain."
