---
name: 场景日记双联
description: "【场景日记双联 / scene-journal-diptych-zine】 Generate prompts and matching raster images for vertical scene-and-journal memory diptychs. Build the upper panel as either a documentary place/event photograph or a vivid life-force portrait scene with a real person doing something, then extract recognizable objects, gestures, contours, textures, color, light, and spatial relations into a sparse Minimal Zine Poster v0.1-inspired collage inside a flash-lit open journal. Use for travel or portrait photos, city and museum memories, people-in-place stories, visual diaries, scene-derived scrapbooks, place/event briefs, or reference collages that need visible provenance between the upper scene and lower journal."
---

# Scene Journal Diptych Zine

Turn the user's source into a final image-generation prompt and a matching raster image. Preserve the memory loop: the upper photograph shows the lived scene; the lower journal physically reconstructs selected elements extracted from that same scene.

## Required References

Read both files before compiling a prompt:

- [references/visual-grammar.md](references/visual-grammar.md) for diptych geometry, hands, journal, light, and scene recipes.
- [references/element-collage.md](references/element-collage.md) for scene-element selection, Minimal Zine Poster v0.1 transformations, page layout, and provenance checks.
- [references/life-force-scene-mode.md](references/life-force-scene-mode.md) when the upper scene contains a main person or the user asks for portrait, traveler, family, street character, or people-centered imagery.

## Core Structure

Keep these six layers in order:

1. Upper documentary scene.
2. Scene element manifest.
3. Minimal-zine material transformation.
4. Lower journal collage.
5. Diptych prompt compilation and generation.
6. Element-provenance validation.

Do not skip the element manifest. Generic travel ephemera is not a substitute for extracting visible scene content.

## Workflow

1. Parse the source.
   - Identify one place or event, its documentary viewpoint, weather or time, emotional temperature, and any exact text.
   - Preserve supplied-photo architecture, objects, people, season, palette, and camera mood. If only text is supplied, define one plausible upper scene first.
   - If a main person carries the scene, activate Life-Force Scene Mode. Build its portrait scene card before extracting elements.

2. Build the upper scene.
   - For a place-led scene, use observational documentary photography.
   - For a person-led scene, preserve supplied identity, face, age, body, expression, clothing, action, and event. For text-only generation, create an original non-celebrity person appropriate to the requested place and culture.
   - Make the person perform one concrete action. Choose an intimate or active camera distance, one foreground layer, real directional light, one clean color relationship, and at most one main optical effect plus one subtle edge effect.
   - Keep faces readable, skin softly matte, hair separated and mobile, and effects away from primary facial features.

3. Extract three to five elements from the upper scene.
   - Always select one primary recognizable object or silhouette.
   - Select at least two more from: cropped photo fragment, material texture, structural line or route, dominant local color, repeated shape, sign fragment, date, weather, or spatial relation.
   - Record each item as `upper source -> preserved identity cue -> lower treatment -> page placement`.
   - Prefer distinctive evidence from this scene over generic destination symbols.
   - In person-led scenes, prefer the action prop, gesture trajectory, clothing hue, moving hair or fabric contour, foreground object, light pattern, and environment relation. Do not turn the face into a decorative silhouette unless the user explicitly requests it.

4. Transform the extracted elements with the Minimal Zine Poster v0.1 subcompiler.
   - Convert the primary element into one paper anchor: torn photo crop, flat saturated silhouette, old printed illustration, object specimen, rough color block, or xerox fragment.
   - Convert secondary elements into halftone crops, line tracings, map contours, translucent overlays, microtype, registration marks, or smaller adjacent panels.
   - Preserve one identity cue per element: silhouette, proportion, hue, texture, direction, crop, or relation to another object.
   - Use one unmistakable high-chroma anchor derived from the upper scene. Keep all other paper fragments, photos, and type subdued.

5. Compose the lower journal.
   - Place the extracted-element collage inside one open cream-paper notebook centered on deep navy woven fabric.
   - Show a visible gutter and exactly two natural hands entering from the lower corners.
   - Keep 45%-70% of the open spread visually quiet. Build one primary cluster plus zero or one smaller counter-cluster; do not fill both pages evenly.
   - Use three to five scene-derived pieces. Add at most one contextual ticket, map, or receipt that is not directly visible above.
   - Make at least one element visibly repeat a shape or crop from the upper panel, and make another repeat its color, texture, route, or spatial relation.

6. Choose a variation recipe.
   - Keep the stacked diptych, navy fabric, open journal, and two hands fixed unless the user explicitly asks to vary them.
   - Vary the upper scene family, primary transformation, page layout, accent hue, typography mode, and print texture.
   - For a batch, change at least three axes between images and avoid repeating the same anchor treatment twice in a row.
   - In a people-centered batch, also vary age or role, action, framing, foreground, color relationship, and optical effect.

7. Compile the prompt in seven compact paragraphs.
   - Canvas and split geometry.
   - Upper place scene or life-force portrait scene card.
   - Upper photography treatment: distance, action, foreground, light, color, and controlled optical effect.
   - Explicit extraction manifest naming three to five visible elements.
   - Lower physical journal, hands, fabric, and flash.
   - Element-by-element paper transformations, page geometry, color anchor, type, and print defects.
   - Emotional tone and hard avoids.

8. Generate and inspect the image.
   - Use built-in image generation unless the user requests prompt-only. Follow the image-generation skill's fallback policy if the built-in tool is unavailable.
   - Prefer a tall 3:4 or 4:5 ratio.
   - Regenerate once if the panels blend, the journal or hands disappear, the lower artifacts become generic, or fewer than three extracted elements remain recognizable.

9. Return the image, final prompt, variation recipe, portrait scene card when active, and element provenance ledger.

## Prompt Rules

- Describe visible pixels and exact transformations. Write `the upper bridge arch reappears as an orange rough-edged line drawing on the left page`, not `bridge memories in the journal`.
- Keep the upper panel naturalistic and observational. Keep the lower panel top-down, tactile, flash-lit, and physically assembled.
- For a person-led upper panel, prioritize concrete action, camera distance, foreground depth, real light, and clean color before lens effects. Never use filters to replace an unconvincing human moment.
- Keep upper-person skin natural and softly matte. Reserve caustics, flare, dispersion, motion blur, or highlight bloom for hair, fabric, water, glass, foreground, and frame edges; keep eyes, nose, mouth, and identity cues clean.
- Apply Minimal Zine Poster v0.1 inside the notebook only: sparse cluster, large paper negative space, one strong chromatic anchor, tiny type, xerox or risograph defects.
- Use one dominant accent taken from a visible upper-scene color. Do not invent an unrelated fashion palette.
- Keep exact text short. Prefer date, place, weather, coordinates, or one brief phrase.
- Preserve paper fibers, torn or softened edges, tape, folds, scuffs, halftone, ink bleed, and slight misregistration.

## Hard Avoids

Avoid generic travel stickers, unrelated tickets or maps, lower-page elements with no visible upper source, simple miniature duplication of the entire upper photo as the only bridge, static centered portrait posing, empty eye contact, generic AI faces, identity drift, plastic or oily skin, effects covering facial features, commercial fashion posing, one blended scene, decorative panel border, gap between panels, floating-book mockup, clean product flat lay, extra lower-panel hands, malformed fingers, hands covering the collage, closed notebook, laptop or phone, dense maximalist scrapbook clutter, kawaii graphics, multiple competing accent colors, commercial headline, logo, CTA, neon, 3D rendering, synthetic cinematic grading, heavy bokeh, and long perfect text.

## Output Format

````markdown
**生成图**

![Scene-journal diptych](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**元素来源表**

| 上层来源 | 保留特征 | 手账转译 | 页面位置 |
| --- | --- | --- | --- |
| [element] | [identity cue] | [paper treatment] | [placement] |

**人物场景卡**（人物模式启用时）

- Person / identity lock: [value]
- Concrete action: [value]
- Distance / angle / foreground: [values]
- Light / color relationship: [values]
- Main / subtle optical effect: [values]

**结构配方**

- Ratio and split: [value]
- Upper scene: [value]
- Primary / secondary transformations: [values]
- Page layout: [value]
- Accent / typography / texture: [values]
````

## Quality Gate

- Does the image read as two distinct edge-to-edge photographs with one horizontal seam?
- Does the upper panel establish a specific real place or event?
- When a main person is present, are identity, action, intimate or active framing, foreground depth, and real directional light all intentional?
- Is the face readable with softly matte skin and no flare, caustics, dispersion, or motion damage across primary features?
- Were three to five elements explicitly extracted before the prompt was written?
- Can at least three lower-page pieces be traced to visible upper-scene sources?
- Does each repeated element preserve a silhouette, proportion, hue, texture, direction, crop, or relation?
- Is the primary extracted element transformed rather than merely described?
- Does the lower spread use Minimal Zine Poster v0.1 grammar: 45%-70% quiet paper, one visual cluster, one high-chroma anchor, sparse microtype, and old-print defects?
- Are generic supporting ephemera limited to zero or one item?
- In person-led scenes, does the journal derive from action, prop, clothing color, moving contour, foreground, light, or environment rather than using the face as generic decoration?
- Are the deep navy fabric, open cream journal, visible gutter, direct flash, and exactly two plausible hands present?
- Are unrelated decoration, dense clutter, long text, branding, UI, mockup styling, and 3D absent?
- Was the image generated unless the user explicitly requested prompt-only?
