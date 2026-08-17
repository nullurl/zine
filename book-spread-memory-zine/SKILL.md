---
name: 摊书记忆页
description: "【摊书记忆页 / book-spread-memory-zine】 Generate open-book memory spread zine prompts and matching raster images from a user photo, photo set, handwritten page, journal spread, book-flatlay reference, poem, or visual brief. Use when the user wants a top-down open notebook or sketchbook spread, two-page collage layout, handwritten Chinese or poetic text on one page, framed photo blocks on facing pages, visible book spine, aged paper, and textured documentary or diary-like composition inspired by gc-minimal-zine-poster-v0-1."
---

# Book Spread Memory Zine

## Overview

Turn the reference into a photographed open-book spread. The result should feel like a real book or sketchbook laid flat on a textured surface, with one page carrying image fragments and the facing page carrying handwriting, captions, or quieter supporting images.

## Core Rules

- Keep the book readable as a book. Show the spine, page edges, and page thickness.
- Use a top-down or near top-down view.
- Make the page roles deliberate: image page, text page, or balanced two-page spread.
- Keep the background physical: stone, leather, asphalt, concrete, wood, or other rough surface.
- Use warm paper, soft shadows, and mild aging.
- Keep handwriting small, intimate, and imperfect.
- Preserve the sparse discipline of gc-minimal-zine-poster-v0-1, but shift the composition into a spread, not a poster.

## Workflow

1. Read the source.
   - If the user supplies a photo, preserve its core subject and photo mood.
   - If the user supplies text only, choose a book-like memory subject: portrait, landscape, meal, flower, travel view, or personal note.

2. Choose a spread structure.
   - Prefer `image-left/text-right` for reflective or essay-like subjects.
   - Prefer `text-left/image-right` for portrait or cinematic subjects.
   - Prefer `paired-pages` when the material has two equally strong fragments.
   - Prefer `central-essay` when a single quote or image should sit inside a large quiet spread.

3. Compile the prompt in four paragraphs.
   - Canvas and book state.
   - Page structure and image placement.
   - Handwriting, captions, and marks.
   - Mood and avoids.

4. Generate the image.
   - Keep the layout flat and photographed, not like a digital mockup.
   - If the text page becomes too dense, reduce the amount of writing.
   - If the book disappears into the background, strengthen page edges and spine contrast.

5. Return the image, final prompt, and the chosen spread recipe.

## Prompt Shape

Use short, imageable instructions.

**Canvas and book state**
- State ratio, camera angle, book type, page tone, and surface material.

**Page structure**
- State which page carries photos, which carries text, how many frames or scraps appear, and how the spine divides the spread.

**Handwriting and marks**
- State handwriting style, caption length, tiny labels, tape, circles, or faint rules.

**Mood and avoids**
- State the emotional register and the hard no list.

## Reference

Read [references/structure.md](references/structure.md) for the reverse-engineered spread grammar, surface types, and recipe families.
