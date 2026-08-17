---
name: 大地墨诗
description: "【大地墨诗 / earth-ink-poem-poster】 Generate weathered calligraphy poetry poster prompts and matching raster images from a Chinese poem, poem fragment, literary phrase, reference image, or visual brief. Use when the user wants aged paper, large handwritten or brush-like Chinese characters, earthy black/sepia/burnt-orange ink, underlines, microtext side columns, grid or stain textures, torn-paper or framed inset panels, and a quiet editorial poem layout inspired by gc-minimal-zine-poster-v0-1."
---

# Earth Ink Poem Poster

## Overview

Turn a poem or literary phrase into a weathered poster with a strong calligraphic mass, quiet paper field, and supporting editorial details. The image should feel handmade and archival, not like a clean commercial flyer.

## Core Rules

- Keep the paper surface dominant.
- Use one main calligraphic or brush-like text mass.
- Add small supporting lines, side text, or microcopy only when they help structure the page.
- Favor earthy ink tones: black, charcoal, umber, sepia, burnt orange, faded ochre.
- Use one accent block or label at most.
- Keep the layout flat, printed, and aged.
- If a reference image is supplied, preserve its imbalance, panel logic, or text/image tension.

## Workflow

1. Read the source.
   - If a poem is supplied, select the strongest line or phrase as the main anchor.
   - If the text is long, extract one central line and one supporting fragment.
   - If only a mood is supplied, invent a short Chinese phrase with a strong visual noun or verb.

2. Choose a layout family.
   - `hero-calligraphy` for one dominant handwritten block and quiet support text.
   - `framed-inset` for a central image or texture window with text around it.
   - `left-ink-right-column` for black or sepia mass on one side and microtext on the other.
   - `split-board` for poster-board or gallery-sheet layouts with multiple editorial zones.
   - `stained-paper-center` for a large paper field with a stained or weathered text cluster in the middle.

3. Compile the prompt in five paragraphs.
   - Canvas and paper field.
   - Primary calligraphic mass or inset panel.
   - Supporting text and accent structure.
   - Texture, paper wear, and print defects.
   - Mood and avoids.

4. Generate the image.
   - Prefer built-in image generation for raster output.
   - If exact glyph fidelity matters more than atmosphere, use a deterministic layout instead of depending on stylized lettering.
   - If the composition becomes too clean, increase paper wear, ink bleed, and misregistration.

5. Return the image, final prompt, and chosen recipe.

## Prompt Shape

Use concrete renderable instructions.

**Canvas and paper**
- State ratio, paper tone, age, and how much empty field remains.

**Primary text mass**
- State the main phrase, whether it is calligraphic or printed, and where it sits.

**Support structure**
- State underline, side column, microtext, label block, inset window, or frame behavior.

**Texture and defects**
- State paper folds, stains, xerox dust, smudge, grid, torn edge, or ink bleed.

**Mood and avoids**
- State the literary mood and the hard no list.

## Reference

Read [references/structure.md](references/structure.md) for reverse-engineered layout grammar, text hierarchy, and prompt recipes.
