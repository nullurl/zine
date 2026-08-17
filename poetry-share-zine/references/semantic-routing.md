# Semantic Image and Style Routing for Poetry

Use this reference before selecting a visual recipe. The purpose is to derive the poster from the supplied poem rather than forcing the poem into a familiar motif.

## 1. Build an Image Map

Extract evidence under these fields. Keep the original words beside every inference.

```text
literal_entities: people, animals, plants, places, weather, objects, materials
actions_vectors: rise, fall, cross, wait, scatter, return, fold, burn, grow, echo
time_light: dawn, noon, dusk, night, season, shadow, artificial light
senses: color, sound, touch, temperature, smell, taste
space_scale: room, street, field, mountain, sky, microscopic, cosmic
emotional_tension: absence/presence, stillness/motion, memory/now, shelter/exposure
formal_cues: repetition, pause, fracture, parallel lines, circular return, abrupt turn
```

Do not treat an abstract noun as a picture by itself. Translate it through the poem's own concrete evidence and verbs.

## 2. Rank Motifs

- Give strongest weight to concrete nouns or images repeated in the title/body, decisive verbs, and the final turn.
- Give medium weight to time, weather, sensory details, and an object that connects two lines.
- Give weak weight to generic emotions without physical evidence.
- Select one primary motif and zero to two supporting motifs. A supporting motif may alter texture, layout, or light without becoming another scene.
- A single word such as sea, body, fear, courage, night, flower, or memory never forces a recipe.
- Prefer the least generic relation that is still grounded in the poem: `key + unopened room`, `moth + lamp`, `train window + receding orchard`, `shadow + noon wall`, not `lonely person`.

Report before generation:

```text
Image map: [primary] / [supporting] / [action relation]
Style: [style-family] / Layout: [layout-id] / Palette: [ink plan]
```

## 3. Motif Families

| Evidence in poem | Useful visual anchors | Avoid the default cliché |
|---|---|---|
| sky, moon, stars, dawn, eclipse, shadow | photogram circle, horizon notch, star chart, long cast shadow | generic galaxy wallpaper |
| wind, rain, snow, fog, thunder, heat | pressure lines, rain index, erased edge, condensation, scorched fiber | stock weather scene |
| tree, leaf, seed, flower, moss, fruit, season | pressed specimen, root map, pollen dots, growth ring, petal shadow | decorative floral border |
| bird, moth, fish, cat, insect, animal trace | one species-specific silhouette, wing dust, track, nest fragment | mascot or cute sticker |
| room, window, lamp, cup, chair, clothing, food | domestic still-life fragment, inventory label, fabric fold, table shadow | lifestyle product photo |
| street, building, bridge, train, traffic, factory | xerox facade, route line, platform grid, window rhythm, signage block without text | cinematic city panorama |
| letter, book, name, language, erasure | torn margin, redaction, ruled line, punctuation constellation, page edge | hanging scroll or fake cover |
| mountain, stone, soil, desert, river, path | contour map, mineral swatch, fault line, sediment band, path axis | full scenic landscape |
| bell, song, radio, footsteps, silence, echo | waveform, concentric interruption, punched holes, staff-like spacing | illustrated musical notes |
| fire, smoke, ash, sun, metal, electricity | singed edge, ember dot, thermal bloom, wire diagram, reflective foil | dramatic flames |
| dream, memory, childhood, distance, loss | misregistered photo ghost, contact sheet, translucent overlap, absent-object outline | sepia nostalgia collage |
| clock, machine, number, science, orbit, map | calibration marks, exploded diagram, orbital trace, specimen grid | generic sci-fi interface |
| skin, hand, eye, hair, sleep, illness | crop, pressure print, gesture trace, fabric/body imprint | anonymous floating body |
| sea, tide, breath, depth, floating | tide chart, shell, wet page, air pocket, horizon, or cobalt vignette when dominant | automatic diver silhouette |

## 4. Style Families

Choose one dominant family. A second family may contribute texture only.

| Style family | Best for | Visual language |
|---|---|---|
| `botanical-cyanotype` | plants, summer, growth, fragility | pressed silhouettes, cyanotype bloom, specimen labels |
| `nocturne-photogram` | night, moon, lamp, solitude, shadow | deep ink field, exposed-paper halos, soft silver grain |
| `weather-index-risograph` | wind, rain, snow, heat, changing time | directional marks, measured bands, dry ink loss |
| `urban-xerox-grid` | cities, transit, labor, architecture | thresholded fragments, route geometry, strict grid |
| `domestic-still-life-print` | rooms, intimacy, ordinary objects, food | one object relation, table shadow, muted spot color |
| `archival-specimen-file` | memory, history, evidence, names | catalog spacing, ghost image, perforation, restrained stamps without fake text |
| `cartographic-contour-zine` | travel, distance, terrain, search | contour lines, path axis, coordinates as non-text ticks |
| `sound-silence-score` | music, voice, echo, pause | waveform gaps, repeated rules, punched rhythm |
| `ink-gesture-field` | force, conflict, sudden motion, severe verse | one controlled brush event, splintered edge, absorbed ink |
| `cut-paper-geometry` | conceptual, playful, analytical, paradox | geometric voids, folded planes, hard/soft counterpoint |
| `chromatic-ghost-print` | dream, unstable memory, double meanings | two-pass misregistration within one hue family, blurred duplicate |
| `film-contact-memory` | sequences, childhood, travel, recollection | one short contact strip, frame gaps, dust and exposure marks |
| `material-swatch-poem` | touch, clothing, craft, body memory | textile/paper/mineral swatches, stitch or grain direction |
| `luminous-storybook-window` | fable, wonder, surreal nature | small painterly portal surrounded by quiet paper |
| `concrete-type-constellation` | repetition, language, naming, formal poems | deterministic type as spatial structure plus one small image anchor |
| `cobalt-breath-poem` | water/breath/depth is the dominant relation or explicitly requested | warm paper, one organic cobalt halftone vignette |

## 5. Layout IDs

- `edge-weather-field`: text in a calm core; weather marks enter from one edge.
- `botanical-border-clearing`: one specimen crosses a corner; the poem occupies the clearing.
- `orbital-object-constellation`: one object plus sparse orbit/echo marks; text counterbalances it.
- `urban-corridor-block`: architecture or transit fragment forms one side corridor.
- `domestic-table-shadow`: one low object relation and a long quiet shadow axis.
- `archive-specimen-grid`: one image specimen and two or three ruled metadata zones.
- `cartographic-path-axis`: text follows or opposes one path/contour axis.
- `soundwave-silence-band`: one interrupted horizontal or vertical rhythm band.
- `split-time-diptych`: two temporal fragments share one paper field without card frames.
- `luminous-dream-window`: one small irregular portal inside a large quiet field.
- `material-swatch-sequence`: two or three tactile samples form a restrained sequence.
- `type-image-counterpoint`: deterministic type structure and one small image anchor oppose each other.

Named recipes may define additional canonical layouts. Use those only after semantic ranking selects that recipe.

## 6. Diversity Gate

- The prompt must name the poem-derived primary motif, its action, and why the layout expresses that action.
- Do not add a person when the poem's strongest evidence is an object, plant, weather event, animal, place, or sound.
- Do not add sea, water, bubbles, a diver, rescue, or depth unless they are supported by the poem and selected as the primary relation.
- Across variants, change the motif family, composition system, texture process, and color logic; moving the same vignette is not a new design.
- Keep all required words out of the generated background and typeset them deterministically afterward.
