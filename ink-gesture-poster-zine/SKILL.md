---
name: 水墨笔势
description: Generate prompts and finished raster images for abstract ink gesture posters, brush-swish studies, minimal paper-space compositions, and accent-dot editorial sheets. Use when the user provides a theme, phrase, feeling, reference image, or abstract brief and wants a tall white-paper poster with one dominant ink gesture, huge negative space, soft scan texture, and a single restrained accent color.
---

# Ink Gesture Poster Zine

Turn the user's theme, phrase, or reference image into:

1. a final image-generation prompt, and
2. a finished raster image with abstract ink-gesture poster grammar.

Fuse Minimal Zine restraint with one expressive ink motion: a swirl, pull, loop, fall, or vertical stroke suspended in a quiet paper field.

## Reference Routing

- Treat supplied images as visual-grammar references unless the user explicitly asks for literal editing.
- Inspect references locally. Extract paper tone, gesture shape, line weight, empty-space ratio, accent color, blur level, and whether the image reads as one central gesture or several fragments.
- Do not copy signatures, watermarks, copied text, or identifiable marks from the reference unless the user explicitly supplies them as content to preserve.
- Read [references/style-grammar.md](references/style-grammar.md) when reverse-engineering the gesture language or correcting drift.
- Read [references/prompt-recipes.md](references/prompt-recipes.md) when choosing a gesture family, accent strategy, or text policy.

## Core Identity

Preserve these signals:

- tall vertical white, cool white, or very pale paper field
- one dominant abstract ink gesture, usually centered or slightly off-center
- lots of empty space around the gesture
- black, charcoal, or soft gray brush motion with watery absorption
- occasional thin orbit lines, arcs, drips, or trailing filaments
- one restrained accent such as red, cobalt, gold, or pale blue
- soft scan grain, paper tooth, feathered edges, and slight bleed
- contemporary minimalist editorial mood, not a full traditional ink painting

## Minimal Zine Fusion

Carry forward from `gc-minimal-zine-poster-v0-1`:

- huge negative space
- one clear visual anchor
- old-paper or scanned-paper texture
- sparse composition
- one accent that stays visible at thumbnail size
- quiet, poetic, editorial temperature

Shift the grammar:

- replace the tiny anchor with one larger ink gesture
- allow the ink to feel like motion or breath, not a scene
- keep typography optional and small
- let the empty paper do as much work as the mark

## Gesture Engine

Choose one family before compiling:

- `central-swirl`: one vertical or diagonal ink swirl with a loose halo.
- `orbit-loop`: thin arcs and looping filaments surrounding a dark ink core.
- `vertical-thread`: a long descending gesture with trailing strands and drips.
- `split-stroke`: two related gestures separated by paper space.
- `suspended-splash`: a floating blot with fine tendrils and one accent dot.
- `brush-figure`: an abstract figure-like ink movement without literal anatomy.

Use one family only. Do not combine all six in one image.

## Text Policy

- Default to textless when the composition is stronger without words.
- If the user asks for text, keep it tiny, short, and secondary.
- Never force a theme word into the poster as a headline unless the user explicitly requests display text.
- Do not invent long paragraphs, branding, URLs, dates, or program metadata.

## Color Engine

Choose one palette:

- monochrome paper: black, charcoal, gray, and white only
- red seal: black gesture with one red circle, drop, or stamp
- cobalt drift: black gesture with one faded blue wash or dot
- gold dust: black gesture with one muted gold splash or grain
- pale sky: black gesture with one soft blue-gray bloom

Keep the accent small but decisive. If the accent vanishes, strengthen it instead of adding more colors.

## Prompt Compiler

Write the final prompt as five compact paragraphs:

1. canvas, paper tone, negative-space ratio, and scan/flat-light finish
2. chosen gesture family, scale, placement, and motion behavior
3. texture: ink absorption, feathering, bleed, drips, line softness
4. typography policy, accent color, and any tiny optional text
5. mood and hard avoids: no scene-building, no UI, no glossy mockup, no busy collage

Compile only visible renderable details. Do not mention source paths, reverse-engineering, or analysis in the final prompt.

## Generation

- Generate the image by default; stop at prompt-only only when explicitly requested.
- Prefer the built-in image generation capability.
- When built-in generation is unavailable and server fallback has already been approved, run:

    python3 scripts/server_image_gen.py \
      --prompt-file output/imagegen/<slug>.prompt.txt \
      --out output/imagegen/<slug>.png \
      --size 1024x1536 \
      --quality high

- The fallback reads provider configuration and `OPENAI_API_KEY` from the environment or Codex config, calls the OpenAI-compatible image endpoint, requests `b64_json`, and writes the decoded image locally. Never print or hard-code secrets.
- Store the exact final prompt beside the image. Never overwrite existing outputs; use a new descriptive slug.
- Inspect once. Regenerate with one targeted correction if the gesture disappears, the accent is too weak, the canvas becomes crowded, or the result turns into a scene or logo.

## Hard Avoids

Always avoid:

- full landscape scene, traditional painting tableau, or story illustration
- UI cards, dashboards, app screens, posters made of panels
- dense text blocks, commercial headline hierarchy, CTA, or branding
- scrapbook clutter, stickers, collage piles, or decorative ephemera
- glossy render, hard shadows, neon, or cinematic lighting
- multiple bright accents or rainbow palettes
- tiny mark lost in a huge blank field

## Output Format

Return the generated image, exact final prompt, and:

- Gesture family: selected family
- Accent: chosen color and form
- Text: textless or tiny-copy policy
- one short interpretation note

## Quality Gate

Before finalizing, check:

- Is there one dominant ink gesture?
- Does the page keep generous white space?
- Is the accent small but visible?
- Do the edges feel like ink on paper rather than digital paint?
- Is the composition clearly a poster, not a scene?
- Did you avoid UI, logos, commercial layout, and collage clutter?
- Did you generate and inspect the final raster image?
