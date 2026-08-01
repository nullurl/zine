---
name: torn-light-archive-poster
description: Generate torn-paper archival light collage poster prompts and matching raster images. Use when the user provides a theme, place, season, memory, night scene, city/river/snow/window/light subject, or reference images and wants a vertical handmade editorial poster with deckled gray paper, irregular torn photo fragments, vellum layers, blueprint linework, botanical traces, typewriter microtext, and quiet poetic atmosphere.
---

# Torn Light Archive Poster

Turn the user's content into both:

1. a final image-generation prompt, and
2. a generated raster image made from that prompt.

This skill fuses the `gc-minimal-zine-poster-v0-1` paper-zine discipline with a denser torn-photo archive collage grammar: gray pulp paper, deckled edges, irregular photographic windows, translucent tracing paper, technical line marks, botanical fragments, and small typewriter labels.

## Style Grammar

Use this visual identity:

- Tall vertical handmade paper poster, usually 9:16 or 3:5.
- Full-frame gray, blue-gray, or warm-gray fibrous paper with deckled edges.
- One dominant irregular torn-photo fragment plus 2-5 secondary torn fragments.
- Photo fragments show dark blue hour, snow lamps, river glare, city glass, winter glow, fireworks, warm windows, trees, or other light-bearing scenes.
- Translucent vellum, rice paper, masking tape, tissue overlays, scraped paper fibers, and lifted torn edges sit over or under the photos.
- Thin black technical linework: blueprint arcs, measurement ticks, map contour lines, elevation marks, crosshair registration marks, dotted paths, or architectural sketches.
- Botanical or seasonal traces: bare branches, blossom twigs, pine needles, willow strands, pressed flowers, snowflake diagrams, seed heads.
- Small typewriter or monospaced text, never a commercial headline: two-part labels such as `SNOW / LAMP`, `CITY / AFTERGLOW`, `BLOOM / CURRENT`, plus one quiet subtitle.
- Restrained palette: gray paper, black linework, deep blue photo fragments, white light specks, and one warm glow accent such as amber, brass, red ornament, or lamp yellow.

## Hard Difference From Minimal Zine

Do not force the original minimal-zine rule of 70%-90% empty paper or one tiny anchor. This style is still quiet, but it is more layered and archival:

- Use 35%-65% paper visibility.
- Use multiple torn fragments, not a single tiny specimen.
- Let the main photo fragment occupy 25%-55% of the canvas.
- Keep the collage handmade, flat, and scanned; do not turn it into a scrapbook, moodboard, or glossy magazine layout.

## Workflow

1. Parse the user's content.
   - Identify subject, season, time of day, place, mood, exact text if supplied, and possible light source.
   - If reference images are supplied, use them as style or subject references according to the user's wording. If not specified, treat them as visual grammar references, not exact image-edit targets.
   - For abstract content, convert it into one light-bearing scene and two or three supporting paper fragments.

2. Choose a recipe.
   - Pick one layout family, main photo anchor, support fragments, linework system, botanical trace, text system, and accent light.
   - Vary the grammar between outputs; do not default to the same centered tear each time.
   - For batches, unusual subjects, or prompt-only requests, read `references/prompt-recipes.md` for compact recipe templates.

3. Compile the prompt in five compact paragraphs:
   - canvas, paper surface, edge treatment
   - main torn-photo fragment and subject
   - secondary fragments, vellum/tape layers, botanical traces
   - technical linework, typography, labels, coordinates
   - color, light, scan texture, and avoid-list

4. Generate the image.
   - Use the built-in image generation capability by default.
   - Do not stop at prompt-only unless the user explicitly asks for prompt-only.
   - If the built-in image tool is unavailable and the user confirms API/server fallback, use `scripts/server_image_gen.py` to call the configured OpenAI-compatible image service directly.
   - The server fallback reads `model_provider`, provider `base_url`, and `OPENAI_API_KEY` from the Codex config or environment. It uses `/images/generations` with `response_format = "b64_json"`, then decodes the image locally; the provider's `wire_api = "responses"` applies only to the text model and must not be inherited for image requests. Do not hard-code secrets in the skill or forward them to returned image URLs.
   - If the output becomes too glossy, too digital, too clean, or too scrapbook-like, regenerate once with stronger flat-scan paper and handmade constraints.

5. Return the image and final prompt.

## Recipe Axes

### Layout Family

- **central-torn-window:** one large irregular central photo tear with small fragments orbiting.
- **vertical-memory-strip:** stacked torn photo islands moving down the page like a field note.
- **diagonal-paper-river:** translucent torn bands crossing the page, with photo fragments embedded.
- **blueprint-margin:** main photo on one side, technical drawing and measurements occupying the margins.
- **seasonal-specimen:** botanical branch or pressed flower links several torn scenes.
- **night-atlas:** multiple dark blue fragments connected by dotted light paths and map marks.

### Main Photo Anchor

- snow path with street lamps
- blue-hour city towers and wet street
- river water with blossom branches
- warm window or old wooden storefront
- winter tree or ornament glow
- fireworks or handheld phone silhouette
- canal, bridge, rain glass, station light, harbor light, courtyard lantern

### Support Fragments

- small blue paper swatch
- monochrome contact-strip photo
- translucent vellum rectangle
- torn blueprint scrap
- pressed flower note
- foil or silver paper fleck
- mesh/halftone architectural patch
- small dark light-bokeh oval

### Linework System

- architectural elevation marks
- contour-map curves
- lamp-post technical sketch
- crosshair and registration marks
- dotted seasonal path
- measurement ruler ticks
- snowflake or flower diagram
- faint circular orbit lines

### Text System

Use 1-3 short text elements only. Prefer uppercase English typewriter labels or concise Chinese labels if the user writes in Chinese.

Examples:

- `SNOW / LAMP`
- `BLUE SILENCE`
- `BLOOM / CURRENT`
- `WATER REMEMBERS`
- `CITY / AFTERGLOW`
- `BLUE HOUR`
- `LIGHT / HELD`
- `AFTERIMAGE`
- `WINTER / GLOW`
- `WET LIGHT`

Text must be small, embedded in the paper, slightly ink-worn, and secondary to the collage.

## Prompt Rules

Always specify:

- "flat orthographic scanned handmade paper collage"
- "deckled fibrous gray paper"
- "irregular torn photographic fragments with exposed white paper fibers"
- "translucent vellum or rice-paper overlays"
- "thin black blueprint/map/measurement linework"
- "small typewriter microtext"
- "matte paper, no cast shadows, no 3D depth"

Preserve:

- deep blue or blue-gray photographic fragments
- warm points of light when the subject needs glow
- visible torn edges and paper fibers
- quiet archive mood

Avoid:

- glossy mockup, drop shadows, 3D paper stack, floating card UI
- commercial poster hierarchy, large headline, logo, CTA
- dense scrapbook stickers, washi-tape overload, cute journaling style
- clean digital white background
- cinematic full-bleed scene, fashion editorial drama, neon cyberpunk
- perfect vector line art, flat app illustration, anime/cartoon
- long readable paragraphs or many captions

## Output Format

````markdown
**生成图**

![Torn Light Archive Poster](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Recipe: [layout / main anchor / support fragments / linework / botanical trace / text / accent]
- [one short note about the content interpretation]
````

## Quality Gate

Before finalizing, check:

- Is it a vertical flat scanned paper collage, not a physical mockup?
- Is 35%-65% of the poster visibly fibrous paper?
- Is there one dominant torn-photo fragment plus supporting scraps?
- Are the torn edges irregular with visible white fibers?
- Are vellum/rice paper/tape overlays present but not glossy?
- Are blueprint/map/measurement marks thin and secondary?
- Is the text small, typewriter-like, and limited to 1-3 short labels?
- Does the image preserve a restrained gray/blue/warm-light palette?
- Does it feel quiet, archival, seasonal, and handmade?
- Did you actually generate the image?
