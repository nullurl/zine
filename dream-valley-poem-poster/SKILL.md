---
name: 梦境山谷诗
description: "【梦境山谷诗 / dream-valley-poem-poster】 Generate surreal floral landscape poetry poster prompts and matching raster images from a Chinese poem, phrase, memory note, reference image, or visual brief. Use when the user wants dreamlike valley scenes, giant flowers, cloud seas, tiny human figures, warped perspective, vivid green/orange/pink fields, and a minimal literary poster structure inspired by gc-minimal-zine-poster-v0-1 but expanded into an atmospheric landscape."
---

# Dream Valley Poem Poster

## Overview

Turn the source into a surreal landscape poster where the poem sits inside or against a vast dream scene. The visual should feel spacious and cinematic, but still sparse in the zine sense: one clear world, one or two human-scale anchors, and controlled text.

## Core Rules

- Keep one dominant landscape world.
- Use large sky, valley, flower field, or cloud mass as the main field.
- Keep the poem short and integrated into the space.
- Add tiny human figures, paths, or architectural hints for scale.
- Use one strong accent family at a time: orange flowers, pink blossoms, blue sky, or green valley.
- Keep the image flat enough to read like a printed poster, not a polished movie still.
- If a reference image is supplied, preserve its scene logic and not just its palette.

## Workflow

1. Read the source.
   - If the user supplies a poem, extract one central line and one anchor word.
   - If the source is only an image or theme, choose one dreamscape metaphor: valley, meadow, cloud sea, floral slope, portal field, or impossible path.

2. Choose a layout family.
   - `wide-horizon-valley` for panoramic fields and clouds.
   - `center-path-garden` for a path or figure leading through flowers.
   - `surreal-vertical-valley` for steep impossible slopes and cloud chambers.
   - `flower-sea-portal` for floral fields opening into sky or architecture.
   - `tiny-figure-scale` for compositions where a single figure or pair gives size.

3. Compile the prompt in five paragraphs.
   - Canvas and landscape field.
   - Scene structure and scale.
   - Poem placement and type behavior.
   - Color, texture, and atmosphere.
   - Mood and avoids.

4. Generate the image.
   - Prefer built-in image generation for raster output.
   - If the result becomes too scenic or too literal, re-tighten the prompt around one surreal world and one text cluster.
   - If the poem is important, keep the text short and legible enough to act as part of the composition.

5. Return the image, final prompt, and chosen recipe.

## Prompt Shape

Use concrete renderable instructions.

**Canvas and landscape field**
- State ratio, horizon or valley structure, openness, and dominant field.

**Scene structure**
- State where the flowers, clouds, trees, paths, buildings, or slope masses sit; include any tiny figure or scale marker.

**Poem placement**
- State where the poem sits, whether it floats, aligns to a path, or is anchored near a figure or horizon.

**Color and atmosphere**
- State the dominant palette, blur, distance, and whether the scene is printed, painted, or slightly surreal.

**Mood and avoids**
- State the emotional register and hard constraints.

## Reference

Read [references/structure.md](references/structure.md) for reverse-engineered landscape grammar, poem placement, and prompt recipes.
