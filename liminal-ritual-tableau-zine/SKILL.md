---
name: 阈限仪式
description: Generate prompts and finished raster images for pale surreal ritual tableau posters, liminal fashion photographs, symbolic triptychs, mirror-and-water scenes, and restrained occult-editorial zines. Use when the user provides a theme, phrase, poem, person, landscape, or reference image and wants white garments, portals, smoke, fire, reflections, eclipse forms, specimen grids, or uncanny ceremonial imagery arranged with sparse Minimal Zine discipline.
---

# Liminal Ritual Tableau Zine

Turn the user's content into both:

1. a final image-generation prompt, and
2. a finished raster poster generated from that prompt.

This style inherits Minimal Zine's attention geometry, negative space, single-anchor discipline, restrained color, and quiet editorial temperature. It replaces the tiny paper specimen with a photographed ritual tableau: a solitary figure, threshold object, material transformation, or short symbolic sequence.

## Mode Policy

Use **Tableau Mode** by default. Use **Sequence Mode** only when the user's idea contains a transformation, before/after relation, journey, or explicit multi-panel request.

- **Tableau Mode:** one dominant scene, one figure or symbolic event, 45%-70% quiet space.
- **Sequence Mode:** two or three related scenes, or a controlled specimen grid; every panel shares one visual law.

Do not turn every request into a triptych. Do not confuse this style with gothic fantasy, costume portraiture, horror, or generic AI surrealism.

## Prompt Compiler

Compile only details that can become visible pixels. Every final prompt must answer these questions in this order.

1. **Format and field**
   - Default to a vertical 2:3 editorial poster, full-frame image, no device mockup.
   - Establish a pale gray, chalk white, fog, black earth, dark water, or oxidized industrial field.

2. **Attention geometry**
   - Place one dominant symbolic event within a simple frame.
   - Keep 45%-70% of the composition visually quiet.
   - Choose one layout family from the Variation Engine and state the figure scale, horizon, and anchor position.

3. **Human or material anchor**
   - Translate the theme into one solitary figure, empty garment, suspended object, framed apparition, reflection, or elemental transformation.
   - Favor distressed white fabric, gauze, veils, wet cloth, plaster, silvered skin, ash, glass, water, smoke, flame, branches, or birds.
   - Poses are frontal, rear-facing, kneeling, suspended, partially submerged, or still in profile. Expression is restrained.

4. **Threshold and transformation**
   - Add one threshold device: rectangular frame, door, arch, mirror, waterline, glass pane, aperture, eclipse, or narrow passage.
   - Add one material action: cloth becomes cloud, dress becomes wings, smoke erases a body, fire occupies an empty frame, reflection disagrees with reality, or glass fractures the scene.
   - The transformation must remain physically legible and photographically plausible.

5. **Color and light**
   - Choose one palette mode from the Variation Engine.
   - Keep bone, white, gray, black, and metallic neutrals dominant.
   - Use at most one chromatic event: rust red, ember orange, cold silver-blue, or muted eclipse amber. It should occupy roughly 2%-12% of the image unless the user asks for stronger color.
   - Use overcast daylight, diffuse studio light, flat winter light, wet reflections, or fire as a localized practical source.

6. **Editorial layer**
   - Typography is optional and sparse: one short title plus tiny archival coordinates, sequence numbers, or a date.
   - Keep type away from faces and the central transformation. Prefer narrow serif, restrained grotesk, or typewriter text.
   - Never imitate visible signatures, watermarks, logos, or source-image text.

7. **Surface and capture**
   - Photographic realism with medium-format restraint, matte print, fine film grain, slight halation, soft paper tooth, and controlled contrast.
   - Preserve fabric weave, water surface, smoke volume, skin texture, and handmade prop imperfections.

8. **Hard avoids**
   - Include the relevant Negative Constraints explicitly.

Write the final prompt as five compact paragraphs: format/geometry; subject/pose; threshold/transformation; palette/light/texture; typography and avoid-list.

## Variation Engine

Select one value from each axis. Rotate layouts and symbols across a batch.

### Layout Family

- `single-portal`: solitary figure centered within or beside a freestanding rectangle
- `ritual-triptych`: three equal or asymmetrical panels showing one transformation
- `reflection-split`: horizon or waterline divides body and altered reflection
- `specimen-grid`: 4-9 controlled studies of one material, gesture, or face
- `stacked-altar`: vertically suspended objects and figures aligned like an installation
- `eclipse-landscape`: small figure against a severe horizon and one celestial disc
- `framed-apparition`: empty frame contains smoke, flame, fabric, or an impossible landscape

### Symbol Family

- frame, door, arch, or narrow opening
- white garment, veil, bandage, or wing-like textile
- smoke, fire, water, ash, or rain
- mirror, reflection, wet glass, or broken pane
- bird, bare branch, crown, antler, or thorn
- eye, eclipse, halo, or dark sun
- suspended island, stone, vessel, or anatomical relic
- sparse circle, line, cross-axis, or measurement geometry

### Palette Mode

- `bone-fog`: chalk white, warm bone, pearl gray, charcoal
- `ash-fire`: cold ash, soot black, distressed white, one ember-orange event
- `silver-smoke`: oxidized silver, white haze, graphite, blue-gray shadow
- `black-water-red`: black water, paper white, neutral skin, restrained rust red
- `eclipse-amber`: pale concrete, smoke gray, black disc, muted amber rim

### Capture Mode

- overcast medium-format location photograph
- controlled gallery installation photograph
- wet-glass portrait with doubled reflection
- archival contact-sheet or specimen study
- cinematic still with flat, quiet daylight

Read [references/style-grammar.md](references/style-grammar.md) when matching a reference image or diagnosing why a result feels generic. Read [references/prompt-recipes.md](references/prompt-recipes.md) for prompt construction and regeneration recipes. Read [references/tableau-symbol-system.md](references/tableau-symbol-system.md) when the concept is abstract and needs a coherent symbol-to-theme mapping.

## Workflow

1. Parse the request.
   - Identify theme, emotional verb, setting, subject, exact text, aspect ratio, and whether references control composition, palette, material, or mood.
   - Treat reference images as visual evidence, not as images to copy.

2. State the visual thesis internally.
   - Reduce the concept to: `[subject] crosses/confronts/becomes [element] at [threshold]`.
   - Example: `a veiled figure remembers the sea through a frame filled with smoke`.

3. Choose a recipe.
   - Pick mode, layout, symbol, palette, and capture mode.
   - Keep one primary metaphor and no more than two supporting symbols.

4. Compile the prompt.
   - Use the eight prompt fields and five-paragraph shape.
   - Specify camera distance, figure scale, physical materials, negative-space share, and exact accent color.
   - Describe transformations as practical photographed effects whenever possible.

5. Generate the image.
   - Use the built-in image generation capability by default.
   - Do not stop at prompt-only unless the user explicitly requests only a prompt.
   - If the built-in route is unavailable, run `scripts/server_image_gen.py` with the final prompt.

6. Inspect and regenerate once when necessary.
   - Regenerate if the result reads as fantasy character art, fashion advertising, horror, ornate religion, or unrelated collage.
   - Tighten figure count, threshold geometry, quiet-space share, and practical material language before adding detail.

7. Return the image, prompt, and selected recipe.

## Reference Image Policy

- Extract structure, palette, lighting, material behavior, camera distance, and symbolic relations.
- Preserve user-provided identity only when explicitly requested and supported by the image-editing route.
- Do not identify people or infer sensitive traits.
- Do not reproduce a source composition beat-for-beat, visible signature, watermark, logo, exact costume, or unique sacred emblem.
- If several references conflict, choose the repeated grammar and discard one-off details.

## Negative Constraints

Always avoid:

- generic fantasy queen, warrior glamour, or gothic cosplay
- gore, body horror, demonic spectacle, or shock imagery
- commercial fashion campaign poses and beauty-retouch gloss
- cathedral ornament, baroque overload, or random religious icon mixing
- dense scrapbook clutter, stickers, decorative borders, and unrelated props
- purple cinematic grading, teal-orange blockbuster color, neon, or glossy CGI
- weightless fabric, impossible anatomy, malformed hands, duplicate limbs, or extra figures
- copied signatures, watermarks, logos, and long pseudo-readable text
- weak scenes where symbols merely float without physical contact or scale logic

## Fallback Script

The fallback script reads the OpenAI-compatible provider from Codex configuration or environment variables. It never stores credentials in the Skill.

```bash
python3 scripts/server_image_gen.py \
  --prompt-file /absolute/path/to/prompt.txt \
  --out output/imagegen/liminal-ritual-tableau-zine-output.png
```

Use `--dry-run` to inspect the request without sending it. Use `--wire-api responses` only when the configured endpoint supports the Responses image-generation tool; the default is the Images API.

## Output Format

````markdown
**生成图**

![Liminal Ritual Tableau Zine poster](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**构图配方**

- Mode: [Tableau or Sequence]
- Recipe: [layout / symbol / palette / capture]
- Interpretation: [one short sentence]
````

## Quality Gate

Before finalizing, check:

- Is there one clear visual thesis and one dominant symbolic event?
- Is 45%-70% of the field quiet enough to preserve tension?
- Is the figure count intentionally one unless the sequence requires repetition?
- Is there a visible threshold and a physically coherent transformation?
- Do textiles, smoke, water, fire, glass, and reflections behave materially?
- Is the palette neutral with no more than one chromatic event?
- Does typography remain sparse and subordinate?
- Does the image avoid generic fantasy, fashion-ad gloss, horror, ornate religion, and dense collage?
- Does the result differ materially from recent outputs in layout or symbol family?
- Was the raster image actually generated?

## Example Requests

- `用 $liminal-ritual-tableau-zine 生成“记忆穿过一扇空门”的海报`
- `用这张参考图的雾白色调和镜面结构，做一张关于重生的三联画`
- `生成一个白衣人物站在黑水边，倒影是一团火的仪式摄影 zine`
