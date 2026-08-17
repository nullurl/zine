---
name: 引力诗海报
description: "【引力诗海报 / gravity-poem-poster】 Generate sparse gravity-based poetry typography poster prompts and matching raster images from a Chinese poem, short phrase, emotional keyword, reference image, or visual brief. Use when the user wants Minimal Zine negative space, aged gray paper, tiny tracked poem lines, enlarged falling keywords, repeated ghost text, one small yellow highlight block, ink smudges, distressed print texture, and experimental literary layout inspired by gc-minimal-zine-poster-v0-1."
---

# Gravity Poem Poster

## Overview

Turn a poem or phrase into a quiet typographic poster where words behave like weight. Keep the page mostly empty, let a few small lines establish the poem, then let selected keywords fall, echo, fade, and land on one sharp color anchor.

## Core Rules

- Keep 75%-90% of the canvas as aged blank paper.
- Use typography as the subject. Do not add illustrations or photo objects by default.
- Start with small, widely tracked poem lines near the lower middle or lower third.
- Select 1-4 important words as larger falling keywords.
- Use repeated gray echoes, offset copies, smudges, or faded ink to show memory and error.
- Use only one chromatic accent, usually a small yellow paper/ink block behind the final keyword.
- Keep the composition literary, quiet, and physically printed.

## Workflow

1. Read the input.
   - If exact poem text is supplied, preserve short lines when possible.
   - If the poem is long, select a short excerpt and 1-4 weighted keywords.
   - If only a mood is supplied, invent a compact Chinese poem fragment and one final anchor word.

2. Choose a layout family.
   - Use `low-center-fall` for maximum blank space.
   - Use `central-axis-drop` for solemn, balanced poems.
   - Use `diagonal-drift` when the emotion suggests instability.
   - Use `yellow-anchor` when one final word should dominate.

3. Compile the image prompt in five paragraphs.
   - Canvas and paper field.
   - Small poem lines.
   - Falling keyword structure.
   - Accent block and print texture.
   - Mood and avoids.

4. Generate the image.
   - Prefer built-in image generation for raster poster output.
   - If exact text fidelity matters more than texture, create a deterministic HTML/SVG/PNG layout instead of relying on generated lettering.
   - If the result becomes too text-dense, reduce lines and enlarge negative space.

5. Return the image, final prompt, and chosen recipe.

## Prompt Shape

Use concrete visual instructions, not conceptual explanation.

**Canvas and paper**
- State ratio, paper tone, texture, negative-space ratio, and scan/print feel.

**Small poem lines**
- State where the small lines sit, tracking, size, color, and whether text is crisp or slightly worn.

**Falling keywords**
- State the chosen words, scale shifts, vertical/diagonal path, repeated ghost copies, opacity decay, and spacing.

**Accent and texture**
- State the single color block, ink smudge, xerox dust, paper fibers, and print defects.

**Mood and avoids**
- State the literary mood and the hard no list.

## Reference

Read [references/structure.md](references/structure.md) for reverse-engineered layout grammar, keyword weighting, and prompt recipes.
