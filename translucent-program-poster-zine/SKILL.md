---
name: 半透明节目单
description: Generate prompts and finished raster images for translucent, type-heavy program posters, experimental event flyers, album/tracklist sheets, design-study posters, calendar-map zines, and misty low-contrast editorial compositions. Use when the user provides a phrase, event, music/program brief, poster reference, date, photo, figure, landscape, or abstract concept and wants a vertical poster with black outer field, pale paper panel, oversized translucent typography, blurred photo fragments, ghost diagrams, small program metadata, scan grain, and Minimal Zine restraint.
---

# Translucent Program Poster Zine

Turn a phrase, event, album/program idea, reference image, or abstract concept into:

1. a final image-generation prompt, and
2. a finished raster image in a translucent experimental program-poster style.

Fuse Minimal Zine paper discipline with larger editorial systems: misty image layers, oversized ghost type, calendar or tracklist microcopy, soft blur, pale gray-blue color, and black exhibition-like margins.

## Reference Routing

- Treat supplied images as visual-grammar references unless the user explicitly requests literal editing.
- Inspect references locally. Extract outer black margin, inner paper ratio, low-contrast haze, type scale, photo blur, diagram marks, panel stacking, and information density.
- Do not copy real event names, dates, venues, artist names, sponsor marks, barcodes, usernames, signatures, or reference text unless the user explicitly supplies exact copy.
- Read [references/style-grammar.md](references/style-grammar.md) when reverse-engineering a reference, preserving the black-frame/pale-panel structure, or correcting drift.
- Read [references/prompt-recipes.md](references/prompt-recipes.md) when selecting layout, type hierarchy, diagram language, or theme translation.

## Core Identity

Preserve these signals:

- vertical poster placed inside a deep black outer field or wide black scan border
- central pale paper panel in off-white, fog gray, blue gray, or washed cream
- translucent overlapping typography: very large ghost words plus tiny metadata
- one blurred photo fragment, soft silhouette, eye crop, human figure, cloudy landscape, tree, or abstract texture
- optional map, calendar spiral, network diagram, thin orbit line, barcode-like stripe, or tracklist table
- low contrast and high haze without becoming blank
- xerox, halftone, risograph grain, paper fibers, scan streaks, and soft misregistration
- restrained color: gray, white, charcoal, faded blue, pale pink, dusty tan, or one rust/cobalt accent
- editorial music/program/design-study mood, not a commercial social flyer

## Minimal Zine Fusion

Carry forward from `gc-minimal-zine-poster-v0-1`:

- paper as the main field
- strong negative space and sparse emotional temperature
- one decisive attention system
- old-print defects and scan texture
- short text used as material
- one restrained color accent

Change the scale:

- allow type to occupy 25%-55% of the panel as a translucent structure
- allow photo fragments to blur into the paper instead of staying tiny
- add program metadata, tracklist, dates, or diagram marks only as graphic texture
- keep the final image quiet and physical despite the stronger typography

## Layout Engine

Choose one family before compiling:

- `transparency-title-sheet`: one pale panel with oversized translucent title near the top and foggy imagery fading downward.
- `event-program-haze`: event/festival/program metadata, ghost repeated title lines, one small image rectangle, and pale poster texture.
- `calendar-map-sheet`: circular calendar numbers, route/map lines, a halftone photo panel, and sparse month labels.
- `type-specimen-figure`: one dark side panel with mono type settings and one blurred human or object silhouette on the right.
- `album-tracklist-poster`: large album title, narrow film-strip image band, tracklist blocks, and cloudy photo wash.
- `design-index-poster`: experimental glyph row, blurred square image fragments, tiny multilingual notes, date at bottom.

Use one family only. Do not combine every motif in one image.

## Subject Translation

- phrase or poem: choose one ghost image that carries the feeling, then use the phrase as oversized translucent type.
- event or program: use invented non-identifying event metadata unless exact text is supplied.
- album or music: use one album title, a short tracklist-like block, and a soft photographic band.
- person: render as blurred halftone silhouette, crop, or spectral figure; avoid celebrity likeness.
- city or place: use a route/map diagram, haze photo, small image window, or calendar-style index.
- nature: use mist, clouds, tree silhouette, flower outline, water texture, or pale landscape wash.

## Typography System

- Use one large title or word mass, plus two or three tiny metadata zones.
- Allow repeated ghost text behind the main title, but keep it low opacity.
- Use condensed grotesk, mono, serif, or calligraphic script only when it suits the layout family.
- Long prose should become unreadable texture, not a readable paragraph.
- Use exact user-supplied words when provided; otherwise invent short fictional text.
- Never fabricate real venues, sponsors, prices, addresses, URLs, QR codes, or scannable barcodes.

## Color Engine

Choose one palette:

- fog white: off-white panel, charcoal type, faint blue-gray stains
- vapor blue: gray-blue field, white text, black silhouette or diagram
- pale event wash: cream/gray panel, faded pink and blue patches, translucent gray type
- graphite specimen: gray field, black side panel, white mono text, soft white silhouette
- album cloud: washed blue sky, ivory panel, black serif title, muted image band
- rust haze: pale gray panel with one rusty-orange translucent gesture

One accent may occupy 1%-8% of the panel. Keep saturation restrained; the image should feel scanned, evaporated, and archival.

## Prompt Compiler

Write the final prompt as six compact paragraphs:

1. canvas, black outer field, inner paper panel ratio, paper tone, and scan/flat-light treatment
2. selected layout family, placement of title, photo fragments, diagrams, and empty areas
3. subject translation: main image anchor, blur/halftone/transparency treatment, and emotional tone
4. typography: exact supplied title or invented title, ghost text, metadata blocks, and text limits
5. palette, texture, paper defects, grain, misregistration, and opacity behavior
6. hard avoids: no copied reference text, real brands, UI, glossy mockup, ad hierarchy, or dense scrapbook

Compile only renderable visual details. Do not mention source paths, reverse-engineering, or analysis in the final prompt.

## Generation

- Generate the image by default; stop at prompt-only only when explicitly requested.
- Prefer the built-in image generation capability.
- When built-in generation is unavailable and server fallback has already been approved, run:

    python3 scripts/server_image_gen.py \
      --prompt-file output/imagegen/<slug>.prompt.txt \
      --out output/imagegen/<slug>.png \
      --size 1024x1536 \
      --quality high

- The fallback reads provider configuration and `OPENAI_API_KEY` from the environment or Codex config, calls the OpenAI-compatible image endpoint, requests `b64_json`, and writes the decoded image locally. Never print or hard-code secrets.
- Store the exact final prompt beside the image. Never overwrite existing outputs; use a new descriptive slug.
- Inspect once. Regenerate with one targeted correction if the poster loses the black outer field, becomes too blank, becomes a commercial flyer, text becomes clean ad copy, or image layers lose translucency.

## Hard Avoids

Always avoid:

- copied event names, venues, dates, sponsors, usernames, signatures, watermarks, or real contact details
- commercial flyer hierarchy, CTA, pricing, ticketing, promo banner, or social-media template
- app UI, dashboard, website mockup, mobile poster editor, or clean digital card layout
- glossy 3D mockup, hard shadows, cinematic lighting, polished stock photography
- dense scrapbook, sticker collage, paper-craft overload, or decorative ephemera pile
- neon cyberpunk, rainbow gradients, cute cartoon, anime, or luxury fashion campaign styling
- perfectly sharp full-bleed photo with text pasted on top
- readable long paragraphs or fake scannable barcodes/QR codes

## Output Format

Return the generated image, exact final prompt, and:

- Layout: selected family
- Anchor: main photo/silhouette/diagram subject
- Type system: title, ghost text, metadata
- Palette: paper field, ink, accent
- one short interpretation note

## Quality Gate

Before finalizing, check:

- Is there a visible black outer field or scan border around a pale poster panel?
- Does the image feel translucent, misty, and printed rather than clean digital?
- Is oversized type a major structural layer without becoming an ad headline?
- Is there one main blurred image, silhouette, or diagram anchor?
- Are metadata blocks tiny and fictional unless supplied by the user?
- Does the poster preserve Minimal Zine restraint despite larger typography?
- Are paper grain, scan noise, opacity shifts, and misregistration visible?
- Did the prompt avoid copied reference text, brands, UI, and commercial campaign logic?
- Did you generate and inspect the final raster image?
