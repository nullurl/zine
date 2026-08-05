# Tattoo Color and Line System

Use this reference when the user asks for tattoo color extraction, a stronger
hand-drawn feeling, expressive linework, or a close match to the supplied
reference family.

## Color roles

Build every palette from roles rather than listing unrelated colors:

- **Anchor ink, 55-70%**: the darkest hue that carries the silhouette and keeps
  the mark readable on skin.
- **Echo color, 15-25%**: a nearby or contrasting secondary line used on only a
  few branches, wings, or filaments.
- **Spark color, 5-10%**: one bright yellow, coral, pink, or cyan accent reserved
  for dots, short flashes, and a focal node.
- **Diluted wash, 10-20%**: transparent pigment behind or beside the structure;
  never cover the whole drawing.

Keep two or three colors for sparse motifs and at most four for fireworks or
filament clusters. On skin, reduce saturation and opacity by roughly one third
while preserving hue relationships. On the paper specimen, allow cleaner and
slightly stronger pigment.

## Reference-derived palettes

- `meadow-signal`: pine green `#31583b`, fresh leaf `#79a64a`, lemon spark
  `#e8cf34`, optional dusty pink `#c96f91`. Use for trees, vines, roots, wind,
  and spring marks.
- `dream-current`: violet `#884c98`, orchid pink `#c25c9a`, lemon `#e8d34b`,
  pale cyan `#5d9ea0`. Use for poetic figures, sea traces, dreams, and abstract
  landscapes.
- `indigo-memory`: deep indigo `#315d86`, blue-gray `#708aa0`, charcoal blue
  `#344954`. Use for butterflies, wings, night water, memory, and melancholy.
- `rust-monoline`: oxblood `#762f2e`, dry sienna `#a05c49`, warm graphite
  `#554442`. Use for intimate figurative marks and restrained single-color work.
- `firework-filament`: teal `#2e8793`, coral `#d76d59`, saffron `#dfa72f`, plum
  `#754675`. Use for fireworks, jellyfish, music, and celebratory thread motifs.

For requests explicitly asking for more colors, route to the `multicolor-echo`
mode and read [hand-type-multicolor.md](hand-type-multicolor.md). It permits
three to five coordinated hues while keeping the anchor line dominant.

Treat these hex values as visual targets, not flat vector fills. Describe the
pigment as dry colored pencil, diluted watercolor, transparent transfer ink,
or broken pastel dust.

## Four-level line hierarchy

1. **Gesture line**: one dominant continuous or nearly continuous stroke that
   defines the silhouette. Let pressure vary and taper both ends.
2. **Structural line**: two to four thinner branches, veins, ribs, roots, or
   horizon marks attached to the gesture line.
3. **Echo line**: one or two lightly offset colored traces that briefly follow
   the gesture, then separate. Do not outline the entire motif twice.
4. **Micro marks**: two to five dots, scratches, star sparks, insects, or short
   dashes. Keep them subordinate.

Use an approximate width relationship of `1 : 0.6 : 0.25` for gesture,
structural, and echo lines. Vary speed and pressure visibly: some edges dry and
grainy, some strokes faint, some intersections darker from pigment overlap.
Allow small gaps and imperfect joins. Avoid smooth vector curves, uniform
outlines, digital neon, airbrush gradients, and heavy black borders.

Additional hand-drawn effects to choose from: nervous botanical wavering,
filament cascade, gesture fracture, wash-outline, ghost-registration, rubbed
pastel block, erased graphite ghost, and colored restart mark. Choose one
dominant effect plus one support effect; do not stack every effect.

## Hand-drawn material cues

- colored-pencil grain remains visible inside the line;
- dry-brush strokes skip over paper fibers;
- translucent wash blooms beside, not exactly inside, the contour;
- tiny pigment dots have irregular size and spacing;
- drips are rare, thin, and tapered;
- line endings dissolve into dust, a dot, or a hairline;
- intersections may darken, but no area becomes a solid black mass unless the
  selected monochrome palette calls for one focal blot.

## Skin transfer behavior

Describe the applied mark as integrated with the body surface:

- follow the wrist, hand, waist, or forearm curvature;
- preserve the same drawing geometry and orientation as the paper specimen;
- slightly soften edge sharpness and lower saturation on skin;
- keep skin pores and natural texture visible through translucent pigment;
- remove sticker borders, white halos, raised ink, gloss, cast shadows, and
  pasted-on decal edges.

## Prompt block

Use this block after selecting a motif and palette:

```text
Use [palette name] as role-based tattoo pigment: [anchor] carries the gesture
line, [echo] appears only on selected branches, [spark] marks the focal node,
and a diluted [wash] blooms sparsely behind the structure. Render one tapered
pressure-sensitive gesture line, two to four thinner structural lines, one or
two partial offset echo traces, and two to five irregular micro marks. Preserve
colored-pencil grain, dry-brush skips, broken joins, transparent overlap, and
hairline endings. On skin, reduce saturation and edge sharpness while keeping
the same geometry; no sticker border, white halo, gloss, or shadow.
```

## Corrections

- If colors become loud: remove one hue, reduce the wash area, and restore the
  anchor ink as the dominant structure.
- If the drawing looks vector-made: require pressure variation, dry grain,
  broken joins, tapered endings, and one partial echo line.
- If linework becomes muddy: remove washes from intersections and keep pigment
  blooms outside the main contour.
- If the tattoo looks pasted on: lower edge sharpness and saturation on skin,
  expose pores through the pigment, and remove all decal borders and shadows.
