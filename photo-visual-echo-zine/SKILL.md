---
name: 影像回响
description: "【影像回响 / photo-visual-echo-zine】 Generate photo-plus-illustration visual echo zine poster prompts and matching raster images. Use when the user provides a travel, landscape, architecture, street, nature, resort, sky, sea, mountain, waterfall, temple, or atmospheric photo and wants a vertical editorial poster that keeps the source photo on top, translates it into a soft hand-painted visual echo below, and finishes with poetic title typography, palette swatches, and aged paper texture."
---

# Photo Visual Echo Zine

Transform a reference photo or scene brief into both:

1. a final image-generation prompt, and
2. a generated raster poster made from that prompt.

Use this as a fusion of `gc-minimal-zine-poster-v0-1` and a travel-photo visual-echo layout: keep the quiet paper-poster sensibility, but replace the tiny minimalist anchor with a structured photo/illustration/editorial triptych.

## Reverse-Engineered Structure

The target poster is a tall vertical 3:5 printed page with three stacked zones:

- **Top photo panel:** full-width original or realistic photo crop, about 36%-42% of canvas height. Keep the real scene legible: horizon, main landmark, water, sky, mountain, architecture, people, or foreground vegetation. No border, no drop shadow.
- **Middle visual echo panel:** full-width hand-painted translation, about 40%-48% of canvas height. Recompose the same scene as watercolor, gouache, ink wash, risograph, or paper-textured illustration. Preserve the major geometry, simplify detail, and let paper texture show through.
- **Bottom editorial band:** warm off-white paper band, about 14%-20% of canvas height. Include a small uppercase label, a thin horizontal rule, a large elegant serif title, a short handwritten subtitle, and 3-4 small color swatches aligned on the right.

A second valid variant merges the middle illustration and bottom text into one continuous paper field: photo on top, then a large airy hand-painted echo with title and swatches embedded near the lower edge.

## Prompt Compiler

Write final prompts as five compact paragraphs in this order.

1. **Canvas and split layout**
   - Specify a vertical 3:5 editorial zine poster.
   - Specify the exact stacked composition: top photo panel, lower hand-painted visual echo, bottom typography band.
   - Use full-bleed rectangular panels with clean horizontal seams and no mockup frame.

2. **Top photo panel**
   - Describe the scene as a plausible travel photograph.
   - Preserve source-specific geometry: skyline, horizon, landmark position, cascade tiers, building silhouette, balloons, trees, mountains, waterline, or people scale.
   - Keep natural light and camera realism; avoid fashion-editorial lighting.

3. **Visual echo panel**
   - Translate the top photo into a softer hand-painted reconstruction.
   - Choose one material language: watercolor wash, gouache on aged paper, ink-line architecture, flattened folk-print landscape, or delicate travel sketch.
   - Keep the same visual memory but simplify: fewer people, softened vegetation, flattened forms, controlled detail, visible paper grain.

4. **Editorial typography and palette**
   - Add the small label `PHOTO / VISUAL ECHO`.
   - Add a thin horizontal rule.
   - Add one large title in high-contrast editorial serif or Didot/Bodoni-like uppercase unless the user asks for title case.
   - Add one short handwritten subtitle as a question, caption, or poetic fragment.
   - Add 3-4 small square color swatches sampled from the scene at the right side of the band.

5. **Print mood and hard avoids**
   - Specify scanned matte paper, old print texture, subtle fibers, low-to-medium contrast, quiet poetic travel memory mood.
   - Avoid glossy poster mockups, floating cards, borders, heavy shadows, 3D rendering, cinematic drama, neon, cute cartoon, dense scrapbook, commercial CTA, logo, and long readable text blocks.

## Visual Rules

- Keep the top panel photographic and the lower panel handmade; the contrast between them is the concept.
- Preserve composition more than literal detail. The lower echo should feel derived from the photo, not like a different scene.
- Let the lower illustration be brighter, cleaner, more poetic, or more symbolic than the photo.
- Use aged cream, warm ivory, or slightly gray paper for the editorial band and illustration ground.
- Use one scene-based palette: greens for forest/waterfall, blues and sand for coast/sky, navy and cream for night architecture, ochre and dusty red for sunrise/balloons.
- Swatches should be small, clean squares with slight paper/ink texture; they are not decorative confetti.
- Text must be short. Prefer 2-5 words for the title and 5-9 words for the subtitle.
- If the user's photo has no obvious title, invent a poetic English title and subtitle.
- If Chinese text is requested, keep it very short and consider pairing with tiny English label text; image models handle long Chinese text poorly.

## Variation Engine

Choose one option from each axis before writing the prompt.

### Scene Family

- waterfall and karst mountains
- chapel or white seaside architecture
- temple, pagoda, shrine, or mountain sanctuary
- night resort, arches, palms, pool, or illuminated facade
- balloons, fields, dawn sky, or aerial distance
- quiet street, bridge, train, market, harbor, garden, or lake

### Echo Style

- translucent watercolor landscape
- flattened gouache travel poster
- ink-and-wash architectural drawing
- paper-cut landscape layers
- soft risograph botanical/terrain print
- pale illustrated memory album

### Title Treatment

- uppercase high-contrast serif headline
- title-case elegant serif headline
- spaced serif letters with strict baseline
- quieter mixed-case serif for integrated lower panel

### Subtitle Treatment

- handwritten question
- italic travel note
- pencil-like memory caption
- tiny archive phrase with weather/date

### Palette Swatches

- four squares: deep green, muted green, pale aqua, clay red
- three squares: cobalt blue, sand beige, muted blue-gray
- four squares: forest green, cinnabar red, mist blue, slate green
- four squares: midnight navy, beige, dark umber, pool teal
- four squares: ochre yellow, dusty red, sage green, blue-gray

## Photo Parsing

When given a reference image, identify:

- main subject and supporting subject
- horizon and panel split opportunities
- top photo mood, weather, and time of day
- 3-5 dominant palette colors
- one large title idea and one short subtitle idea
- what details must survive in the painted echo
- what details can be removed for clarity

If the user gives multiple photos, choose the one with the clearest single subject unless they ask for a series. For a series, keep the same layout grid and vary title, palette, and echo style.

## Example Prompt Fragments

Use these as structural references, not fixed outputs.

```text
Vertical 3:5 editorial zine poster, clean stacked layout: the top 40% is a full-width realistic travel photo of tiered waterfalls in a lush karst valley, the middle 44% is a hand-painted visual echo on aged cream paper, and the bottom 16% is an off-white typography band with no frame or shadow.
```

```text
In the lower echo panel, repaint the same chapel, sand horizon, ocean line, tiny visitors, clouds, and faint rainbow as translucent watercolor, softer and brighter than the photo, with visible paper grain and simplified forms.
```

```text
Bottom band: small uppercase label "PHOTO / VISUAL ECHO", thin rule, large Didot-like title "A CHAPEL UNDER BLUE", handwritten subtitle "Where does the rainbow touch the sea?", three small square swatches on the right: cobalt blue, sand beige, muted blue-gray.
```

## Workflow

1. Parse the image or brief into subject, mood, title, subtitle, and palette.
2. Choose a scene family, echo style, title treatment, subtitle treatment, and palette swatch set.
3. Compile a five-paragraph prompt using the Prompt Compiler.
4. Generate the image by default unless the user explicitly asks for prompt-only.
5. Inspect the result. Regenerate once if:
   - the top photo and lower echo do not match,
   - the layout is not vertically stacked,
   - the title band is missing,
   - the page loses the zine/editorial paper feeling,
   - the output becomes a generic single illustration or a commercial poster.

## Output Format

````markdown
**生成图**

![Photo Visual Echo Zine poster](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Recipe: [scene family / echo style / title treatment / subtitle treatment / swatches]
- Title: [title]
- Subtitle: [subtitle]
- [one short note about how the photo was translated]
````

## Quality Gate

Before finalizing, verify:

- Vertical 3:5 poster.
- Top panel reads as realistic photo.
- Lower panel reads as handmade visual echo of the same scene.
- Bottom editorial typography band or integrated lower typography is present.
- Title is short and visually dominant.
- Subtitle is handwritten, brief, and poetic.
- 3-4 scene-derived swatches appear on the right.
- Paper grain, scan texture, and old-print softness are visible.
- No glossy mockup, border, card, logo, CTA, 3D, neon, cartoon, or dense scrapbook layout.
