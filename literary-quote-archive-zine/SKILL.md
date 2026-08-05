---
name: 文学语录
description: Generate prompts and finished raster images for quiet literary quote archive posters with aged cream paper, editorial serif typography, italic outline keywords, short highlighted quote lines, numbered metadata, torn photographic or illustrated collage anchors, and one restrained accent color. Use when the user provides a quote, poem fragment, author, book, sentence, theme, or reference image and wants a typographic zine poster rather than a generic social quote card.
---

# Literary Quote Archive Zine

Turn the user's quote, phrase, or theme into both a final image-generation prompt and a finished raster poster. The default artifact is a tall 3:5 editorial sheet on warm aged paper: large author/title typography and a short quote occupy the upper-left, while one restrained torn-paper image or abstract material anchor grows from the lower-right with generous empty paper around it.

This Skill reverse-engineers the visual prompt logic of `gc-minimal-zine-poster-v0-1` and fuses it with the supplied literary-poster references. It preserves the source Skill's vertical paper canvas, attention geometry, negative space, one high-chroma anchor, sparse microtext, and scanned print defects, while elevating typography into the main compositional object.

## Mode Policy

Use **Quote Archive Mode** by default. Use **Word / Image Mode** when the user supplies only a theme or a single word and wants the text-image relationship to carry the poster.

- **Quote Archive Mode:** author, title, short quote, attribution, one image/material anchor.
- **Word / Image Mode:** one oversized keyword, one short supporting line, and one lower-page visual study.

Do not create a social-media quote card, a dense book cover, or a fully illustrated scene.

## Prompt Compiler

Write the final prompt as five compact paragraphs in this order.

### 1. Canvas and quiet field

State:

- tall vertical 3:5 or 2:3 paper poster
- full-frame warm ivory, parchment, or faded cream paper
- 65%-85% calm paper field with subtle fibers, stains, and soft scan variation
- no border, device mockup, drop shadow, or UI card
- lower-right or lower-center image cluster occupying 15%-30% of the canvas

The paper should feel tactile and slightly aged, not beige wallpaper or a clean digital background.

### 2. Editorial header system

Use a compact archive header in the upper-left and upper-right:

- colored square index label such as `01`, `02`, or a user-supplied sequence number
- tiny uppercase section label such as `LITERARY NOTES`, `SELECTED WORDS`, or `ARCHIVE EDITION`
- large black or deep navy author surname/name in an elegant high-contrast serif
- large italic outline title or keyword overlapping slightly below the author
- tiny location, book, year, or edition line aligned to the title

Use only exact user-supplied names and text when correctness matters. If the user gives no author, invent no real author attribution.

### 3. Quote hierarchy

Place a short quote block in the upper-left or left-middle, aligned to a generous column:

- 3-7 short lines in dark italic serif or literary roman type
- oversized quotation mark in the one accent color
- highlight only the final clause or one key phrase in the accent color
- a thin horizontal rule and tiny attribution line beneath
- preserve visible line breaks when supplied by the user

Keep the quote visually legible and short. For long text, select one central sentence rather than requesting a full paragraph of perfect text from the image model.

### 4. Lower image and material anchor

Choose one lower-page anchor:

- torn monochrome photograph of a gate, wall, desert, mountain, room, tree, road, or landscape
- archival botanical specimen, leaf, branch, flower, or translucent fabric
- geometric color field with halftone and paper tear
- photocopied building, chair, window, cloud, or landscape fragment
- a small object specimen partially covered by torn paper

The image should emerge from the lower-right or lower-center and remain subordinate to the text. Use torn edges, halftone, photocopy softness, low-contrast grayscale, and overlapping paper scraps. Do not make a full-bleed realistic scene.

### 5. Accent, footer, and avoid-list

Choose one accent hue: rust red, cobalt blue, burnt orange, muted violet, mustard yellow, or leaf green. Keep paper and supporting image neutral. Use the accent in the index block, quote mark, highlighted phrase, outline keyword, or one image detail; do not use every accent placement at once.

Add tiny footer metadata: `SELECTED WORDS`, edition number, page number, or a small rule and corner mark. End with the relevant negative constraints.

## Typography System

### Author Display

- large uppercase or title-case high-contrast serif
- black, deep navy, or charcoal
- top-left with generous breathing room
- no celebrity-style portrait or logo treatment

### Outline Keyword

- large italic serif outline, 1-2 words
- accent color or hairline version of the author color
- can drift behind or under the quote block
- should be partially cropped only when the word remains readable

### Quote Text

- literary italic serif or restrained old-style serif
- dark ink, 3-7 lines, short line length
- accent only on one final clause or key word
- quote mark large but simple

### Archive Microtype

- narrow grotesk or monospaced uppercase
- 6-12 words maximum per line
- top-right and footer only
- low contrast and never the primary focus

## Layout Families

- `left-quote-lower-photo`: classic reference layout with text upper-left and torn image lower-right
- `oversized-word-archive`: giant outline keyword crosses the middle and touches the visual anchor
- `paper-window-quote`: small image window appears behind or beside the quote with large cream margins
- `diagonal-material-study`: lower collage rises diagonally through translucent paper and geometry
- `quiet-object-page`: quote and author sit high while one isolated object anchors the bottom
- `sequence-card`: repeated page number, index block, and stable type system for a quote series

## Color Engine

Use one accent per poster. Suggested pairings:

- rust red + old courtyard, autumn leaves, stone, or memory
- cobalt blue + bird, sky, egg, ocean, or awakening
- burnt orange + desert, sunlight, fire, or summer
- muted violet + room, solitude, night, or interior thought
- mustard yellow + age, gold, desire, or warmth
- leaf green + field, aloneness, garden, or renewal

The accent should occupy roughly 0.8%-2.5% of the canvas or 15%-35% of the active collage cluster, remain opaque, and be visible at thumbnail size. Never reduce it to a barely visible dot unless the user explicitly asks for near-monochrome.

## Minimal Zine Prompt Bridge

### Preserve from the source Skill

- vertical 3:5 paper poster
- 70%-90% quiet paper field
- one visual anchor and restrained attention geometry
- one high-chroma accent with subdued grayscale support
- short sparse text and small archive details
- flat scan, paper fibers, xerox softness, halftone, ink bleed, and slight misregistration
- poetic, archival, diary-like editorial temperature

### Adapt for literary posters

- tiny visual cluster becomes a lower-page torn image/material anchor
- one object label becomes author/title/quote hierarchy
- color anchor appears in a quote mark, highlighted clause, index box, and/or image detail
- microtext becomes edition, sequence, attribution, and footer metadata
- the quote is the main visual subject; imagery is its material counterweight

### Do not import

- sample author names, exact quotes, page numbers, or source-specific slogans
- long explanations about the style inside the image prompt
- clean commercial book-cover hierarchy, glossy magazine typography, or a social quote-card frame

## Workflow

1. Parse the content.
   - Identify exact quote, author, title, language, tone, keyword, and visual metaphor.
   - If no quote is supplied, create a short original line or ask the user for one; do not attribute it to a real author.

2. Select a layout and anchor.
   - Choose one layout family, one accent hue, one image/material anchor, and one texture recipe.
   - Keep the lower collage small enough to preserve paper dominance.

3. Compile the prompt.
   - State page geometry, header hierarchy, quote line breaks, anchor treatment, accent behavior, and footer metadata.
   - Use exact text only when supplied. Keep generated text short.

4. Generate the image.
   - Use the built-in image generation capability by default.
   - If unavailable, run `scripts/server_image_gen.py` with the final prompt.

5. Inspect and regenerate once when needed.
   - Regenerate if author/quote hierarchy collapses, paper disappears, the anchor becomes full bleed, the accent color spreads, or the result looks like a social quote card.
   - For exact typography, preserve the image as a visual draft and typeset final copy separately when necessary.

6. Return the image, prompt, copy deck, and selected recipe.

## Text Policy

- Treat user-supplied text as verbatim content and preserve punctuation and line breaks in the prompt.
- Do not invent attribution to real writers.
- Do not copy any quote, author, title, or watermark from the reference images unless the user explicitly supplies it.
- If the image model distorts long text, report that the visual layout is generated but exact typography may require later typesetting.

## Reference Image Policy

- Extract page ratio, header position, type scale, quote column, oversized outline word, lower collage placement, paper texture, accent color, and footer logic.
- Use the reference set as a design system, not as a source of exact text or imagery.
- Do not reproduce visible names, quotes, signatures, sequence numbers, or page labels from the references.
- Do not infer authorship or copyright status from a reference.

## Negative Constraints

Always avoid:

- social media quote card, motivational template, corporate presentation, or generic book cover
- full-bleed photography, glossy magazine spread, or busy scrapbook
- long pseudo-readable text, invented real-author attribution, copied quotes, logos, watermarks, and signatures
- too many fonts, decorative borders, stickers, tape, ribbons, and unrelated objects
- multiple competing accent colors, neon, HDR, purple cinematic grading, teal-orange grading, CGI, 3D, and hard shadows
- perfectly clean digital white, plastic texture, stock-photo staging, and commercial ad hierarchy

## Fallback Script

The fallback reads the OpenAI-compatible provider from Codex configuration or environment variables and never stores credentials in the Skill.

```bash
python3 scripts/server_image_gen.py \
  --prompt-file /absolute/path/to/prompt.txt \
  --out output/imagegen/literary-quote-archive-zine-output.png
```

Use `--dry-run` to inspect the request without sending it. The default is the Images API; use `--wire-api responses` only for a compatible Responses image-generation endpoint.

## Output Format

````markdown
**生成图**

![Literary Quote Archive Zine](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**文案结构**

- Author: [exact author or original/no attribution]
- Quote: [short quote]
- Layout: [layout family]
- Accent: [one hue]
````

## Quality Gate

Before finalizing, check:

- Is the canvas a tall aged-paper editorial poster?
- Does 65%-85% of the page remain calm paper or quiet negative space?
- Is the author/title/quote hierarchy readable and intentional?
- Is the quote short enough for image generation?
- Is there one lower-page image or material anchor rather than a full scene?
- Is only one high-chroma accent used?
- Are the header and footer microtype subordinate?
- Does the result avoid social-card, book-cover, advertising, scrapbook, and glossy digital aesthetics?
- Were reference names, quotes, signatures, and watermarks excluded unless supplied?
- Was the raster image actually generated?

## Example Requests

- `用 $literary-quote-archive-zine 做一张关于“抵达”的文学语录海报`
- `参考这些图的米白纸张、红色强调字和下方撕纸照片，生成一句原创短诗海报`
- `把“云走得很慢，像在等待一座山想起自己。”做成文学档案海报，不要署名`
