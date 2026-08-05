---
name: 水墨纹身
description: Generate prompts and finished raster images for monochrome sumi-e gesture tattoos, black-ink animal and botanical tattoo specimens, and dark editorial body-placement portraits. Use when the user supplies a motif, animal, plant, phrase, body location, or reference images and wants expressive brush tattoos with a dominant anatomical gesture, ink wash, dry-brush fracture, orbit filaments, large negative space, optional restrained red or cobalt accent, textured-paper artwork, or believable tattoo placement on an arm, shoulder, back, waist, collarbone, or thigh.
---

# Sumi Gesture Tattoo Zine

Turn a motif, reference set, or placement request into:

1. a production-ready image prompt, and
2. a finished raster image in one selected output mode.

Fuse the negative-space discipline of `gc-minimal-zine-poster-v0-1` with
expressive black-ink tattoo drawing and anatomically believable body placement.
The result is an art study, not a tattoo advertisement or a sticker catalog.

## Output Routing

Choose one mode before compiling:

- `paper-specimen`: isolated tattoo artwork on bright fibrous paper.
- `body-portrait`: the tattoo integrated into a low-key editorial body crop.
- `paired-proof`: one restrained diptych with matching paper artwork and skin
  placement; use only when the user asks to compare design and placement.

When ambiguous, use `body-portrait` for requests containing tattoo placement,
skin, shoulder, arm, back, waist, or portrait. Use `paper-specimen` for tattoo
design, artwork, flash, motif, drawing, or prompt-study requests. Never generate
two separate paid images unless the user explicitly asks for variants.

## Reference Routing

- Treat supplied images as visual-grammar references unless literal editing is
  explicitly requested.
- Extract the repeated rules before subject details: canvas ratio, body crop,
  exposed-skin shape, motif axis, anchor count, black-mass ratio, wash ratio,
  filament direction, empty-space ratio, light direction, and background value.
- Preserve a requested motif or body location, but do not copy a reference
  person's identity, visible watermark, signature, or exact tattoo artwork.
- Read [references/structure-grammar.md](references/structure-grammar.md) for
  reference analysis, silhouette construction, and measured layout families.
- Read [references/motif-recipes.md](references/motif-recipes.md) when choosing
  a snake, bird, butterfly, octopus, flower, jellyfish, or abstract motif.
- Read [references/placement-lighting.md](references/placement-lighting.md) for
  anatomy, camera crop, skin behavior, clothing, and lighting controls.
- Read [references/prompt-recipes.md](references/prompt-recipes.md) when a request
  is brief, when combining subjects, or when correcting visual drift.

## Core Identity

Preserve these signals:

- one dominant black-ink gesture organized around one vertical, diagonal, or
  wrapped anatomical axis;
- recognizable animal or botanical fragments interrupted by abstraction;
- dense black nodes balanced by diluted gray wash and untouched skin or paper;
- one to four hairline orbit curves, whip lines, or trailing filaments;
- dry-brush skips, bristle splits, pigment pools, splatter, feathering, and
  controlled ink bleed;
- large quiet areas around the mark, with no decorative filler;
- either bright textured paper or a restrained dark portrait with skin as the
  light field;
- monochrome by default; one red, cobalt, or muted gold accent is optional and
  must remain subordinate.

Carry forward from Minimal Zine Poster v0.1: one anchor, large negative space,
flat material texture, one decisive accent, quiet editorial temperature, and no
commercial hierarchy. Replace its tiny object cluster and microtype with one
larger wearable ink gesture. Default to textless.

## Gesture Skeleton

Construct every tattoo in five passes:

1. **Body axis**: one S-curve, vertical stem, diagonal flight path, or wrapped
   coil that follows the chosen body surface.
2. **Primary creature or plant**: one dominant readable subject; allow up to
   two smaller echoes only when the recipe requires motion or sequence.
3. **Black mass**: two or three concentrated pigment nodes occupying 25%-45%
   of the tattoo mark, never the whole design.
4. **Wash and fracture**: one to three gray blooms, broken anatomy fragments,
   dry-brush gaps, and white paper/skin channels.
5. **Trajectory**: one to four thin arcs or filaments and no more than five
   micro splatters, dots, or geometric nodes.

The motif must remain readable at thumbnail scale. Do not solve weak structure
by adding more animals, leaves, loops, or splashes.

## Ink Material Engine

Use three value roles:

- `carbon anchor`, 35%-50%: dense matte black for the main silhouette and focal
  joints;
- `diluted wash`, 20%-35%: transparent gray absorption, feathering, and ghost
  anatomy;
- `open substrate`, 25%-45%: untouched paper or visible skin inside and around
  the motif.

Line hierarchy:

- one pressure-sensitive gesture stroke with visible bristle width changes;
- two to six thinner structural contours or feather/leaf/tentacle ribs;
- one to four hairline orbit traces with tapered endings;
- sparse dots or splatters clustered near focal nodes, never sprayed uniformly.

Allow dry-brush skips, broken joins, pooled intersections, and ink dragged over
paper tooth. Avoid uniform vector outlines, airbrush shading, smooth digital
gradients, glossy black, sticker borders, and random grunge everywhere.

## Minimal Accent Engine

Default to black, charcoal, gray, paper/skin, and no color. When the user asks
for color or when a Minimal Zine accent materially improves the image, choose
exactly one:

- vermilion circle or seal behind one focal node;
- small cobalt wash touching 8%-15% of the ink cluster;
- muted gold dust occupying less than 5% of the mark.

The accent must remain visible at thumbnail size but never recolor the full
animal, create rainbow ink, or turn the image into a decorative poster.

## Body Integration

For `body-portrait` and `paired-proof`:

- align the tattoo axis with the humerus, forearm tendon, scapula, spine, waist
  curve, rib arc, collarbone, or thigh direction;
- let the design bend and foreshorten with the surface;
- keep pores, folds, tendon transitions, and bone landmarks visible through ink;
- soften tattoo edges slightly without blurring the gesture skeleton;
- use dark clothing or hair to frame the exposed-skin shape, not to cover it;
- crop or softly obscure identity; the tattoo and body surface are the subject;
- no decal halo, gloss, raised ink, cast shadow, or rectangular transfer edge.

For `paired-proof`, both panels must derive from one locked tattoo master. Keep
the bell contour, dominant gesture, filament paths, orbit arcs, droplets,
proportions, and orientation identical. The skin panel may change only through
anatomical curvature, foreshortening, pigment blending, pores, and lighting. Do
not generate the paper and skin designs independently, and reject any proof
that contains a second residual tattoo beneath the transferred master.

Read [references/placement-lighting.md](references/placement-lighting.md) before
prompting a shoulder, back, waist, or difficult arm pose.

## Prompt Compiler

Write the final prompt as five compact paragraphs:

1. mode, canvas ratio, substrate or body crop, negative-space amount, and light;
2. body axis, placement, anatomy, clothing/hair frame, and camera crop;
3. motif, gesture skeleton, black masses, diluted washes, orbit lines, and
   matching geometry on skin or paper;
4. monochrome value roles, optional single accent, texture, and textless policy;
5. mood plus hard avoids.

For `paper-specimen`, omit body details from paragraph 2 and instead state the
motif's size, position, and substrate space. Compile only visible renderable
details. Do not mention source paths, reverse engineering, hidden analysis, or
Skill names in the final image prompt.

## Generation

- Generate the image by default; stop at prompt-only only when explicitly asked.
- Prefer the built-in image generation capability.
- When built-in generation is unavailable and server fallback has already been
  approved, run:

  ```bash
  python3 scripts/server_image_gen.py \
    --prompt-file output/imagegen/<slug>.prompt.txt \
    --out output/imagegen/<slug>.png \
    --size 1024x1536 \
    --quality high
  ```

- Use `1024x1536` for vertical body portraits and specimens, `1024x1024` for
  shoulder/back studies, and `1536x1024` only for paired proofs.
- Store the exact prompt beside the image. Never overwrite existing output.
- Inspect once. Regenerate with one targeted correction if anatomy is malformed,
  the tattoo floats above skin, the motif becomes unreadable, black fills become
  muddy, or negative space disappears.

## Hard Avoids

Always avoid:

- commercial tattoo advertisement, flash catalog, price, CTA, logo, QR code;
- copied reference identity, watermark, signature, or exact tattoo composition;
- pin-up posing, fetish framing, explicit nudity, plastic skin, beauty retouching;
- malformed limbs, extra fingers, broken shoulders, impossible spine or ribs;
- sticker border, white halo, gloss, raised ink, cast shadow, pasted decal look;
- tribal bands, biker flash, heavy sleeve fill, gothic ornament unless requested;
- dense collage, multiple competing creatures, decorative grunge everywhere;
- vector-perfect curves, clip-art animals, glossy 3D, neon, cyberpunk, UI cards;
- long text, headlines, metadata blocks, or branding;
- flat black silhouette with no wash, fracture, white channels, or bristle life.

## Output Format

Return the generated image, exact final prompt, and:

- Mode: selected output mode
- Axis: selected body or paper gesture axis
- Motif: subject and supporting fragments
- Ink: black/wash/open-substrate ratio
- Accent: none or the single selected accent
- one short interpretation note

## Quality Gate

Before finalizing, check:

- Is there one dominant gesture and one readable motif family?
- Does the mark have dense black, diluted gray, and open skin/paper channels?
- Are filaments sparse, tapered, and structurally useful?
- Is at least 45% of a paper specimen quiet substrate?
- Does a body tattoo follow anatomy and retain pores without decal edges?
- Is the body crop believable, restrained, and free of identity dependence?
- If color exists, is there only one thumbnail-visible accent?
- Did Minimal Zine restraint survive without shrinking the tattoo into a tiny dot?
- Did the output avoid ads, text, logos, collage clutter, and glossy rendering?
- Was the final raster image generated and inspected?
- In `paired-proof`, can every major stroke and ink node be matched one-to-one
  between paper and skin, with no duplicated or residual design?
