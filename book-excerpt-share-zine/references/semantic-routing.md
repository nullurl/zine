# Semantic Image and Style Routing for Book Excerpts

Use this reference before selecting a visual recipe. Derive the visual system from the supplied passage while preserving bibliographic truth.

## 1. Build an Evidence Map

```text
literal_entities: people, animals, plants, places, weather, objects, materials
actions_vectors: rise, fall, cross, wait, scatter, return, fold, burn, grow, echo
time_light: era, season, hour, shadow, natural or artificial light
senses: color, sound, touch, temperature, smell, taste
space_scale: room, street, landscape, microscopic, cosmic
argument_tension: cause/effect, freedom/control, memory/history, self/society
source_evidence: verified book, author, era, location, supplied page or image
```

Keep the passage's exact words beside every inferred motif. Do not invent period details from an unknown source.

## 2. Rank and Route

- Strongest: repeated concrete entities, decisive actions, a final turn, or a verified source artifact.
- Medium: time, place, weather, sensory evidence, or an object connecting the argument.
- Weakest: generic emotion or genre assumptions unsupported by the passage.
- Select one primary motif and zero to two supporting motifs.
- A single word such as sea, fear, body, city, flower, memory, science, or night never forces a recipe.
- Translate abstract arguments through passage evidence: `closed door + key`, `queue + clock`, `root + boundary line`, not a generic symbolic person.

Report before generation:

```text
Evidence map: [primary] / [supporting] / [action or argument relation]
Style: [style-family] / Layout: [layout-id] / Palette: [ink plan]
Source status: [confirmed fields / omitted unknown fields]
```

## 3. Subject Families

- celestial/time/light: horizon, shadow study, star chart, clock trace, eclipse disc
- weather/air/temperature: pressure lines, rain index, snow field, fog erasure, thermal stain
- botanical/seasonal: pressed specimen, root map, fruit cross-section, growth ring, seed inventory
- animal/ecological: species-specific trace, feather/wing dust, nest, shell, track, scale pattern
- domestic/material: lamp, cup, chair, garment, meal, tool, table shadow, fabric fold
- urban/transit/labor: facade xerox, route line, platform grid, bridge span, machine fragment
- language/book/archive: margin, redaction, page edge, index tab, punctuation field, document fragment
- terrain/travel/geology: contour map, path axis, mineral specimen, fault line, sediment band
- sound/music/silence: waveform gap, repeated rule, perforated rhythm, acoustic ring
- fire/energy/industry: singed fiber, ember point, wire diagram, metal reflection, smoke veil
- memory/dream/history: ghost exposure, contact strip, translucent overlap, absent-object outline
- science/math/system: calibration marks, orbital trace, specimen grid, network relation, measured interval
- body/gesture/health: hand pressure, eye crop, sleep imprint, pulse interval, garment/body trace
- water/breath/depth: tide chart, air pocket, wet page, shell, horizon, or cobalt vignette when dominant

## 4. Style Families

Choose one dominant family and, at most, one supporting texture.

- `botanical-cyanotype`: nature, ecology, growth, inheritance
- `nocturne-photogram`: night, solitude, vigilance, shadow
- `weather-index-risograph`: climate, uncertainty, time, change
- `urban-xerox-grid`: city, labor, systems, criticism, transit
- `domestic-still-life-print`: intimacy, family, ordinary ethics, memory
- `archival-specimen-file`: history, testimony, evidence, biography
- `cartographic-contour-zine`: travel, borders, exile, search, terrain
- `sound-silence-score`: music, speech, silence, repetition, pause
- `ink-gesture-field`: conflict, force, rupture, severe argument
- `cut-paper-geometry`: philosophy, paradox, comparison, abstraction
- `chromatic-ghost-print`: memory, ambiguity, unreliable narration
- `film-contact-memory`: recollection, sequence, place-based narrative
- `material-swatch-reading`: craft, clothing, touch, labor, material culture
- `scientific-annotation-plate`: science, observation, systems, classification
- `luminous-storybook-window`: fable, myth, wonder, surreal passages
- `editorial-source-strip`: concise excerpts with confirmed metadata
- `cobalt-breath-excerpt`: water/breath/depth is dominant or explicitly requested

## 5. Layout IDs

- `edge-weather-field`: passage in a calm core; weather enters from one edge.
- `botanical-border-clearing`: one specimen defines a corner and leaves a reading clearing.
- `orbital-object-constellation`: one object and sparse relation marks counterbalance the passage.
- `urban-corridor-block`: one architectural/transit fragment creates a side corridor.
- `domestic-table-shadow`: one low object relation with a long shadow axis.
- `archive-specimen-grid`: passage plus one specimen and restrained source zones.
- `cartographic-path-axis`: passage aligns with or opposes one path/contour line.
- `soundwave-silence-band`: one interrupted rhythm band separates reading zones.
- `split-time-diptych`: two temporal fragments share one paper field without framed cards.
- `scientific-plate-margin`: one measured specimen occupies a margin beside the passage.
- `luminous-dream-window`: one small irregular portal sits inside a large quiet field.
- `material-swatch-sequence`: two or three material samples form a restrained sequence.
- `type-image-counterpoint`: excerpt block and one small image anchor form a deliberate counterweight.

Named recipes may define additional layouts. Use them only after evidence ranking selects the recipe.

## 6. Diversity and Truth Gate

- The prompt must name the passage-derived primary motif, its action/argument, and why the selected layout expresses it.
- Do not add a person when an object, plant, weather event, animal, place, diagram, or sound carries the passage more precisely.
- Do not add sea, bubbles, diving, rescue, or floating unless selected from passage evidence.
- Do not fabricate cover art, author portrait, era, location, page number, publisher, or source notation.
- Across variants, change subject family, composition, texture process, and color logic.
- Generate text-free backgrounds; typeset the exact excerpt and confirmed metadata deterministically.
