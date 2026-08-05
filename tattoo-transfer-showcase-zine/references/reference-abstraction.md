# Reference Abstraction and Precision

Use this file when the user supplies a reference set and asks for a closer or
more accurate result. Extract visual grammar, not literal content.

## Four abstraction layers

1. **Silhouette**: identify the single readable outer gesture first: a vertical
   stem, spreading wing, hanging filament cluster, rising branch, or low horizon
   trace. Keep the silhouette recognizable at thumbnail size.
2. **Structural skeleton**: reduce the motif to one primary axis, two to four
   secondary branches, and one focal node. Keep the same directional flow in
   the skin photo and the paper specimen.
3. **Material behavior**: describe the marks as colored-pencil or dry-brush
   contours, diluted watercolor blooms, transparent overlapping washes, broken
   pigment, tiny splatters, and occasional drips. Never call the result glossy,
   vector, polished, or photorealistic.
4. **Micro-accents**: add only two to five small accents selected from dots,
   seed-like sparks, a tiny butterfly, a small star, a short underline, or a
   loose color thread. These accents support the silhouette and do not become
   separate sticker designs.

For color or line-focused requests, route the extracted structure through
[color-line-system.md](color-line-system.md) before compiling the final prompt.
Use its color roles and four-level line hierarchy instead of copying every hue
or stroke visible in the source.

## Reference-set synthesis

The supplied examples consistently combine:

- an airy horizontal double-page sheet with a roughly 45/55 photo-to-paper
  split;
- a softly exposed close crop of a hand, wrist, ankle, waist, or forearm on
  the left, often with white or oatmeal cotton at the edge;
- a pale warm paper field on the right, with visible fibers but no hard border;
- a single handmade tattoo drawing aligned to the same scale and geometry as
  the applied mark;
- generous blank space above and around the drawing;
- one or two small lines of Chinese or bilingual text below the drawing;
- a tiny size note and a restrained invented studio mark near the bottom.

## Motif extraction examples

- Wind-blown tree: vertical trunk axis, three sweeping branch fans, blurred
  directional leaf strokes, deep blue sky only as a palette cue; do not put a
  full landscape into the tattoo.
- Botanical vine: one rising stem, asymmetric leaf ribs, exposed root or
  tendril ending, moss green contour, lemon-yellow highlight, sparse green
  freckles.
- Butterfly or wing: one open wing gesture, broken interior veins, a darker
  focal body, one watercolor mass, and a few detached pigment flecks.
- Firework or jellyfish filament: compact upper node, long separated hanging
  lines, color-separated threads, small sparks; preserve vertical rhythm.
- Wuxia or landscape trace: one tiny human or mountain focal mark only when
  requested, framed by two sweeping colored lines rather than a fully rendered
  scene.

## Precision controls

Put these controls directly into the final prompt:

- `same motif geometry in both panels`;
- `one dominant silhouette, no competing subjects`;
- `primary axis and branch count remain consistent`;
- `applied tattoo is small, legible, and follows the body contour`;
- `isolated artwork is a clean specimen redraw, not a new interpretation`;
- `keep 60-75% of the paper side as quiet negative space`;
- `use only the named palette accents`;
- `no extra lettering, signatures, logos, or alternate designs`.

If the generated result drifts, fix one variable at a time: first remove extra
motifs, then correct the axis and panel matching, then adjust line weight and
color saturation. Do not solve a geometry problem by adding detail.

## Reference priority order

When references conflict, follow this order:

1. user-specified motif and exact text;
2. shared layout and paper treatment across the set;
3. silhouette and body placement;
4. line and pigment behavior;
5. micro-accents and metadata.

Never reproduce a reference signature, watermark, quotation, brand mark, or
identifiable text unless the user explicitly supplies it as content to keep.
