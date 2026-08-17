---
name: 流光花园绘本
description: "【流光花园绘本 / luminous-garden-storybook-zine】 Generate prompts and finished raster images for luminous painterly storybook scenes inspired by glowing gardens, rain-washed city parks, snowy old towns, violet-blue forests, floral courtyards, tiny figures, animals, lantern windows, and dense gouache-like brush texture. Use when the user gives a place, mood, season, story fragment, image reference, or subject and wants a full-bleed magical editorial illustration rather than a sparse paper zine poster."
---

# Luminous Garden Storybook Zine

Turn the user's theme, image, place, season, or story fragment into:

1. a final image-generation prompt, and
2. a generated raster image made from that prompt.

Use the `imagegen` skill for generation or editing. Prefer the local configured CLI/API path when the user explicitly asks for local image generation, image-gen CLI, model/API controls, or pptoken.

## Style Thesis

Create full-bleed painterly storybook worlds with dense floral or architectural detail, luminous atmosphere, and a quiet narrative. This skill is the dense, immersive counterpart to `gc-minimal-zine-poster-v0-1`: keep its prompt-compiler discipline, but replace sparse paper-negative-space logic with all-over scene composition, layered depth, and glowing brushwork.

## Reference-Derived Structure

Use these image-structure rules as the core style:

- **Frame:** wide cinematic landscape by default; use vertical only when requested. No border, no paper mockup, no empty poster field.
- **Depth:** build foreground silhouettes or flowers, midground paths/water/gardens/roofs, and background trees/towers/city lights. Use winding paths, stairways, bridges, shorelines, courtyards, or rooflines to pull the eye through the image.
- **Density:** fill 80%-100% of the canvas with scene material. Let flowers, rain lines, snow, windows, foliage, and tiny lights form repeating texture fields.
- **Light:** use small warm lights against cool blue-violet surroundings: lanterns, windows, fountains, reflected water, rain glints, sunset edges, or glowing snow streets.
- **Scale:** include tiny people, cats, deer, birds, tents, umbrellas, benches, or garden ornaments only when they support the scene. They should be small narrative accents, not central character art.
- **Brushwork:** visible gouache/acrylic/digital-paint strokes, rough canvas tooth, dry-brush vertical streaks, broken color dabs, scumbled foliage, and simplified shape masses.

## Visual DNA

Use this as prompt material:

- **Color base:** deep ultramarine, periwinkle, blue-violet, teal green, dark bottle green, and shadow navy.
- **Accent light:** peach, coral, warm window orange, candle yellow, pale pink flowers, lavender highlights.
- **Garden mode:** clipped hedges, flower beds, fountains, stone paths, white or pale garden ornaments, distant classical or gothic architecture, dappled summer light.
- **Rain city mode:** blue-violet rainfall, wet parks, glowing windows, red/coral umbrellas, reflected paths and canals, dark tree silhouettes.
- **Snow town mode:** old roofs, chimneys, snowy lanes, warm lantern shops, dense rooftops, distant towers, falling snow.
- **Forest lake mode:** dark trees, mist, glowing pond, lantern-like reflections, pale blossoms, shrine/garden stones, soft magical haze.
- **Dream field mode:** backlit grass and flowers, luminous rain or star-like particles, translucent animal silhouettes, soft bokeh-like sparkle, but keep painterly not photographic.

## Prompt Compiler

Write the final image prompt as four compact paragraphs:

1. **Scene frame and geography:** aspect ratio, viewpoint, environment, foreground/midground/background, main path or compositional route.
2. **Narrative anchors:** tiny figures/animals/objects, architecture or garden elements, season/weather, what the viewer discovers while scanning.
3. **Color and light:** cool base palette, warm accent lights, reflections or glow, dominant color proportions, time of day.
4. **Medium and constraints:** painterly gouache/acrylic texture, visible brushwork, canvas tooth, stylization level, hard avoids.

Make the prompt concrete and imageable. Do not write style essays into the final generation prompt.

## Variation Engine

Choose one option from each axis before writing the prompt.

### Layout

- garden-courtyard: hedges and flower beds organized by paths, fountains, gates, or ruins
- rain-park: urban garden or park in rainfall with umbrellas and reflected lights
- snow-village: dense old town rooftops, lantern streets, falling snow
- forest-lake: dark wooded water garden with glowing reflections and pale ornaments
- hillside-camp: tents, sleeping figures, animals, shoreline or mountain slope
- balcony-city: layered rooftops, windows, terraces, distant towers
- luminous-field: low flowers and grasses against sparkling rain or night air

### Camera

- high oblique view over layered scenery
- eye-level path entering the garden
- slightly elevated panorama
- low foreground grass or flowers framing the scene
- distant overlook with dark silhouette frame

### Atmosphere

- summer evening garden
- rainy blue hour
- snowy festival night
- misty forest dawn
- moonlit lake
- after-rain city glow
- dreamlike floral twilight

### Narrative Accent

- red umbrellas
- cats hidden in foliage
- deer silhouettes
- sleeping campers
- tiny pedestrians with lanterns
- birds or black silhouettes
- empty benches and glowing windows
- fountain, shrine lantern, or garden tower

## Generation Workflow

1. Parse the user's subject into a place, season/weather, time of day, and one quiet narrative accent.
2. Choose a recipe from the Variation Engine. If the user provides reference images, preserve their structure, palette, and subject roles before inventing new details.
3. Compile the four-paragraph prompt. Include exact text only if the user requested in-image text; otherwise avoid typography.
4. Generate the raster image. Use `imagegen` built-in mode unless the user explicitly requests local CLI/API/pptoken.
5. Inspect the output for scene density, luminous palette, depth path, small narrative details, and visible painterly texture. Regenerate once if the image becomes generic fantasy art, photoreal, anime, sparse poster, or flat decorative pattern.
6. Save final images under `output/imagegen/luminous-garden-storybook-zine/` for workspace-bound outputs.

## Hard Avoids

Avoid sparse paper poster layout, large blank negative space, zine microtypography, clean vector art, flat UI illustration, photorealistic stock image, anime character poster, cute mascot focus, 3D render, neon cyberpunk, generic fantasy castle, over-sharp concept art, heavy black outlines, commercial ad copy, logos, watermarks, and long readable text.

## Output Format

```markdown
**生成图**

![Luminous garden storybook image](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Recipe: [layout / camera / atmosphere / narrative accent]
- [one short note on how the user's subject was translated]
```

## Quality Gate

Before finalizing, check:

- Does it read as a full-bleed painted storybook scene, not a sparse paper zine poster?
- Is there a clear foreground, midground, and background?
- Does a path, waterway, stair, roofline, or light trail guide the eye?
- Are cool blue-violet/green masses balanced with warm coral/orange/yellow lights?
- Are flowers, rain, snow, windows, foliage, or sparkles creating dense texture fields?
- Are small figures/animals/objects tiny enough to support scale rather than dominate?
- Is the brushwork visible and painterly, with rough texture and broken color?
- Did the prompt avoid photorealism, anime poster tropes, 3D render, neon cyberpunk, blank-paper minimalism, logos, and long text?
