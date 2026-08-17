---
name: 幻彩幽灵印
description: "【幻彩幽灵印 / chromatic-ghost-print-zine】 Generate chromatic ghost-print zine prompts and matching raster images from a user theme, phrase, object, city/nature photo, texture photo, or visual brief. Use when the user wants RGB channel separation, analog scan glitches, risograph/halftone grain, high-chroma overprint, black-and-white photo bases with translucent color insert panels, distorted everyday photography, reverse-engineered image prompts, or a noisy experimental zine/poster look."
---

# Chromatic Ghost Print Zine

## Overview

Transform the user's content into a compact image-generation prompt, then generate a raster image from it unless the user explicitly asks for prompt-only. The style fuses minimal zine prompt discipline with full-frame chromatic aberration, scan damage, overprinted color channels, and everyday photographic subjects.

## Source DNA

Use this reverse-engineered structure as the visual identity:

- **Subjects:** ordinary observed material: tree canopy, bark, building facade, streetlamp, skyline, wet pavement, patio furniture, leaves, moss, dirt, branches, sunset trees, small ground specimens.
- **Frame:** usually vertical phone-poster around 4:7 or 3:5; square or horizontal is allowed when the input photo shape matters. The image is flat, cropped, and poster-like, not a mockup.
- **Optical process:** visible RGB channel separation, color misregistration, xerox/scanner noise, VHS-like horizontal white scratches, halftone dots, coarse film grain, posterized contrast, crushed blacks, and color bleeding at edges.
- **Color behavior:** cyan/blue skies, acid green shadows, hot red/magenta fringes, yellow/orange overprint, teal/orange duotone fields, or a single broad spectral band on black. Color is strong and physical, not pastel.
- **Composition:** either full-frame distorted photography, a black-and-white base image with rectangular color overlays, a dark negative-space field with one diagonal chromatic band, or a posterized seasonal texture field.
- **Mood:** experimental, tactile, damaged, nocturnal or sunburned, urban/natural, archival, memory-fragment, late-analog zine.

Do not copy the quiet negative-space grammar of `gc-minimal-zine-poster-v0-1` by default. Borrow its prompt compiler discipline, recipe selection, compact output format, and quality gate; shift the visual result toward dense chromatic print damage.

## Workflow

1. Parse the input.
   - If images are supplied, treat them as source photographs. Preserve their recognizable structure, camera angle, and main subject unless the user asks for reinterpretation.
   - If only text is supplied, choose one plausible everyday photographic subject that can carry the idea.
   - Extract mood, location, season, material, phrase, and any requested aspect ratio.

2. Choose one recipe from the Variation Engine.
   - Change visual grammar between generations, not only color.
   - Prefer a full-frame recipe when the source image has strong structure.
   - Prefer overlay recipes when the source has reflective surfaces, water, pavement, or quiet landscape.
   - Prefer duotone field recipes for leaves, dirt, moss, bark, and other ground textures.

3. Compile a prompt in the required field order.
   - Write concrete imageable instructions. Avoid explaining the concept.
   - Name the subject, crop, analog process, channel offset behavior, color palette, scan defects, and hard avoids.
   - Include text only if the user supplied it or asks for a poster with lettering. Long clean text is usually wrong for this style.

4. Generate the image.
   - Use built-in image generation by default.
   - If a generated result lacks visible RGB separation, scan damage, or analog print texture, tighten the prompt and regenerate once.
   - If a supplied source photo becomes unrecognizable when it should be preserved, regenerate once with stronger preservation language.

5. Return the image, prompt, and recipe.

## Prompt Compiler

Write final prompts as four compact paragraphs in this order:

1. **Canvas and source:** aspect ratio, crop, source subject, viewing angle, flat scanned/printed surface.
2. **Composition:** full-frame photo, overlay rectangles, diagonal spectral band, macro texture, or duotone field; state major shapes and empty/dense areas.
3. **Chromatic print treatment:** exact RGB split behavior, palette, halftone/risograph/xerox texture, scanlines, scratches, noise, posterization, edge bleeding.
4. **Mood and avoids:** analog zine mood plus negative constraints.

Use this prompt skeleton:

```text
[Canvas/source paragraph]

[Composition paragraph]

[Chromatic print treatment paragraph]

[Mood and avoid-list paragraph]
```

## Reverse Prompt Patterns

Use these as compact pattern references. Do not copy them verbatim when the user's subject differs.

- **Foliage glitch prompt:** vertical full-frame upward-looking tree canopy photograph, cyan sky gaps, foliage becomes dense black key plate with red, green, blue channel shadows, extreme risograph grain, tiny white horizontal VHS scratches, high saturation, no border, no typography.
- **Urban signal prompt:** vertical street photograph with building facade on one side, curved streetlamp crossing open blue sky, distant skyline, strong cyan base, green and magenta channel offsets around every edge, scanner scratches across the sky, posterized shadows.
- **Macro bark prompt:** extreme close crop of bark or stone texture, no horizon, relief-like cracks, white highlights and black cavities, aggressive RGB misregistration, coarse halftone dots, xerox noise, full-frame tactile abstraction.
- **Color window prompt:** black-and-white wet pavement or landscape photo fills the canvas; a large translucent color rectangle overlays the center with the same scene in electric cyan/blue/red channel drift; a smaller rectangle offsets below, flat collage edges, scan grain.
- **Diagonal spectral prompt:** near-black poster field with one wide diagonal light strip crossing the top third, white-yellow core with red upper edge and blue/cyan lower edge, noisy granular interior, sparse horizontal white scratches in the black.
- **Seasonal duotone prompt:** top-down leaves, moss, dirt, or small ground plants posterized into burnt orange, yellow, oxidized teal, and black; rough fabric/paper texture; screenprint gaps; flattened natural detail.

## Variation Engine

Pick one family and keep it legible:

- **channel-drift-canopy:** vertical full-frame foliage, branches, or moss; cyan sky or teal ground; dense RGB leaf echoes; black crushed masses; thin horizontal scan scratches.
- **urban-signal-ghost:** building edge, streetlamp, skyline, facade, or glass windows; hard perspective; blue/cyan field; green/red offset shadows; VHS scratches across open sky.
- **bark-or-surface-macro:** extreme close-up of bark, stone, wet pavement, dirt, or paper; tactile relief; harsh posterized channel separation; no visible horizon.
- **mono-base-color-window:** grayscale photo fills the canvas; one large translucent color rectangle and one smaller offset rectangle reveal a chromatic version of the same scene; edges remain geometric and flat.
- **rotated-contact-overlay:** black-and-white landscape or patio scene rotated or misaligned; a large color insert panel partially covers it; the color layer can be rotated 90 degrees if it creates tension.
- **diagonal-spectral-cut:** mostly black field; one wide diagonal beam or strip with white/yellow core and red, green, cyan, blue offsets; sparse white scan scratches above and below.
- **seasonal-duotone-field:** fallen leaves, moss, ground, branches, or tree silhouettes posterized into orange/yellow/teal/black; paper or fabric grain; screenprint texture.
- **soft-cyan-orange-photo:** gentler real-photo base with cyan-blue cast and warm yellow/orange subject; visible grain and slight blur; less glitch, more memory.

## Color Recipes

Use one dominant recipe unless the chosen family requires spectral RGB:

- **RGB offset:** cyan/blue image layer, acid green lateral shadow, red/magenta lateral shadow, deep black key plate.
- **Cyan sky:** saturated cobalt/cyan field with green/red ghosted architecture or foliage.
- **Black with spectral band:** matte black, white/yellow core, red upper fringe, cyan/blue lower fringe, green transitional edge.
- **Teal-orange print:** oxidized teal shadows, burnt orange ground, yellow leaf highlights, black ink gaps.
- **Blue wet-night insert:** grayscale base, electric blue/cyan color window, small red/green pixel fringing.
- **Sunburned nature:** orange sky or ground, dark teal/black trees, tiny bright yellow highlights.

Avoid beige minimalism, soft pastel toning, clean gradient backgrounds, and polished neon cyberpunk. The image can be high-chroma, but it should look printed, scanned, or damaged.

## Typography

Use typography sparingly. Most outputs should be image-led.

- Allowed: tiny typewriter caption, date stamp, fragmented microtext, faint registration marks, small catalog number.
- Optional poster text: one short phrase, imperfectly printed, partially blurred or misregistered.
- Avoid: commercial headline hierarchy, logo, CTA, brand lockup, long clean sentences, UI labels.

## Negative Constraints

Always avoid:

- glossy 3D rendering, cinematic depth of field, polished product-ad lighting
- clean vector illustration, anime, cute cartoon, sticker collage
- generic cyberpunk neon city, futuristic hologram UI, vaporwave grid
- perfectly sharp modern stock photography
- smooth gradients without print texture
- readable long text blocks
- random extra people, faces, logos, signs, or landmarks not present in a source image
- overcomplicated scrapbook layouts unless the user explicitly asks for collage density

## Output Format

````markdown
**生成图**

![Chromatic ghost-print zine image](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Recipe: [variation family / color recipe / texture process / aspect ratio]
- Source interpretation: [one short note]
````

If the user asks for reverse prompting only, omit image generation and return the analyzed structure plus the final prompt.

## Quality Gate

Before finalizing, check:

- Does the image use one clear recipe from the Variation Engine?
- If source images were supplied, is the main source structure still recognizable when preservation was requested?
- Is RGB channel separation, overprint, scanline, halftone, xerox, or grain visible at thumbnail size?
- Does the palette match one of the color recipes without becoming smooth digital neon?
- Does the frame read as flat print or scanned photo rather than 3D mockup?
- Are text elements absent or small and imperfect unless the user explicitly requested prominent type?
- Did the prompt avoid commercial ad layout, clean UI, anime/cartoon, stock-photo polish, and invented logos?
