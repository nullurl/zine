---
name: dream-bloom-veil-zine
description: 【梦境花绽纱幕 / dream-bloom-veil-zine】 Generate prompts and finished raster images for dreamy botanical veil-overlay zines, soft-focus floral scenes with misted pastel blooms, translucent paper-veil atmosphere, luminous hazy light, and painterly-photographic hybrid texture. Use when the user gives a flower, season, garden, mood, color, memory, or reference image and wants a misted dreamy botanical zine rather than a sparse paper poster, a full-bleed storybook scene, or a calendar planner.
---

# Dream Bloom Veil Zine

Turn the user's flower, season, garden, mood, color, memory, or reference image into:

1. a final image-generation prompt, and
2. a generated raster image made from that prompt.

Use the `imagegen` skill for generation or editing. Prefer the local configured CLI/API path when the user explicitly asks for local image generation, image-gen CLI, model/API controls, or pptoken.

## Style Thesis

Create misted, soft-focus botanical zines where flowers emerge from and dissolve into a translucent veil of pale color. The image should feel like a botanical photograph seen through condensation, tracing paper, or early-morning mist: blooms are recognizable but never crisp, edges bleed into a warm haze, and the whole surface carries a paper-like grain or fiber texture. This skill is the dreamy botanical counterpart to `gc-minimal-zine-poster-v0-1`: keep its prompt-compiler discipline, but replace sparse single-anchor logic with all-over atmospheric bloom, veil overlay, and muted pastel density.

## Reference-Derived Structure

Use these rules as the core visual grammar:

- **Frame:** vertical portrait, typically 3:4 to 3:5. No border, no mockup, no calendar grid. The entire canvas is the botanical scene.
- **Surface:** the whole image carries a paper-fiber grain, subtle canvas tooth, or film-grain noise that prevents it from reading as a clean digital photo. The texture is uniform and gentle, never harsh or posterized.
- **Veil:** a translucent milky overlay mists the entire image. Blooms are soft-edged, as if seen through condensation, vellum, or light fog. Detail is present but never razor-sharp. The veil reduces micro-contrast without killing color identity.
- **Bloom logic:** flowers or botanical subjects fill 50%-80% of the canvas. They can be dense clusters, sparse sprigs, single oversized bloom, or scattered petals. Stems and leaves are soft, not botanical-illustration crisp.
- **Depth:** shallow depth-of-field feel. Foreground blooms are slightly more defined, midground softens, background dissolves into haze. No hard horizon line.
- **Light:** diffuse, directionless, early-morning or overcast. No harsh shadows, no spotlight, no sunset rim. A warm luminous bloom may glow gently from within the flowers, as if light passes through petals.
- **Color palette:** muted pastels dominate. Cream, blush pink, dusty rose, pale lavender, muted blue-violet, sage green, warm ivory, soft coral. One slightly warmer or cooler accent may push through, but the overall temperature is gentle and restrained. No high-chroma primaries, no neon.
- **Mood:** dreamy, nostalgic, tender, quiet, feminine without being saccharine, like a pressed-flower memory or a garden seen at dawn through sleepy eyes.

## Visual DNA

Use this as prompt material:

- **Bloom modes:** peonies, roses, ranunculus, anemones, sweet peas, cosmos, hydrangeas, wisteria, lavender sprigs, wildflowers, dried flowers, seed heads, grasses, or single oversized petals.
- **Veil modes:** condensation glass, tracing-paper overlay, early-morning mist, soft fog, milk-skin bloom, vellum diffusion, light-leak wash, or pale color wash.
- **Color systems:**
  - blush-cream: pale pink, ivory, warm white, soft green foliage
  - blue-violet-mist: dusty lavender, periwinkle, muted blue, pale sage
  - sepia-nostalgia: warm ivory, faded brown, dried-flower amber, muted gold
  - coral-sage: soft coral, dusty pink, sage green, warm cream
  - monochrome-warm: single warm hue family in varying lightness, near-tonal
- **Texture modes:** paper fiber grain, soft film grain, canvas tooth, watercolor-paper surface, subtle scan noise, dry-pigment speckle.
- **Light modes:** early-morning diffuse, overcast softbox, through-petal translucency, window-light haze, light-leak gentle bloom.

## Prompt Compiler

Write the final image prompt as four compact paragraphs:

1. **Canvas and surface:** aspect ratio, vertical portrait, full-frame botanical scene, paper-fiber grain or canvas tooth over the whole image, no border or mockup.
2. **Bloom and composition:** what flowers, how densely they fill the frame, foreground-to-background softening, single cluster or scattered, any stem or foliage detail.
3. **Veil and color:** translucent milky mist overlay, how it softens edges and reduces micro-contrast, chosen pastel palette system, warm or cool temperature, any inner glow.
4. **Light, mood, and constraints:** diffuse directionless light, dreamy nostalgic mood, painterly-photographic hybrid, hard avoids.

Make the prompt concrete and imageable. Specify exact flowers, palette, veil type, and density. Do not write style essays into the generation prompt.

## Variation Engine

Choose one option from each axis before writing the prompt.

### Bloom Layout

- **single-oversized-bloom:** one large flower or petal cluster filling 40%-60% of the frame, soft-edged, luminous
- **dense-cluster:** many blooms packed together filling 60%-80%, overlapping petals, shallow depth
- **sparse-sprig:** a few stems or sprigs with lots of misty space around them, delicate and airy
- **scattered-petals:** loose petals drifting across the frame, no organized bouquet, dreamlike
- **border-bloom:** flowers framing the edges with a soft-focus void or haze in the center
- **dried-pressed:** flattened dried flowers, herbarium sheet feel, muted earth tones

### Veil Mode

- **condensation:** blooms seen through glass condensation, water-droplet softness, cool-moist
- **tracing-paper:** translucent paper overlay, blooms visible but veiled, warm ivory tint
- **early-mist:** garden at dawn, natural fog softening all edges, pale and luminous
- **milk-skin:** thin milky wash over the entire image, reducing contrast and saturating gently
- **vellum-diffusion:** frosted vellum texture, blooms ghosted and soft, very low micro-contrast
- **light-leak:** gentle warm light-leak wash from one corner, nostalgic film feel

### Color System

- **blush-cream:** pale pink, ivory, warm white, soft green
- **blue-violet-mist:** dusty lavender, periwinkle, muted blue, pale sage
- **sepia-nostalgia:** warm ivory, faded brown, dried-flower amber, muted gold
- **coral-sage:** soft coral, dusty pink, sage green, warm cream
- **monochrome-warm:** single warm hue family, tonal variation only

### Texture Mode

- **paper-fiber:** visible paper-pulp grain across the surface
- **film-grain:** soft photographic grain, analog feel
- **canvas-tooth:** subtle woven-canvas texture
- **watercolor-paper:** cold-pressed watercolor surface texture
- **scan-noise:** gentle scanner noise and dust specks

### Light Mode

- **early-morning:** diffuse dawn light, cool-warm balance
- **overcast-softbox:** even gray-day softness, no shadows
- **through-petal:** light glowing through translucent petals from behind
- **window-haze:** soft window light diffused through curtain or mist
- **light-leak-bloom:** warm analog light leak, gentle and irregular

### Mood Mode

- **dreamy:** soft, floating, half-awake
- **nostalgic:** memory-like, faded, tender
- **quiet:** still, meditative, unhurried
- **tender:** gentle, intimate, warm
- **melancholic:** slightly sad beauty, bittersweet softness
- **ethereal:** otherworldly, luminous, barely-there

## Generation Workflow

1. Parse the user's content.
   - Identify the flower or botanical subject, season, mood, color preference, and any reference image role.
   - If no flower is specified, choose one that fits the mood. If no mood is given, default to dreamy.
   - If a reference image is provided, use it to determine palette, bloom type, and veil density rather than copying its literal content.

2. Select a variation recipe.
   - Pick bloom layout, veil mode, color system, texture mode, light mode, and mood mode from the Variation Engine.
   - Ensure the choices form a coherent atmosphere. For example, condensation veil pairs well with early-morning light and blue-violet-mist color; tracing-paper veil pairs well with sepia-nostalgia and film-grain texture.
   - Do not default to the same recipe every time. Vary across runs.

3. Write the final image prompt.
   - Use the Prompt Compiler to compile the user's content into the four-paragraph prompt shape.
   - Specify exact flowers, palette hues, veil type, bloom density, and texture. Keep it concrete and decisive.
   - Specify in-image text only if the user provides it. Otherwise, the image should be textless or carry only faint illegible marks.

4. Generate the image.
   - Use the `imagegen` skill by default.
   - If the user asks for local CLI, pptoken, or a specific model/API, follow that path.
   - Do not stop after prompt-only unless the user explicitly asks for prompt-only.
   - Inspect the result at thumbnail scale. If the veil is absent and the image reads as a crisp botanical photo, tighten the veil wording and regenerate once. If the image is too dark or too saturated, strengthen the muted-pastel and soft-focus language and regenerate once.

5. Return the image and prompt.

## Hard Avoids

Always avoid:

- crisp sharp-edged botanical photography or studio product shots
- high-chroma primary colors, neon, or oversaturated blooms
- hard directional lighting, spotlight, rim light, or harsh shadows
- full-bleed storybook scene with architecture, paths, or tiny figures (use `luminous-garden-storybook-zine` instead)
- sparse single-anchor paper poster with 70%-90% negative space (use `gc-minimal-zine-poster-v0-1` instead)
- calendar grid, planner layout, or social-poster border (use `monthly-memory-planner-zine` instead)
- 3D rendering, CGI, plastic texture, or glossy surface
- cartoon, anime, kawaii, or flat illustration
- text blocks, headlines, commercial poster hierarchy, or logo
- dark moody gothic, neon-cyberpunk, or high-contrast drama
- too many competing colors or a busy scrapbook density
- horizon lines, landscapes, or wide cinematic aspect ratios unless explicitly requested

## Output Format

```markdown
**生成图**

![Dream Bloom Veil Zine image](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Recipe: [bloom layout / veil mode / color system / texture / light / mood]
- [one short note about the content interpretation]
```

If generated images render directly without a file path, show the image normally and still include the final prompt.

## Quality Gate

Before finalizing, check:

- Did the prompt use the four-paragraph Prompt Compiler?
- Did the run choose a variation recipe across bloom layout, veil, color, texture, light, and mood?
- Is the structure materially different from recent visible outputs?
- Is the image a vertical portrait with full-frame botanical scene?
- Do flowers fill 50%-80% of the canvas?
- Is a translucent veil visible, softening edges and reducing micro-contrast?
- Does the whole surface carry paper-fiber, film-grain, or canvas-tooth texture?
- Is the palette muted pastel with no high-chroma primaries?
- Is the light diffuse and directionless with no hard shadows?
- Does the mood read as dreamy, nostalgic, or tender?
- Did the prompt avoid crisp studio photography, storybook scenes, sparse paper posters, planner grids, 3D, cartoon, neon, and commercial hierarchy?
- Did you actually generate the image?

## Example Requests

- "用 dream-bloom-veil-zine 做一张关于粉色牡丹的图"
- "用 dream-bloom-veil-zine 做一张晨雾中的薰衣草田"
- "用这张参考图做一张同风格的干花 zine"
- "用 dream-bloom-veil-zine 做一张复古暖色调的玫瑰"
- "用 dream-bloom-veil-zine 做一张蓝紫色迷雾花丛"
