---
name: 档案卷宗
description: Generate prompts and finished raster images of tactile archival dossiers, evidence folders, field notebooks, experimental manuals, research files, observation sheets, flight plans, bureaucratic forms, and ring-bound paper artifacts. Use when the user wants black-background archive-object photography, aged administrative paper, typed forms, handwritten annotations, stamps, clips, punched holes, document pockets, controlled primary-color inserts, or a fusion of minimal zine design with physical records and institutional ephemera.
---

# Archival Dossier Zine

Turn the user's theme, object, story, research topic, organization, or reference images into both:

1. a final image-generation prompt, and
2. a generated raster image.

The style fuses minimal-zine attention discipline with physical archive objects: folders, forms, ring binders, clips, evidence photos, stamps, handwriting, filing tabs, and aged paper displayed as one designed artifact.

## Reference Routing

- Treat supplied images as visual-grammar or subject references unless the user explicitly asks for a literal edit.
- Analyze local reference images locally. Extract structure, material, typography, color, hardware, wear, and display geometry into the prompt.
- Do not upload private local reference images to an untrusted third-party endpoint. The bundled server fallback is text-only.
- Read `references/style-grammar.md` when reverse-engineering references, diagnosing style drift, or writing a high-fidelity prompt.
- Read `references/prompt-recipes.md` for batches, unusual subjects, paired states, or when the artifact type is unclear.

## Core Identity

Always preserve these signals:

- One physical paper artifact or one tight artifact family shown against a deep neutral black field.
- Large black negative space, usually 50%-78% of the frame.
- Artifact occupies roughly 20%-48% of the frame and remains fully visible with breathing room.
- Straight-on overhead scan or restrained catalog perspective; the object must be inspectable.
- Material construction is visible: kraft board, ivory forms, gray folders, tracing paper, page edges, rings, clips, punched holes, tabs, pockets, strings, or fasteners.
- Information is structured through forms, tables, ruled cells, index labels, dates, page numbers, stamps, typed lines, handwritten notes, and small evidence-photo windows.
- Paper shows believable use: softened corners, oxidation, smudges, faded ink, fold marks, pinholes, rubbed edges, slight warping, and imperfect registration.
- Palette is institutional and restrained: black stage, ivory/kraft/gray paper, black or navy ink, plus one controlled chromatic system.
- Output feels like an actual found document object, not a flat poster pretending to be archival.

## Fusion With Minimal Zine

Carry forward the following minimal-zine principles:

- one dominant attention cluster
- decisive negative space
- sparse hierarchy rather than advertising hierarchy
- small serif, typewriter, monospaced, or administrative sans text
- matte scan texture and old reproduction defects
- one unmistakable high-chroma anchor visible at thumbnail size
- quiet, distant, research-like emotional temperature

Change the original minimal-zine geometry:

- Use black negative space outside the artifact rather than 70%-90% empty paper inside a poster.
- Let the document object carry many small internal layers while keeping the overall frame simple.
- Allow forms, tables, and paper stacks, but organize them into one coherent file system.
- Avoid a tiny floating symbol with no physical construction; hardware and document logic must be legible.

## Artifact State Engine

Choose one state before writing the prompt:

- **closed-file:** one closed binder, folder, notebook, or manual cover; restrained labels and hardware.
- **open-dossier:** an open folder or binder spread with pockets, forms, inserts, and fasteners.
- **single-record-sheet:** one vertical institutional form with a photo, table, stamps, and marginal notes.
- **ring-bound-log:** stacked cards or pages held by rings, prongs, clips, or wire loops.
- **paired-state-study:** closed and open views of the same artifact, separated by generous black space.
- **chromatic-experiment-file:** dense editorial paperwork with one vivid cyan, yellow, pink, blue, or orange insert system.

Do not default to `open-dossier` every time. Vary state, camera angle, paper tone, hardware, and chromatic system between outputs.

## Prompt Compiler

Write the final prompt in six compact paragraphs, in this order:

1. **Frame and stage**
   - vertical or square frame; pure or near-black seamless field; large negative space; artifact scale and position.

2. **Artifact and state**
   - exact folder, binder, notebook, form, report, or record; closed/open/paired state; camera geometry; physical dimensions and silhouette.

3. **Construction and layers**
   - board, paper, pockets, tracing sheets, inserts, photos, tables, rings, clips, tabs, strings, holes, and edge wear.

4. **Information system**
   - type hierarchy, exact short labels, dates, numbering, stamps, handwriting, ruled cells, diagrams, and photo captions.

5. **Color and reproduction**
   - paper tones, ink colors, one chromatic system, metal finish, diffuse catalog light, film/scan defects, and material aging.

6. **Avoid list**
   - explicit constraints against glossy product mockups, floating UI cards, clean stationery ads, random scrapbook clutter, long perfect text, and dramatic cinematic lighting.

## Information Rules

- Use only 1-4 exact readable labels. Keep them short.
- Let secondary text become plausible microtype, typewriter texture, ruled cells, or partial handwriting rather than long readable prose.
- Use dates, accession codes, page numbers, stamps, classification marks, or coordinates to create document logic.
- Use diagrams that fit the subject: equipment profile, cloud sketch, route plan, specimen outline, object elevation, material test, or index grid.
- Never reproduce sensitive personal information, real classified data, real credentials, or deceptive official records.

## Color Engine

Choose one system:

- **institutional-neutral:** ivory, warm kraft, gray board, black ink, faded red stamp.
- **navy-index:** cool gray folder, ivory insert, navy rules, one orange or blue filing tab.
- **primary-experiment:** kraft/ivory base with one saturated cyan, lemon yellow, vermilion, or magenta insert family.
- **pastel-manual:** restrained blush, powder blue, cream, and gray, anchored by black hardware.
- **sepia-record:** oxidized cream paper, brown-black type, graphite handwriting, faded red accession marks.

For normal outputs, one high-chroma color should occupy about 1%-6% of the whole frame or 10%-30% of the artifact. In `chromatic-experiment-file`, allow 12%-28% of the artifact to use the chosen color while keeping the black stage dominant.

## Color Trend Enhancement

Use this only when the user asks for brighter color, richer color, preserved source color, a named palette mood, or when the draft would otherwise become too gray, beige, dark, or flat. Preserve this skill's layout grammar first; color is an enhancement layer, not a replacement for structure.

Pick one dominant palette and optionally one small adjacent accent. Assign colors to visible roles such as paper field, photo grade, ink, label, material, shadow, highlight, or motion accent. Do not combine more than two palettes unless the user explicitly asks for chaotic or maximal color.

- forest green: #92AD76, #B6CCAA, #E3EBDD, #71906A, #435F45. Use for botanical, tropical, moss, spring, garden, healing, or green-reverie briefs.
- purple luxury: #7B5FA4, #A487C6, #D8C9EE, #9A8AB6, #5B376D. Use for dreamy, ritual, night floral, velvet, memory, or quiet-luxury briefs.
- vintage mocha: #885949, #C87949, #E6BC8C, #D9D2C8, #203A35. Use for cafe, archive, editorial, old-photo, paper, or warm city briefs.
- earth warm brown: #A5673D, #C89A6B, #E8D6C3, #7B5A42, #3D2C22. Use for handmade, soil, leather, textile, relic, desert, or autumn briefs.
- deep sea blue: #0F2E48, #1E4F73, #5C87B2, #AFC5DA, #E6F0F8. Use for ocean, rain, night water, cloud-sea, distance, or cinematic calm.
- mist blue gray: #9FB0C3, #C9D3DF, #EEF2F6, #75879A, #31485D. Use for rain, fog, glass, winter, quiet architecture, or analytical moods.
- sunset orange: #FF9A42, #FFC185, #FFE9D3, #C66A31, #7B3D1E. Use for warm light, cafe lamps, islands, evening, energy, or celebratory accents.
- cream soft pink: #F6D7DE, #FBE9EE, #FFF7F8, #E9C6D1, #C39BAA. Use for bright journaling, tender memory, blossoms, soft albums, or feminine notes.
- sea-salt blue: #A8D8EA, #D8EDF5, #F8FCFD, #7FB8CF, #5A8097. Use for airy coastal, island, pool, travel, summer, or brighter-water requests.
- desert elegant white: #F7F4EE, #E7DED1, #D1C6B8, #A99F91, #736F66. Use as a clean bright base when the image needs lift without saturation.

When brightening a dark output, increase paper/background luminance with desert elegant white, sea-salt blue, or cream soft pink before increasing saturation. When preserving a reference image, keep its main hues first, then harmonize them with the closest palette above.

## Generation

- Use built-in image generation by default and do not stop at prompt-only unless explicitly requested.
- When built-in image generation is unavailable and server fallback has already been approved, use `scripts/server_image_gen.py` with the final prompt.
- The fallback reads provider configuration and `OPENAI_API_KEY` from the environment or Codex config, calls `/images/generations`, requests `b64_json`, and writes the image locally. Never hard-code secrets.
- Use a tall output such as `1024x1536` for single sheets, folders, and notebooks. Use square only when the paired-state layout needs it.
- Inspect the output once. Regenerate with a targeted correction if the artifact becomes a generic stationery mockup, loses its black field, lacks believable hardware, or renders as a flat poster.

## Hard Avoids

Always avoid:

- bright white studio sweep instead of a black field
- glossy luxury stationery photography
- soft floating product shadow or dramatic spotlight cone
- pristine corporate brand mockup
- laptop, phone, app UI, web cards, or dashboard styling
- random stickers, cute journaling, decorative washi overload
- dense multicolor scrapbook composition
- fantasy treasure map, steampunk props, occult symbols
- full-bleed scene, cinematic depth of field, neon, cyberpunk
- huge commercial headline, logo lockup, CTA
- long perfectly readable paragraphs or fake legal documents
- perfectly clean vector forms with no paper or reproduction texture

## Output Format

````markdown
**生成图**

![Archival Dossier Zine](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- State: [artifact state]
- Recipe: [artifact / layers / hardware / information / color / wear]
- [one short note about the interpretation]
````

## Quality Gate

Before finalizing, check:

- Is the artifact visibly physical and inspectable?
- Does black negative space dominate the outer frame?
- Is there one coherent artifact family rather than unrelated ephemera?
- Are board, paper, pockets, page edges, and fasteners materially believable?
- Do forms, tables, photos, stamps, handwriting, and diagrams follow one information system?
- Is text limited to a few exact labels plus plausible microtype?
- Is the chromatic system controlled and visible at thumbnail size?
- Are wear, ink, paper, and scan defects present without becoming dirty decoration?
- Does the output avoid generic stationery mockups and cute scrapbooking?
- Did you actually generate the image?
