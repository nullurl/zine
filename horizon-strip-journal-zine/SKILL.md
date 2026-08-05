---
name: 地平线日记
description: Generate prompts and finished raster images for hand-drawn landscape journal zines that combine 4-6 rounded panoramic photo strips with pencil sketches, ink marks, watercolor notes, small captions, and Minimal Zine paper-poster discipline. Use when the user provides a place, weather, memory, sentence, object, or reference image and wants a quiet handmade field diary rather than a dense scrapbook.
---

# Horizon Strip Journal Zine

Turn the user's theme or reference into both a final image-generation prompt and a finished raster image. The default artifact is a tall 3:5 or 2:3 paper page with 4-6 equal horizontal rounded windows. Photo strips and hand-drawn journal interventions alternate through the sequence: a cloud photograph may be followed by a pencil cloud study, a moon photograph by a tiny ink constellation, or a field photograph by a hand-drawn map line.

This is a derivative of `horizon-strip-memory-zine` and `gc-minimal-zine-poster-v0-1`. It preserves the original Minimal Zine prompt logic: large quiet paper field, clear attention geometry, one visual anchor, restrained accent color, small editorial type, scanned-paper texture, and no commercial poster hierarchy. It expands the image anchor from one tiny paper cluster into a disciplined 4-6-cell visual diary.

## Mode Policy

Use **Journal Strip Mode** by default. Use **Reference Fusion Mode** when a reference image is supplied and its layout, crop, palette, and hand-drawn behavior must be extracted.

- **Journal Strip Mode:** 4-6 rounded landscape windows with alternating photo and hand-drawn treatments.
- **Reference Fusion Mode:** match the repeated structure of the reference, then add hand-drawn interventions without copying exact content, text, or marks.

Use five cells by default. Four cells are suitable for a short visual poem; six cells are suitable for a full day, route, or weather sequence. Do not add cells merely to fit more objects.

## Prompt Compiler

Write the final prompt as five compact paragraphs in this order.

### 1. Page and attention geometry

State:

- tall vertical 3:5 or 2:3 full-frame matte paper page
- 4-6 equal-width panoramic strips stacked vertically
- identical large rounded corners and even off-white gutters
- no card shadow, device mockup, decorative border, or interface styling
- quiet page margins and a clear top-to-bottom reading rhythm

The strips may occupy most of the page, but preserve visible paper between them. The white page is the structural field, not a UI background.

### 2. Cell-by-cell narrative

List every cell in order and label its treatment:

- `photo strip`: real landscape photograph with one distant anchor
- `photo + sketch`: photograph with a restrained pencil or ink contour over one feature
- `hand-drawn study`: colored-pencil, graphite, ink, or translucent watercolor observation on paper
- `map / notation`: a sparse horizon diagram, route line, weather symbol, plant study, or moon phase
- `material strip`: paper, tracing sheet, rubbing, ticket fragment, or small color swatch used only when it serves the memory

Use no more than two consecutive cells of the same treatment. Every cell has one dominant visual event: cloud, tree line, power pole, moon, garden, roof, road, water, animal, plant, or handwritten observation.

### 3. Minimal Zine visual anchor

Apply the original Minimal Zine rules inside the strip system:

- one clear visual anchor visible at thumbnail size
- one main high-chroma hue, preferably cobalt, ultramarine, pear green, lemon yellow, orange, or tomato red
- keep the paper, grayscale photo regions, microtext, and secondary marks subdued
- make the chromatic anchor a small but opaque drawn mark, cutout, subject detail, or color block; never let it dissolve into a weak dot or global wash
- use sparse typewriter, serif, or monospaced text only when it improves the diary reading

For one image, the saturated anchor should occupy approximately 0.8%-2.5% of the page or 15%-35% of the active visual cluster. Use only one main hue and a tiny supporting hue when physically necessary.

### 4. Hand-drawn and paper treatment

Specify how hand-drawn matter enters the page:

- imperfect graphite, colored pencil, wax crayon, dry brush, fountain pen, or translucent watercolor
- visible pressure changes, broken contours, erased edges, paper fibers, registration drift, and slight misalignment
- marginal arrows, tiny circles, date marks, weather symbols, plant labels, route lines, or underlined words
- hand-drawn layers should sit in a strip or gutter with clear attachment to a photographed feature

The drawings are observational and economical, not cartoon characters, kawaii stickers, or decorative doodle clouds. Keep 70%-90% of any hand-drawn cell visually quiet. For a mixed photo cell, cover only 5%-20% of its image area with linework unless the user asks for a heavier drawing.

### 5. Capture, type, and avoid-list

End with analog compact-camera or medium-format photography, matte absorbent paper, soft scan, gentle film grain, low-to-medium contrast, subtle halftone or photocopy wear, and diffuse light. Add at most one short phrase, date, or location line in the white margin. Explicitly avoid full-bleed scenery, dense scrapbook clutter, commercial travel design, glossy 3D, cinematic grading, neon, long clean text, logos, watermarks, and copied source marks.

## Cell Rhythm Engine

Select one rhythm and then specify the treatment of each cell.

### Photo / Drawing Alternation

`photo -> pencil study -> photo + ink -> watercolor map -> photo`

Best for cloud watching, nature diary, a place remembered through observations, and calm visual poems.

### Time and Weather

`warm cloud photo -> blue-hour drawn sky -> moon photo -> mist garden sketch -> green field photo`

Best for one day, a season, rain, summer, or a slow evening.

### Near / Far / Trace

`close plant photo -> route drawing -> distant house photo -> horizon notation -> field or animal photo`

Best for travel, leaving home, walking, and uncertain geography.

### Image / Paper / Image

`photograph -> tracing-paper line study -> photograph -> handwritten archive strip -> photograph`

Best when the reference image has strong photography and the user asks for hand-accounted memory.

## Layout Families

- `five-window-diary`: five equal rounded strips; photo and drawing alternate with a quiet middle cell
- `sky-to-ground-journal`: cloud, infrastructure, night, garden, field
- `day-to-night-notebook`: warm light, blue hour, moon, dawn, wet ground
- `weather-contact-sheet`: each cell records cloud, wind, rain, visibility, or reflection
- `route-memory-strip`: foreground, path, structure, horizon, destination
- `six-cell-field-notes`: three photo cells and three hand-drawn or annotated cells interleaved

## Minimal Zine Prompt Bridge

Use the source Skill's prompt principles as a compiler, not as literal prose to paste into every request.

### Preserve

- vertical paper poster and flat scanned-paper view
- large negative space and a restrained visual cluster
- one imageable anchor rather than a full illustrated scene
- muted grayscale support with one saturated opaque accent
- short serif/typewriter text and tiny archive details
- old print defects: paper fibers, risograph grain, xerox softness, halftone, ink bleed, or slight misregistration

### Adapt

- tiny cluster becomes 4-6 panoramic windows with stable gutters
- one object anchor becomes one anchor per cell, linked by a shared place or weather
- one color accent may recur as a hand-drawn mark, but it remains one hue family
- paper fragments become restrained field-note layers, not dense scrapbook decoration

### Do not import

- source paths, sample metadata, signatures, dates, captions, or exact objects from the original sample
- the original tiny-cluster scale when it would make the strip sequence unreadable
- `near-monochrome`, `no strong accent`, or `pale accent` unless the user explicitly asks for that

## Workflow

1. Parse the theme and reference.
   - Identify subject, mood, exact phrase, place, season, and whether the image controls layout, palette, texture, or content.
   - If the theme is abstract, reduce it to one place-memory and one material verb such as `watch`, `collect`, `trace`, `wait`, or `return`.

2. Select four to six cells.
   - Choose a rhythm, layout family, palette, one anchor hue, and one drawing medium.
   - Assign every cell a treatment before writing the prompt.

3. Compile the five-paragraph prompt.
   - State geometry first, then cell order, then the Minimal Zine color anchor, then hand-drawn behavior, then surface and avoids.
   - Keep text short and optional. Image models are not reliable for long diary writing.

4. Generate the image.
   - Use the built-in image generation capability by default.
   - If unavailable, run `scripts/server_image_gen.py` with the final prompt.

5. Inspect at thumbnail scale and regenerate once when needed.
   - Regenerate if rounded windows merge, hand-drawn cells look like cartoons, the page becomes a dense scrapbook, the accent color disappears, or the photo/drawing alternation is not legible.

6. Return the image, final prompt, cell rhythm, and anchor color.

## Reference Image Policy

- Extract stable geometry: page ratio, count, crop ratio, corner radius, gutter, horizon placement, and sequence direction.
- Extract visual behavior: cloud density, distance, lens softness, muted colors, and the amount of empty paper.
- Add hand-drawn layers as an interpretation of the reference, not as a copy of its exact details.
- Do not reproduce watermarks, signatures, logos, exact text, or a source image pixel-for-pixel.
- Do not infer identity or sensitive traits from a reference.

## Negative Constraints

Always avoid:

- dense scrapbook, maximalist journaling, sticker packs, tape clusters, washi borders, or decorative clutter
- rounded UI cards, shadows, gradient backgrounds, device mockups, and polished template language
- full-bleed landscape with fake divider lines instead of separate cells
- cartoon clouds, kawaii drawings, anime, childish clip art, or generic watercolor scenery
- commercial travel brochure, real-estate listing, lifestyle campaign, or stock montage feeling
- oversaturated HDR, purple cinematic grading, teal-orange blockbuster grading, neon, CGI, and 3D
- weak gray-on-gray color where the required anchor disappears
- long pseudo-readable text, logos, copied captions, signatures, and watermarks

## Fallback Script

The fallback reads the OpenAI-compatible provider from Codex configuration or environment variables and never stores credentials in the Skill.

```bash
python3 scripts/server_image_gen.py \
  --prompt-file /absolute/path/to/prompt.txt \
  --out output/imagegen/horizon-strip-journal-zine-output.png
```

Use `--dry-run` to inspect the request without sending it. The default is the Images API; use `--wire-api responses` only for a compatible Responses image-generation endpoint.

## Output Format

````markdown
**生成图**

![Horizon Strip Journal Zine](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**构图配方**

- Mode: [Journal Strip or Reference Fusion]
- Cells: [photo / sketch / photo+ink / map / photo]
- Anchor color: [one hue]
- Interpretation: [one short sentence]
````

## Quality Gate

Before finalizing, check:

- Are there exactly 4-6 intentional rounded horizontal cells?
- Are widths, corner radii, gutters, and page margins consistent?
- Does each cell have one clear landscape or journal event?
- Are photo, hand-drawn, and mixed treatments visibly interleaved?
- Does each drawing attach to a real observed feature rather than float as decoration?
- Is one opaque high-chroma anchor visible at thumbnail size?
- Is the page mostly quiet paper rather than dense scrapbook material?
- Are typography and microtext sparse, short, and subordinate?
- Does the result retain analog paper/scan texture without becoming a UI template?
- Did the output avoid commercial, cartoon, neon, CGI, and copied-source aesthetics?
- Was the raster image actually generated?

## Example Requests

- `用 $horizon-strip-journal-zine 做一张云、月亮、庭院和田野的手账风景页`
- `参考这张五条风景图，加入铅笔手绘和少量手写批注`
- `生成四格“雨后散步”照片与手绘地图交错的 Minimal Zine`
