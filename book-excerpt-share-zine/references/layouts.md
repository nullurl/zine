# Book Excerpt Share Layouts

Build the evidence map in [semantic-routing.md](semantic-routing.md), then use [gc-grammar.md](gc-grammar.md) and select one family below. The passage determines the visual subject; the family supplies a coherent composition, print process, and source hierarchy.

## Source Record

```text
excerpt: exact supplied quotation
book_title: confirmed title or omitted
author: confirmed author or omitted
translator: confirmed translator or omitted
edition: confirmed edition/publisher or omitted
location: confirmed chapter/page or omitted
reader_note: user commentary, explicitly labeled
```

Never complete missing fields unless the user asks for research and the source is verified.

## Format Rules

| Format | Use | Layout behavior |
|---|---|---|
| 4:5 | default social card | excerpt plus one compact source line |
| 3:5 | pure GC poster | largest quiet field and restrained anchor |
| 9:16 | story or longer passage | quiet top/bottom UI zones |
| 1:1 | one short quotation | central counterpoint with minimal metadata |

Move to a carousel before reducing body text below comfortable mobile size.

## Recipe Selection

1. Match the top-ranked evidence and action/argument to a style family in [semantic-routing.md](semantic-routing.md).
2. Choose the least generic family that preserves source truth and reading comfort.
3. Choose a layout ID whose geometry mirrors the passage: sequence, contrast, enclosure, movement, interruption, classification, or return.
4. Use `minimal-excerpt-specimen` only when the passage has no strong concrete relation.
5. Use `open-book-reading` only when a supplied page or physical reading act is primary.
6. Use named families such as `editorial-source-strip` or `cobalt-breath-excerpt` only when evidence or explicit direction supports them.

## Recipe Families

### Minimal Excerpt Specimen

- Keep 62%-82% quiet paper with one source-grounded object, old illustration, texture window, or diagram occupying 7%-16%.
- Prefer `archive-specimen-grid`, `orbital-object-constellation`, or `type-image-counterpoint`.

### Botanical Cyanotype

- Use one exact plant/species, root system, seed, fruit cross-section, growth ring, or ecological relation supported by the passage.
- Prefer `botanical-border-clearing`, `archive-specimen-grid`, or `scientific-plate-margin`.
- Avoid generic floral decoration and invented scientific labels.

### Nocturne Photogram

- Use one moon, lamp, window, moth, shadow, roofline, or surveillance relation from the passage.
- Prefer `luminous-dream-window`, `edge-weather-field`, or `type-image-counterpoint`.
- Use deep ink with exposed-paper halos; avoid generic star fields.

### Weather Index Risograph

- Express climate, uncertainty, season, time, or change through pressure lines, rain index, fog erasure, snow gaps, or thermal stain.
- Prefer `edge-weather-field` or `soundwave-silence-band`.
- Keep weather as a structural force, not a scenic stock background.

### Urban Xerox Grid

- Use one facade, bridge, platform, route, machine, office window rhythm, or industrial fragment.
- Prefer `urban-corridor-block`, `cartographic-path-axis`, or `split-time-diptych`.
- Useful for urban narrative, labor, systems, criticism, and modern history.

### Domestic Still-Life Print

- Build one exact relation among supplied objects, garments, furniture, tools, meals, or room traces.
- Prefer `domestic-table-shadow` or `orbital-object-constellation`.
- Useful for intimacy, family, ordinary ethics, grief, and memory without using a generic portrait.

### Archival Specimen File

- Use one verified artifact, document edge, photograph ghost, object trace, map fragment, or absence outline.
- Prefer `archive-specimen-grid` or `split-time-diptych`.
- Use restrained perforation, ruled zones, dust, and misregistration without fabricated institutional text.

### Cartographic Contour Zine

- Translate travel, borders, exile, terrain, search, and distance into contours, paths, faults, or route axes.
- Prefer `cartographic-path-axis` or `split-time-diptych`.
- Do not add unsupported place names or tourist-map styling.

### Sound-Silence Score

- Translate speech, music, echo, silence, repetition, testimony, or interruption into measured intervals and gaps.
- Prefer `soundwave-silence-band` or `type-image-counterpoint`.
- Keep excerpt lettering deterministic; generated backgrounds contain no notation text.

### Ink Gesture Field

- Use one controlled brush/ink event for rupture, force, conflict, violence, or decisive argument.
- Prefer `edge-weather-field` or `type-image-counterpoint` and preserve a large reading-safe region.

### Cut-Paper Geometry

- Translate philosophical contrast, paradox, systems, boundaries, or comparison into folded planes and cut voids.
- Prefer `split-time-diptych`, `orbital-object-constellation`, or `type-image-counterpoint`.
- Avoid corporate infographic polish.

### Chromatic Ghost Print

- Use one duplicated object, portrait crop, place, or document fragment for ambiguity, memory, unreliable narration, or temporal overlap.
- Prefer `split-time-diptych` or `luminous-dream-window`.
- Keep misregistration within one hue family or a restrained two-ink opposition.

### Film Contact Memory

- Use two to four small verified or passage-grounded fragments for sequential memory, travel, biography, or place-based narrative.
- Keep the strip compact; omit invented dates and captions.

### Material Swatch Reading

- Use textile, paper, wood, stone, metal, ash, food, or tool surfaces when labor, touch, class, craft, or material culture is central.
- Prefer `material-swatch-sequence` or `archive-specimen-grid` with two or three samples maximum.

### Scientific Annotation Plate

- Use one specimen, calibration relation, orbit, network, cross-section, or measured interval for science, observation, medicine, and systems.
- Require `scientific-plate-margin` or `archive-specimen-grid`.
- Use ticks and geometry without invented labels, numbers, findings, or claims.

### Luminous Storybook Window

- Use one small irregular painterly portal for fable, myth, wonder, folklore, or surreal transformation.
- Require `luminous-dream-window`; keep the portal under about 25% and preserve the reading field.

### Editorial Source Strip

- Use for concise quotations with confirmed title/author/source metadata.
- Set the excerpt as primary, metadata as a restrained strip, and one small source-related image or ink block as counterweight.
- Never fabricate a cover, publisher mark, endorsement, or sponsor row.

### Open Book Reading

- Use only for a supplied page, physical annotation, or a passage specifically about reading/material books.
- Treat pages as the quiet field and keep the surrounding surface flat and uncluttered.
- Do not default to an open book merely because the input is an excerpt.

### Gathered Marginalia

- Use only when multiple source artifacts are supplied.
- Build one compact cluster of at most three scraps and keep quotation, source, and commentary in distinct zones.

### Cobalt Breath Excerpt

- Use only when selected by the evidence map or explicit request, then read [cobalt-breath.md](cobalt-breath.md).
- Water vocabulary may instead become a tide chart, wet page, shell specimen, harbor light, route, or reflection.

## Card Architecture

1. Optional supplied category/title.
2. Exact excerpt as the primary readable block.
3. Confirmed source line, normally `《书名》｜作者`.
4. Optional confirmed translator, edition, chapter, or page.
5. Optional reader note, explicitly labeled and separated.

For a carousel, continue without repetition and place full confirmed metadata on the final card.

## Hard Avoids

- invented metadata, fake cover art, publisher logos, endorsements, reviews, or page numbers
- unsupported sea, diver, anonymous body, rescue, or lonely-figure imagery
- generic open books, full-bleed landscapes, stock cities, or decorative floral borders
- commercial book-ad hierarchy, purchase language, CTA, or giant title packaging
- AI-generated text, unrelated collage, excessive tape, nested cards, glossy mockups, 3D, neon, or anime
- variants that only recolor or reposition the same visual vignette
- text squeezed below mobile readability or placed over noisy imagery
