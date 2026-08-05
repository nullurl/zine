# Hand, Type, and Multicolor Composition

Use this reference when the user asks for hand placement, hand-specific body
features, richer color combinations, abstract accents, or a more considered
caption and typography pairing.

## Hand and placement direction

Treat the hand as a structural surface, not a generic model photo. Choose one
crop and one anatomical direction:

- **Back of hand**: show five distinct fingers, natural knuckle rhythm, nail
  edges, and the central metacarpal plane. Align a long vine, figure, wing, or
  wave with the middle-finger tendon or sweep it toward the thumb web.
- **Palm-side hand**: show believable palm creases and a soft cupped gesture;
  keep the tattoo lighter and avoid covering the entire palm.
- **Wrist-to-forearm**: use the wrist crease as a deliberate crossing point;
  let a vertical stem, whale, filament, or root follow the forearm axis.
- **Fingers**: use one or two fingers only, with the mark following the joint
  direction. Do not wrap every finger unless explicitly requested.
- **Waist or ankle**: use fabric edges and body curvature as the frame; keep the
  tattoo legible at a small scale.

Prompt anatomical invariants: five fingers when a full hand is shown, correct
finger count and joint spacing, natural nails, believable knuckles and tendons,
no fused digits, no extra fingers, no plastic skin, no jewelry unless requested.
Keep the crop quiet: white or oatmeal cotton, soft daylight, no fashion pose,
no dramatic shadows, no face, and no stock-photo styling.

## Body-to-tattoo mapping

1. Lock the body crop and gesture direction.
2. Place the primary tattoo axis over a real anatomical flow: tendon, wrist
   crease, forearm length, collarbone, waist curve, or ankle line.
3. Allow the tattoo to bend with the surface but keep its isolated redraw in the
   same orientation and proportion.
4. Lower skin-side saturation and edge sharpness while retaining pores and
   natural folds. Never simulate a decal with a white border, glossy film, or
   cast shadow.

## Multicolor composition

Use a `multicolor-echo` mode only when the user asks for richer colors or the
reference set clearly contains several hues. Select one role for each color:

- **Anchor**: deepest green, indigo, brown, or charcoal; carries the main
  silhouette and 35-50% of the visible mark.
- **Bridge**: a nearby hue that connects warm and cool colors along one branch
  or wash, 15-25%.
- **Counterpoint**: a contrasting hue placed on one focal feature, 10-20%.
- **Spark A / Spark B**: two small high-chroma accents, each no more than 5-8%,
  used for dots, stars, short threads, or tiny abstract symbols.
- **Paper wash**: one pale transparent bloom, 10-15%, kept behind the structure.

Use three to five hues total. Keep the anchor line visibly dominant; do not
make a rainbow outline or give every branch a different color. Repeat each
support color at least twice so it reads as a system rather than noise.

Useful combinations:

- `garden-chroma`: moss green + chartreuse + dusty magenta + pale cyan;
- `dream-pulse`: violet + orchid pink + lemon yellow + muted teal;
- `coast-signal`: indigo + aqua + coral + saffron;
- `rust-bloom`: oxblood + sienna + faded lilac + old gold;
- `paper-firework`: charcoal + teal + coral + saffron + plum.

## Abstract element vocabulary

Choose two to five elements that echo the main motif, not a collection of
separate stickers:

- pigment freckles, loose color threads, tapered drips, short dashes;
- tiny butterflies, leaves, stars, bubbles, sparks, or seed shapes;
- partial wave, root, orbit, horizon, sound pulse, or wind gesture;
- erased graphite ghosts, registration dots, rubbed pastel blocks, or one
  translucent color cloud.

Place accents asymmetrically around the focal node or along the motion path.
Keep the abstract elements smaller and lighter than the main silhouette, with
at least 60% of the paper panel left calm.

## Line-effect modes

Choose one dominant mode and one supporting effect:

- **nervous botanical**: thin wavering contour, leaf-vein scratches, dry green
  pigment, sparse yellow or pink marks;
- **filament cascade**: long tapered threads, small suspended dots, transparent
  color changes, rare drips;
- **gesture fracture**: one broken sweeping line, offset echo strokes, rubbed
  blocks, and visible restart marks;
- **wash-outline**: precise contour over a pale watercolor bloom, a few softened
  interior gaps, no full fill;
- **ghost-registration**: faint offset duplicate in one secondary color, tiny
  crop or registration marks, still one readable tattoo.

Avoid combining more than two modes. The primary contour must remain legible at
small transfer size.

## Typography pairing

Use a three-level type stack:

1. **Primary caption**: one short poetic line, centered or low-right below the
   artwork, in a small serif, typewriter, or restrained handwritten style.
2. **Secondary translation or whisper**: optional one-line English/Chinese
   counterpart at 60-75% of the primary size, never a paragraph.
3. **Metadata**: tiny size, field note, or edition code aligned separately near
   the bottom edge.

Match the type color to the anchor ink or a softened bridge hue. Let a single
accent word use the counterpoint color only when it improves hierarchy. Keep
line spacing open, avoid bold display headlines, and never copy reference
quotes, signatures, or watermarks.

Examples:

- `风轻咬夏日的动脉` / `the green sea in your eyes.`
- `化身孤岛` / `the island breathes`
- `去看烟花吧` / `field note 03`

Use user-supplied text verbatim when provided; otherwise invent original short
copy and keep it secondary to the tattoo.

## Prompt block

```text
Use a [hand crop] with anatomically correct fingers, knuckles, tendons, nails,
and natural skin texture; align the tattoo with the [anatomical direction].
Use [multicolor mode] with [anchor], [bridge], [counterpoint], two tiny
[spark colors], and one pale paper wash. Keep one dominant silhouette, two to
five asymmetrical abstract accents, and [line-effect mode] plus [supporting
effect]. Pair a short primary caption with an optional smaller translation and
separate tiny metadata; no extra fingers, no sticker edge, no rainbow outline,
no clutter.
```

## Corrections

- If hands look artificial: reduce the crop, specify the exact hand surface,
  and require distinct fingers, knuckles, tendons, and natural nails.
- If multicolor becomes noisy: return to one anchor, one bridge, one
  counterpoint, and two tiny sparks.
- If text dominates: shorten the caption, lower contrast, and move metadata
  away from the main line.
- If abstract accents compete: keep only elements that repeat the tattoo's
  movement or palette.
