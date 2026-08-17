---
name: 复印纸几何
description: "【复印纸几何 / xerox-paper-geometry-zine】 Generate sparse xerox-paper geometry zine prompts and matching raster images from a user photo, building/foliage reference, object, phrase, mood, or visual brief. Use when the user wants black-and-white photocopied image fragments, tall paper-poster layouts, large quiet negative space, pale graph or fabric paper texture, thin hairline curves, rough registration borders, burgundy halftone circles or solid vertical blocks, architectural/plant xerox crops, or reverse-engineered minimal zine prompt structures based on gc-minimal-zine-poster-v0-1."
---

# Xerox Paper Geometry Zine

## Overview

Transform the user's content into a compact image-generation prompt, then generate a raster image unless the user explicitly requests prompt-only. This style borrows the disciplined prompt compiler and sparse paper logic of `gc-minimal-zine-poster-v0-1`, but shifts the visual language toward black xerox architecture, paper-study geometry, grid fields, registration marks, and deep burgundy print accents.

## Source DNA

Use this reverse-engineered structure as the core identity:

- **Canvas:** tall vertical phone-poster, usually 9:16, 4:7, or 3:5; flat scanned paper; no mockup, no perspective desk scene.
- **Surface:** off-white, pale gray, or faint gridded paper with visible fiber, fabric weave, scan softness, and light aging. The paper is an active field, not a blank digital background.
- **Photo anchor:** harsh black-and-white xerox crop of ordinary architecture and plants: apartment wall, windows, vines, overgrown facade, shrub mass, exterior AC units, stair edges, wall cracks. It should feel copied, bitmap-thresholded, and imperfect.
- **Geometry:** one or two clean primitive shapes interrupt the paper: burgundy halftone circle, black dot, long oxblood vertical rectangle, translucent gray panel, rough rectangular frame, or thin off-register border.
- **Line system:** pale dusty-red hairlines, loose arcs, thread curves, or crossing registration paths drifting behind the photo. Lines are faint and continuous, not decorative vines.
- **Negative space:** 55%-85% quiet paper. The design can be top-heavy, left-column, centered strip, or split-panel, but it must stay sparse and editorial.
- **Print defects:** broken black edges, photocopy grain, halftone speckle, scan streaks, rough rectangle borders, slight misalignment, low ink density, faint graph lines.

Do not default to colored RGB glitch, dense scrapbook, cute collage, or commercial poster language. The energy should be architectural, quiet, archival, and tactile.

## Workflow

1. Parse the input.
   - If a source image is supplied, preserve its main structure but convert it into a black-and-white xerox fragment.
   - If only text is supplied, choose one ordinary architectural or botanical subject that can be photographed and copied.
   - Extract any requested phrase, date, location, mood, geometry color, or aspect ratio.

2. Choose a recipe from the Variation Engine.
   - Change layout grammar between generations, not only accent shape.
   - Keep one dominant photo fragment or one repeated pair of fragments.
   - Use geometry to create tension, not decoration.

3. Compile the final image prompt.
   - Use the Prompt Compiler field order.
   - Make the paper, photo placement, photo treatment, geometric accent, line system, and negative constraints explicit.
   - Include text only if the user requested it. If text appears, keep it tiny, partial, or archival.

4. Generate the image.
   - Use image generation by default.
   - If the result looks like a clean digital poster, regenerate once with stronger paper, xerox, and rough-edge wording.
   - If the accent disappears at thumbnail size, regenerate once with a larger burgundy/black geometric mark.

5. Return the image, prompt, and selected recipe.

## Prompt Compiler

Write final prompts as four compact paragraphs:

1. **Canvas and paper:** vertical ratio, paper tone, paper texture, border or no border, negative-space percentage.
2. **Xerox photo anchor:** subject, crop, position, scale, thresholded black-and-white treatment, repeated or single.
3. **Geometry and line system:** exact accent shape, color, placement, opacity/halftone, pale red hairlines, rough registration borders, graph/fiber details.
4. **Mood and avoids:** quiet archival zine mood plus hard negative constraints.

Use this skeleton:

```text
[Canvas and paper paragraph]

[Xerox photo anchor paragraph]

[Geometry and line system paragraph]

[Mood and avoid-list paragraph]
```

## Variation Engine

Pick one layout family and one accent system:

- **center-column-specimen:** one narrow vertical xerox photo strip centered on paper, 65%-80% empty margin, one burgundy halftone circle partly touching the photo top.
- **top-band-empty-field:** black xerox photo band occupies the top 25%-35%; the lower 60% is quiet paper, optionally with faint fabric texture or grid.
- **grid-red-column:** pale graph-paper field, top xerox strip, one long oxblood vertical rectangle through the center with rough black registration border.
- **left-xerox-column:** tall black xerox crop runs down the left 35%-45%; right side remains empty paper.
- **translucent-frame-stack:** partial xerox photo near the top; large translucent gray rectangle below with broken black border, faint image ghosting inside.
- **double-contact-sheet:** two identical or near-identical xerox photo panels stacked vertically, separated by paper gap, black dots or circles aligned above/below.
- **thin-border-orbit:** full poster has a rough black rectangular border, one central photo fragment, pale red curves crossing behind, small halftone dot accent.
- **split-paper-photo:** photo and paper divide the page into unequal vertical or horizontal fields with a hard seam.

Accent systems:

- **burgundy-halftone-circle:** dark wine-red dot-screen circle, 5%-10% of canvas width, usually top-center or near the photo edge.
- **black-registration-dot:** matte black circle, slightly rough, used as a pin or weight.
- **oxblood-vertical-block:** long solid rectangle, 15%-30% of canvas width, rough black ink border, semi-opaque or opaque.
- **translucent-gray-panel:** soft gray rectangle, large but quiet, with broken xerox edge marks.
- **pale-red-threadlines:** dusty red thin curves crossing behind all content, low opacity.
- **rough-border-box:** thin uneven black rectangular frame around page or panel.

## Reverse Prompt Patterns

Use these references when the user asks to reverse-prompt a similar image. Adapt subject and proportions; do not copy a sample line by line.

- **Central window specimen:** tall off-white paper poster with rough black page border; narrow vertical black-and-white xerox crop of a weathered building facade centered; dark burgundy halftone circle overlaps the top edge; faint dusty-red crossing curves behind; scanned linen paper texture.
- **Top xerox band:** vertical paper sheet with top third occupied by high-contrast xerox facade-and-vines photo; bottom two-thirds empty pale gray paper; no accent except paper fiber and scan haze.
- **Graph field red column:** pale graph paper covers the poster; top band contains a black xerox architecture crop; a long oxblood rectangle drops down the center with broken black rectangular border marks.
- **Left strip empty page:** vertical poster split with a dense black xerox architecture strip on the left and large blank paper on the right; no color accent, only thresholded copy grain.
- **Ghost frame stack:** upper xerox photo fragment partly hidden behind a large translucent gray rectangle; rough black border traces the rectangle; huge pale paper field below.
- **Double contact sheet:** two stacked black xerox building panels centered; one black circle above and one below; pale red line loops across the background.

## Color and Texture Rules

- Default palette: paper white, pale gray, black xerox ink, one deep burgundy or oxblood accent, optional dusty red hairlines.
- Use burgundy as a material ink: halftone dot, solid block, or translucent printed film. Do not make it glossy or neon.
- Keep the black photo harsh and broken: threshold dots, photocopy grain, crushed black foliage, missing midtones, rough scan streaks.
- Preserve negative space. A large accent block is allowed only when the rest of the page remains quiet.
- Use graph lines, linen weave, scan noise, and paper fibers subtly. They should be visible but not become a decorative pattern.

## Typography

Typography is optional and usually absent.

- Allowed: tiny typewriter date, small catalog number, faint crop mark labels, unreadable microtext.
- Keep text near an edge, inside a panel, or aligned to the photo strip.
- Avoid long readable phrases, big headlines, logos, slogans, and CTA-like commands.

## Negative Constraints

Always avoid:

- glossy mockups, hard shadows, desk scenes, 3D paper stacks
- colorful RGB glitch, neon, cyberpunk, vaporwave, smooth gradients
- stock-photo realism, cinematic lighting, shallow depth of field
- decorative scrapbook clutter, stickers, tape pieces, washi borders
- cute cartoon, anime, vector illustration, polished brand poster
- ornate typography, large commercial headlines, logo lockups
- too many colors or multiple competing photo subjects

## Output Format

````markdown
**生成图**

![Xerox paper geometry zine image](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Recipe: [layout family / accent system / paper texture / aspect ratio]
- Source interpretation: [one short note]
````

If the user asks for reverse prompting only, omit image generation and return the analyzed structure plus the final prompt.

## Quality Gate

Before finalizing, check:

- Did the prompt use the four-paragraph Prompt Compiler?
- Does 55%-85% of the image read as tactile paper or grid/fiber field?
- Is the photo anchor clearly black-and-white xerox, not grayscale stock photography?
- Is there one controlled geometry accent or line system rather than many decorations?
- If burgundy/oxblood is used, is it visible at thumbnail size and physically printed?
- Are paper borders, panel edges, or photo edges rough enough to avoid clean digital layout?
- Does the composition avoid full-bleed scenes, glossy mockups, neon, cartoons, and commercial poster hierarchy?
