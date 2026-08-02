---
name: telos-editorial-zine
description: Generate sparse monochrome editorial zine posters and matching prompts/images. Use when the user wants a white-field concept cover, thesis-like poster, minimal paper layout, tiny grayscale anchor, conceptual title or numbering, or a quiet editorial composition from a theme, sentence, object, memory, or reference image.
---

# Telos Editorial Zine

Create a sparse monochrome editorial poster and the prompt used to generate it.

## Reference Routing

- Treat supplied images as grammar or subject references unless the user explicitly asks for a literal edit.
- Read [references/style-grammar.md](references/style-grammar.md) when reverse-engineering a reference image or correcting layout drift.
- Read [references/prompt-recipes.md](references/prompt-recipes.md) when choosing a layout or translating an abstract theme.

## Core Identity

Preserve these signals:

- Tall 3:5 or 2:3 paper frame.
- Mostly white, cream, or very pale gray paper, usually 75%-92% of the canvas.
- One small grayscale anchor only; avoid strong color unless the user explicitly asks for it.
- Anchor can be a tiny photo, object, diagram, clipping, or specimen.
- Typography is small black serif, sans, or typewriter mixed with faint microtext.
- One short title, optional numbering or date, and limited supporting copy.
- Flat scanned-paper look with visible fibers, mild photocopy wear, and no studio mockup.
- Mood: conceptual, editorial, thesis-cover, archive-like, quiet, distant.

## Fusion With Minimal Zine

Carry forward:

- one attention cluster
- generous empty paper
- sparse text with material presence
- matte scan defects and paper fibers
- one clear visual metaphor, not a full scene

Change the grammar:

- remove the bright chromatic anchor from the source style
- keep the composition near-monochrome
- let the image feel more like an editorial sheet or thesis cover than a poster collage

## Layout Engine

Choose one family before compiling:

- center-specimen: tiny centered anchor with large surrounding blank.
- lower-note: small anchor low on page with title above.
- upper-corner-card: compact image or diagram block in a corner with drifted type.
- off-center-thesis: image and title slightly off-axis like a cover sheet.
- single-record: one specimen or photo with catalog text.
- double-fragment: two small grayscale fragments with a narrow gap.

Use one layout family only.

## Color Trend Enhancement

Use this only when the user asks for brighter color, richer color, preserved source color, a named palette mood, or when the draft would otherwise become too gray, beige, dark, or flat. Preserve this skill's layout grammar first; color is an enhancement layer, not a replacement for structure.

Pick one dominant palette and optionally one small adjacent accent. Assign colors to visible roles such as paper field, photo grade, ink, label, material, shadow, highlight, or motion accent. Do not combine more than two palettes unless the user explicitly asks for chaotic or maximal color.

- forest green: #92AD76, #B6CCAA, #E3EBDD, #71906A, #435F45. Use for botanical, tropical, moss, spring, garden, healing, or green-reverie briefs.
- purple luxury: #7B5FA4, #A487C6, #D8C9EE, #9A8AB6, #5B376D. Use for dreamy, ritual, night floral, velvet, memory, or quiet-luxury briefs.
- vintage mocha: #885949, #C87949, #E6BC8C, #D9D2C8, #203A35. Use for cafe, archive, editorial, old-photo, paper, or warm city briefs.
- earth warm brown: #A5673D, #C89A6B, #E8D6C3, #7B5A42, #3D2C22. Use for handmade, soil, leather, textile, relic, desert, or autumn briefs.
- deep sea blue: #0F2E48, #1E4F73, #5C87B2, #AFC5DA, #E6F0F8. Use for ocean, rain, night water, cloud-sea, distance, or cinematic calm.
- mist blue gray: #9FB0C3, #C9D3DF, #EEF2F6, #75879A, #31485D. Use for rain, fog, glass, winter, quiet architecture, or analytical moods.
- sunset orange: #FF9A42, #FFC185, #FFE9D3, #C66A31, #7B3D1E. Use for warm light, cafe lamps, islands, evening, energy, or celebratory accents.
- cream soft pink: #F6D7DE, #FBE9EE, #FFF7F8, #E9C6D1, #C39BAA. Use for bright journaling, tender memory, blossoms, soft albums, or feminine notes.
- sea-salt blue: #A8D8EA, #D8EDF5, #F8FCFD, #7FB8CF, #5A8097. Use for airy coastal, island, pool, travel, summer, or brighter-water requests.
- desert elegant white: #F7F4EE, #E7DED1, #D1C6B8, #A99F91, #736F66. Use as a clean bright base when the image needs lift without saturation.

When brightening a dark output, increase paper/background luminance with desert elegant white, sea-salt blue, or cream soft pink before increasing saturation. When preserving a reference image, keep its main hues first, then harmonize them with the closest palette above.

## Prompt Compiler

Write prompts in four compact paragraphs:

1. Frame, paper tone, empty-space share, overall scale.
2. Anchor, placement, treatment, and physical medium.
3. Typography, short title, numbering or date, and microtext limits.
4. Scan texture, paper fibers, grayscale logic, and hard avoids.

## Generation

- Generate the image by default; do not stop at prompt-only unless the user explicitly asks for prompt-only.
- Use the built-in image generation capability.
- Inspect once. Regenerate with one targeted correction if the image becomes too colorful, too dense, too glossy, or too close to a scrapbook or ad layout.

## Hard Avoids

Always avoid:

- saturated accent colors unless explicitly requested
- dense collage clutter
- commercial poster hierarchy
- clean UI, dashboard, app card, or website mockup
- glossy studio lighting or 3D mockup shadows
- full-bleed scenery
- cute illustration, anime, neon, cyberpunk, or fashion-drama styling
- long readable paragraphs, logos, CTA text, or copied reference text

## Output Format

````markdown
**生成图**

![Telos Editorial Zine](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Layout: [selected family]
- Anchor: [main visual subject]
- Tone: [paper / type / scan / mood]
````

## Quality Gate

Before finalizing, check:

- Is the composition visibly sparse and paper-led?
- Is there one small grayscale anchor rather than a busy scene?
- Does the page keep generous negative space?
- Is the title short and subordinate?
- Are text, numbering, and microtext limited and material?
- Does the scan feel matte, fibrous, and editorial?
- Does the result avoid color-heavy collage, UI, glossy mockup, and commercial styling?
- Did you actually generate the image?
