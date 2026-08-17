---
name: 极简Zine V2
description: "【极简Zine V2 / gc-minimal-zine-poster-v0-2】 Generate Minimal Zine Poster v0.2 prompts and matching raster images for poetic editorial posters with richer directions: Eastern ink/Song-painting mood, vintage natural-science diagrams, old textbook motion studies, star charts, Swiss/Bauhaus/editorial graphics, collage, cinematic atmosphere, Japanese woodblock, data-visualization art, generative trajectories, and surreal poetic migration scenes. Use when the user gives a theme, sentence, object, article idea, reference image, or style brief and wants a sparse but more emotionally or conceptually infectious poster image."
---

# Minimal Zine Poster v0.2

Turn the user's content into both:

1. a final image-generation prompt, and
2. a generated raster image made from that prompt.

v0.2 keeps the v0.1 paper-zine discipline but allows stronger visual infection through selected art directions: Eastern poetic, vintage diagram, modern graphic, cinematic atmosphere, and experimental data.

## Mode Policy

Use **Standard Mode** for all generation unless the user explicitly asks for prompt-only.

Use the v0.2 Prompt Compiler to turn the user's content into a compact, imageable, high-fidelity prompt. Do not output a broad style essay. The final prompt must describe only visible pixels, layout, material treatment, type behavior, reproduction texture, mood, and avoid-list.

## Direction Policy

Choose one primary direction and, only when useful, one secondary modifier. Do not mix more than two directions in one image.

Prefer the user's explicit style request. If no direction is specified, choose by content:

- **Eastern poetic:** autumn, migration, birds, mountains, moon, wind, silence, seasonal emotion, Chinese/Japanese literary mood.
- **Vintage natural-science diagram:** animals, plants, flight, specimens, observation, coordinates, labels, archival research, museum notebook.
- **Old textbook physics:** movement, trajectory, timing, velocity, angle, experiment, contrast between rational diagram and poetic text.
- **Star-chart migration:** night, navigation, moon phase, compass, seasonal route, constellation-like path.
- **Swiss editorial:** exhibition poster, issue cover, strong title, clean grid, restrained commercial polish without ad language.
- **Bauhaus geometry:** paths, time nodes, arrows, circle-line composition, abstract order.
- **Magazine cover/editorial:** polished social/poster layout, issue number, date, vertical Chinese, short subtitle.
- **Collage memory:** journey, maps, postmarks, tickets, handwritten dates, travel fragments, remembered places.
- **Cinematic atmosphere:** stronger emotion, dusk, mist, lake, remote lights, narrative distance, album/film poster energy.
- **Japanese woodblock:** moon, cloud curves, bird silhouettes, flat ink fields, handmade print texture.
- **Controlled guochao:** Chinese cultural poster, seal, auspicious cloud, red/gold accents; keep restrained, not souvenir-like.
- **Data poetry:** wind speed, route, temperature, altitude, time nodes, seasonal measurement.
- **Generative trajectory:** particles, flow fields, algorithmic curves, flock motion, dynamic-poster still.
- **Surreal poetic:** scale shift, huge bird shadow, tiny human, horizon-axis, fate-line trajectory.

When the user supplies a current minimal poster or existing work, preserve the core subject, title, and strongest motif, then upgrade only the visual grammar.

## v0.2 Prompt Compiler

Every Standard Mode prompt must answer these rendering questions in this order.

### 1. Canvas

Use a tall vertical 3:5 paper-poster frame unless the user asks for another format. The base surface is aged paper, xuan paper, silk-paper, old book paper, newsprint, or museum archive stock. The image is a flat orthographic scan, not a photographed mockup.

### 2. Attention Geometry

Keep 55%-85% quiet surface. v0.2 may be fuller than v0.1, but it still needs room to breathe. Use one main cluster or one clear scene-diagram relationship occupying about 12%-35% of the canvas. Avoid edge-hugging unless the direction is Swiss/editorial and the margin system is explicit.

### 3. Image Anchor

Convert the user's theme into one imageable anchor:

- bird flock, single bird, wing fragment, feather, moon, mountain line, map shard, coordinate trace, specimen panel, field-note diagram, data curve, shadow, ticket, old printed illustration, abstract trajectory, or small scene window.

For complex articles, extract one central visual metaphor instead of illustrating every idea.

### 4. Anchor Treatment

Make the anchor belong to the chosen material:

- ink wash, dry-brush flying white, mineral pigment, silk-fiber fading, old restoration stains, engraving linework, letterpress, risograph grain, halftone, xerox softness, map folds, stamp bleed, screenprint misregistration, woodblock flatness, or data-plot hairlines.

Do not weaken the selected accent color with `pale`, `muted`, `faded`, or `low saturation` unless the user explicitly requests that.

### 5. Typography System

Use sparse, intentional type. Choose one short readable phrase and optional microtext. Long text usually fails in image generation.

Valid text systems:

- vertical Chinese title with tiny English transliteration
- archive label with date, place, weather, specimen number
- typewriter observation note
- Swiss grid title and issue number
- caption pressed against image edge
- formula-like phrase beside a trajectory
- semi-legible microtext, fragmented letters, or map annotations

When no text is supplied, invent one short poetic phrase in Chinese or English.

### 6. Color Logic

Use restrained color with one decisive accent. v0.2 permits a richer palette than v0.1 but must keep a dominant material base.

Default accents by direction:

- Eastern poetic: cinnabar red, mineral blue-green, ink gray, ochre.
- Song-painting/restoration: pale silk base with celadon, ochre, ink gray, one cinnabar seal.
- Natural-science diagram: tomato red route, black/brown ink, aged cream paper.
- Old textbook physics: red dashed curve, graphite grid, black bird silhouettes.
- Star chart: deep indigo field or aged blue-black paper with warm gold linework.
- Swiss editorial: black, warm paper, one red/cobalt accent.
- Bauhaus: red curve, black shape, yellow/cream field.
- Collage: aged paper, black ink, one red postmark or route line.
- Cinematic: one atmosphere family plus one restrained accent, such as dusk orange with dark red or blue-gray with silver.
- Woodblock: indigo, cinnabar, warm paper.
- Data/generative: black/gray data marks with one saturated route or node color.

The accent should be visible at thumbnail scale. If using a route line, make it substantial enough to read as a compositional mark, not a hairline.

### 7. Reproduction Texture

Render as a printed or scanned artifact: matte absorbent paper, visible fibers, mottling, old print defects, imperfect registration, softened ink edges, archive stains, or field-notebook wear. Use diffuse light, low-to-medium contrast, and no hard 3D shadow.

### 8. Emotional Temperature

Set the feeling before object recognition: quiet, poetic, autumnal, archival, lonely, migratory, museum-like, observational, time-worn, cinematic, mysterious, or data-poetic.

### 9. Hard Avoids

Avoid full-bleed stock-photo realism, product ad layouts, logo/CTA, generic travel poster, glossy mockups, clean UI white, 3D rendering, neon cyberpunk, cute cartoon, anime poster, fashion editorial drama, dense sticker scrapbook, overloaded captions, too many colors, and long perfectly readable text blocks.

## Direction Recipes

Before writing the prompt, select one recipe. If recent outputs used the same direction, change the direction or layout.

### A. Eastern Poetic

- **New Chinese ink:** xuan paper, ink wash cloud, dry-brush birds, faint mountain, cinnabar route or seal.
- **Song painting restoration:** silk texture, celadon/ochre/ink palette, small inscription, repaired stains, museum artifact feeling.
- **Haiku illustration:** almost empty paper, one seasonal scene fragment, short line of text, stronger emotional silence.

Use for "雁过无声", "秋声", "归途", "候鸟", seasonal solitude, wind, old paper sky.

### B. Vintage Diagram

- **Natural-science illustration:** bird specimen, motion sequence, Latin/English/Chinese labels, scale bar, observation date.
- **Old textbook physics:** coordinate grid, time marks, angle/velocity arrows, parabolic or migratory curve, poetic conflict text.
- **Star chart:** moon phase, compass, constellation lines, migration route as star trail.

Use when the image already has coordinates, numbering, routes, arrows, or scientific framing.

### C. Modern Graphic

- **Swiss international:** strict grid, enlarged number, large but sparse title, black/paper/red or cobalt palette.
- **Bauhaus geometry:** circles, arrows, time nodes, red arc, black silhouettes, flat color blocks.
- **Editorial cover:** issue title, date, vertical Chinese, small subtitle, polished art-magazine hierarchy.
- **Collage:** old map, postmark, ticket, torn paper, handwriting, red route line.

Use for more shareable posters, issue covers, exhibition visuals, social media headers, or commercial-but-artful variants.

### D. Atmospheric

- **Cinematic poster:** dusk, mist, lake, mountain shadow, distant lights, flock as narrative beat; still keep paper/print treatment.
- **Japanese woodblock:** flat moon, cloud bands, indigo/cinnabar, carved line texture, bird silhouettes.
- **Controlled guochao:** restrained seal, cloud motif, gold line, bold Chinese title; avoid festive souvenir density.

Use when the user asks for stronger emotion, story, scene, season, music-cover mood, or decorative art.

### E. Experimental

- **Data visualization art:** wind field, route, altitude, temperature, speed, time nodes, diagram legend as poetry.
- **Generative trajectory:** flock as particles, flow lines, repeated dots, algorithmic curve, dynamic-poster still.
- **Surreal poetic:** scale break, giant bird shadow, tiny figure, horizon-axis, red fate line.

Use for conceptual series, exhibition research, motion-poster stills, or abstract migration/time/path themes.

## Variation Axes

After choosing a recipe, select one from each axis.

### Layout Family

- center-specimen
- lower-left-field-note
- upper-right-map-fragment
- vertical-title-scroll
- dual-panel-observation
- grid-poster
- orbit-chart
- horizon-axis
- moon-window
- collage-corner

### Anchor Type

- ink bird flock
- motion-sequence birds
- old printed bird illustration
- feather specimen
- moon and bird silhouette
- map shard with route
- coordinate trajectory
- field-note panel
- data curve and nodes
- huge shadow with tiny figure
- torn paper sky window

### Typography Mode

- vertical Chinese title
- typewriter micro-observation
- bilingual archive label
- formula-like caption
- Swiss issue title
- scattered letters
- inscription and seal
- map annotation
- almost textless caption

### Texture Mode

- xuan-paper ink bleed
- silk painting restoration
- aged book paper mottling
- letterpress ink bite
- halftone print wear
- xerox softness
- risograph grain
- folded map abrasion
- woodblock registration
- scanned field notebook

### Mood Mode

- autumn silence
- migratory distance
- museum calm
- observational curiosity
- dusk melancholy
- cold morning solitude
- night navigation
- old journey memory
- rational poetry
- slight surrealism

## Prompt Shape

Write the final Standard Mode prompt as four compact paragraphs:

1. canvas + paper surface + negative space + cluster/layout
2. subject metaphor + anchor type + direction-specific treatment
3. typography + accent color/material/share + diagram/print defects
4. flat-scan mood + reproduction texture + avoid-list

In paragraph 3, state the exact accent hue, its form, and how visible it is. Prefer concrete wording such as `cinnabar-red dashed migration route occupying about 2% of the canvas`, `opaque cobalt-blue map shard`, or `warm gold constellation lines`.

## Workflow

1. Determine mode.
   - Use Standard Mode.
   - Use prompt-only only if the user explicitly requests prompt-only.

2. Parse the user's content.
   - Identify subject, theme, supplied text, reference image role, desired direction, mood, and output use.
   - For a complex brief, extract one central imageable metaphor.
   - If no title is supplied, invent a short phrase.

3. Select the recipe.
   - Pick one primary direction from Direction Recipes.
   - Optionally add one secondary modifier when it reinforces the theme.
   - Pick layout, anchor, typography, texture, and mood from Variation Axes.

4. Compile the prompt.
   - Use the four-paragraph Prompt Shape.
   - Make the prompt decisive about placement, scale, material, accent, and type behavior.
   - Keep text short enough for image models.

5. Generate the image.
   - Use the built-in image generation capability by default.
   - Do not stop after writing the prompt.
   - If the result obviously violates the recipe, regenerate once with tighter constraints.
   - If the accent disappears at thumbnail scale, regenerate once with stronger accent size/material wording.

6. Return the image and prompt.

## Negative Constraints

Always avoid:

- generic stock-photo scenes
- full-bleed commercial travel posters unless the user explicitly asks for a scenic poster
- product ad layout, logo lockup, CTA, or brand campaign feeling
- glossy mockup photos or heavy paper shadows
- clean digital UI background
- 3D rendering, cinematic lens blur, neon, cyberpunk
- cute cartoon, kawaii, anime, mascot illustration
- overly festive guochao souvenir style
- dense scrapbook/sticker overload
- too many decorative motifs
- long, clean, perfectly readable text blocks
- prompts that list all 16 directions at once

## Output Format

````markdown
**生成图**

![Minimal Zine Poster v0.2 style poster](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Mode: Standard
- Recipe: [primary direction + optional modifier / layout / anchor / typography / accent / texture / mood]
- [one short note about the content interpretation]
````

If generated images render directly without a file path, show the image normally and still include the final prompt.

## Quality Gate

Before finalizing, check:

- Did the run use Standard Mode and the v0.2 Prompt Compiler?
- Did it select one primary direction, not a mixed style list?
- Does the image still read as a poetic printed poster rather than a generic illustration?
- Does the poster preserve meaningful quiet surface?
- Is the visual anchor clear at thumbnail scale?
- Is the accent color visible and materially specified?
- Is typography part of the composition without becoming a long text block?
- Does the selected direction match the user's content and requested mood?
- Did the prompt include print/scan/material defects?
- Did the prompt avoid commercial ad, glossy mockup, stock-photo, 3D, neon, cute, anime, and overloaded collage aesthetics?
- Did you actually generate the image unless prompt-only was requested?

## Example Requests

- "用 $gc-minimal-zine-poster-v0-2 做一张《雁过无声》，偏复古博物学图谱。"
- "用 $gc-minimal-zine-poster-v0-2 做宋画秋色版，主题是归途。"
- "用 $gc-minimal-zine-poster-v0-2 把候鸟迁徙做成数据诗歌海报。"
- "用 $gc-minimal-zine-poster-v0-2 做一张日式版画风的秋雁月夜。"
