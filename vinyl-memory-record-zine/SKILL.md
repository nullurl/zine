---
name: 黑胶记忆
description: "【黑胶记忆 / vinyl-memory-record-zine】 Generate vinyl record memory package prompts and matching raster images. Use when the user gives a personal memory, trip, event, pet story, food moment, concert, seaside day, photo, short sentence, or emotional brief and wants it transformed into a fictional vinyl album flatlay with translucent marbled records, album sleeve, back cover, track list, labels, barcodes, delicate bilingual typography, soft paper texture, and warm editorial product photography."
---

# Vinyl Memory Record Zine

Turn the user's content into both:

1. a final image-generation prompt, and
2. a generated raster image made from that prompt.

## Source Grammar

This style fuses Minimal Zine Poster v0.1's restraint with a vinyl packaging system. The references convert casual memories into fictional record releases: a square album cover, one or two translucent vinyl discs, a back cover or insert card, soft colored tabletop, and small poetic metadata.

Stable visual traits:

- **Frame:** square or near-square editorial flatlay, usually 1:1 or 4:3, viewed from above with soft product shadows.
- **Objects:** album sleeve, back cover, inner card, one or two transparent/marbled vinyl records, round center labels, barcode, catalog code, track list, side A/side B metadata.
- **Layout:** three- or four-object package system: sleeve upper-left, record upper-right, record lower-left, back cover lower-right. Objects are neatly spaced, grid-aware, and slightly offset.
- **Surface:** soft matte tabletop in butter yellow, sea green, muted blue, cream, pale beige, or warm sand; no black void and no hard studio drama.
- **Memory translation:** personal events become album concepts, track names, label names, catalog IDs, small icons, and cover imagery.
- **Cover imagery:** a simplified illustration or photo-based motif from the memory: cake slice and candles, shaved ice, rainy festival tray, sparkling sea, gelato, small animals, mountain, umbrella, rail, hand-held object, or abstract waves.
- **Vinyl material:** translucent clear vinyl with subtle radial grooves, cloudy milk-white plastic, pastel marbling, faint red/blue/yellow streaks, transparent rim, center label in a matching accent color.
- **Typography:** delicate serif, narrow sans, small Japanese/Chinese/English bilingual captions, track lists, side labels, edition numbers, catalog codes, barcode, tiny legal text.
- **Mood:** tender, nostalgic, small-label, indie record release, summer diary, memory archive, soft commercial editorial, carefully designed but not glossy luxury.

Never include the chat prompt bubble, phone UI, "Vinyl Image Generator" label, or screenshot interface. Those are source context, not part of the final image.

## Mode Policy

Use **Standard Mode** for all generation. Compile only renderable visual details into the final prompt. If the user supplies one or more photos, treat them as memory references: extract subject, location, colors, and emotional cues; do not preserve private faces or exact text unless the user explicitly asks.

## Standard Prompt Compiler

Write the final prompt as four compact paragraphs in this order:

1. **Canvas and Flatlay**
   - State frame ratio, tabletop color, overhead product-flatlay view, and object count.
   - Specify the package layout: sleeve, record(s), back cover, insert card.

2. **Memory-to-Album Concept**
   - Convert the user's memory into a fictional album title, artist/label name, and cover motif.
   - Mention the central object or scene translated into record packaging art.

3. **Record and Print System**
   - Define vinyl material, marbling, center label color, sleeve art, back-cover tracklist, barcode, catalog code, edition number, and tiny metadata.
   - Specify typography behavior and any bilingual text.

4. **Color, Texture, Mood, Avoids**
   - State the palette, paper/plastic textures, print process, lighting, and negative constraints.

Keep exact in-image text short. Use believable fictional names and catalog codes. Avoid long readable prose because image models distort it.

## First-Principles Fields

Every prompt must answer:

1. **What is the package system?**
   - album sleeve plus vinyl disc plus back cover or insert; optionally a second disc.

2. **Where are the objects?**
   - use a clear flatlay arrangement. Avoid pileups, messy collage, and perspective-heavy product mockups.

3. **What memory becomes the album concept?**
   - identify a concrete memory anchor: cake, cats, seaside inn, zoo trip, festival rain, sea sparkle, gelato, ducks, sunset, train, food, friends.

4. **What is on the cover?**
   - one simple motif, not a full narrative scene. Use subtle illustration, print texture, or a restrained photo crop.

5. **What does the vinyl look like?**
   - translucent clear or milky disc, visible radial grooves, pastel marbling, matching center labels, side A/side B variants.

6. **What print details make it believable?**
   - tracklist, barcode, catalog code, edition number, label logo, small table/grid lines, registration marks, legal text, side labels.

7. **What is the color logic?**
   - soft tabletop plus cream paper plus 1-3 memory-linked accent colors. Colors can be stronger than Minimal Zine Poster, but should remain gentle and editorial.

8. **What should be avoided?**
   - no phone UI, prompt bubble, chat screenshot, generic stock mockup, CD jewel case, black background, glossy luxury ad, crowded props, hands unless user asks, or real brand copying.

## Memory Translation Engine

Translate memory details into vinyl-specific artifacts:

- **Location:** becomes label name, small map mark, venue line, or catalog prefix.
- **Food:** becomes cover motif, track title, label icon, or center-label color.
- **Weather:** becomes vinyl marbling, wave/rain lines, sleeve texture, or track names.
- **Friends:** becomes band/artist name, edition note, liner text, or side names.
- **Pets:** becomes icon marks, track titles, tiny sleeve illustration, or label mascot.
- **A date:** becomes catalog number or tiny edition stamp.
- **A photo:** becomes a simplified cover crop, halftone image panel, or illustrated motif.
- **A strong emotion:** becomes album title and palette temperature.

Use invented fictional text when the user gives only a memory. Do not expose private names, addresses, phone numbers, tickets, or exact photo metadata unless explicitly supplied for use.

## Variation Engine

Choose one option from each axis before writing the prompt.

### Layout Family

- **classic-four-piece:** sleeve upper-left, vinyl upper-right, second vinyl lower-left, back cover lower-right
- **sleeve-and-disc-pair:** sleeve left, one large vinyl right, small insert below
- **diagonal-release-grid:** objects form a soft diagonal with large tabletop gaps
- **double-vinyl-edition:** two translucent discs with different center labels plus sleeve/back card
- **cover-led-system:** large sleeve dominates, record and back card support it
- **back-cover-led-system:** tracklist card is prominent with vinyl discs as secondary objects
- **single-disc-minimal:** one sleeve and one disc with abundant tabletop negative space
- **festival-archive-release:** sleeve, record, ticket-like insert, tracklist card, and barcode
- **food-memory-release:** food illustration/photo cover plus warm clear vinyl and recipe-like tracklist
- **seaside-label-release:** wave motifs, pale blue vinyl, shell/rail/sunlight details

### Memory Motif

- cake slice with candles
- shaved ice or dessert bowl
- gelato cones
- seaside sparkle or wave field
- rainy festival tray
- small animal icons
- train window or station sign
- inn room window
- picnic table
- mountain silhouette
- umbrella and raindrops
- tiny hand-drawn map
- abstract sound-wave lines
- sunlit railing or pier

### Vinyl Material

- clear milky vinyl with yellow marbling
- translucent aqua vinyl with coral streaks
- smoky grey-blue vinyl with dark radial veins
- clear vinyl with red and teal clouds
- pale sea-glass vinyl
- warm cream transparent vinyl
- cloudy white vinyl with honey streaks
- frosted vinyl with rain-blue streaks

### Typography Mode

- delicate serif album title
- narrow sans all-caps catalog text
- Japanese title plus tiny English subtitle
- Chinese title plus small English metadata
- Italian-style serif title and tracklist
- soft lowercase indie label type
- typewriter catalog details
- gridded back-cover track list
- tiny side A/side B label text
- handwritten catalog note as accent only

### Print Detail Mode

- barcode and catalog number
- edition number such as 127/300
- tiny label logo
- registration cross marks
- thin tracklist rules
- side A and side B panels
- small legal text block
- miniature waveform or wave line
- recipe-like ingredient list
- little icon set derived from memory

### Surface Palette

- butter yellow tabletop
- deep sea green tabletop
- muted blue tabletop
- warm sand tabletop
- pale cream tabletop
- soft grey-beige tabletop
- dusty aqua tabletop
- late-afternoon peach tabletop

### Mood Mode

- small birthday memory
- seaside summer diary
- rainy festival afterglow
- gelato travel postcard
- quiet pet celebration
- nostalgic friend trip
- soft indie label release
- warm after-sunset memory
- gentle food-and-music archive
- private vacation soundtrack

## Color Engine

- Use one dominant tabletop color, one paper color, and 1-3 accent colors from the memory.
- Match vinyl marbling to the cover: cake uses honey/yellow/coral; sea uses aqua/teal/coral; rain uses blue/grey/orange; gelato uses cream/aqua/raspberry.
- Keep colors matte and printed. Avoid neon, metallic chrome, hard gradients, and saturated corporate palettes.
- The vinyl may be translucent and luminous, but the whole image should remain soft and tactile.
- If the user asks for monochrome, keep packaging cream/black/grey and use translucent smoke vinyl.

## Standard Prompt Shape

Use this exact shape:

```text
Square or 4:3 editorial product flatlay of a fictional vinyl record memory package on a [surface palette] matte tabletop, overhead view, soft natural shadows, [layout family] with [object list], neat spacing, no phone UI, no chat bubble, no screenshot elements.

For [user memory], invent an album concept titled "[short title]" by [fictional artist/label]. Use [memory motif] as the sleeve cover art, simplified into restrained print/illustration/photo texture; include a matching back cover or insert card with side A/side B track names inspired by the memory.

Show [vinyl material] with visible radial grooves, translucent rim, marbled streaks, and center labels in [label colors]. Add [typography mode], [print detail mode], tiny catalog code, edition number, barcode, label logo, thin rules, and small bilingual metadata. Keep text believable but short.

Palette: [tabletop/paper/accent palette], matte cream paper, translucent vinyl plastic, subtle risograph/offset print grain, gentle product photography. Tender indie record release mood, memory archive feeling. Avoid real brand copying, phone screenshot UI, prompt bubble, glossy luxury mockup, crowded props, hard shadows, neon, 3D render, CD jewel case, and full narrative scene.
```

## Workflow

1. Parse the user's content.
   - Identify the memory subject, place, people/pets, food, weather, date, and emotional tone.
   - If photos are supplied, extract visual motifs and palette; do not require literal photo reproduction.

2. Invent album metadata.
   - Create one short album title, one fictional artist or label name, one catalog code, and 4-8 track names.
   - Keep text compact. Use bilingual text only when it fits the memory or user language.

3. Select a variation recipe.
   - Pick layout family, memory motif, vinyl material, typography mode, print detail mode, surface palette, and mood.
   - For batches, vary layout, surface color, vinyl material, and cover motif.

4. Write the final prompt.
   - Use the Standard Prompt Shape.
   - Specify object positions, vinyl material, sleeve art, back-cover details, and avoid-list.
   - Explicitly exclude chat bubbles and screenshot UI.

5. Generate the image.
   - Use image generation by default.
   - If the user asks for prompt-only, return only the prompt and recipe.
   - If the result includes UI, a chat bubble, or a phone screenshot, regenerate once with stronger "only the vinyl package flatlay" wording.

6. Return the image and prompt.

## Negative Constraints

Always avoid:

- chat bubble, app screenshot, phone UI, "Vinyl Image Generator" label, browser frame, or social media overlay
- copying real record labels, real album art, real logos, real barcodes tied to existing products, or private personal data
- CD jewel case, cassette tape, streaming-player UI, playlist screenshot, or digital music app
- generic black vinyl only, unless the user explicitly asks for black vinyl
- glossy luxury mockup, hard studio shadows, extreme perspective, desk clutter, hands, plants, coffee, or lifestyle props
- busy scrapbook collage, stickers, cute cartoon overload, anime, 3D render, neon, cyberpunk, or gradient poster background
- full narrative illustration on the tabletop; keep the narrative inside the package art
- long clean readable paragraphs; use tiny liner notes as texture

## Output Format

````markdown
**Generated Image**

![Vinyl memory record package](absolute-image-path-or-rendered-image)

**Final Prompt**

```text
[final prompt used for image generation]
```

**Notes**

- Mode: Standard
- Recipe: [layout / motif / vinyl material / typography / print detail / palette / mood]
- [one short note about how the memory became a fictional record release]
````

If generated images render directly without a file path, show the image normally and still include the final prompt.

## Quality Gate

Before finalizing, check:

- Did the image show a vinyl record package flatlay, not a poster or screenshot?
- Are there at least two physical package objects such as sleeve, record, back cover, or insert?
- Does the vinyl look translucent, grooved, and marbled rather than a flat circle?
- Does the cover motif clearly translate the user's memory?
- Are tracklist, barcode, catalog code, side labels, and center labels present?
- Is the tabletop soft, matte, and editorial?
- Does typography feel like a small indie record release?
- Did the prompt avoid real brands, private data, phone UI, chat bubble, and screenshot elements?
- Did you actually generate the image unless the user asked for prompt-only?

## Example Requests

- "Use $vinyl-memory-record-zine for my two cats' birthday and cake memory."
- "Use this seaside photo and make a fictional transparent-vinyl album package."
- "Turn my Fuji Rock rainy festival memory into a vinyl record release image."
