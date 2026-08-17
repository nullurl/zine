---
name: 地平线回忆
description: "【地平线回忆 / horizon-strip-memory-zine】 Generate prompts and finished raster images for vertical memory zines built from rounded horizontal landscape strips. Use when the user provides a theme, place, weather, sentence, or reference image and wants cloud studies, moonlit horizons, rural scenery, gardens, roads, utility lines, animals, or quiet time-sequenced photographs arranged as a clean contact-sheet poster with white gutters, soft film color, and restrained Minimal Zine composition."
---

# Horizon Strip Memory Zine

Turn the user's idea into both a compact image-generation prompt and a finished raster image. The default artifact is a tall white editorial sheet containing five rounded-corner panoramic photo windows stacked vertically with even gutters. Each window is a separate but related moment; together they form a quiet memory, weather diary, or place sequence.

This Skill reverse-engineers the structural discipline of `gc-minimal-zine-poster-v0-1`: strict attention geometry, generous negative space, one coherent visual system, restrained text, and a tactile scanned/printed feeling. It replaces the tiny paper cluster with a precise photographic strip system.

## Mode Policy

Use **Strip Mode** by default. Use **Sequence Mode** when the user explicitly asks for a chronology, day-to-night progression, journey, or multiple locations.

- **Strip Mode:** 4-6 equal panoramic windows; each strip carries one visual event.
- **Sequence Mode:** 5-7 strips ordered by time, elevation, distance, weather, or emotional intensity.

Keep the outer page quiet and the internal windows consistent. Do not turn the result into a generic collage, mood board, or scrapbook.

## Prompt Compiler

Every final prompt must specify these fields in order:

1. **Page geometry**
   - Tall vertical 3:5 or 2:3 white/off-white page.
   - 4-6 wide horizontal panoramic strips, stacked with equal white gutters.
   - Each strip has the same large radius, consistent width, and no visible border or shadow.

2. **Strip rhythm**
   - State the number of strips and their order.
   - Make the sequence vary in altitude or distance: sky, infrastructure, night, garden, field, road, water, or distant architecture.
   - Preserve a calm top-to-bottom rhythm; no strip should visually overpower all others without a narrative reason.

3. **Image content**
   - Give every strip one legible anchor: cumulonimbus cloud, thin tree line, utility poles, moon and bird, house and lawn, rice field, horses, road, coast, or window reflection.
   - Keep subjects distant and atmospheric. Avoid portraits unless explicitly requested.
   - Use panoramic crops with low horizon, deep sky, or layered terrain.

4. **Color and light**
   - Choose one palette family: `cloud cream and sky blue`, `blue-green rural dusk`, `charcoal moonlight`, `mist gray garden`, or `field green with warm earth`.
   - Keep the whole set coherent but allow time-of-day changes.
   - Use soft natural light, slight haze, mild bloom, and muted but present color. No global gray wash.

5. **Capture and surface**
   - Analog compact-camera or medium-format landscape photography, gentle film grain, slight lens softness, subtle dust, matte print, and restrained contrast.
   - Preserve real scale relationships in poles, houses, trees, horses, birds, and moon.

6. **Typography**
   - Text is optional. If used, add one tiny title, date, location, or sequence number on the page margin, never across the photos.
   - Keep the type small, quiet, and short: 2-5 words or a compact date line.

7. **Hard avoids**
   - State: no collage clutter, no sticker decorations, no arbitrary frame colors, no gradients, no 3D render, no glossy mockup, no commercial travel advertisement, no fake long text, no watermark.

Write the final prompt as four compact paragraphs: page/strip geometry; ordered strip content; color/capture; typography and avoid-list.

## Strip Architecture

Select one architecture and one narrative order.

### Architectures

- `five-window-diary`: five equal strips, each a different quiet observation
- `sky-to-ground`: clouds, electrical horizon, moon, garden, field
- `day-to-night`: warm cloud, blue hour, moon, mist, dark field
- `near-to-far`: foreground plants, house, utility line, hill, distant animal
- `weather-contact-sheet`: clear sky, cumulus, rain haze, moon, wet grass
- `single-place-variations`: one location repeated across light, crop, and distance

### Narrative Orders

- time: afternoon -> dusk -> night -> dawn
- altitude: sky -> horizon -> tree line -> garden -> ground
- distance: close texture -> middle ground -> distant landscape
- emotional: open -> interrupted -> solitary -> sheltered -> released

## Color Engine

Use one dominant family and one small temperature shift. Preserve photographic color inside the strips.

- `cloud cream and sky blue`: pale cyan sky, cream cloud, soft tree-line green
- `blue-green rural dusk`: slate blue, eucalyptus green, faded grass, warm roof light
- `charcoal moonlight`: deep blue-gray, brown moon, tiny black bird silhouette
- `mist gray garden`: soft gray sky, layered green, muted yellow building or path
- `field green with warm earth`: agricultural greens, ochre soil, distant blue car or red marker

Do not make every strip monochrome. Do not introduce purple cinematic grading or a different color identity in each panel.

## Workflow

1. Parse the request.
   - Extract place, season, weather, exact phrase, time range, objects, and reference-image role.
   - Treat a reference as evidence for architecture, crop, color, and grain; do not copy its exact scenery or text.

2. Form the sequence thesis.
   - Reduce the concept to `[a place] remembered through [a sequence of horizons]`.
   - Example: `a summer evening remembered from cloud, power line, moon, garden, and field`.

3. Select architecture, narrative order, palette, and capture mode.
   - Keep one visual grammar across all strips.
   - Use 5 strips unless the user specifies another count.

4. Compile the prompt.
   - Specify exact strip count, corner radius, gutter width, page proportion, crop logic, and order.
   - Describe each strip in one concrete sentence.
   - Keep typography secondary and do not request long readable copy from the image model.

5. Generate the image.
   - Use the built-in image generation capability by default.
   - If unavailable, run `scripts/server_image_gen.py` with the final prompt.

6. Inspect and regenerate once when needed.
   - Regenerate if strips merge, gutters disappear, corners are inconsistent, the image becomes a single full-bleed landscape, or the colors drift between panels.
   - Tighten layout instructions before adding more objects.

7. Return the image, final prompt, and selected architecture.

## Reference Image Policy

- Extract the repeated system: rounded horizontal crops, white gutters, page ratio, strip count, horizon placement, palette, and film surface.
- Preserve the user's own subject or place when supplied, but do not infer identity or sensitive traits.
- Do not reproduce watermarks, signatures, logos, exact captions, or a source image pixel-for-pixel.
- If references conflict, follow the repeated layout grammar and choose the clearest palette family.

## Negative Constraints

Always avoid:

- random scrapbook stickers, tape, paper scraps, decorative borders, or polaroid frames
- irregular strip sizes, uneven gutters, inconsistent rounded corners, or floating panels
- one large full-bleed scene with fake horizontal dividers
- commercial travel brochure, real-estate listing, or stock-photo montage feeling
- oversaturated HDR, heavy teal-orange grading, purple grading, neon, CGI, and 3D depth
- cartoon clouds, fantasy landscapes, impossible moon scale, malformed animals, or unreadable clutter
- long clean paragraphs, prominent logos, watermarks, and copied source text

## Fallback Script

The fallback reads the OpenAI-compatible provider from Codex configuration or environment variables. It never stores credentials in the Skill.

```bash
python3 scripts/server_image_gen.py \
  --prompt-file /absolute/path/to/prompt.txt \
  --out output/imagegen/horizon-strip-memory-zine-output.png
```

Use `--dry-run` to inspect the request without sending it. The default is the Images API; pass `--wire-api responses` only for a compatible Responses endpoint.

## Output Format

````markdown
**生成图**

![Horizon Strip Memory Zine](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**构图配方**

- Mode: [Strip or Sequence]
- Architecture: [architecture / order / palette]
- Interpretation: [one short sentence]
````

## Quality Gate

Before finalizing, check:

- Is the page a tall vertical sheet with 4-6 intentional panoramic windows?
- Are the rounded corners, widths, and white gutters consistent?
- Does each strip contain one legible landscape event?
- Do all strips share a coherent capture and color system?
- Is the order meaningful rather than arbitrary?
- Does the page remain visually quiet outside the strips?
- Are the moon, clouds, poles, buildings, animals, and horizons physically scaled?
- Is typography sparse or absent?
- Did the result avoid scrapbook clutter, commercial travel design, CGI, and oversaturated HDR?
- Was the raster image actually generated?

## Example Requests

- `用 $horizon-strip-memory-zine 做一张关于夏天傍晚的五条风景记忆页`
- `参考这张图的圆角横幅结构，生成“雨后的田野”`
- `做一张从云、月亮、庭院到草地的竖向风景联系表`
