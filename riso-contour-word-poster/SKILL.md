---
name: riso-contour-word-poster
description: "Generate riso contour word-poster prompts and matching raster images. Use when the user gives a theme, abstract concept, mood, word list, article idea, place, object, or reference image and wants a bold blue-background poster with risograph/woodcut contour textures, fingerprint-like line fields, coral-pink and cream ink forms, sparse floating lowercase words, paper grain, and modern poetic editorial composition."
---

# Riso Contour Word Poster

Turn the user's content into both:

1. a final image-generation prompt, and
2. a generated raster image made from that prompt.

## Source Grammar

This style fuses Minimal Zine Poster v0.1's poetic restraint with a more graphic print system: a saturated blue poster field, one or more rectangular texture plates, and sparse floating words. The references look like risograph or woodcut prints scanned from rough paper.

Stable visual traits:

- **Frame:** vertical poster, usually 3:4 or 4:5, with a solid medium-blue background filling the page.
- **Texture plate:** one large centered rectangle, one edge-cropped rectangle, or several smaller print panels arranged in a grid/collage.
- **Image language:** dense contour lines, topographic waves, woodgrain, fingerprint rings, branching white negative channels, small boat silhouettes, leaf/tree-vein structures, wave fields, or abstract terrain.
- **Ink system:** medium blue base, cream/off-white paper gaps, coral-pink/red ink, and darker blue linework. The palette is limited and punchy.
- **Typography:** lowercase rounded sans words, thin white or cream, floating around and sometimes over the print plate. Words are conceptual labels, not a headline block.
- **Space:** strong blue negative space surrounds the plate; words are placed in open areas, left edge, top center, lower edge, or across image boundaries.
- **Texture:** risograph grain, offset misregistration, distressed paper speckles, uneven ink density, xerox noise, and rough printed edges.
- **Mood:** warm, abstract, optimistic, elemental, movement-oriented, reading-room calm, modernist zine/editorial, poetic map of feeling.

Do not copy the exact words from references unless the user asks. Treat `warm`, `freedom`, `advance`, `reading`, `unrestrained`, and `upward` as examples of word behavior.

## Mode Policy

Use **Standard Mode** for all generation. Compile only visible print-layout instructions into the final prompt. If the user supplies references, borrow structure, palette, and mark-making; do not reproduce the exact reference composition line-for-line.

## Standard Prompt Compiler

Write the final prompt as four compact paragraphs in this order:

1. **Canvas and Background**
   - State the vertical frame, saturated blue paper field, print plate count, and negative space.
   - Specify whether the print plate is centered, cropped, edge-aligned, or paneled.

2. **Contour Motif**
   - Convert the user's theme into one abstract contour subject: waves, terrain, woodgrain, fingerprint rings, tree/leaf veins, boat, valley, river, wind map, or branching path.
   - Define how cream negative channels, coral ink masses, and blue line fields interact.

3. **Words and Print Process**
   - Choose 4-7 short words from the theme and place them as floating lowercase labels.
   - Specify typography, scale, placement, and how words cross or avoid the texture plate.
   - Add risograph/woodcut grain, misregistration, paper speckles, and rough edges.

4. **Color, Mood, Avoids**
   - State palette ratios, emotional temperature, and hard negatives.

Keep prompts concrete. Avoid long style essays.

## First-Principles Fields

Every prompt must answer:

1. **What is the blue field?**
   - solid medium-blue matte paper background, not sky, water, UI, or gradient.

2. **What is the print plate?**
   - a rectangular risograph/woodcut texture area with visible rough paper grain and limited inks.

3. **What contour logic carries the theme?**
   - use repeated lines, rings, branching veins, waves, terrain bands, or flowing channels. Avoid a detailed literal scene.

4. **Where do the words sit?**
   - place floating words as part of the composition: top, left edge, lower margin, over a plate, partially crossing boundaries, or arranged around panels.

5. **How much is empty?**
   - 35%-70% of the full canvas may remain solid blue. The image can be more graphic than Minimal Zine Poster, but still needs breathing room.

6. **What is the ink system?**
   - blue, coral-pink/red, cream/off-white, and optionally darker blue. No broad rainbow palette.

7. **What material process defines it?**
   - risograph, relief print, woodcut, halftone, overprint, misregistration, paper tooth, scratch, grain, or xerox wear.

8. **What should be avoided?**
   - no glossy digital gradient, photoreal landscape, UI poster, corporate infographic, complex illustration, 3D render, neon, stock design, or dense text.

## Word Engine

When the user gives a theme, extract 4-7 words:

- Prefer short lowercase English words unless the user asks for another language.
- Use emotional/action words rather than explanatory labels.
- Good word types: `warm`, `drift`, `reading`, `upward`, `quiet`, `advance`, `open`, `unbound`, `return`, `pulse`, `slow`, `bright`.
- Keep words visually sparse. Do not make a paragraph or slogan.
- Use one word per location. Overlap only when the reference-like boundary crossing is desired.
- If the user supplies exact words, preserve them but keep the layout sparse.

## Variation Engine

Choose one option from each axis before writing the prompt.

### Layout Family

- **center-plate:** one large centered rectangular texture plate with words around it
- **left-crop-plate:** plate cropped off the right edge with blue column on the left
- **full-bleed-plate-with-margin:** large plate fills most of the right or lower area, leaving one blue band
- **panel-quartet:** four rectangular print panels separated by clean blue gutters
- **two-floating-panels:** two small plates in upper area and one long strip near bottom
- **tree-vein-monolith:** one large branching organic white shape divides blue and coral fields
- **boat-in-contours:** small cream/blue boat silhouette embedded in line waves
- **fingerprint-grid:** concentric fingerprint rings across two panels
- **wave-river-plate:** wide cream channels flow through blue and coral terrain
- **oversized-crop:** contour plate extends beyond the frame, words float in remaining blue.

### Contour Motif

- wave topography
- fingerprint rings
- woodgrain bands
- river channels
- branching tree veins
- leaf skeleton
- small boat in currents
- hillside contour map
- wind field
- coral reef texture
- book-page ripple
- upward plume
- abstract shorelines
- sediment layers

### Plate Treatment

- rough rectangular risograph print
- distressed relief-print block
- xeroxed paper texture window
- overprinted coral and blue field
- cream negative-space channels
- cropped print fragment
- stacked small paper panels
- torn-edge print rectangle
- halftone-contour plate
- misregistered two-color ink pass

### Typography Mode

- rounded lowercase sans
- thin geometric sans
- small cream words around the plate
- white words crossing plate edges
- left-column word stack
- words scattered around panels
- one word at top center and others at margins
- partial-overlap words on texture
- tiny calm labels, no headline
- spacious single-word anchors

### Texture Mode

- risograph grain
- woodcut scratch lines
- paper tooth speckles
- offset misregistration
- ink dropout
- rough screenprint edge
- xerox noise
- uneven overprint
- scratched paper surface
- halftone dust

### Mood Mode

- warm movement
- abstract freedom
- reading calm
- upward momentum
- open air
- tide memory
- map of feeling
- restless optimism
- quiet advance
- elemental growth

## Color Engine

- Default to a medium-blue background covering the whole canvas.
- Use coral-pink/red as the main contrast ink and cream/off-white as paper/negative-space ink.
- Keep darker blue linework inside the plate when useful.
- Approximate ratios: blue background 40%-70%, textured plate 30%-65%, coral 10%-40% of plate, cream 10%-35% of plate.
- Do not add green, purple, yellow, orange, or black unless the user explicitly asks.
- Avoid gradients. Use flat ink, overprint, paper grain, and speckled distress.

## Standard Prompt Shape

Use this exact shape:

```text
Vertical 4:5 or 3:4 riso contour word poster on a solid medium-blue matte paper background, [35%-70%] blue negative space, [layout family] composition with [print plate count/position], flat scanned print view, no frame, no mockup.

For [user theme], create an abstract [contour motif] inside the print plate: dense contour lines, fingerprint/woodcut texture, cream negative-space channels, coral-pink ink fields, darker blue linework, and rough printed edges. Keep it symbolic and map-like, not a literal scene.

Place [4-7 words] as sparse lowercase [typography mode], in cream/white, positioned [word placement]. Add [plate treatment] with [texture mode], visible risograph grain, ink dropout, paper tooth, slight misregistration, scratches, and distressed screenprint texture.

Palette: medium blue field, coral-pink/red ink, cream/off-white ink, darker blue linework only. Mood: [mood mode], poetic modern zine, abstract editorial print. Avoid photorealism, glossy gradients, corporate infographic, UI layout, dense paragraphs, stock poster design, 3D render, neon, cute cartoon, and full narrative illustration.
```

## Workflow

1. Parse the user's content.
   - Identify theme, mood, exact words if supplied, and possible contour metaphor.
   - If no words are supplied, invent 4-7 short lowercase words from the theme.

2. Select a recipe.
   - Pick layout family, contour motif, plate treatment, typography mode, texture mode, mood mode, and color proportions.
   - For batches, vary the plate layout and contour motif, not only the words.

3. Write the final prompt.
   - Use the Standard Prompt Shape.
   - State exact word placement, plate position, color ratio, and texture process.
   - Keep text short because image models distort long text.

4. Generate the image.
   - Use image generation by default.
   - If the user asks for prompt-only, return only the prompt and recipe.
   - If the result becomes photoreal, gradient-heavy, or too busy, regenerate once with stronger risograph/woodcut and flat blue field wording.

5. Return the image and prompt.

## Negative Constraints

Always avoid:

- photoreal landscape, realistic ocean, realistic trees, or detailed scenic illustration
- glossy digital gradients, glass effects, 3D render, cinematic lighting, depth of field
- corporate infographic, UI card, dashboard, app screen, chart, or presentation slide
- crowded typography, paragraphs, slogans, brand ads, CTA, product mockup, logo lockup
- rainbow palette, neon colors, pastel scrapbook, stickers, cute cartoon, anime
- black background, beige-dominant poster, or one-note grey design
- overly clean vector flatness without grain, ink distress, or paper texture
- copying the exact reference words unless user explicitly asks

## Output Format

````markdown
**Generated Image**

![Riso contour word poster](absolute-image-path-or-rendered-image)

**Final Prompt**

```text
[final prompt used for image generation]
```

**Notes**

- Mode: Standard
- Recipe: [layout / contour motif / plate treatment / typography / texture / palette / mood]
- [one short note about how the theme became a contour word poster]
````

If generated images render directly without a file path, show the image normally and still include the final prompt.

## Quality Gate

Before finalizing, check:

- Is there a solid medium-blue poster background?
- Is the main visual a risograph/woodcut contour texture plate?
- Are coral-pink/red, cream/off-white, and blue the only dominant colors?
- Do 4-7 sparse lowercase words float around or across the plate?
- Does the layout preserve meaningful blue negative space?
- Is the image symbolic and map-like rather than a literal scene?
- Are risograph grain, paper tooth, ink dropout, scratches, and misregistration visible?
- Does the prompt avoid gradients, photorealism, UI, corporate infographic, dense text, and generic poster design?
- Did you actually generate the image unless the user asked for prompt-only?

## Example Requests

- "Use $riso-contour-word-poster for a theme about slow freedom and reading."
- "Make a blue riso poster with words: warm, upward, open, return."
- "Turn this abstract reference into the same contour-word poster style."
