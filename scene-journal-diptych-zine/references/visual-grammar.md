# Scene-Journal Diptych Visual Grammar

## Reverse-Engineered Structure

The reference set uses a stable two-part memory loop rather than a conventional book flat lay.

| Layer | Stable construction | Narrative function |
| --- | --- | --- |
| Whole canvas | Tall 3:4 or 4:5 portrait image, two edge-to-edge photographs, one clean horizontal seam, no outer border | Reads as one editorial zine page |
| Upper panel | Roughly 42%-55%; eye-level documentary photograph of a street, city, transit site, museum, landscape, or event | Shows the lived place and moment |
| Lower panel | Roughly 45%-58%; overhead or near-overhead tableau on deep navy cloth | Shows how the moment is remembered |
| Human anchor | Two natural hands enter from the lower corners and hold an open notebook | Adds bodily scale, intimacy, and authorship |
| Paper anchor | Cream or lightly aged two-page spread with visible gutter, page edges, and mild curl | Creates the analog archive |
| Element provenance | Three to five notebook pieces are transformed from visible upper-scene objects, crops, contours, textures, relations, or colors | Makes the journal a material reconstruction of the scene rather than generic travel decor |

## Fixed Visual DNA

- Preserve the hard horizontal diptych. The seam is clean and direct, not torn, framed, overlapped, or separated by a margin.
- Keep the upper photograph observational, imperfect, and naturally lit. It may feel like a compact-camera or 35 mm travel photograph.
- Keep the lower photograph tactile and more immediate: direct on-camera flash or a small hard light, mild falloff, realistic hand shadows, visible cloth weave, and brighter cream pages.
- Show one open journal centered in the lower panel. Keep both pages usable and the gutter unmistakable.
- Show exactly two hands. Let thumbs lightly stabilize page corners without hiding the collage.
- Use deep navy cloth as the principal lower background. It is a compositional field, not a decorative prop.
- Keep the journal assemblage edited: two to five main artifacts, a few marks, and at least one quieter paper zone.
- Build the assemblage from an explicit scene element manifest. Preserve a recognizable identity cue from each selected upper element when it reappears below.
- Apply Minimal Zine Poster v0.1 grammar inside the pages: one compact cluster, large cream-paper negative space, one saturated scene-derived anchor, sparse microtype, and old-print defects.
- Preserve analog defects: fibers, softened photo print, fold, tape, stamp, ink bleed, scuff, halftone, or slight misregistration.

## Scene-Derived Collage Vocabulary

Select three to five transformations from visible upper-scene sources.

- distinctive object or figure -> torn photo crop, isolated specimen, old printed illustration, or flat saturated silhouette
- facade, bridge, doorway, stair, cup, vehicle, plant, or roof -> contour tracing or geometric reduction
- bark, water, steam, pavement, textile, food, shadow, or reflected light -> xerox strip, halftone window, or rough ink field
- route, rail, river, shoreline, branch, queue, or repeated chairs -> pale structural line, map-like contour, perforation, or registration rhythm
- visible local hue -> one opaque risograph block, cutout, partial-color crop, or bold fragmented type
- date, time, weather, price, room, platform, or place -> short typewriter caption, stamp, or imperfect handwritten microdata

Add at most one contextual ticket, map, receipt, or label that is not directly visible above. Avoid placing all transformation types in one image.

## Variable Axes

Choose one option from each axis.

### Upper Scene

- city-street arrival
- public-transit passage
- museum or gallery visit
- waterfront or ferry crossing
- architecture encounter
- market, cafe, or everyday object stop
- landscape pause
- person-led travel moment
- family or companion event
- local character in action

### Upper Camera Character

- eye-level compact-camera snapshot
- slightly low architectural view
- centered documentary facade
- candid passing street frame
- quiet wide establishing shot
- mild motion-blurred transit frame
- intimate 24-35 mm action frame
- foreground-obscured medium-close portrait
- low or tilted human moment

### Journal Page State

- crop-plus-color / quiet facing page
- specimen-and-trace / microdata edge
- dual-scene-relation / one crossing phrase
- silhouette-in-block / sparse callouts
- map-under-anchor / blank grid counterpage
- irregular-cutout-orbit / one small counter-cluster

### Handwriting Density

- one short date and place
- two or three fragmentary notes
- one intimate paragraph plus tiny labels
- almost textless, with arrows and stamps only

### Accent

- transit yellow
- ticket red
- museum pink
- package orange
- map cobalt
- botanical green

Use one dominant accent and at most one minor secondary accent.

## Master Reverse Prompt

```text
Create a tall 3:4 vertical editorial photo-zine as two distinct edge-to-edge photographs stacked vertically, joined by one clean horizontal seam with no border and no gap. The upper panel occupies about 48% of the canvas and the lower panel about 52%. Keep both halves photographic and materially believable.

Upper panel: an eye-level documentary travel photograph of [PLACE / EVENT / SCENE], showing [RECOGNIZABLE SUBJECT], [WEATHER / TIME / SEASON], naturally available light, restrained muted city-film colors, slightly imperfect compact-camera framing, gentle 35 mm grain, no staged commercial polish.

From the upper photograph, extract [PRIMARY OBJECT] preserving [SILHOUETTE / PROPORTION / CROP], [SECONDARY FRAGMENT] preserving [TEXTURE / RELATION], and [STRUCTURAL OR COLOR ELEMENT] preserving [CONTOUR / DIRECTION / HUE], plus optional [MICRODATA]. These named upper-scene elements are the source materials for the lower collage; do not replace them with generic travel decorations.

Lower panel: a near-overhead photograph on deep navy woven fabric. Exactly two natural hands enter from the lower left and lower right and lightly hold open a cream-paper travel notebook centered in frame. Show the spine, gutter, page edges, slight page curl, realistic fingers and thumb placement, direct on-camera flash, localized bright paper highlights, soft hand shadows, and tactile cloth weave.

Inside the notebook, transform [PRIMARY OBJECT] into [TORN CROP / SILHOUETTE / SPECIMEN / COLOR BLOCK] at [PLACEMENT]; transform [SECONDARY FRAGMENT] into [HALFTONE / XEROX / DUAL PANEL] at [PLACEMENT]; transform [STRUCTURAL OR COLOR ELEMENT] into [CONTOUR / OVERLAY / OPAQUE RISOGRAPH ANCHOR] at [PLACEMENT]. Preserve every named identity cue. Keep 45%-70% quiet cream paper, one compact cluster, one controlled [EXACT SCENE-DERIVED HUE] anchor occupying 15%-35% of the cluster, sparse [HANDWRITING OR TYPE MODE], and [PRINT TEXTURES]. Use tape or stamps only as physical attachment evidence.

Mood: intimate travel memory, analog field diary, tactile personal archive, quiet European or East Asian independent editorial zine. Avoid blended or overlapping panels, torn divider, decorative frame, gap between images, floating-book mockup, clean product flat lay, extra hands, malformed fingers, closed book, hands covering content, generic scrapbook decoration, dense clutter, long perfect text, glossy stock-photo realism, logo, CTA, digital UI, 3D rendering, neon, heavy cinematic grading, and unrelated ephemera.
```

## Compiler Notes

Replace every bracketed slot with concrete visible content. Prefer nouns, preserved identity cues, transformation verbs, and spatial instructions over abstract adjectives. Name the visible source and its paper treatment, for example `the bridge arch visible above reappears as an orange rough-edged line illustration on the lower-left page` rather than `bridge memories`.

When the user supplies one photo:

- Use it as the upper panel's direct content reference.
- Extract three to five visible elements from its objects, shapes, crops, textures, routes, relations, colors, date, or weather.
- Preserve one identity cue for every element transformed below.
- Do not claim factual tickets or labels that contradict the source; generic ephemera is optional and limited to one supporting item.

When the user supplies several photos:

- Select the strongest establishing image for the upper panel.
- Convert one or two secondary images into scene-element crops, not automatic full-photo miniatures.
- Extract additional shape, texture, contour, relation, or color sources from the establishing image.
- Keep one paper zone quiet so the spread remains readable.

When the user supplies text only:

- Translate the brief into one plausible documentary scene.
- Define the scene's object, contour, texture, relation, and color sources before building the journal.
- Make the same defined sources appear above and below in transformed form.

## Example Recipes

### Museum Day

Upper panel: a natural photograph of one memorable exhibit with a distinctive silhouette, pedestal geometry, wall color, and floor shadow. Lower panel: turn the silhouette into a museum-pink flat cutout, the pedestal into a pale geometric block, and the floor shadow into a graphite contour; keep one tiny exhibit crop and a blank grid counterpage.

Element provenance: exhibit silhouette -> pink cutout; pedestal proportion -> pale block; floor-shadow direction -> graphite contour.

### Rainy Train Arrival

Upper panel: wet station platform at blue hour with a rounded train nose, cobalt stripe, diagonal platform edge, and repeated ceiling lights. Lower panel: a torn grayscale train-nose crop beside one cobalt ink stripe; the platform edge becomes a graphite diagonal and the lights become registration dots; keep a spare ruled right margin.

Element provenance: train crop, stripe hue and direction, platform perspective, and light rhythm all come directly from above.

### Market Object Memory

Upper panel: an everyday market scene with one recognizable bottle, package, flower, or food object, plus a repeated stall pattern and one strong package color. Lower panel: isolate the object as a specimen, reduce the stall pattern to a pale halftone grid, and use the package hue as one rough ink block; add a date and keep the facing page nearly blank.

Element provenance: object silhouette, stall rhythm, and package hue appear below through three different material treatments.

## Failure Corrections

- If the result becomes one surreal composite, add `two separate photographs; the upper scene never continues into the lower tabletop`.
- If a white margin appears, add `edge-to-edge crop; the two panels touch directly at the seam`.
- If the lower panel becomes a digital mockup, add `real photographed cloth, real paper thickness, realistic flash falloff and hand shadows`.
- If the journal is too dense, reduce to three artifacts and make one page 40%-60% blank.
- If the connection is generic, remove unrelated ephemera and state three exact `upper source -> preserved cue -> lower treatment` mappings.
- If the journal only duplicates the whole upper photo, isolate one primary object and transform two other scene elements into a contour, texture, relation, or color field.
- If the transformed element loses identity, restate its silhouette, proportion, orientation, crop, or adjacent object.
- If hands fail, state `exactly two anatomically plausible adult hands, five fingers per hand, no jewelry unless requested, thumbs resting at the outer lower page corners`.
- If the upper scene dominates, restore a near-even 48/52 split and enlarge the journal to occupy 72%-88% of the lower panel width.

## Image-Level Checklist

- One canvas, two photographs, one seam.
- Upper image establishes where or what happened.
- Lower image shows navy cloth, two hands, and one open cream journal.
- Three to five extracted elements are declared before the lower collage.
- At least three lower pieces can be traced to visible upper sources through preserved identity cues.
- 45%-70% quiet paper surrounds one compact main cluster.
- One dominant scene-derived high-chroma anchor; subdued supporting photos, type, and marks.
- Generic supporting ephemera is absent or limited to one item.
- Natural light above, direct flash below.
- Mild grain and analog defects across both halves.
- No decorative frame, digital mockup, commercial copy, or unrelated clutter.
