# Scene Element Extraction and Journal Collage

## Contents

- [Purpose](#purpose)
- [Reverse-Engineered Minimal-Zine Effects](#reverse-engineered-minimal-zine-effects)
- [Element Manifest](#element-manifest)
- [Transformation Library](#transformation-library)
- [Page Composition](#page-composition)
- [Prompt Compiler](#prompt-compiler)
- [Examples](#examples)
- [Failure Corrections](#failure-corrections)

## Purpose

Build the lower journal from the upper scene itself. Extract visual evidence first, then transform it into sparse paper collage material. Do not decorate the journal with generic tourism symbols after the fact.

Apply the logic of `gc-minimal-zine-poster-v0-1` at notebook-page scale:

- large quiet paper field
- one compact attention cluster
- one imageable anchor
- one saturated chromatic anchor
- sparse microtype and archive data
- old-photo, xerox, risograph, halftone, scan, or letterpress defects

Do not import its whole-poster canvas rule. The outer artwork remains a photographic diptych; only the open journal behaves like a pair of small minimal-zine pages.

## Reverse-Engineered Minimal-Zine Effects

| Source grammar | Visible effect | Adaptation inside the journal |
| --- | --- | --- |
| `typhoon-memory` | Grayscale square crop overlaps a saturated blue geometric semicircle; microtype hovers near the cluster | Pair one scene crop with one abstract shape derived from the object's motion, contour, or negative space |
| `moon-tide` | Two quiet adjacent photo panels create a conceptual relation; one thin text line crosses them | Use dual-panel fragments when two upper-scene elements form a meaningful pair |
| `pause-map` | Faint map contour supports rough cobalt letterpress type and scattered coordinates | Convert routes, facades, branches, rails, or river lines into pale structural tracings beneath a colored word or shape |
| `yellow-step` | A grayscale architectural crop sits beside a saturated rectangular abstraction of the same geometry | Rebuild a scene element twice: once as a faded crop, once as a bold color block preserving its proportion |
| `night-door` | A cobalt rectangle carries a tiny figurative trace while sparse archive text orbits it | Use a saturated carrier block when the scene has a strong doorway, window, sign, sky, water, or shadow field |
| `shore-pause` | A rough red block contains a white silhouette; callout lines label parts of the visual metaphor | Isolate a recognizable silhouette from the scene and embed it in a rough ink field with two or three tiny callouts |

The reusable principle is transformation with preserved identity, not copying these sample objects or colors.

## Element Manifest

Select three to five elements. Fill every column before writing the final prompt.

| Role | Upper source | Preserve | Lower treatment | Placement |
| --- | --- | --- | --- | --- |
| Primary anchor | Most distinctive object, figure, facade, vehicle, plant, dish, bridge, or exhibit | Silhouette, proportion, or crop | Torn photo, flat silhouette, old illustration, specimen, color block, xerox crop | Main cluster |
| Scene fragment | One localized view or object relation | Camera crop or adjacency | Faded photo panel, contact frame, dual-panel fragment | Beside or under anchor |
| Structural trace | Route, roofline, rail, branch, shoreline, shadow, steam, or repeating geometry | Direction and contour | Pencil tracing, map line, perforation, callout, translucent overlay | Through or around cluster |
| Color sample | Most useful visible scene hue | Exact color family and material association | Opaque risograph cutout, rough ink block, partial-color crop, bold type | 15%-35% of cluster |
| Microdata | Place, date, time, weather, price, platform, room, or short phrase | Meaning, not long wording | Typewriter caption, stamp, coordinates, tiny handwritten note | Loose edge of cluster |

For a person-led upper scene, expand eligible sources to the action prop, gesture trajectory, clothing hue or pattern, moving hair or fabric contour, foreground occlusion, and light pattern. Preserve identity if a portrait crop is used, but prefer event evidence over a decorative face silhouette.

Non-negotiable rules:

- Include the primary anchor plus at least two other roles.
- Derive at least three items directly from visible upper-scene content.
- Use contextual ephemera only after scene-derived items are defined.
- Add no more than one plausible ticket, receipt, or map if it was not actually visible above.
- Preserve a different identity cue for at least two elements; do not reduce every source to text labels.
- When a main person is present, derive at least two elements from the person's action, prop, clothing, foreground, or light interaction rather than from generic location ephemera.

## Transformation Library

### Direct Material Transformations

- **Torn photo crop:** retain the exact camera crop or object relation; mute only the photo, not the accent.
- **Xerox fragment:** flatten a texture or object into low-contrast black-gray with rough edge loss and toner wear.
- **Halftone window:** turn a localized scene texture into coarse dots inside a small rectangular or irregular window.
- **Old printed illustration:** redraw the object as an archival line engraving or softened single-ink illustration.
- **Object specimen:** isolate one object on cream paper with a tiny index label and minimal shadow.

### Abstract Identity Transformations

- **Flat silhouette:** preserve the object's recognizable outer contour in one opaque high-chroma ink.
- **Geometric reduction:** reduce an arch, stair, doorway, roof, cup, vehicle, or tree canopy to one or two blocks while keeping proportion.
- **Contour tracing:** retain a route, river, roofline, branch, rail, steam path, or horizon direction as a pencil or ink line.
- **Color carrier:** use a scene-derived door, sign, vehicle stripe, reflection, fabric, food, flower, or sky hue as the sole saturated field.
- **Relation diagram:** preserve the adjacency or overlap of two upper objects as dual panels, offset shapes, or a line connecting fragments.

### Reproduction Treatments

Choose one primary and one secondary texture:

- xerox softness
- risograph grain
- letterpress ink bleed
- halftone degradation
- scan noise and paper fibers
- softened film-print grain
- slight color misregistration
- torn or deckled edge

Do not stack every texture on every element.

## Page Composition

Treat the open spread as one continuous but gutter-aware canvas.

- Keep 45%-70% of the spread as visible cream paper.
- Let the main collage cluster occupy about 22%-40% of the open spread.
- Let the primary anchor occupy 35%-60% of that cluster.
- Let one saturated color anchor occupy about 15%-35% of the cluster or 4%-10% of the spread. It must remain visible at thumbnail size.
- Place zero or one counter-cluster on the facing page, no larger than half the main cluster.
- Allow one fragment to approach or cross the gutter only when page folds remain believable.
- Keep tiny type near the cluster; do not distribute labels evenly across every margin.
- Use tape, stamps, pencil marks, or registration dots as attachment evidence, not decoration.

### Layout Families

- **crop-plus-color:** faded scene crop beside a saturated geometric reduction of the same element
- **specimen-and-trace:** isolated object specimen with a contour line and microdata
- **dual-scene-relation:** two small related crops joined by one short phrase or line
- **silhouette-in-block:** recognizable scene silhouette cut from a rough saturated ink field
- **map-under-anchor:** pale route or structural contour beneath one bolder object or type anchor
- **irregular-cutout-orbit:** torn primary cutout with sparse letters, dots, or callouts around it

## Prompt Compiler

Write the extraction before describing the lower page:

```text
Extract these visible elements from the upper photograph before constructing the lower journal: (1) [PRIMARY SOURCE] preserving [IDENTITY CUE], (2) [SECONDARY SOURCE] preserving [IDENTITY CUE], (3) [STRUCTURAL OR COLOR SOURCE] preserving [IDENTITY CUE], plus optional (4-5) [MICRODATA OR TEXTURE]. These are the source materials for the page collage, not generic travel decorations.

Inside the open journal, transform element 1 into [PRIMARY PAPER TREATMENT] at [PLACEMENT]; transform element 2 into [SECONDARY TREATMENT] at [PLACEMENT]; transform element 3 into [TRACE / COLOR ANCHOR] at [PLACEMENT]. Preserve the named identity cue in every transformation. Use [LAYOUT FAMILY], 45%-70% quiet cream paper, one compact cluster, one [EXACT HUE] saturated ink anchor occupying 15%-35% of the cluster, sparse [TYPE MODE], and [PRIMARY / SECONDARY TEXTURES].
```

Use decisive correspondences:

- `the same steam curve above becomes a thin graphite contour below`
- `the bridge arch above becomes an orange rough-edged silhouette below`
- `the tea chair grid above becomes two offset green halftone rectangles below`
- `the train's blue stripe above becomes the only cobalt risograph block below`

Avoid vague correspondences:

- `include memories of the place`
- `add matching travel elements`
- `decorate with local ephemera`

## Examples

### Chengdu Teahouse

Manifest:

- gaiwan cup -> preserve lid-and-bowl silhouette -> botanical-green flat specimen
- plane-tree bark -> preserve mottled vertical texture -> xerox texture strip
- bamboo-chair rows -> preserve repeated diagonal grid -> pale halftone geometry
- humid green light -> preserve hue -> one opaque green risograph block
- morning time -> preserve meaning -> tiny typewriter timestamp

Page recipe: `specimen-and-trace`; green gaiwan specimen on the left page, bark strip and chair-grid tracing partly behind it, tiny time note near the cluster, facing page mostly blank.

### Metro Arrival

Manifest:

- train nose -> preserve rounded silhouette -> torn grayscale photo crop
- blue train stripe -> preserve hue and direction -> cobalt horizontal ink block
- platform edge -> preserve diagonal perspective -> graphite line crossing under the crop
- repeated station lights -> preserve rhythm -> four tiny registration dots

Page recipe: `crop-plus-color`; no generic metro map required unless it is the one optional contextual artifact.

### Night Bridge

Manifest:

- bridge arch -> preserve contour -> orange line illustration
- amber river reflection -> preserve vertical broken rhythm -> rough orange ink bars
- dark water -> preserve texture -> black-gray halftone window
- skyline spacing -> preserve relation -> two tiny offset photo rectangles

Page recipe: `map-under-anchor` or `dual-scene-relation`; keep more than half the right page blank.

## Failure Corrections

- If the journal shows generic tickets and maps, remove them and restate the three exact upper-scene sources first.
- If the lower page only repeats the whole upper photo, crop one distinctive element and transform two others into silhouette, trace, texture, or color.
- If the extracted object is no longer recognizable, state the preserved contour, proportion, orientation, and one adjacent cue.
- If the collage is too dense, keep the primary anchor, one secondary fragment, one structural trace, and one microdata line; remove all other pieces.
- If the accent is washed out, request `fully saturated opaque [HUE] risograph ink` and enlarge it to 15%-35% of the cluster.
- If the color feels unrelated, name its exact visible upper source and remove competing hues.
- If the page looks digitally composited, require real paper thickness, tape overlap, torn fiber edges, flash falloff, and subtle hand shadows.
- If the top and bottom blend, require two distinct photographs and one clean edge-to-edge horizontal seam.
