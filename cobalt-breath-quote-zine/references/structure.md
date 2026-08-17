# Cobalt Breath Quote Zine Structure

## Contents

- Reverse-engineered source DNA
- Attention geometry
- Layout families
- Metaphor engine
- Color and reproduction
- Typography
- Prompt patterns
- Hard avoids

## Reverse-engineered Source DNA

- Every reference uses a `1080x1440` vertical `3:4` frame.
- Warm cream, oatmeal, or yellow-gray paper fills the entire canvas. Fibers, specks, scratches, and mottling are visible at all scales.
- The page stays sparse: one Chinese text block and one cobalt visual vignette, sometimes joined by tiny archival marks.
- The vignette is not a pasted photo card. It dissolves into the page through brush masks, deckled tears, toner loss, halftone, and paper-colored holes.
- Imagery is blue monochrome or blue-gray duotone. Dark cobalt carries the conceptual subject; lighter blue carries sea, air, mist, or memory.
- Subjects are simple but relational: writer and sea, floating body and ripple, hands and sandcastles, pet and supporting text, bubble column, letter in water, diver and depth line, swimmer and scale.
- Mood is reflective, existential, humane, bookish, and quietly surreal rather than dramatic.

## Attention Geometry

- Quiet paper: 55%-78%.
- Main text: 10%-24%, usually upper-left, upper-center, left-middle, or right-middle.
- Image vignette: 18%-35%, usually center, lower-middle, or right-middle.
- Text-to-image gap: broad enough to keep both elements independent; do not connect them with heavy rules.
- Safe margins: about 8%-12% of canvas width.
- Optional micro marks: below 1% total area and low contrast.

## Layout Families

### `upper-text-lower-sea-strip` — Upper Text / Lower Sea Strip

- Place a compact text block around the upper third.
- Use a wide, low, ragged-edged sea vignette across the middle or lower-middle.
- Put one seated/writing figure, letter, hand, or small action at one end of the strip.
- Best for writing, persistence, courage, and the boundary between self and world.

### `upper-text-lower-organic-pool` — Upper Text / Lower Organic Pool

- Place text in the upper-left or upper-center.
- Use one oval, leaf-like, or irregular blue pool below it.
- Let one floating body, pair of hands, or single object sit inside the pool with faint ripples.
- Best for surrender, rest, fear, memory, and transformation.

### `left-specimen-right-passage` — Left Specimen / Right Passage

- Put one small portrait, pet, object, or photo specimen at left-middle.
- Set the main passage in a calm right-side column.
- Add optional translation or micro labels under the primary text.
- Best for rescue, companionship, tenderness, and human-scale reflection.

### `left-passage-tall-water-window` — Left Passage / Tall Water Window

- Put a short quote on the left.
- Use a tall torn blue window on the right with bubbles, a descending object, or a deep-water gradient made from halftone density rather than smooth digital gradient.
- Best for breath, depth, silence, and awareness.

### `upper-passage-lower-letter-sea` — Upper Passage / Lower Letter Sea

- Put the quote in the upper-left.
- Use a wide lower blue vignette with one paper letter, notebook, rope, or hand partly submerged.
- Best for courage, unsent words, beginning, and changing decisions.

### `source-fragment-depth-axis` — Source Fragment / Depth Axis

- Place one small reproduced page, note, or two-panel source fragment near the top.
- Place a narrow diver/person vignette below it on a long vertical depth line.
- Put one short quote and tiny measurement label to the sides.
- Best for documentary reading notes, measured depth, practice, and repeated attempts.

### `split-metaphor-relation` — Split Metaphor Relation

- Put the quote on the left and a conceptual scene on the right.
- Combine one person with one meaningful object or altered landscape, such as swimmer plus scale, writer plus endless paper, hands plus sandcastle, or body plus bubble trail.
- Keep both subjects inside one shared organic print field.
- Best for body image, effort, resilience, loss, and self-perception.

## Metaphor Engine

Choose one relation, not a list of symbols:

- breath ↔ bubbles, surface, pause, return
- fear ↔ depth, dark water, falling line, closed eyes
- courage ↔ first step, opened letter, reaching hand, one breath
- growth ↔ sandcastle, repeated practice, unstable structure
- writing ↔ paper trail, sea strip, endless page, ink current
- rescue ↔ pet, hand, small body, world-scale consequence
- body ↔ scale, shoreline, weight that the sea ignores
- memory ↔ submerged object, faded portrait, ripple, missing ink
- loss and celebration ↔ two shores, broken castle, receding tide

Keep the relationship visually legible without explanatory icons.

## Color and Reproduction

- Paper: warm ivory, oatmeal, pale straw, or aged cream.
- Primary ink: cobalt, ultramarine, Prussian blue, or indigo-blue.
- Secondary ink: gray-blue or charcoal-blue only.
- Use halftone dots, coarse toner, risograph grain, dry-brush gaps, faded edges, scan noise, and visible paper fibers.
- Let paper color show through highlights and skin. Avoid clean white digital cutouts.
- Use no contrasting red, yellow, green, pink, or orange accent unless explicitly requested.

## Typography

- Use medium-small Chinese Song/Ming-style text with generous line height.
- Keep one passage to 4-8 short lines or one compact paragraph.
- Set source/author 25%-40% smaller and lighter than the main text.
- Use faint Latin microtype only as texture: breath, depth, archive, sea level, time, or registration notes.
- Add at most one short rule, one crosshair system, or two tiny plus marks.
- Compose required text deterministically; never rely on image-model lettering.

## Prompt Patterns

### General Background Prompt

```text
Vertical 3:4 editorial zine on full-frame warm oatmeal handmade paper, visible fibers and age specks, 65% quiet negative space, flat orthographic scan with no border or mockup.

Reserve a clean text-safe block in [position]. Place one [wide strip / organic pool / tall window / left specimen / split relation] cobalt vignette in [position], occupying about [18%-35%], with rough brush-mask edges and paper-colored gaps.

Inside the vignette show one conceptual relation: [person/object/action] connected to [sea/breath/depth/writing/weight/rescue]. Render it as cobalt and gray-blue duotone photography or printed illustration with halftone dots, xerox softness, risograph grain, missing toner, and faded edges.

Quiet existential book-zine mood. Add only faint registration ticks and micro marks. No letters, no words, no logos, no watermark, no full-bleed scene, no clean rectangular photo, no multicolor palette, no glossy depth, no cinematic lighting, no commercial poster hierarchy.
```

### Pattern Notes

- For a supplied photo, preserve subject, pose, and camera direction; change only the print treatment and page composition.
- For text-only input, choose one metaphor relation from the engine and keep it physically plausible inside the surreal page logic.
- For a carousel, alternate layout family while preserving paper, cobalt ink, typography, and reproduction defects.

## Hard Avoids

- full-bleed ocean or lifestyle photography
- generic blue filter without halftone or paper integration
- clean photo rectangles, rounded cards, drop shadows, or nested panels
- more than one dominant metaphor or many small decorative objects
- smooth digital gradients, glossy skin, cinematic depth, high-resolution stock realism
- commercial headline, CTA, logo, fake publisher mark, or invented quotation source
- long unreadable copy, AI-generated text, decorative handwriting, or excessive multilingual filler
- anime, cute cartoon, sticker collage, neon, cyberpunk, or bright multicolor accents
- invented layout or recipe names; only the seven backticked canonical layout IDs above are valid
- hanging rice-paper or scroll displays, wall-gallery staging, red seals, ornate calligraphy headlines, and decorative English titles
