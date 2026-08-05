# Prompt Recipes

Use these recipes when selecting a layout, motif, and palette.

## Layout Recipes

### split-skin-paper

Best default for most requests.

Prompt elements:

- wide 16:9 scanned transfer sheet
- left 45% soft skin placement photo
- right 55% isolated tattoo drawing on ivory paper
- one small caption under the drawing
- tiny size note near the lower right

### soft-photo-margin

Use for quiet, poetic, or memory-like themes.

Prompt elements:

- small faded photo inset on the left
- large unbroken paper field on the right
- tattoo artwork floats slightly above center
- caption sits low and small

### paired-specimen

Use for clear product comparison or "reference image as baseline" requests.

Prompt elements:

- left and right panels aligned like a specimen record
- applied tattoo on skin mirrors the isolated drawing
- faint registration marks or tiny dots
- small edition metadata

### floating-transfer

Use for dreamy, natural, or soft-color requests.

Prompt elements:

- no hard panel edge
- skin photo fades into paper tone
- tattoo art hovers with watercolor edges
- small handwritten caption

### catalog-card

Use when the user asks for a sticker, transfer, tattoo pack, or product sheet.

Prompt elements:

- restrained catalog layout, not advertisement
- transfer size and fictional item code
- one clean design, optionally one tiny alternate fragment
- no CTA, price, QR code, or brand logo

## Motif Recipes

### botanical-line

Fine green vine, fern, staghorn fern, leaf stem, seed pod, or moss trace. Add yellow spark or tiny pale pink bloom only if the palette allows.

### water-air-line

Fish, wave, cloud, jellyfish, rain, shell, or sea ribbon. Use cobalt, aqua, violet, or blue-gray washes with thin charcoal structure.

### wing-flutter

Butterfly, moth, bird, phoenix feather, or wing-shaped mark. Use asymmetry and small ink flecks so it feels handmade.

### abstract-talisman

Ink ribbon, brush trail, firework thread, smoke, memory diagram, small poem glyph, or constellation trace. Keep it tattooable and not logo-like.

### object-memory

Turn a personal object into a small transfer mark: cup, ticket, flower, mountain, window, umbrella, key, or stone. Use one object only.

## Precision Recipe

Use this recipe after the normal layout, motif, and palette choices when the
user asks to extract more reference effects:

```text
Reference-derived but original tattoo mark: one [silhouette] built on a [vertical/diagonal/horizontal] primary axis, [2-4] secondary [branches/filaments/ribs], one [focal node], and [2-5] detached [dots/sparks/flecks]. Use [line material] with [1-3] translucent [wash colors], controlled broken edges, and a few tapered drips. The applied skin image and isolated paper specimen must be the same drawing at the same orientation and scale logic. Keep the mark sparse, printable, and legible; no extra subjects.
```

### element-stack examples

- **Botanical**: rising stem + asymmetric leaf ribs + exposed root/tendril + moss green contour + lemon-yellow glints + three green freckles.
- **Wind**: central trunk/axis + three swept branch fans + blurred directional strokes + cobalt/leaf-green wash + two loose threads.
- **Wing**: open wing silhouette + broken vein structure + dark body node + blue or violet wash + four pigment flecks.
- **Filament**: compact top node + five to seven separated hanging threads + alternating color lines + three sparks.

## Caption Recipes

- Chinese short line: `云走得很慢`
- Bilingual whisper: `slow cloud / field note`
- Size note: `8 x 3 cm`
- Edition mark: `transfer no. 04`
- Tiny studio mark: invented lowercase words only, no known brand or copied signature

If the user gives a phrase, use it as the caption and avoid adding a second poetic sentence.

## Palette Recipes

- `green-botanical`: ivory paper, soft skin, charcoal line, moss green wash, yellow spark.
- `blue-water`: ivory paper, pale denim/cotton hint, cobalt line, aqua wash, gray-blue dots.
- `pink-butterfly`: warm paper, rose pink bloom, leaf green line, coral specks.
- `violet-ocean`: cool paper, violet line, lemon yellow spark, blue-gray shadow.
- `ember-phoenix`: warm ivory paper, tomato red wing, sienna wash, dark brown line.
- `black-minimal`: charcoal line, paper fibers, one small red seal or cobalt dot.

For stronger reference-derived color and hand-drawn linework, use the expanded
role-based palettes and reusable prompt block in
[color-line-system.md](color-line-system.md). Do not mix multiple palette recipes.
For hand crops, bilingual captions, multicolor abstract accents, or additional
line-effect variants, use [hand-type-multicolor.md](hand-type-multicolor.md).

## Prompt Skeleton

```text
Wide horizontal [16:9/4:3] tattoo transfer showcase sheet, [layout family], pale [paper tone] with scanned paper fibers, generous negative space, flat orthographic view.

Left side: soft daylight skin-placement photo of [body area], natural skin tone, [fabric/clothing hint], the same small temporary tattoo applied at [scale/location], low contrast photo softness but the tattoo remains clear.

Right side: isolated tattoo transfer artwork of [motif], [line quality], [palette], watercolor bloom and tiny ink dots, printable fine-line temporary tattoo design centered on textured paper with quiet blank space.

Small caption text: "[short caption]" in [type style] beneath/near the artwork, optional tiny [size/edition mark] placed discreetly, no real brand, no copied signature.

Intimate handmade editorial mood, matte scan, soft natural light, no commercial ad, no CTA, no QR code, no logo, no heavy tattoo realism, no dense sticker sheet, no glossy mockup.
```
