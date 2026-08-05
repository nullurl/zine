# Prompt Recipes

Use one recipe as a structural starting point. Replace subjects and exact copy from the user's request. Do not copy text or identifiable content from references.

## Contents

- Reference-aware base prompt
- Recipes A-F: original density and subject families
- Recipes G-H: palette-locked reference assemblies
- Copy rules
- Regeneration corrections

## Six-Paragraph Reference-Aware Base Prompt

```text
Tall vertical [ratio] flat scanned literary collage on [scanner white / worn fog-gray] fibrous paper, using [mode]. Preserve [paper share] exposed paper and matte orthographic presentation, with no frame, desk, mockup, black border, or card shadow.

Build exactly [3-7] hard-edged rectangular image plates. One [subject] plate occupies [38%-62%] of the page; [secondary plates] overlap its edges by [5%-25%]. Keep edges mostly parallel, allow only [zero/one] slight rotation, and show crop seams, torn fibers, or translucent registration offsets instead of rounded cards or an even grid.

Use one coherent subject family: [dominant subject] repeated as [positive/negative, sharp/blurred, color/grayscale, whole/cropped]. Select [2-5] integrated elements from [misted mountain / branch veil / river strip / cobalt apparition / white flower negative / eye strip / violet portrait / eye-line tear / bird field / tape fold / abrasion strip]. Make at least one insert interrupt a landscape edge and one material seam cross a plate boundary.

Use this regional palette map: neutral scanner-white paper [share], charcoal/forest-black plate [share], forest/moss green [share], mineral blue/blue-gray [share], saturated cobalt or ultraviolet exposure [share], cold violet insert [share], and optional oxidized-peach residue below 2%. Preserve each hue in its assigned plate; no global desaturation, monochrome conversion, sepia, teal merge, or purple wash.

Set the exact text “[short user copy]” in rough monospaced typewriter ink on [margin strip / translucent patch / center field], with irregular baseline, ribbon dropout, and no attribution unless supplied. Add selected tape folds, torn seams, rubbed emulsion, xerox grain, toner clumping, generation loss, scanner streaks, halftone, and slight color misregistration.

Mood: [absence / forgetting / passage / waiting / distance / memory], quiet and literary, like damaged field evidence. Avoid scrapbook stickers, washi decoration, Polaroid stacks, rounded UI cards, clean modular grids, full-bleed glossy photography, commercial titles, logos, CTA, 3D shadows, cinematic grading, neon, sepia postcard styling, unrelated images, copied text, signatures, watermarks, and long pseudo-readable paragraphs.
```

## Recipe A: Cobalt Apparition

Mode: Exposure Bloom.

- paper: 15%-22% scanner white
- panels: one 55% dark landscape/body plate; one 35% lower negative plate; two narrow texture scraps
- subject: anonymous hand, body fragment, flower, or object transformed into electric cobalt bloom
- secondary subject: one blown-out white botanical negative
- type: narrow poem strip at left, 3-6 short lines
- seam: one translucent lower tape strip

Use for touch, apparition, dream, signal, and embodiment.

## Recipe B: Mountain and Missing Portrait

Mode: Mountain Archive.

- paper: 20%-30%
- panels: large deep-green mountain plate, offset mineral-blue copy, lower terrain strip, small violet portrait/object insert
- subject transform: landscape color separation; portrait crossed by one torn white fiber or scratch
- type: small translucent patch at upper-right
- seam: rough torn paper crossing the portrait's upper edge

Use for forgetting, distance, unnamed places, return, wilderness, and identity as trace.

## Recipe C: Paper Sky Migration

Mode: Pale Migration.

- paper: 55%-68% pale scanner white and fog
- panels: three overlapping translucent sky rectangles plus one bottom meadow or mountain strip
- subject: 12-20 blurred birds, including two smeared echoes; vary scale and sharpness
- type: centered rough typewriter stanza beneath the birds
- color: near-monochrome mineral blue-gray with one restrained cobalt bird or registration ghost

Use for leaving, seasons, waiting, freedom, and fragile passage.

## Recipe D: White Flower Negative

Mode: Exposure Bloom or Remains Atlas.

- panels: dark forest plate, grayscale texture plate, one botanical photo, one overexposed negative copy
- subject transform: same flower as dim photo and clipped white silhouette
- type: separated evidence blocks in open white paper
- color: forest black-green plus a small ultraviolet-blue emulsion patch

Use for memory, disappearance, mourning, growth, and remains.

## Recipe E: Forest Memory Atlas

Mode: Remains Atlas.

- paper: 48%-62%
- panels: main foggy forest plate plus six fragments of branch, water, cloud, terrain, flower, and rubbed texture
- layout: irregular descending cluster with one large empty upper-right or lower-right field
- type: one 3-line statement and two isolated short fragments
- color: cold violet sky plate or cobalt cloud fragment

Use for essays, collected days, family memory, field notes, and layered recollection.

## Recipe F: Eyes as Residue

Mode: Exposure Bloom.

- panels: main dark landscape/object plate, one narrow eye fragment, one larger negative botanical or texture plate
- subject transform: eyes reduced to two dark forms in a blue-gray mask field
- type: side strip or lower margin, never directly across the eyes
- color: cobalt bloom belongs to a hand, body, or flower rather than the eye strip

Use for observation, recognition, absence, secrecy, and dream perception.

## Recipe G: Palette-Locked Mountain Assembly

Mode: Palette-Locked Reference + Mountain Archive.

- paper: 22%-30% neutral scanner white; keep it free of blue/green tint
- panels: pale branch transparency, large forest-green mountain, mineral-blue mountain duplicate, river-stone strip, cold-violet anonymous portrait insert
- interruptions: torn white fiber across the portrait eye line; tape fold crosses the upper mineral-blue plate
- type: small upper-right typewriter patch over pale mist, never over the portrait
- regional palette: 25% paper/fog, 32% charcoal/forest black, 20% forest green, 16% mineral blue, 5% cold violet, 2% cobalt exposure
- optional trace: one tiny oxidized-peach rubbed patch below 1%

Use when references show layered mountains, a portrait insert, cool color separation, and the user explicitly asks to retain color and collage behavior.

## Recipe H: Palette-Locked Exposure Assembly

Mode: Palette-Locked Reference + Exposure Bloom.

- paper: 15%-22% scanner white
- panels: dark mountain/forest plate, gray abrasion strip, eye-mask strip, lower negative botanical plate
- transformed subject: cobalt hand/body/flower apparition with white-hot center
- second brightness event: clipped white flower negative, no new hue
- regional palette: 20% paper/gray, 45% charcoal/forest black, 18% moss green, 12% cobalt/ultraviolet, 5% blue-gray/violet
- type: narrow left poem strip

Use when the reference's strongest signal is fluorescent cobalt against dark green xerox plates.

## Copy Rules

- Preserve exact user text verbatim.
- Omit attribution when the user says no signature or supplies no author.
- For Chinese, target one sentence of 8-28 characters or 2-4 short lines.
- For English, target 2-6 short lowercase lines in typewriter rhythm.
- Do not invent real names, venues, archives, institutions, or dates.
- Do not reuse visible wording from references.

## Regeneration Corrections

### Panels look like cards

Add:

```text
all image plates are raw rectangular photocopy crops with zero corner radius and no shadows; their depth is shown only through toner opacity, torn fibers, and physical overlap
```

### Collage is too decorative

Add:

```text
remove stickers, stationery, labels, stamps, ribbons, decorative tape, and all unrelated fragments; keep one subject family, four image plates, one poem patch, and one material seam
```

### Main subject disappears

Add:

```text
one transformed subject occupies 22%-30% of the page and remains recognizable at thumbnail size through a strong silhouette and one clear exposure state
```

### Cobalt becomes a global filter

Add:

```text
cobalt appears only inside the transformed subject or one discrete image plate; all paper, type, and surrounding photographs remain scanner white, charcoal, forest, and fog gray
```

### Reference palette is lost

Add:

```text
lock color by region: neutral scanner-white paper, separate forest-green ground plate, separate mineral-blue atmosphere plate, saturated cobalt exposure only in the transformed subject, cold-violet only in the portrait or eye insert, optional oxidized-peach abrasion below 2%; no global monochrome, sepia, teal blend, purple wash, or overall desaturation
```

### Extracted elements look like stickers

Add:

```text
every insert must physically interrupt another plate: the portrait crosses the landscape edge, the eye-line tear crosses the portrait, the tape fold crosses the blue plate, and the poem patch overlaps only pale atmosphere; zero floating decorative stickers
```

### Result is too dark

Add:

```text
increase exposed scanner-white paper to 35%, add one pale fog plate, preserve only one deep charcoal image plate, and keep the cobalt anchor fully saturated
```

### Text is garbled

Shorten to one exact sentence, place it on a clear pale paper patch, use one typewriter style, and remove all other text.
