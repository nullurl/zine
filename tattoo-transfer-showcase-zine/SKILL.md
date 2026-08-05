---
name: 纹身转印
description: Generate prompts and finished raster images for poetic tattoo transfer showcase sheets, temporary tattoo sticker catalog pages, body-placement mockups, and delicate tattoo design presentation zines. Use when the user provides a theme, phrase, motif, reference image, tattoo idea, botanical/animal/ink symbol, color brief, hand-placement request, multilingual copy, or product-style request and wants a refined sheet with a soft anatomically believable skin-placement photo, isolated tattoo artwork, expressive hand-drawn linework, reference-derived multicolor transfer ink, abstract accents, sparse typography, handmade print texture, and minimal zine negative space.
---

# Tattoo Transfer Showcase Zine

Turn the user's theme, phrase, motif, or reference image into:

1. a final image-generation prompt, and
2. a finished raster image of a tattoo transfer showcase sheet.

Default to the full showcase sheet: one placement mockup on skin plus one isolated tattoo artwork panel. Generate only the standalone tattoo art when the user explicitly asks for the artwork only.

## Reference Routing

- Treat supplied images as visual-grammar references unless the user asks for literal editing.
- Extract: canvas ratio, split layout, skin/body crop, paper tone, tattoo motif, color palette, line weight, watercolor bleed, caption placement, size mark, and empty-space ratio.
- Do not copy watermarks, real brand names, artist signatures, sample quotes, or identifiable reference text unless the user supplies exact text to preserve.
- Read [references/style-grammar.md](references/style-grammar.md) when matching reference structure or correcting visual drift.
- Read [references/prompt-recipes.md](references/prompt-recipes.md) when choosing a layout, tattoo family, caption policy, or color treatment.
- Read [references/reference-abstraction.md](references/reference-abstraction.md) when the user provides multiple reference images, asks to extract more elements, or asks for a more precise match.
- Read [references/color-line-system.md](references/color-line-system.md) when the user asks to extract tattoo colors, strengthen the hand-drawn quality, improve line feeling, or match the supplied color-and-line reference family.
- Read [references/hand-type-multicolor.md](references/hand-type-multicolor.md) when the user asks for hand or finger placement, more colors, abstract color elements, bilingual or multi-line text, or richer typography pairing.

## Reference Analysis Workflow

When references are supplied, inspect them before compiling the prompt. Record
one short value for each field: canvas ratio, photo crop, body area, motif
silhouette, primary axis, branch count, focal node, line behavior, pigment
behavior, palette, caption position, and negative-space ratio. Treat repeated
features as rules and one-off features as optional accents.

Build the tattoo in four passes:

1. **Silhouette**: choose one outer gesture that remains readable at small size.
2. **Skeleton**: add one axis, two to four branches or filaments, and one focal node.
3. **Material**: apply fine broken contour, translucent wash, dry-brush grain, and sparse pigment bleed.
4. **Accents**: select no more than five tiny dots, sparks, insects, marks, or color threads.

Keep the same silhouette, axis, scale, and accent family in the applied tattoo
photo and isolated redraw. Read [references/reference-abstraction.md](references/reference-abstraction.md)
for motif-specific translations and correction order.

## Core Identity

Fuse Minimal Zine restraint with tattoo transfer presentation:

- wide horizontal 16:9 or 4:3 canvas, flat scanned-paper view
- pale cream, ivory, or light warm paper background
- left-side soft lifestyle placement photo: wrist, forearm, hand, collarbone, shoulder, waist, ankle, or back
- right-side isolated tattoo design on textured paper with large negative space
- delicate fine-line drawing, translucent ink, watercolor splash, tiny dots, drips, and airy marks
- short poetic caption beneath or near the isolated design
- optional tiny size notation such as `8 x 3 cm`, edition code, or fictional studio mark
- intimate, lightweight, handmade, skin-friendly, editorial catalog mood

Carry forward from `gc-minimal-zine-poster-v0-1`: negative space, one clear visual anchor, scanned paper, sparse type, one visible chromatic accent, and quiet poetic temperature. Shift the grammar from a tiny vertical poster anchor to a horizontal tattoo showcase sheet.

## Composition Engine

Choose one layout before compiling:

- `split-skin-paper`: left 45% skin placement photo, right 55% isolated tattoo on paper.
- `soft-photo-margin`: small skin photo inset on the left, much larger blank paper field around the right artwork.
- `paired-specimen`: two equal panels, left applied tattoo, right clean transfer artwork, aligned like a specimen sheet.
- `floating-transfer`: right artwork floats in negative space, left skin crop fades into paper with no hard border.
- `catalog-card`: product-sheet feeling with tiny caption, size, and edition mark, still quiet and non-commercial.
- `micro-gallery`: one skin crop plus two tiny alternate transfer fragments, used only for batch or variant requests.

Use one layout family only. Keep the sheet calm and legible.

For reference-matching requests, lock the layout before changing the motif:
left photo about 45%, right specimen about 55%, vertical alignment shared,
no hard divider, and 60-75% of the paper side left quiet. Do not add a second
design to compensate for a weak primary motif.

## Tattoo Motif Engine

Translate the user's subject into one tattooable motif:

- botanical vine, fern, leaf stem, flower, root, moss, seed, or tree trace
- butterfly, moth, bird wing, phoenix feather, fish, jellyfish, shell, wave, cloud, moon, mountain, or star
- abstract ink ribbon, brush trail, spark, firework filament, rain mark, smoke line, or memory symbol
- small phrase-shaped mark, talisman, ticket-like trace, or poetic diagram

Prefer fine line art plus watercolor or ink bloom. Avoid heavy realism, biker tattoo style, thick tribal patterns, gothic flash sheets, skull-heavy motifs, and dense full-sleeve designs unless the user explicitly asks.

For a reference-derived design, use one dominant silhouette, one primary axis,
two to four secondary branches, one focal node, and two to five micro-accents.
Describe geometry explicitly so the image model does not replace a sparse mark
with a generic botanical illustration or a full scene.

## Typography Policy

- Use one short caption, preferably the user's phrase if supplied.
- If no text is supplied, invent a short poetic Chinese or English line.
- Keep all text small, secondary, and slightly imperfect: serif, typewriter, handwritten pencil, or thin editorial sans.
- Optional metadata may include a tiny size note, edition code, date, or fictional studio mark. Use invented marks only; do not use real brands or copied signatures.
- Never create a commercial CTA, URL, price, QR code, big headline, or dense product copy.

## Color Engine

Choose one main palette. For reference-led palette or line requests, use the
role ratios, hex targets, line hierarchy, and skin-transfer behavior in
[references/color-line-system.md](references/color-line-system.md).

Core palettes:

- `green-botanical`: moss green, yellow sparkle, charcoal line.
- `blue-water`: cobalt, sky blue, aqua wash, gray ink.
- `pink-butterfly`: rose pink, leaf green, pale coral bloom.
- `violet-ocean`: violet, lemon yellow, blue-gray line.
- `ember-phoenix`: tomato red, burnt sienna, warm brown ink.
- `black-minimal`: charcoal line with one small red, blue, or gold accent.

Keep skin tones soft and natural. Keep paper light. The tattoo artwork can be more saturated than the photo, but it should still feel printable as a transfer sticker.

Assign colors by function: one anchor ink carries 55-70% of the structure, one
echo color carries 15-25%, one spark color carries 5-10%, and a transparent
wash remains sparse. Use two or three colors by default and no more than four.
Use `multicolor-echo` only for an explicitly multicolor request; then route the
palette through [references/hand-type-multicolor.md](references/hand-type-multicolor.md)
and use three to five coordinated hues with one dominant anchor. Never create
a rainbow outline.

## Line Engine

Build linework in four levels: one tapered pressure-sensitive gesture line,
two to four thinner structural lines, one or two partial offset echo traces,
and two to five irregular micro marks. Preserve colored-pencil grain, dry-brush
skips, broken joins, pigment overlap, and hairline endings. Keep the gesture
line dominant; do not use uniform vector outlines or duplicate the whole motif
with a second contour.

On skin, soften edges and reduce saturation while keeping pores visible through
the pigment. Preserve the same geometry as the paper specimen. Never render a
sticker border, white halo, raised ink, gloss, or cast shadow.

When the crop includes a hand, specify the visible surface and anatomical flow.
Require correct fingers, knuckles, tendons, nails, and joint spacing before
placing the tattoo along the tendon, wrist crease, finger direction, or thumb
web. Read [references/hand-type-multicolor.md](references/hand-type-multicolor.md)
for hand crops, multicolor composition, abstract accents, line-effect modes, and
typography pairing.

## Prompt Compiler

Write the final prompt as five compact paragraphs:

1. canvas, sheet material, layout family, panel ratio, and negative-space amount
2. left skin-placement mockup: body area, softness, clothing/fabric hints, lighting, applied tattoo scale
3. right isolated tattoo: motif, four-level line hierarchy, color roles, watercolor/ink marks, paper texture, and matching skin-transfer behavior
4. typography: exact short caption, optional smaller translation, size note, tiny studio/edition mark, placement, type style, and color hierarchy
5. flat scanned mood and hard avoids: no ad, no logo, no UI, no heavy realism, no copied watermark, no clutter

For image-reference requests, append a precision sentence after paragraph 3:
`The left applied tattoo and right isolated specimen must share the same motif
geometry, primary axis, branch count, scale, and color accents; redraw the
reference grammar as one clean tattooable mark, without adding subjects.`

Compile only visible renderable details. Do not mention source paths, reverse-engineering, or hidden analysis in the final prompt.

## Generation

- Generate the image by default; stop at prompt-only only when explicitly requested.
- Prefer the built-in image generation capability.
- When built-in generation is unavailable and server fallback has already been approved, run:

    python3 scripts/server_image_gen.py \
      --prompt-file output/imagegen/<slug>.prompt.txt \
      --out output/imagegen/<slug>.png \
      --size 1536x1024 \
      --quality high

- The fallback reads provider configuration and `OPENAI_API_KEY` from the environment or Codex config, calls the OpenAI-compatible image endpoint, requests `b64_json`, and writes the decoded image locally. Never print or hard-code secrets.
- Store the exact final prompt beside the image. Never overwrite existing outputs; use a new descriptive slug.
- Inspect once. Regenerate with one targeted correction if the sheet lacks the left placement mockup, the right tattoo artwork is missing, text dominates, the image becomes a product advertisement, or the reference marks are copied too literally.

## Hard Avoids

Always avoid:

- single standalone tattoo art when the user asked for a showcase sheet
- commercial ad layout, CTA, price, QR code, logo lockup, real brand name, or copied signature
- dense product catalog, too many stickers, scrapbooking clutter, or mood-board collage piles
- heavy blackwork realism, biker flash, gothic skull themes, tribal bands, full-sleeve renders
- glossy 3D mockup, hard shadow, cinematic lighting, UI card, app screen, or stock-photo ad
- long readable text blocks or exact copied reference captions
- dark muddy paper unless the user asks for a dark style

## Output Format

Return the generated image, exact final prompt, and:

- Layout: selected layout family
- Motif: selected tattoo motif
- Palette: selected palette
- Text: caption and metadata policy
- one short interpretation note

## Quality Gate

Before finalizing, check:

- Does the image read as a tattoo transfer showcase sheet?
- Is there a visible skin-placement mockup and a separate isolated tattoo artwork?
- Is the canvas horizontal with pale paper and generous empty space?
- Is the tattoo delicate, printable, and skin-friendly?
- Does the caption stay small and secondary?
- Did you avoid copied brand text, signatures, watermarks, CTA, and commercial layout?
- Did you generate and inspect the final raster image?
- For reference-derived work, do both panels share the same geometry and does the motif remain one clear tattooable mark?
- Are the added effects limited to the selected line, wash, pigment, and micro-accent rules?
- Does the linework have a dominant gesture, thinner structure, partial echo traces, and sparse micro marks instead of a uniform vector outline?
- Does the palette have one dominant anchor ink and no more than three supporting color roles?
- Does the skin tattoo show natural pores without sticker edges, white halo, gloss, or shadow?
- If a hand is shown, are the fingers, knuckles, tendons, nails, and joints anatomically believable?
- If multicolor is requested, do three to five hues form a coordinated anchor/bridge/counterpoint/spark system rather than a rainbow outline?
- Is the text a restrained caption stack with optional translation and separate metadata, not a copied quote or headline?
