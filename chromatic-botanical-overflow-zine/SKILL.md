---
name: 植物色谱
description: "【植物色谱 / chromatic-botanical-overflow-zine】 Generate prompts and finished raster images for botanical photographs that overflow a white instant-photo frame into a flat saturated color field. Use when the user provides a flower, branch, leaf, lotus, tree, plant reference, season, phrase, or palette and wants a clean editorial botanical poster with a cutout subject crossing the frame boundary, preserved source colors, generous negative space, and Minimal Zine paper restraint rather than a scrapbook or commercial flower ad."
---

# Chromatic Botanical Overflow Zine

Turn a flower, plant, branch, season, memory, phrase, or reference image into both a final image-generation prompt and a finished vertical raster poster. The default artifact is a flat saturated color field containing one slightly offset white-bordered photo frame, one botanical image window, and a realistic plant branch or bloom that exits the frame and enters the surrounding field.

This Skill fuses `gc-minimal-zine-poster-v0-1` negative-space discipline with the reference grammar of color-field botanical cutouts: a solid rose, green, blue, sage, or mustard background; an off-white instant-photo border; a natural photograph inside the frame; and one or more flowers, leaves, or branches crossing the border. It is intentionally distinct from botanical scrapbook pages, multi-photo moodboards, and floral identity posters.

## Reference Routing

- Treat supplied images as visual-grammar and palette references unless the user explicitly asks for a literal edit.
- Extract background hue, frame offset, frame size, photo-window ratio, border thickness, blank caption area, plant crossing direction, subject scale, shadow softness, color contrast, and visible paper share.
- Preserve the source color relationships by role: flat background field, white frame, botanical subject, dark stem, flower center, and optional tiny accent.
- Do not copy exact flowers, personal photographs, logos, signatures, watermarks, or distinctive text from references.
- Do not upload private local references to an untrusted third-party endpoint. The bundled server fallback is text-only.
- Read [references/style-grammar.md](references/style-grammar.md) when reverse-engineering a reference or fixing structure and color drift.
- Read [references/prompt-recipes.md](references/prompt-recipes.md) when choosing a composition, plant behavior, or palette lock.

## Mode Policy

Choose one mode before compiling the prompt.

- **Blossom Overflow Mode:** one large flower branch crosses a centered or slightly offset frame, with blossoms outside the frame at one corner. Default for cherry, peach, plum, magnolia, or flowering branches.
- **Single Stem Specimen Mode:** one stem, leaf, fern, or seed head rises through a quiet frame and exits one edge. Best for minimal botanical studies.
- **Frame and Counterbranch Mode:** the interior photo shows the plant context while a cutout branch enters from the opposite edge, creating a controlled diagonal crossing.
- **Color-Field Herbarium Mode:** a single plant specimen and its photo frame sit inside a bold field with a blank lower caption area and almost no extra graphics.
- **Palette-Locked Reference Mode:** preserves a supplied reference background hue and plant color hierarchy while changing the botanical subject or crop. Use whenever the user asks to retain, match, or extract reference colors.

Default to **Blossom Overflow Mode** for a flower branch. Use **Color-Field Herbarium Mode** when the brief is abstract, product-free, or nearly textless.

## Structural Rules

### Canvas and Field

- Use a vertical 3:5, 4:5, or 2:3 poster canvas.
- Fill 65%-88% of the canvas with one flat, matte, high-chroma color field.
- The field is a solid printed surface, not a smooth gradient or realistic room background.
- Preserve 10%-25% quiet field around the frame and plant silhouette.
- Use soft paper tooth, mild scan noise, and very shallow contact shadow only.

### Frame

- Use exactly one main off-white or warm-white instant-photo frame.
- Frame width: 45%-72% of canvas; frame height: 52%-78% of canvas.
- Offset the frame slightly from center by 2%-12% of its width or height.
- Border thickness: 3%-7% of the frame width.
- Add a blank lower caption strip occupying 10%-18% of frame height unless the user requests text there.
- The inner photo window occupies 76%-90% of the frame width and 65%-82% of the frame height.
- The frame can sit behind the plant cutout; it must not become a rounded UI card, floating 3D object, or stack of several cards.

### Overflow Geometry

- One botanical branch, stem, leaf cluster, or flower group must visibly cross the frame boundary.
- The overflow should occupy 12%-35% of the canvas and extend beyond one or two edges, usually a corner or diagonal.
- Keep the plant anatomically continuous: the interior photograph and exterior cutout must share branch direction, lighting, species, and color.
- Use one main overflow direction: lower-left to center, lower-right to upper-right, top-center downward, or diagonal corner escape.
- Overlap the plant over the white border in front; do not simply crop the photo at the frame edge.
- Allow one small foreground flower or leaf to cross the frame while most of the specimen remains readable.

## Botanical Subject System

Choose one subject family:

- flowering branch: cherry, peach, plum, apple, magnolia, or unnamed spring blossom
- single flower: lotus, peony, orchid, poppy, camellia, or wildflower
- leaf structure: monstera, lotus leaf, fern, eucalyptus, vine, or broad tropical leaf
- woody specimen: bare branch, budding twig, seed head, or small tree crown

Use one dominant plant and no more than two secondary elements such as buds, leaves, a second branch, or a blurred flower in the photo window. Avoid unrelated botanical species in one image.

## Color Engine

### Reference Palette Lock

When references are supplied, preserve color by region rather than applying a global filter.

1. Identify the flat background field hue and its lightness.
2. Preserve the white frame as a neutral contrast anchor.
3. Keep flower petals, leaves, stems, and centers naturally distinct from the background.
4. Preserve the original saturation level; do not automatically mute a vivid field or oversaturate a pale flower.
5. Permit one tiny adjacent accent only when it exists in the reference.

Common field roles:

- dusty rose / blush `#C98496` or `#D59AA9`
- forest green `#1D6B51` or `#235D48`
- muted sage `#729B7A` or `#6D9272`
- sky blue `#5D91CC` or `#79A9D6`
- deep pine `#263F34` or `#304A3D`
- mustard yellow `#E6C400` or `#DDBB00`
- pale periwinkle `#AFC5EA`

These values are guides for the relationship, not clean digital fills. Keep the background visibly flat and uninterrupted. Use a single dominant field color per image. Do not blend all references into a rainbow board.

## Typography and Caption Policy

- Default to no text. The reference composition can work as a nearly textless botanical image poster.
- If the user provides exact text, place only one short line in the blank lower caption strip or below the frame.
- Use small serif, typewriter, or understated monospaced lettering; never use a giant commercial headline.
- Do not invent author names, dates, product names, studio names, logos, or signatures.
- Keep the caption strip blank when the user says no署名, no text, or no attribution.

## Material and Lighting

- Realistic but softly photographed plant detail inside the frame.
- Cutout branch outside the frame has clean yet slightly feathered edges, natural translucent petals, and no obvious digital halo.
- Matte white paper frame with subtle fiber grain and a very soft contact shadow.
- Flat studio daylight or diffuse overcast light, consistent inside and outside the frame.
- Mild print texture, low-resolution raster softness, slight edge wear, and restrained scan noise.
- No glossy plastic frame, dramatic 3D depth, hard cast shadow, or desktop still life.

## Minimal Zine Bridge

Preserve from `gc-minimal-zine-poster-v0-1`:

- vertical paper poster and flat scanned appearance
- one dominant image anchor with decisive negative space
- restrained short text or no text
- one clear color logic rather than decorative rainbow accents
- tactile paper and print surface
- quiet editorial mood

Adapt:

- tiny paper object becomes one complete botanical frame and one overflow silhouette
- one color accent becomes a full solid field when the reference depends on color blocking
- photograph and cutout remain one continuous subject, not a photo collage
- paper border is the structural container; plant overflow creates the only major depth cue

## Prompt Compiler

Write the final prompt as six compact paragraphs:

1. Canvas, solid color field, ratio, exposed-field share, and flat scanned-paper treatment.
2. Exact frame size, offset, border thickness, inner photo window, and blank caption strip.
3. Botanical subject, photo framing, species/season, and overflow direction.
4. Color roles: field hue, frame neutral, plant colors, stem/center contrast, and any reference-palette lock.
5. Material, lighting, edge treatment, shadow softness, and optional short text.
6. Emotional temperature and hard avoids.

Compile only visible renderable details. Never mention source paths, reverse engineering, or the reference-image analysis in the final prompt.

## Workflow

1. Parse the brief.
   - Identify plant, season, exact text, field color, frame behavior, overflow direction, and whether the reference controls palette, geometry, or subject.

2. Select one mode and one overflow recipe.
   - Fix frame dimensions, plant crossing edge, background field, photo-window crop, and caption policy before writing the prompt.

3. Compile the six-paragraph prompt.
   - State the color field and frame geometry before poetic mood.
   - Preserve supplied text exactly and omit attribution when requested.

4. Generate the image.
   - Use the built-in image generation capability by default.
   - If unavailable and configured server fallback is permitted, run `scripts/server_image_gen.py` with the final prompt.
   - Store the exact prompt beside the output and never overwrite an existing image unless explicitly requested.

5. Inspect once and regenerate once if needed.
   - Regenerate if the flower stays inside the frame, the frame becomes a card stack, the field turns into a gradient, the colors drift, or the branch loses continuity.

6. Return the image, prompt, mode, frame geometry, overflow direction, and palette roles.

## Hard Avoids

Always avoid:

- multi-photo scrapbook, Polaroid stack, moodboard grid, tickets, stickers, washi tape, or stationery clutter
- rounded UI cards, website layouts, app panels, social templates, or product mockups
- full-bleed flower with no white frame or no color field
- background gradients, rooms, desks, vases, packaging, or commercial flower advertising
- glossy 3D frame, hard perspective, floating paper stack, heavy shadow, or digital halo
- neon rainbow colors, muddy desaturation, global tint, and uncontrolled color mixing
- unrelated plant species, duplicate fake photos, malformed stems, impossible petal anatomy
- long text, copied reference words, brand names, signatures, watermarks, or CTA

## Fallback Script

The fallback reads the OpenAI-compatible provider from Codex configuration or environment variables and never stores credentials in the Skill.

```bash
python3 scripts/server_image_gen.py \
  --prompt-file /absolute/path/to/prompt.txt \
  --out output/imagegen/chromatic-botanical-overflow-zine-output.png
```

Use `--dry-run` to inspect the request without sending it. The default is the Images API and `gpt-image-2`; use `--wire-api responses` only for a compatible Responses image-generation endpoint.

## Output Format

````markdown
**生成图**

![Chromatic Botanical Overflow Zine](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**构图配方**

- Mode: [Blossom Overflow / Single Stem / Frame and Counterbranch / Color-Field Herbarium / Palette-Locked Reference]
- Frame: [ratio, offset, border, caption strip]
- Overflow: [plant and crossing direction]
- Palette: [background field / frame / botanical colors]
````

## Quality Gate

Before finalizing, check:

- Is there exactly one main white botanical frame?
- Is the surrounding field a flat intentional color rather than a gradient?
- Does one continuous plant subject visibly cross the frame boundary?
- Does the inner photo and exterior cutout share species, branch direction, light, and color?
- Is 65%-88% of the canvas a coherent color field with enough quiet space?
- Is the frame matte and paper-like rather than glossy or 3D?
- Are colors preserved by role when a reference palette is supplied?
- Is text absent or short and subordinate?
- Does the result avoid scrapbook clutter, UI cards, commercial flower ads, and copied reference content?
- Was a finished raster image generated and inspected?

