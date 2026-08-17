---
name: 随想便签
description: "【随想便签 / random-thoughts-note-zine】 Generate clipped Random Thoughts note-zine prompts and matching raster images. Use when the user gives a mood, season, memory, phrase, photo reference, place, article idea, or short poem and wants a quiet vertical photo poster with a folded paper/photo background, a white receipt-like note clipped near the upper right, metal paperclip or staples, RANDOM THOUGHTS title, Chinese handwritten paragraphs, dashed separator, RECORD signature, soft shadows, and casual journal stationery aesthetics."
---

# Random Thoughts Note Zine

Turn the user's content into both:

1. a final image-generation prompt, and
2. a generated raster image made from that prompt.

## Source Grammar

Use this visual identity:

- vertical 3:5 or 4:5 phone poster, like a photographed folded sheet or printed photo page
- quiet background photo: trees, blue sky, clouds, tiled architecture, empty field, asphalt road markings, dusk silhouettes, soft landscape, or minimal wall
- subtle paper-fold cross: one vertical crease near center and one horizontal crease around the lower third or middle
- a metal paperclip near the upper left, sometimes clipped to the page edge
- a white narrow receipt/card note pinned near the upper right or right-center
- note has lightly serrated top/bottom edge, tiny metal staples or slanted clip marks at the top
- note header: `RANDOM THOUGHTS` in black condensed sans, all caps
- body: short Chinese handwritten lines, sparse paragraph blocks, imperfect ink, diary-like rhythm
- footer: dashed line plus `RECORD ' 季候风` or a similar short record/signature mark
- color: clean white note, black ink, pale blue/grey/lavender sky, green trees, beige tile, asphalt black, soft pastel clouds
- mood: quiet seasonal wind, casual record, light nostalgia, overheard thought, everyday poetic stationery

The result should feel like a mobile photo collage or printed paper note taped into a visual diary, not a clean UI card and not a commercial quote poster.

## Mode Policy

Use **Standard Mode** for all generation. Use the Standard Mode Prompt Compiler below to convert the user's content into compact, imageable prompts.

Use prompt-only output only when the user explicitly asks for prompt-only.

## Standard Mode Prompt Compiler

Default generation should compile only visible image instructions.

### First-Principles Fields

Every prompt must answer these rendering questions in this order:

1. **Canvas:** What is the frame?
   - tall vertical 3:5 or 4:5 phone-poster; photographed paper/photo surface; no mockup, no UI, no device frame.

2. **Background Photo:** What everyday scene sits behind the note?
   - choose one: leafy trees against blue-grey sky, tiled building facade, empty field under pale sky, asphalt road markings and shadows, dusk tree silhouette, pastel cloud wall, soft campus walkway, distant shrubs, or minimal horizon.

3. **Folded Surface:** How does the paper/photo page behave?
   - visible fold creases: a vertical center fold and one horizontal fold; slight page texture, soft blur, low-contrast print grain, gentle uneven exposure.

4. **Clipped Note Anchor:** What is the main object?
   - a narrow white receipt-like note card in the upper-right/right-center, occupying about 18%-30% of the canvas height; subtle paper shadow; serrated or torn receipt edges.

5. **Fasteners:** What holds the note?
   - two tiny diagonal staples or clip marks near the top of the note, plus optional metal paperclip hanging near the upper-left page edge. Use realistic metal, not decorative icons.

6. **Typography System:** What text appears?
   - note title must be `RANDOM THOUGHTS` in black uppercase condensed sans. Body should be 3-7 short Chinese handwritten lines or compact paragraph blocks. Bottom has a dashed separator and `RECORD ' 季候风` or user-supplied signature.

7. **Text Accuracy Policy:** How to handle image-model text limitations?
   - keep body text short and handwritten-looking. If the user supplies exact text, include it but warn only in final if generated text may not be perfectly legible. Do not ask unless exact wording is mission-critical.

8. **Color Logic:** What palette carries the mood?
   - pale blue, sky grey, lavender, soft green, beige tile, asphalt black, white note, black ink, occasional yellow/blue road stripe. Keep saturation natural and slightly faded.

9. **Reproduction Texture:** What makes it tactile?
   - phone-photo softness, paper fibers, fold lines, receipt-paper edge, mild shadow, print grain, slight chromatic softness, no hard studio light.

10. **Emotional Temperature:** What should the viewer feel first?
   - quiet, airy, everyday, seasonal, diary-like, gentle, casual, slightly nostalgic, private thought record.

11. **Hard Avoids:** What must not appear?
   - app UI, digital sticky note, clean vector card, product ad, poster headline hierarchy, dense scrapbook, cute stickers, glossy mockup, 3D render, neon, overly perfect text layout.

### Standard Prompt Shape

Write the final Standard Mode prompt as four compact paragraphs:

1. canvas + folded photo/paper background + scene choice
2. note placement + note material + paperclip/staples
3. title/body/footer typography + color and texture
4. mood + text constraints + avoid-list

Describe the final image, not the reference images or this skill.

## Variation Engine

Before writing the prompt, choose one option from each axis. Vary background and note placement, not only text.

### Layout Family

- **tree-note-right:** leafy trees under blue-grey sky, note clipped in upper right
- **tile-cloud-note:** beige tiled architecture with sky/clouds, note above the diagonal building edge
- **field-empty-note:** huge pale sky and low green field, note floating in upper right
- **asphalt-shadow-note:** road surface, painted stripes, hard shadows, note on the right
- **dusk-silhouette-note:** dark tree silhouette and purple/pink sky, note high right
- **pastel-cloud-note:** soft lavender-blue cloud field, note isolated in the upper right
- **minimal-horizon-note:** mostly blank folded sky page with a tiny horizon strip below
- **contact-sheet-memory:** several note-photo variants arranged on a fuzzy or paper background, only when the user asks for a collection/contact sheet

### Background Scene

- windy green tree canopy
- blue sky with low clouds
- white tile building facade
- empty field and shrubs
- asphalt with blue and yellow painted lines
- dark dusk tree silhouette
- pale lavender cloud wall
- distant campus architecture
- folded sky paper with tiny landscape
- soft road shadow geometry

### Note Shape

- tall narrow receipt with serrated top and bottom
- clean white card with torn bottom edge
- slightly curled thermal-paper strip
- narrow memo sheet with subtle deckled edge
- long rectangle pinned near top right
- small receipt floating over the scene
- right-center note overlapping background geometry

### Fastener Mode

- paperclip near upper-left page edge, no clip on note
- two diagonal staples at note top
- four small slanted staple marks at note corners
- paperclip plus two note staples
- tiny silver pins near note top edge
- minimal fasteners, only two black clip marks

### Text Mode

- title plus four short Chinese handwritten paragraphs
- title plus sparse single-line Chinese thoughts
- title plus exact user-supplied Chinese text
- title plus short bilingual footer only
- title, body, dashed line, `RECORD ' 季候风`
- almost blank note with only two handwritten lines
- denser handwritten record, but still airy

### Palette Mode

- pale blue sky, green trees, white note, black ink
- deep blue sky, cream tile, white note, graphite shadows
- light sky blue, beige ground, soft green horizon
- asphalt black, cyan stripe, pale yellow stripe, white note
- lavender dusk, black trees, white note, pink cloud edge
- powder blue and pale pink clouds, white note, black ink
- cool grey paper, blue fold shadow, fresh green tree blur

## Workflow

1. Parse the user's content.
   - Identify the mood, season, place, and any exact note text.
   - If no note text is supplied, invent short Chinese handwritten diary lines around the theme.
   - Keep invented text short: 3-7 lines or 3-5 compact paragraph blocks.

2. Select a variation recipe.
   - Choose layout, background scene, note shape, fastener mode, text mode, and palette from the Variation Engine.
   - Use contact-sheet-memory only if the user asks for a set, moodboard, or collection.

3. Write the final image prompt.
   - Use the Standard Prompt Shape.
   - Specify exact title `RANDOM THOUGHTS`, note position, paperclip position, fold creases, and footer treatment.
   - If exact text is supplied, include it; otherwise provide suggested Chinese body text in the prompt.
   - Keep the background photographic and the note tactile.

4. Generate the image.
   - Use the available image generation capability by default.
   - Do not stop after prompt-only unless the user asks for prompt-only.
   - If the result becomes a clean quote poster, UI card, or sticker scrapbook, tighten the prompt and regenerate once with stronger `photographed folded paper`, `white receipt note`, `paperclip`, `staples`, and `phone-photo background` wording.

5. Return the image and prompt.

## Negative Constraints

Always avoid:

- app UI, notes app screenshot, phone screenshot, device frame
- digital sticky note, vector card, clean Figma mockup
- commercial quote poster, marketing headline, logo, CTA, brand layout
- dense scrapbook, stickers, washi tape clutter, cute journaling decoration
- glossy mockup, 3D paper render, hard studio shadow
- neon, cyberpunk, high-chroma gradient, luxury editorial drama
- anime, cartoon, illustration-heavy style
- perfectly typeset long Chinese paragraphs
- unreadably tiny note or note centered like a formal poster
- missing paperclip, missing note, or missing `RANDOM THOUGHTS` title

## Output Format

````markdown
**生成图**

![Random Thoughts Note Zine style poster](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Mode: Standard
- Recipe: [layout / background / note shape / fastener / text / palette]
- [one short note about the content interpretation]
````

If generated images render directly without a file path, show the image normally and still include the final prompt.

## Quality Gate

Before finalizing, check:

- Did the run use the Standard Mode Prompt Compiler?
- Did the run choose a recipe across layout, background, note shape, fastener, text, and palette?
- Is the image a vertical photographed paper/photo poster?
- Is a folded page or folded photo surface visible?
- Is there a white receipt-like note near the upper-right or right-center?
- Does the note include `RANDOM THOUGHTS`?
- Is there handwritten Chinese body text or the user-supplied text?
- Is there a dashed separator plus record/signature footer?
- Is a metal paperclip and/or note staples visible?
- Does the background feel like an everyday photo, not a clean vector backdrop?
- Did the prompt avoid UI, commercial quote poster, dense scrapbook, glossy mockup, neon, cartoon, 3D, and text-heavy layout?
- Did you actually generate the image?

## Example Requests

- "用 $random-thoughts-note-zine 做一张关于夏天云层的随机思绪便签图"
- "Use $random-thoughts-note-zine to make a quiet note poster about a campus afternoon."
- "用这张天空照片做一张 RANDOM THOUGHTS 便签 zine"
- "Use $random-thoughts-note-zine prompt-only with exact Chinese note text."
