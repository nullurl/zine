---
name: 光谱字体
description: "【光谱字体 / spectral-type-field-zine】 Generate prompts and finished raster images for pale experimental typography posters with ghosted photographs, soft blur, xerox grain, translucent text layers, distorted display type, program or tracklist microtext, sparse diagrams, and restrained signal colors. Use when the user provides a theme, event, album, exhibition, program, phrase, body study, or reference image and wants an atmospheric editorial flyer rather than a dense commercial event poster."
---

# Spectral Type Field Zine

Turn the user's theme, event, text, or reference into both a final image-generation prompt and a finished raster poster. The default artifact is a tall pale paper field containing one ghosted photographic presence, two to four controlled typography layers, a concentrated information zone, and a small signal-color mark.

This Skill fuses the attention geometry of `gc-minimal-zine-poster-v0-1` with translucent experimental flyers, type specimens, album press sheets, calendar diagrams, and soft photocopied image fields. It keeps the source Skill's negative space, single anchor, restrained accent, print defects, and flat scanned artifact while allowing typography to become an atmospheric spatial layer.

## Mode Policy

Use **Spectral Field Mode** by default. Use **Program Mode** when the user supplies event, exhibition, album, festival, schedule, cast, or tracklist information. Use **Type Specimen Mode** only when the font/glyph system is the actual subject.

- **Spectral Field Mode:** one ghost image, one display phrase, one microtext band.
- **Program Mode:** exact information deck, top or bottom program zone, ghost image field.
- **Type Specimen Mode:** one distorted glyph family, weight samples, one spectral figure or object.

Do not create a dense nightclub flyer or a generic Y2K poster. The center field must breathe.

## Prompt Compiler

Write the final prompt as five compact paragraphs in this order.

### 1. Canvas and atmospheric field

State:

- vertical 2:3, 3:5, or poster-standard portrait artboard
- pale gray, washed white, fog blue, silver, or translucent blush paper field
- 55%-80% low-information atmospheric space
- flat scanned print, no device mockup, drop shadow, UI card, or default black presentation border
- soft paper fibers, toner noise, faded ink, and diffuse edge variation

The field may contain subtle color clouds, erased patches, or translucent emulsion but must not become a smooth digital gradient.

### 2. Spectral image anchor

Translate the theme into one low-contrast presence:

- blurred eye, hand, face fragment, standing body, flower, branch, cloud, bird, tree, crowd, silhouette pair, or object
- photocopied landscape or calendar image
- inverted negative, solarized contour, frosted-glass crop, motion smear, rasterized shadow, or eroded halftone

Keep the anchor at 10%-35% opacity or embed it into the paper through toner and grain. It should occupy 12%-35% of the canvas and remain subordinate to the type system. Use one subject, not a montage of unrelated photos.

### 3. Typography hierarchy

Use two to four typography layers with distinct jobs:

- one bold grotesk or condensed sans display phrase
- one deformed, calligraphic, variable, or custom glyph word
- one monospaced or narrow grotesk microtext band
- optional serif, script, or outlined secondary phrase

Typography may overlap, repeat, stretch, fade, rotate, or cross the image, but the hierarchy must remain intentional. Place the main information in one concentrated zone at the top, left edge, or bottom. Keep at least 35%-55% of the page free of high-contrast type.

### 4. Diagram and signal system

Choose no more than two support systems:

- thin orbit, route, timeline, or calendar curve
- tiny squares, nodes, ticks, registration marks, or dates
- a narrow side label or vertical program line
- small barcode, weight table, track numbers, or venue list
- one translucent rectangle or image strip

Choose one signal color: pale pink, dusty coral, rust brown, icy cyan, muted cobalt, acid-lime used sparingly, or warm cream against gray. The signal should occupy roughly 0.5%-2% of the canvas and remain visible at thumbnail scale.

### 5. Print surface, copy policy, and avoid-list

Use photocopy bloom, xerox grain, newsprint noise, vellum transparency, low-resolution raster, toner dropout, offset misregistration, scan streaks, and lightly degraded edges. Preserve exact user-supplied names, dates, titles, and program copy when required. For long listings, reduce text to a short deck because image models distort dense text. End with the relevant negative constraints.

## Layout Families

- `top-script-haze`: script/display type across the top, ghost flower or liquid form, manifesto footer
- `ghost-schedule-stack`: repeated faded program names at the top, pale image field, tiny side labels
- `route-clock-field`: months or locations arranged around a thin circular route with one silhouette anchor
- `blurred-sense-catalog`: custom glyph headline plus three blurred sensory crops and metadata columns
- `sky-hymn-footer`: washed sky field, almost invisible top word, vivid type cluster near the bottom
- `spectral-figure-specimen`: black type column paired with a pale standing figure and orbital lines
- `calendar-leaf`: overlapping paper sheets, photocopied tree or object, dates flowing in a loop
- `program-launch-split`: large empty upper field, central program copy, translucent lower image/brush layer
- `album-press-sheet`: atmospheric cover image, central title, narrow film/photo strip, bottom tracklist

## Spectral Image Engine

### Blur Modes

- frosted-glass blur with soft rectangular crop
- long-exposure movement smear
- defocused macro eye or skin crop
- toner bloom around a figure silhouette
- low-resolution halftone body fragment
- cloud-like erased emulsion
- double-exposure shadow with paper texture

### Contrast Modes

- pale-on-pale spectral presence
- black-and-white negative split
- silver-gray image with white toner bloom
- fog blue field with cream subject
- washed blush field with charcoal glyphs

Do not use blur to hide an otherwise stock image. Blur must define the visual concept and material process.

## Typography Engine

### Display Layers

- heavy grotesk schedule stack
- stretched condensed sans title
- custom distorted glyph band
- looping handwritten or calligraphic script
- large serif album title

### Information Layers

- monospaced date and venue list
- narrow side label
- tracklist or program table
- weight/style specimen table
- microtext footer or manifesto

### Rules

- maximum four type families
- one primary display layer
- one secondary expressive layer
- one microtype system
- one optional serif/script contrast
- no long filler paragraphs unless the user supplied them and exact rendering is not required

## Minimal Zine Prompt Bridge

### Preserve from the source Skill

- vertical paper canvas and flat scanned appearance
- 55%-80% quiet field and one dominant visual anchor
- one restrained high-chroma signal
- sparse archive type, dates, and registration marks
- xerox softness, halftone, paper fibers, ink bleed, and misregistration
- quiet, distant, experimental editorial mood

### Adapt for spectral type fields

- tiny object cluster becomes one low-opacity spectral image
- microtext expands into a controlled top/bottom program zone
- colored cutout becomes one signal line, tick, glyph, or translucent block
- typography overlaps the image and becomes part of the atmosphere
- negative space is washed emulsion rather than plain paper only

### Do not import

- source artist names, event dates, tracklists, venues, signatures, or logos
- black screenshot margins as part of the poster design
- unrelated decorative flowers, icons, or faux technical data
- full-resolution glossy photography and commercial headline hierarchy

## Copy Deck

Before generating Program Mode, compile:

```text
Title: [exact]
Subtitle: [exact or omit]
Date / time: [exact or omit]
Venue / location: [exact or omit]
Participants / tracks: [short exact list]
Footer: [sponsor or archive line, exact or omit]
Signal word: [1-3 words]
```

If exact text is not supplied, do not invent real performers, venues, sponsors, institutions, or dates. Use abstract labels such as `PROGRAM`, `FIELD NOTES`, or no listing.

## Workflow

1. Parse the request.
   - Identify theme, event type, exact copy, subject, mood, image role, and reference-image controls.
   - Decide whether the visual is a spectral poster, program, or type specimen.

2. Select a recipe.
   - Choose one layout family, one spectral anchor, two to four type layers, up to two diagram systems, and one signal color.

3. Compile the prompt.
   - State artboard ratio, quiet-space share, anchor opacity, copy hierarchy, type zone, signal marks, and print process.
   - Keep user-supplied text verbatim and short enough for reliable generation.

4. Generate the image.
   - Use the built-in image generation capability by default.
   - If unavailable, run `scripts/server_image_gen.py` with the final prompt.

5. Inspect and regenerate once when needed.
   - Regenerate if the result is too blank, type becomes an unreadable wall, the ghost image disappears, signal colors spread, or the poster looks like a glossy event ad.
   - Tighten hierarchy and opacity before adding new elements.

6. Return the image, final prompt, copy deck, and selected recipe.

## Reference Image Policy

- Extract atmospheric density, image opacity, typography zones, font contrast, diagram behavior, signal color, and print degradation.
- Treat supplied references as a design system, not as assets or copy sources.
- Do not reproduce visible artist names, dates, venue lists, tracklists, signatures, logos, or exact layouts.
- Do not infer identity or sensitive traits from blurred people or body fragments.

## Negative Constraints

Always avoid:

- generic Y2K chrome, cyberpunk, rave flyer, neon nightclub poster, or glossy fashion campaign
- full-bleed crisp photography, polished gradient, 3D glass, chrome type, lens flare, and cinematic lighting
- dense text wall, random font soup, illegible pseudo-language, and fake technical data
- centered corporate event hierarchy, call-to-action buttons, QR codes, social media UI, or black screenshot frame
- multiple bright accent colors, dominant purple grading, teal-orange grading, and one-note pastel wash
- decorative stickers, scrapbook tape, cute flowers, emoji-like icons, and unrelated symbols
- copied names, event data, logos, signatures, watermarks, or sponsor marks

## Fallback Script

The fallback reads the OpenAI-compatible provider from Codex configuration or environment variables and never stores credentials in the Skill.

```bash
python3 scripts/server_image_gen.py \
  --prompt-file /absolute/path/to/prompt.txt \
  --out output/imagegen/spectral-type-field-zine-output.png
```

Use `--dry-run` to inspect the request without sending it. The default is the Images API; use `--wire-api responses` only for a compatible Responses image-generation endpoint.

## Output Format

````markdown
**生成图**

![Spectral Type Field Zine](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**视觉配方**

- Mode: [Spectral Field / Program / Type Specimen]
- Layout: [layout family]
- Anchor: [spectral image]
- Signal: [one color]
````

## Quality Gate

Before finalizing, check:

- Does the artboard read as a pale printed field rather than a black screenshot or UI?
- Does 55%-80% of the page remain low-information atmosphere?
- Is there one legible spectral image anchor?
- Are there only two to four typography layers with clear jobs?
- Is information concentrated in one or two zones rather than spread everywhere?
- Are diagram marks sparse and meaningful?
- Is one signal color visible but restrained?
- Does the surface read as xerox, vellum, toner, raster, or degraded print?
- Did the result avoid glossy commercial, rave, Y2K chrome, font soup, and copied reference data?
- Was the raster image actually generated?

## Example Requests

- `用 $spectral-type-field-zine 生成一张关于“透明”的雾蓝字体实验海报`
- `把这场展览的标题、日期和地点做成幽灵人物与节目单叠印海报`
- `生成灰白低对比的字体标本页，加入模糊手部和细轨迹线`
