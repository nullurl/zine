# Poetry Share Layouts

Build the image map in [semantic-routing.md](semantic-routing.md), then use [gc-grammar.md](gc-grammar.md) and select one family below. The poem chooses the subject; the family supplies a coherent composition and print process.

## Format Rules

| Format | Use | Text-safe behavior |
|---|---|---|
| 4:5 | default social card | 60%-80% width with generous margins |
| 3:5 | pure GC poster | largest quiet field and smallest type/anchor cluster |
| 9:16 | story or lock screen | keep top/bottom UI zones quiet |
| 1:1 | two to five short lines | central counterpoint or lower-third poem block |

Use a carousel before shrinking the poem. Keep typography and material process consistent while allowing motif development across cards.

## Recipe Selection

1. Match the top-ranked motif and action to the style table in [semantic-routing.md](semantic-routing.md).
2. Choose the least generic family that can express the poem without inventing content.
3. Choose a layout ID whose geometry mirrors the poem's action: falling, crossing, repeating, enclosing, scattering, returning, or pausing.
4. Use `minimal-poem-specimen` only when the poem has no strong concrete image or relation.
5. Use a named legacy family such as `gravity-word`, `earth-ink`, or `cobalt-breath-poem` only when semantic evidence supports it or the user requests it.

## Recipe Families

### Minimal Poem Specimen

- Keep 72%-88% quiet paper with one poem-derived object, silhouette, printed specimen, or texture window occupying 7%-15%.
- Use `orbital-object-constellation`, `archive-specimen-grid`, or `type-image-counterpoint`.
- Best for aphoristic poems without a strong scene.

### Botanical Cyanotype

- Use one exact species or plant part implied by the poem: root, seed, stem, fruit, leaf, pollen, or pressed flower.
- Prefer `botanical-border-clearing` or `archive-specimen-grid`; keep the poem in the unexposed paper clearing.
- Use cyanotype blue or one plant-derived green with exposed-paper whites. Avoid generic floral ornament.

### Nocturne Photogram

- Use one moon, lamp, window, moth, shadow, roofline, or horizon relation from the poem.
- Prefer `luminous-dream-window`, `edge-weather-field`, or `type-image-counterpoint`.
- Use deep indigo/black with silver-gray bloom or one warm lamp accent; do not create a generic starry sky.

### Weather Index Risograph

- Translate wind, rain, snow, fog, heat, or thunder into pressure lines, directional marks, erased edges, droplets, or thermal stains.
- Prefer `edge-weather-field` or `soundwave-silence-band`.
- Let weather alter the paper boundary and stanza rhythm rather than becoming a scenic backdrop.

### Urban Xerox Grid

- Use one facade, bridge span, train window rhythm, platform edge, route, or industrial fragment.
- Prefer `urban-corridor-block`, `cartographic-path-axis`, or `split-time-diptych`.
- Use thresholded black/gray with one signal hue. Avoid panoramic city photography and fake signage.

### Domestic Still-Life Print

- Build one relation among supplied everyday objects: cup and cooling ring, chair and empty coat, lamp and closed book, bowl and fruit shadow.
- Prefer `domestic-table-shadow` or `orbital-object-constellation`.
- Use muted risograph or letterpress with one warm accent. Avoid catalog or lifestyle-ad styling.

### Archival Specimen File

- Use one memory artifact, absence outline, ticket edge, photograph ghost, name fragment, or object trace supported by the poem.
- Prefer `archive-specimen-grid`, `split-time-diptych`, or `film-contact-memory` treatment.
- Use perforations, ruled zones, dust, and misregistration without fake words, dates, or institutional marks.

### Cartographic Contour Zine

- Translate distance, travel, borders, paths, terrain, and search into contour, route, fault, or coordinate-like ticks.
- Prefer `cartographic-path-axis` or `split-time-diptych`.
- Use one land/route hue plus subdued contour lines; avoid literal tourist maps and unsupported place names.

### Sound-Silence Score

- Translate bell, radio, voice, echo, footsteps, pause, or repeated syntax into intervals and interrupted bands.
- Prefer `soundwave-silence-band` or `type-image-counterpoint`.
- Use deterministic poem typography; do not ask the image model to draw musical notation or words.

### Ink Gesture Field

- Use one brush event to carry force, rupture, impact, or a decisive verb.
- Prefer `edge-weather-field` or `type-image-counterpoint`; keep at least half the page quiet.
- Avoid decorative calligraphy. The complete poem remains conventionally typeset.

### Cut-Paper Geometry

- Translate paradox, enclosure, division, repetition, or analytical thought into folded planes and cut voids.
- Prefer `split-time-diptych`, `orbital-object-constellation`, or `type-image-counterpoint`.
- Use two paper tones and one saturated edge or plane; avoid clean corporate infographic styling.

### Chromatic Ghost Print

- Use one duplicated silhouette, object, place fragment, or shadow to express memory, ambiguity, or two temporal states.
- Prefer `split-time-diptych` or `luminous-dream-window`.
- Keep misregistration inside one hue family or a restrained two-ink opposition.

### Film Contact Memory

- Use a short sequence of two to four tiny scene/object fragments when the poem genuinely unfolds through time.
- Use `split-time-diptych` or a restrained contact strip inside the quiet field.
- Avoid scrapbook density, multiple captions, and invented dates.

### Material Swatch Poem

- Use textile, wood, paper, stone, metal, skin imprint, ash, or food surface when touch/material is central.
- Prefer `material-swatch-sequence` or `archive-specimen-grid` with two or three samples maximum.
- Show grain direction, fold, stitch, fracture, or wear; do not turn swatches into product cards.

### Luminous Storybook Window

- Use one small painterly portal for fable, wonder, childhood, impossible landscapes, or surreal transformation.
- Require `luminous-dream-window`; keep the portal irregular and under about 24% of the card.
- Preserve surrounding paper for the exact poem. Avoid full-bleed fantasy illustration.

### Concrete Type Constellation

- Use when repetition, naming, fragmentation, or stanza geometry is itself the strongest image.
- Prefer `type-image-counterpoint` or `soundwave-silence-band` with one small non-text anchor.
- Construct all type deterministically; never rely on image-model lettering.

### Gravity Word

- Enlarge only one supplied keyword and let echoes fall, rise, or orbit according to the poem's verb.
- Keep the word-and-echo system within 8%-22% and retain the full poem as readable text.

### Earth Ink

- Use absorbed black/sepia ink, folds, and one short supplied phrase for classical, severe, historical, or geological language.
- Add one ochre, mineral blue, or tomato-red registration mark. Do not make a generic calligraphy poster.

### Cobalt Breath Poem

- Use only when selected by the semantic image map or explicit request, then read [cobalt-breath.md](cobalt-breath.md).
- Water vocabulary may instead become a tide chart, shell specimen, wet page, harbor light, route, or reflective surface.

## Typography and Carousel

- Preserve exact line and stanza breaks unless reflow is necessary for the format.
- Use no more than two type families and three weights; keep normal Chinese letter spacing at `0`.
- Prevent punctuation from starting a line and keep attribution away from edges.
- Card 1 establishes the motif; middle cards evolve one relation; the final card resolves the poem and carries attribution.

## Hard Avoids

- unsupported sea, diver, anonymous body, rescue, or lonely-figure imagery
- generic full-bleed landscapes, galaxies, flower borders, or stock city scenes
- AI-generated gibberish, fake metadata, logos, CTAs, and sponsor marks
- several unrelated saturated colors or variants that only recolor the same layout
- dense scrapbook, excessive tape, decorative stickers, glossy mockups, hard shadows, 3D, neon, or anime
- low-contrast poem text, cropped attribution, orphan punctuation, or content inside mobile UI zones
