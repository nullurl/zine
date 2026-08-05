---
name: 余烬剪影
description: Generate prompts and finished raster images for dark negative-space memory posters with one irregular warm aperture containing a limited-color sunset, moon, mountain, water, home, road, or human silhouette scene. Use when the user provides a phrase, relationship, place, memory, reference image, or emotional theme and wants a charcoal-black screenprint zine with burned-paper, cave-mouth, canopy, or torn-ink window geometry and tiny editorial typography.
---

# Ember Aperture Silhouette Zine

Turn the user's content into both a final image-generation prompt and a finished raster image. The signature artifact is a tall matte-black paper poster in which 75%-88% of the page remains dark. One irregular opening reveals a warm, limited-color memory scene rendered like screenprint, woodcut, ink drawing, or aged animation background. Human figures appear as small silhouettes inside the opening.

This Skill reverses the light/dark relationship of `gc-minimal-zine-poster-v0-1` while retaining its attention geometry, single visual anchor, restrained color, sparse typography, print defects, and quiet editorial temperature. The original tiny high-chroma paper anchor becomes one substantial warm aperture surrounded by a much larger black field.

## Mode Policy

Use **Aperture Mode** by default. Use **Ember Sequence Mode** only for an explicit transformation or diptych/triptych request.

- **Aperture Mode:** one dark page, one opening, one memory scene, one relationship gesture.
- **Ember Sequence Mode:** two or three small openings connected by the same silhouette, horizon, or time progression.

Never create multiple decorative portals by default. The emotional force comes from one protected window inside darkness.

## Prompt Compiler

Write the final prompt as five compact paragraphs in this order.

### 1. Canvas and black field

State:

- vertical 2:3, 3:5, or 9:16 matte paper poster
- full-frame charcoal-black, blue-black, or soot-black ink field
- 75%-88% dark negative space with subtle paper fibers and uneven ink density
- one central or lower-middle opening occupying approximately 12%-28% of the page
- flat scanned print, no frame, no mockup, no glossy depth

The black field must read as printed matter or a physical foreground mass, not as an empty digital gradient.

### 2. Aperture geometry

Choose one aperture family and describe its silhouette precisely:

- overhanging tree-canopy opening
- cave mouth or grotto entrance
- burned-paper hole with ember edges
- eroded ink mask or peeled poster window
- flame-shaped vertical void
- doorway hidden in dense branches
- torn photographic emulsion

The opening should be vertically tapered or arched, with a wider lower scene and a narrower upper gap. Edges contain branches, leaves, soot, torn fibers, or ink erosion. Add only a few detached pinholes or flecks; do not turn the page into random grunge.

### 3. Interior memory scene

Translate the user's theme into one simple layered scene inside the aperture:

- sky or celestial sign: crescent moon, dim sun, star, or cloud band
- distant layer: mountain, island, roof line, tree line, or horizon
- middle layer: sea, lake, field, road, courtyard, or window light
- foreground relation: one to three small silhouettes, a lone figure, two hands, a child, an animal, a bicycle, a bench, or an empty path

Use simplified contour lines, horizontal water marks, flat shapes, and readable scale. Human silhouettes remain anonymous and emotionally legible through spacing or gesture. Do not infer or claim identities from references.

### 4. Minimal Zine color and print logic

Use one warm anchor family inside the aperture:

- ember orange + peach + muted tomato
- amber + rust + dusty rose
- pale moon cream + burnt orange + mauve-gray
- lemon dusk + vermilion + charcoal violet
- user-selected single high-chroma hue with two quieter tonal steps

The aperture is the one high-chroma anchor and may occupy 12%-28% of the page because it replaces the original Minimal Zine cluster. Keep the surrounding ink and figures nearly black. Use 3-5 flat printed inks, visible halftone, woodcut or screenprint contour, slight misregistration, faded edge, paper grain, and low-to-medium contrast outside the aperture. No global orange wash.

### 5. Typography and avoid-list

Typography is optional and tiny: one short title of 2-8 characters or words, widely spaced near the bottom or side margin, plus an optional date or sequence number. Use narrow serif, monospaced, typewriter, or small grotesk type. Never copy visible source text, signatures, artist names, or watermarks. End with the relevant negative constraints.

## Aperture Families

- `canopy-window`: dense leaves and branches define a vertical arch
- `cave-mouth`: rock or dark interior opens toward a distant landscape
- `burned-paper`: irregular charred fibers expose the scene below
- `eroded-ink`: black screenprint flakes away into a memory image
- `flame-void`: opening narrows upward like a candle flame
- `hidden-door`: geometric doorway partly swallowed by organic darkness
- `emulsion-tear`: photographic surface peels or dissolves into a warm scene

## Memory Scene Families

- `shoreline-bond`: figures holding hands before water and a distant island
- `lone-return`: one figure facing a road, house light, or mountain pass
- `home-at-dusk`: roof line, courtyard, window light, and one waiting figure
- `moon-over-water`: crescent, horizontal water marks, distant ridge, quiet silhouettes
- `field-passage`: layered fields, narrow road, bicycle, animal, or walking pair
- `empty-afterimage`: no people, only bench, clothing, footprints, or lit doorway
- `object-memory`: one meaningful object enlarged inside the aperture with a tiny horizon

## Attention Geometry

The opening must remain the only dominant anchor.

- place it on the vertical center axis or slightly below center
- keep at least 25% uninterrupted darkness above it
- preserve wide dark margins on both sides
- avoid edge-hugging unless the user explicitly asks for a cropped opening
- put human silhouettes near the lower third of the aperture, not the entire poster
- keep the celestial sign small and separated from the figures

At thumbnail size, the viewer should first see a black field, then one warm opening, then the interior relationship.

## Minimal Zine Prompt Bridge

### Preserve from the source Skill

- vertical paper poster and flat orthographic scan
- one clear visual anchor surrounded by large negative space
- one coherent high-chroma color strategy
- sparse serif, typewriter, monospaced, or small grotesk typography
- risograph grain, xerox softness, halftone degradation, ink bleed, and misregistration
- quiet, poetic, distant, nostalgic, archival mood

### Invert for this Skill

- aged light paper becomes matte charcoal-black printed paper
- tiny colored specimen becomes one warm negative-space aperture
- visible paper occupies the dark field through grain and ink variation
- the anchor is a scene seen through absence, not a full-bleed illustration

### Do not import

- tiny blue dots, floating letters, paper snippets, or arbitrary color blocks when they weaken the aperture
- exact source dates, words, signatures, objects, or sample composition
- `clean UI white`, commercial headline hierarchy, glossy mockup, or 3D lighting

## Workflow

1. Parse the request.
   - Extract theme, relationship, place, time, exact text, and reference-image role.
   - Reduce the idea to `[memory] seen through [aperture material]`.

2. Select the recipe.
   - Choose mode, aperture family, interior scene, relationship gesture, palette, and print process.
   - Use one opening and one scene by default.

3. Compile the prompt.
   - State black-field percentage, opening size/location, exact edge material, interior layers, silhouette action, palette, typography, and avoids.
   - Describe visible physical processes rather than vague words such as magical or dreamy.

4. Generate the image.
   - Use the built-in image generation capability by default.
   - If unavailable, run `scripts/server_image_gen.py` with the final prompt.

5. Inspect and regenerate once when needed.
   - Regenerate if the aperture is too large, darkness reads as a gradient, the interior becomes photorealistic, silhouettes dominate, orange spreads across the page, or the result resembles a commercial movie poster.

6. Return the image, prompt, and selected recipe.

## Reference Image Policy

- Extract field ratio, aperture contour, edge material, layer order, limited palette, silhouette scale, print linework, and typography position.
- Treat reference text and signatures as non-transferable. Do not reproduce them.
- Preserve a user's own relationship or subject only when explicitly requested; otherwise use anonymous silhouettes.
- Do not copy the exact source scenery, family pose, title, or aperture outline pixel-for-pixel.

## Negative Constraints

Always avoid:

- full-bleed sunset or landscape without a surrounding black field
- clean geometric oval, heart, keyhole, or stock vignette unless explicitly requested
- random grunge texture, excessive pinholes, distressed overlays, and fake burnt edges everywhere
- horror cave, threatening figures, gore, demonic imagery, occult symbols, or jump-scare darkness
- generic movie poster, streaming thumbnail, dramatic title hierarchy, logo lockup, or credit block
- photorealistic people, detailed faces, glamour silhouettes, superhero poses, and incorrect anatomy
- glossy digital painting, 3D render, neon, purple grading, teal-orange blockbuster lighting, and lens flare
- dense scrapbook, decorative stickers, multiple unrelated scenes, or too many accent colors
- copied signatures, watermarks, artist names, source captions, and long pseudo-readable text

## Fallback Script

The fallback reads the OpenAI-compatible provider from Codex configuration or environment variables and never stores credentials in the Skill.

```bash
python3 scripts/server_image_gen.py \
  --prompt-file /absolute/path/to/prompt.txt \
  --out output/imagegen/ember-aperture-silhouette-zine-output.png
```

Use `--dry-run` to inspect the request without sending it. The default is the Images API; use `--wire-api responses` only for a compatible Responses image-generation endpoint.

## Output Format

````markdown
**生成图**

![Ember Aperture Silhouette Zine](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**构图配方**

- Mode: [Aperture or Ember Sequence]
- Recipe: [aperture / scene / palette / print process]
- Interpretation: [one short sentence]
````

## Quality Gate

Before finalizing, check:

- Does the poster remain 75%-88% charcoal-black field?
- Is there exactly one dominant irregular aperture by default?
- Does the aperture occupy approximately 12%-28% of the page?
- Are the edge material and opening silhouette physically legible?
- Is the interior scene layered simply enough to read at thumbnail size?
- Are human figures small, anonymous, and relational rather than heroic?
- Is warm color isolated inside the aperture with no global orange wash?
- Does the surface read as screenprint, woodcut, ink, or aged print rather than glossy digital art?
- Is typography tiny, sparse, and free of copied source text?
- Did the output avoid horror, generic cinema advertising, CGI, random grunge, and full-bleed sunset?
- Was the raster image actually generated?

## Example Requests

- `用 $ember-aperture-silhouette-zine 生成“我们走回有灯的地方”`
- `参考这张图的黑色树洞和暖色窗口，做一张关于故乡的海报`
- `生成一张月牙、海面和三个人物剪影组成的暖色记忆孔洞 zine`
