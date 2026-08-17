---
name: 树冠诗海报
description: "【树冠诗海报 / canopy-poem-poster】 Generate sparse canopy-framed poetry poster prompts and matching raster images from a Chinese poem, short phrase, memory note, landscape reference, or visual brief. Use when the user wants large negative space, watercolor or soft painted foliage around the edges, a pale open center for poem lines, tiny figures or vehicle-like markers, muted green and cream atmospheres, and a quiet literary poster inspired by gc-minimal-zine-poster-v0-1."
---

# Canopy Poem Poster

## Overview

Turn a poem or memory into a poster where the open center is held by soft landscape edges. The composition should feel like a quiet painted clearing: pale paper or sky in the middle, blurred canopy at the margins, and small lines of text floating in the open field.

## Core Rules

- Keep 70%-90% of the canvas open and quiet.
- Let soft foliage, cloud, mist, or painted terrain frame the edges.
- Make the poem small and spare, not full-page dense.
- Use one main text cluster and at most one secondary anchor.
- Preserve a flat, printed, or scanned feel.
- Keep the mood reflective, airy, and lightly surreal.
- If a photo reference is supplied, preserve its open clearing, edge frame, and overall color atmosphere.

## Workflow

1. Read the source.
   - If exact poem text is supplied, preserve short lines and key phrases.
   - If only a feeling is supplied, invent a compact Chinese poem fragment with one anchor word.
   - If a photo is supplied, treat it as a structural reference for the open center and edge framing.

2. Choose a layout family.
   - `center-clearing` for a large open middle with canopy at the borders.
   - `edge-canopy` for stronger foliage framing on two or more sides.
   - `diagonal-clear-path` for a path-like open lane through the composition.
   - `tiny-marker-field` for poems with tiny people, cars, or signs as scale marks.

3. Compile the prompt in five paragraphs.
   - Canvas and paper field.
   - Canopy structure and open clearing.
   - Poem placement and type behavior.
   - Micro-markers, accent, and texture.
   - Mood and avoids.

4. Generate the image.
   - Use built-in image generation by default.
   - If the poem text matters more than painterly texture, use a deterministic layout approach instead of relying on approximate lettering.
   - If the center becomes too busy, clear space first and reduce marker count.

5. Return the image, final prompt, and selected recipe.

## Prompt Shape

Use concrete imageable instructions.

**Canvas and paper**
- State ratio, paper tone, open-space ratio, and whether the field reads as paper, sky, or fog.

**Canopy and clearing**
- State where the soft green or painted masses sit around the borders and how large the central clearing remains.

**Poem layout**
- State the small poem lines, their placement, size, tracking, and whether they float, cluster, or drift.

**Markers, accent, texture**
- State tiny cars, figures, path marks, or one high-chroma anchor if used; keep the print grain and blur soft.

**Mood and avoids**
- State the literary mood and hard constraints.

## Reference

Read [references/structure.md](references/structure.md) for reverse-engineered layout grammar, poem strategies, and prompt recipes.
