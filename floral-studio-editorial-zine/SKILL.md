---
name: 花艺编辑
description: Generate prompts and finished raster images for minimalist floral-studio editorial posters, botanical identity sheets, letterpress plant studies, monogram-led flower pages, and sparse type-driven botanical compositions. Use when the user provides flowers, plants, botanical references, floral branding cues, a reference image, or a short phrase and wants a vertical paper poster with antique type, ghost botanical illustration, cool off-white or sky-blue paper, and a calm Minimal Zine fusion.
---

# Floral Studio Editorial Zine

Turn a flower, plant, botanical reference, or floral identity brief into:

1. a final image-generation prompt, and
2. a finished raster image with floral-studio editorial grammar.

Fuse Minimal Zine restraint with a printed botanical studio sheet: one dominant paper field, one visual anchor, sparse type, and a physical print feel.

## Reference Routing

- Treat supplied images as visual-grammar references unless the user explicitly asks for a literal edit.
- Inspect local references first. Extract canvas ratio, paper tone, text hierarchy, monogram behavior, specimen style, background color, and how much empty field remains.
- Do not copy exact brand names, email addresses, watermarks, or distinctive reference text unless the user explicitly supplies it as content to preserve.
- Read [references/style-grammar.md](references/style-grammar.md) when reverse-engineering the reference look or fixing style drift.
- Read [references/prompt-recipes.md](references/prompt-recipes.md) when choosing a layout family, title treatment, or color approach.

## Core Identity

Preserve these signals:

- tall vertical poster ratio, usually 3:4, 4:5, or 3:5
- one large paper field with generous breathing room
- cool off-white, paper-gray, or dusty sky-blue base
- one main botanical anchor: flower stem, fern, orchid, petal silhouette, butterfly-like mark, or monogram specimen
- typewriter or letterpress type, compact and sparse
- big initials or a short studio title when the image calls for identity design
- soft scanned-paper texture, mild print wear, and flat light
- restrained black, charcoal, or sky-blue ink with one controlled accent
- a handmade editorial mood, not a commercial campaign

## Minimal Zine Fusion

Carry forward:

- large negative space
- one dominant attention route
- old-paper softness and sparse composition
- one clear color or ink anchor
- short readable text
- calm, archival, diary-like tone

Shift the grammar:

- replace scrapbook clutter with a single botanical print or identity sheet
- let the monogram, flower mark, or specimen become the main visual object
- use type as a structural element, not a headline block
- keep the poster physically printed, not glossy or digital UI-like

## Layout Engine

Choose one family before compiling:

- `single-specimen-sheet`: one botanical specimen centered in a quiet field with a small text block.
- `identity-block-poster`: large initials or monogram dominate the upper half, with a floral mark below.
- `blue-field-studio-sheet`: dusty sky-blue background with black botanical illustration and scattered type.
- `ghost-press-page`: pale paper, faint specimen, and a low-contrast press-like title.
- `two-panel-sheet`: one specimen panel and one text-heavy panel, kept sparse and balanced.

Use one family only. Do not mix scrapbook collage, photo grids, vellum overlays, ticket cards, and identity posters in one image.

## Typography System

- Use short title text only: 1-4 words, or a compact monogram.
- If no title is provided, invent a plausible studio label such as `FLORAL STUDIO`, `BOTANIC PRESS`, `NORTH PETAL`, or `FIELD NO. 1`.
- Use one type voice for the main copy and one for tiny supporting lines.
- Keep the text block compact, slightly misregistered, and material rather than polished.
- Do not force long prose, contact details, or brand campaign copy into the image.

## Color Engine

Start with one of these directions:

- cool ivory with charcoal type
- dusty sky blue with black illustration
- paper gray with faded cobalt text
- soft moss paper with black specimen lines
- pale cream with a restrained blue accent

Use one dominant ink or paper hue per image. Keep it controlled; do not drift into rainbow palettes, neon, or fashion-editorial color noise.

## Prompt Compiler

Write the final prompt as five compact paragraphs:

1. canvas, paper tone, margin, and flat-light reproduction
2. layout family, paper hierarchy, and placement of the main botanical anchor
3. title / monogram / tiny supporting text treatment
4. ink color, texture, misregistration, and paper wear
5. mood and hard avoids: no UI, no glossy mockup, no scrapbook overload, no commercial campaign styling

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
- Store the exact final prompt beside the image. Never overwrite an existing output; choose a new descriptive slug.
- Inspect once. Regenerate with one targeted correction if the botanical anchor disappears, the title dominates, the page becomes too dense, or the result turns into a generic poster or UI mockup.

## Hard Avoids

Always avoid:

- glossy mockup or 3D product render
- app UI, dashboard, or website card layout
- dense scrapbook collage, sticker overload, or photo grid clutter
- commercial flower-brand campaign styling
- neon rainbow palette or fashion-editorial drama
- long readable paragraphs, copied email text, watermarks, or signatures
- literal packaging, logo reveal, or sales CTA

## Output Format

Return the generated image, exact final prompt, and:

- Layout: selected family
- Anchor: main botanical or monogram subject
- Palette: paper and ink combination
- Typography: title and tiny-copy treatment
- one short interpretation note

## Quality Gate

Before finalizing, check:

- Is the composition a sparse floral editorial sheet, not a scrapbook?
- Is there one clear botanical anchor or monogram?
- Does the page breathe with visible negative space?
- Is the title short and subordinate?
- Are the paper and ink materials legible as printed matter?
- Is the palette controlled and not overly colorful?
- Did you avoid UI, glossy mockup, ads, and copied reference text?
- Did you generate and inspect the final raster image?
