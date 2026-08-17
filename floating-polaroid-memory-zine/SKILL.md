---
name: 悬浮拍立得记忆
description: "【悬浮拍立得记忆 / floating-polaroid-memory-zine】 Generate centered floating-polaroid memory zine prompts and matching raster images from a user photo, landscape, garden, sky, travel snapshot, or visual brief. Use when the user wants a single instant-photo-style frame, thick white border, softly blurred matching background, dreamy pastel or muted color wash, gentle vignette, and a small polished memory-object look inspired by gc-minimal-zine-poster-v0-1 but simplified into one floating image card."
---

# Floating Polaroid Memory Zine

## Overview

Turn the source into one centered instant-photo card floating over a blurred, color-matched field. The effect should feel like a preserved snapshot lifted out of its environment: crisp inner photo, soft outer echo, white border, and a calm memory mood.

## Core Rules

- Use one main photo card, usually centered.
- Keep the border thick, white, and clearly rectangular.
- Repeat the photo colors into the background as a soft blur or glow.
- Keep the background large and quiet.
- Use gentle pastel, misty, or muted tones.
- Avoid collage clutter, multiple cards, or heavy text.
- Keep the result flat and photographed, not like a digital mockup.

## Workflow

1. Read the source.
   - If a photo is supplied, preserve its main subject and color mood.
   - If only text is supplied, choose one memory-like subject: sky, tree, flower, field, street, water, or a small personal scene.

2. Choose one floating-card recipe.
   - `single-center-card` for most inputs.
   - `soft-bloom-background` for flowers, trees, or bright color fields.
   - `misty-landscape-card` for sky, fields, and distant scenery.
   - `night-glow-card` for dusk, blue hour, or city-light scenes.

3. Compile a prompt in four paragraphs.
   - Canvas and background.
   - Floating card and image crop.
   - Blur, glow, and border treatment.
   - Mood and avoids.

4. Generate the image.
   - Keep the card legible as a real printed instant photo.
   - If the background gets too detailed, blur it harder.
   - If the card disappears, increase border contrast and inner image sharpness.

5. Return the image, final prompt, and chosen recipe.

## Prompt Shape

Use short, imageable instructions.

**Canvas and background**
- State ratio, overall mood, and the blurred background field.

**Floating card**
- State the card size, placement, border thickness, and source crop.

**Blur and glow**
- State how the card color echoes into the backdrop, plus any soft haze or vignette.

**Mood and avoids**
- State the emotional register and the hard no list.

## Reference

Read [references/structure.md](references/structure.md) for the reverse-engineered card geometry, color behavior, and recipe families.
