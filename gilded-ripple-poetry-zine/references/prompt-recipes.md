# Prompt Recipes

Use one recipe per image. Do not combine multiple layout families unless the user asks for a series.

## Recipe Fields

Before writing the final prompt, choose:

- Layout family
- Central subject
- English title
- Subtitle band
- Chinese title placement
- Water palette
- Glimmer accent
- Print texture

## Layout Families

### ripple-title

Use for rivers, lakes, rain, quiet water, memory, geese, and general poetic themes.

- Large ornate English title at top.
- Central rectangular water panel, 40%-50% page height.
- Blue ripples, small birds, reeds, or floating flowers.
- Vertical Chinese title on left margin.
- Subtitle band below panel.
- Dotted rules and tiny metadata at bottom.

Prompt phrase:
`a strict vintage zine poster grid with an ornate English calligraphic title at the top, a central rectangular aqua-water risograph panel, a vertical Chinese title along the left margin, and a bold all-caps serif subtitle band below`

### dusk-coast

Use for coast, island, windmill, sunset, orange light, travel, and evening.

- Wide horizon panel with coast, windmill, boat, island, or sea wall.
- Warm gold or orange sun reflection.
- Bottom-right Chinese title block.
- Top title can be script or engraved serif.
- Oval label and tiny coastal coordinates as decorative microtext.

Prompt phrase:
`a vintage cream-paper coastal poster with a central sunset sea-panel, small windmill or boat silhouette, gold reflection on turquoise water, ornate top title, and a bottom-right Chinese title block`

### bird-water

Use for geese, cranes, gulls, ducks, swans, migration, pond, and river.

- Birds glide through the central water panel.
- Reeds, small ripples, or flower clusters support the panel.
- English title can be lyrical and long, but ask the model for ornamental title behavior rather than exact long text.
- Chinese type appears as a vertical side title plus tiny caption.

Prompt phrase:
`geese gliding over blue-green water inside a printed illustration panel, surrounded by cream paper, sage typography, vertical Chinese editorial title, tiny dotted rules, and a gold ripple accent`

### fish-cloud-sea

Use for surreal water phrases, "fish water cloud sea", dream, floating, and imaginary landscapes.

- Fish silhouettes move through cloud-like wave bands.
- Central panel can look like a poetic map or old science plate.
- Add pale cloud sea, aqua water, golden circular mark, and small annotation arrows.
- Keep surrealism quiet, not fantasy-drama.

Prompt phrase:
`a poetic printed panel where fish silhouettes swim through cloudlike sea bands, aqua and pale blue waves, one small golden sun seal, strict vintage editorial typography, and Chinese vertical annotations`

### floral-pond

Use for spring, rain garden, botanical themes, tropical plants, flowers, lotus, reeds, and humid green moods.

- Water panel includes pond plants, petals, leaves, or wet stems.
- Botanical margin marks or small flower icons can appear.
- Palette can shift toward light green, teal water, cream paper, and gold pollen-like dots.
- Keep plant details printed and editorial, not lush photo realism.

Prompt phrase:
`a cream-paper botanical water zine poster with a central teal pond panel, printed leaves and flowers, ornamental English title, short Chinese side title, sage-green type, dotted botanical rules, and warm gold pollen glimmers`

### oval-label-poster

Use when the user asks for editorial, label, collection, archive, menu, or literary cover feeling.

- Central water panel is smaller, with an oval label and strict rules.
- More metadata and typographic ornaments are allowed.
- Keep the page elegant and readable at thumbnail scale.

Prompt phrase:
`an ornate small-press literary poster with a central blue-water plate, oval label, condensed serif metadata, dotted rules, vertical Chinese title, and a large engraved English heading`

## Title System

When the user provides exact text, use it as the main title if short enough.

When no title is provided:

- English title: make a poetic 2-5 word phrase from the subject. Examples: `Ripple Garden`, `Golden Water Notes`, `Cloud Sea Almanac`, `Pond Light`.
- Subtitle band: make a short all-caps phrase. Examples: `WHERE LIGHT DRIFTS`, `A SMALL WATER RECORD`, `NOTES ON BLUE WEATHER`.
- Chinese title: use a short Chinese poetic title derived from the user's theme. Avoid long sentences.

For image prompts, do not demand perfect long text. State that large title typography should be decorative and partially imperfect if needed.

## Prompt Skeleton

Use this structure:

```text
Vertical 4:5 cream aged-paper poster, flat scanned small-press print, visible fibers, no mockup. [Layout family] with [title placement], [central panel size], and ordered margins.

Central illustration panel: [subject], [water/coast/pond treatment], [supporting objects], risograph/lithograph grain, soft worn edges, mild ink misregistration.

Typography: ornate English [script/engraved/serif] title reading "[short title]" at the top, bold all-caps serif subtitle band reading "[short subtitle]", short Chinese [vertical side title/bottom-right title block], tiny editorial metadata, dotted rules, oval label or small seals, no paragraphs.

Palette: bright cream paper, sage/olive typography, aqua/teal/blue water, [gold/marigold/orange] glimmer accent on ripples or sun reflection, restrained two-to-three-color print with warm black-brown speckles.

Mood: poetic vintage water zine, literary, nostalgic, hand-printed, bright but aged. Avoid modern travel ad, glossy mockup, UI, stickers, Polaroid scrapbook, neon, cartoon, cinematic full-bleed scene, logo, CTA, long clean text.
```

## Batch Variation

For multiple outputs, vary:

- one layout family
- one water subject
- title position
- Chinese title position
- glimmer accent scale
- border and label marks

Do not vary into unrelated styles. All images should still read as the same Gilded Ripple Poetry Zine system.
