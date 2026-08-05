---
name: 复印缺席
description: Generate prompts and finished raster images for poetic xerox nature collages with source-palette preservation, overlapping landscape photographs, botanical negatives, blurred birds, anonymous portrait and eye fragments, typewriter poetry, exposed tape, paper seams, cobalt light blooms, forest green plates, cold violet inserts, and weathered photocopy grain. Use when the user supplies a theme, poem, memory, landscape, flower, bird, person, or reference image and wants a color-faithful analog literary collage about absence, forgetting, distance, migration, or traces rather than a decorative scrapbook.
---

# Xerox Absence Collage Zine

Turn a theme, phrase, poem, memory, or reference into both a final image-generation prompt and a finished vertical raster poster. The default artifact is a flat scanned paper page assembled from three to seven rectangular nature-image fragments, one dominant transformed subject, a short typewriter text block, and a controlled cool-color reproduction palette. When references are supplied, preserve their color hierarchy and collage density before introducing new content.

This Skill fuses the quiet attention discipline of `gc-minimal-zine-poster-v0-1` with layered photocopy landscapes, negative flowers, blurred migration studies, torn portrait evidence, and literary archive pages. It expands the source Skill's small cluster into an irregular field of overlapping image plates while preserving decisive paper space, a single conceptual anchor, a coherent reproduction palette, and restrained type.

## Reference Routing

- Treat supplied images as visual-grammar references unless the user explicitly asks to edit one.
- Extract panel geometry, overlap order, paper ratio, subject repetition, tonal separation, type placement, tape behavior, scan grain, accent area, dominant hue families, regional saturation, and light/dark area proportions.
- Preserve source color relationships by role: paper, landscape base, shadow plate, atmosphere plate, transformed subject, portrait/eye insert, and rare warm residue. Do not collapse a green-blue-violet reference into monochrome.
- Do not reproduce visible poems, names, signatures, logos, watermarks, exact portraits, or exact layouts from references.
- Never infer identity or sensitive traits from an anonymous portrait.
- Analyze local references locally. The bundled server fallback is text-only and does not upload reference images.
- Read [references/style-grammar.md](references/style-grammar.md) when analyzing references or correcting structural drift.
- Read [references/prompt-recipes.md](references/prompt-recipes.md) when choosing a mode, layout, or regeneration correction.

## Mode Policy

Choose one mode before compiling the prompt.

- **Exposure Bloom Mode:** dense charcoal image field, one electric-cobalt or white negative botanical/body presence, narrow marginal poem. Best for apparition, touch, signal, dream, and embodied memory.
- **Mountain Archive Mode:** overlapping misty landscape plates, one small anonymous portrait or object insert, one typed note on translucent paper. Best for distance, forgetting, wilderness, water, and return.
- **Pale Migration Mode:** 50%-70% pale paper and fog, blurred birds across translucent sky rectangles, one field or mountain strip, central poem. Best for seasons, leaving, freedom, waiting, and passage.
- **Remains Atlas Mode:** high-white page with a loose matrix of tree, flower, water, cloud, and terrain fragments plus separated type blocks. Best for collected memories, essays, archives, and fragmented narrative.
- **Palette-Locked Reference Mode:** preserve the supplied reference's forest green, mineral blue, cobalt/ultraviolet, cold violet, scanner white, and rare oxidized residue while translating its panel grammar to new content. Best whenever the user says keep, retain, match, or extract reference color and collage effects.

Default to **Mountain Archive Mode** for landscape or memory themes. Use **Pale Migration Mode** when the brief implies air, movement, birds, time, or large quiet space. Route all explicit color-preservation requests through **Palette-Locked Reference Mode**, then borrow the density pattern from one of the other four modes.

## Structural Rules

### Page

- Vertical 2:3, 3:5, or 4:5 paper artifact.
- Off-white scanner bed or fibrous paper remains visible around the collage.
- Flat orthographic capture; no framed print mockup, desk scene, card shadow, or black presentation border.
- Preserve 12%-30% exposed paper in dense modes and 45%-70% in pale modes.

### Panel Geometry

- Use three to seven rectangular image plates.
- One main plate occupies roughly 38%-62% of the page.
- Two to five secondary plates overlap its edges by 5%-25% of their own area.
- Keep panel edges mostly parallel to the page; allow no more than one slight rotation.
- Use hard crop seams, translucent overlaps, torn paper edges, or scanner registration offsets. Avoid rounded cards and evenly spaced grids.
- At least one image plate should cross or interrupt another rather than merely sit beside it.

### Subject System

Choose one dominant subject family, one transformed echo, and up to three supporting traces. Supporting traces must share the same place, memory, or reproduction process:

- landscape: mountain ridge, forest, meadow, river stones, sea edge, cloud bank
- botanical: white flower, leaf, branch, seed head, blurred bloom
- movement: bird flock, one smeared bird, drifting cloud, wind-bent grass
- human trace: anonymous silhouette, cropped eyes, obscured face, hand, absent chair
- residual object: window, tape fold, envelope edge, torn note, scratched transparency

Repeat or transform the dominant subject once: positive/negative, sharp/blurred, color/grayscale, or whole/cropped. Do not assemble unrelated stock images.

### Reference Element Library

Select two to five elements from the reference-derived library; do not use all of them in one page:

- misted mountain stack with three receding tonal ridges
- mineral-blue cloud plate laid over a forest-green mountain plate
- narrow river-stone, meadow, or water strip anchoring the bottom edge
- blurred branch canopy used as a pale background veil
- cobalt hand/body/flower exposure with a white-hot xerox center
- overexposed white flower negative on a charcoal-green plate
- narrow blue-gray eye strip, simplified mask field, or two isolated eyes
- cold-violet anonymous portrait insert with a black silhouette body
- thin torn white fiber or scratch crossing the portrait's eye line
- bird flock distributed across two or three translucent sky plates, mixing sharp and motion-smeared birds
- taped top edge with folds, trapped air, milky glare, and lifted corners
- one rubbed vertical xerox strip, scratched transparency, or generational copy scar
- separated typewriter evidence blocks rather than one continuous paragraph

Use elements as structural evidence. A portrait insert, eye strip, or flower negative should interrupt a landscape plate; it should not float as a decorative sticker.

### Occlusion Chain

Build a readable front-to-back sequence:

1. scanner white or pale rubbed paper
2. blurred branch, fog, or gray background plate
3. dominant forest/mountain/sky plate
4. offset mineral-blue or green duplicate plate
5. transformed subject or portrait/eye insert
6. torn white seam, tape fold, or rubbed emulsion crossing one boundary
7. typewriter patch above one quiet region

Require at least two visible interruptions: one plate crossing another and one material seam crossing a plate edge. Avoid evenly distributed collage fragments.

### Typography

- Use rough monospaced typewriter text, imperfect carbon-ribbon density, irregular baseline, and occasional doubled letters or toner dropout.
- Place one short poem or sentence in a margin, translucent paper patch, or quiet center rectangle.
- Keep exact user-supplied copy verbatim. Do not add an author unless supplied.
- When no copy is supplied, invent no more than 4 short lines and avoid names, venues, dates, or institutions.
- Long copy should be reduced to a visual block because image models distort paragraphs.
- Typography is evidence, not a headline: no commercial title hierarchy or oversized clean sans-serif slogan.

## Color and Exposure Engine

Build from scanner white, charcoal, soot black, fog gray, forest green, mineral blue, weathered cobalt, and cold violet.

### Standard Color Event

Choose one primary chromatic event:

- electric cobalt or ultraviolet-blue exposure bloom
- desaturated cobalt landscape plate
- cold violet portrait insert
- a tiny oxidized peach or moss residue only when it supports the source palette

In dense modes, cobalt may occupy 4%-14% of the page as the transformed subject. In pale modes, keep saturated color to 1%-5%. White negative flowers may become a second brightness event but not a second hue. Preserve the saturated anchor through grain; do not wash it into an imperceptible pastel mark.

Use color as a printing event, not global cinematic grading. The surrounding photography stays muted and material.

### Reference Palette Lock

Use this whenever the user supplies references and asks to retain their colors.

1. Identify four to seven visible palette roles rather than averaging the whole image.
2. Preserve the approximate area share of each role within a tolerance of about 10 percentage points.
3. Keep hue identities separated by plate: green belongs to forest/ground, mineral blue to mist/sky, cobalt to exposure, violet to portrait or twilight, white to paper/negative bloom.
4. Preserve local saturation in the colored plate even after adding grain. Do not apply a global desaturation, sepia wash, pastel veil, or monochrome filter.
5. Allow one rare warm residue, such as oxidized peach or muted clay, below 2% of the page only when it exists in the reference.

Reference-derived palette roles:

- scanner white and fog paper: 20%-60%
- charcoal and forest black-green: 20%-48%
- muted forest/moss green: 10%-32%
- mineral blue and blue-gray: 10%-35%
- cobalt or ultraviolet exposure: 3%-14%
- cold violet portrait/sky insert: 2%-10%
- oxidized peach residue: 0%-2%

Treat these as region budgets, not flat digital swatches. Preserve visible green-blue-violet separation at thumbnail size.

## Material Engine

Use several compatible analog defects, not every defect at once:

- coarse xerox grain and toner clumping
- photocopy generation loss and soft halftone dots
- scanner streaks, dust, rubbed edges, and paper fibers
- overexposed white bloom or fluorescent cobalt toner
- offset color misregistration and double exposure
- translucent tape with creases, trapped air, and milky reflections
- torn paper, deckled fiber, rubbed emulsion, and hard rectangular crop seams
- slight vertical banding, ghost images, and low-resolution raster edges

The surface should feel handled and repeatedly copied. Avoid polished vintage filters or fake digital noise overlays with uniform texture.

## Minimal Zine Bridge

Preserve from `gc-minimal-zine-poster-v0-1`:

- vertical paper artifact and flat scanned view
- one conceptual anchor and one coherent color strategy; reference mode may retain several allied source hues assigned to separate material roles
- short typewriter/monospaced text
- negative space, quiet emotional temperature, and old-print defects
- no commercial hierarchy, UI, glossy 3D, or cinematic advertising

Adapt:

- the tiny 8%-25% cluster becomes an irregular 3-7 plate collage
- one object becomes one subject repeated through two reproduction states
- one colored cutout becomes a cobalt exposure bloom, color-separated image plate, or violet portrait fragment
- microtext becomes a visible but subordinate literary evidence block
- blank paper may alternate with dense dark plates rather than surround one isolated specimen

Do not import source-specific signatures, dates, captions, or sample objects.

## Prompt Compiler

Write the final image prompt as five compact paragraphs in this order.

1. **Page and mode:** ratio, paper tone, exposed-paper share, scan view, and selected density mode.
2. **Panel map:** exact number and size hierarchy of rectangular plates, overlap order, crop seams, and placement.
3. **Subject transformation and palette:** dominant natural or human trace, repeated state, selected reference elements, regional palette roles, approximate area shares, and exposure event.
4. **Typography and materials:** exact short copy, typewriter behavior, text location, tape/torn-paper details, and chosen print defects.
5. **Mood and avoids:** emotional temperature followed by the relevant negative constraints.

Compile only details that become pixels. Never mention source paths, reverse-engineering, prompt analysis, or named reference artists in the final prompt.

## Workflow

1. Parse the request.
   - Identify theme, exact text, subject family, emotional verb, palette, and whether references control content, structure, color, or all three.
   - When color preservation is requested, write a palette-role map before selecting subjects.
   - Reduce abstract ideas to one visual relation such as `mountain / obscured portrait`, `bird / paper sky`, `flower / negative light`, or `water / missing fragment`.

2. Select a mode and recipe.
   - Choose one mode, one layout recipe, three to seven plates, one repeated subject, two to five reference-derived elements, one text zone, and one color strategy.
   - If the page becomes decorative, remove a supporting plate before removing the main subject.

3. Compile the prompt.
   - State measurable structure before mood language.
   - In reference mode, state each hue's material role and region share. Never ask for vague `same colors` or a global color grade.
   - Preserve exact user text and attribution policy.
   - Use reference structure without copying reference text, identity, or exact arrangement.

4. Generate the image.
   - Use the built-in image generation capability by default.
   - If unavailable and the configured server fallback is permitted, run `scripts/server_image_gen.py` with the final prompt.
   - Store the final prompt beside the image and use a descriptive output slug. Never overwrite an existing output unless explicitly requested.

5. Inspect and regenerate once when needed.
   - Regenerate if panels become rounded cards, the page becomes a generic scrapbook, the main subject is unclear, type becomes a commercial headline, the cobalt event disappears, source green/blue/violet separation collapses, or all photographs merge into one full-bleed scene.
   - Correct geometry or hierarchy before adding detail.

6. Return the image, final prompt, mode, panel map, selected elements, subject transformation, and palette-role map.

## Hard Avoids

Always avoid:

- cute scrapbook, sticker journal, washi-tape decoration, Polaroid stack, ticket collage, or stationery flat lay
- rounded UI cards, social templates, app panels, clean modular dashboard grids, or device mockups
- full-bleed glossy landscape photography with text simply placed over it
- vintage postcard styling, sepia nostalgia, beige-only junk journal, or decorative lace
- fashion campaign, album-cover glamour, large commercial headline, logo, CTA, QR code, or sponsor wall
- 3D paper depth, hard drop shadows, dramatic perspective, cinematic lens flare, HDR, neon, chrome, or cyberpunk
- unrelated image montage, arbitrary rainbow accents, collapsed monochrome when source colors are requested, global purple grading, or teal-orange grading
- copied poems, signatures, logos, private text, exact faces, watermarks, or pseudo-readable filler paragraphs

## Fallback Script

The fallback reads the OpenAI-compatible provider from Codex configuration or environment variables and never stores credentials in the Skill.

```bash
python3 scripts/server_image_gen.py \
  --prompt-file /absolute/path/to/prompt.txt \
  --out output/imagegen/xerox-absence-collage-zine-output.png
```

Use `--dry-run` to inspect the request without sending it. The default is the Images API and `gpt-image-2`; use `--wire-api responses` only for a compatible Responses image-generation endpoint.

## Output Format

````markdown
**生成图**

![Xerox Absence Collage Zine](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**构图配方**

- Mode: [Exposure Bloom / Mountain Archive / Pale Migration / Remains Atlas / Palette-Locked Reference]
- Panels: [main plate + secondary overlap map]
- Elements: [2-5 selected reference-derived elements]
- Subject transformation: [positive/negative, sharp/blurred, color/grayscale, or whole/cropped]
- Palette roles: [paper / landscape / atmosphere / transformed subject / insert / rare residue]
````

## Quality Gate

Before finalizing, check:

- Does the result read as a flat scanned paper collage rather than a digital template?
- Is the selected mode visible at thumbnail scale?
- Are there three to seven intentional rectangular plates with at least one real overlap?
- Is one plate clearly dominant?
- Is there one coherent subject family repeated through two states?
- Are two to five extracted elements structurally integrated rather than scattered as decoration?
- Does the overlap order create at least two visible interruptions?
- Is exposed paper within the selected mode's range?
- Is the typewriter text short, subordinate, and attribution-safe?
- Is the cobalt or chosen color event clearly visible but controlled?
- When reference colors were requested, are forest green, mineral blue, cobalt, cold violet, paper white, and rare warm residue preserved by region rather than flattened by a global grade?
- Are tape, tears, grain, and registration defects material rather than decorative?
- Does the image avoid rounded cards, scrapbook clutter, commercial hierarchy, glossy photography, and copied source information?
- Was a finished raster image generated and inspected?
