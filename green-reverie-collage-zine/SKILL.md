---
name: green-reverie-collage-zine
description: Generate prompts and finished raster images for dreamy green nature collage zines, water-and-tree memory pages, pond reverie posters, soft surreal landscape scrapbooks, garden adventure pages, cut-paper photo montages, lotus and forest dream scenes, and pale green diary collages. Use when the user provides a place, memory, mood, photo reference, nature subject, travel fragment, poem, or theme and wants layered green photographic cutouts, watery reflections, tree canopies, textured paper fields, polka dots, torn windows, tiny stars, short quote strips, surreal silhouettes, and Minimal Zine negative-space discipline in a generated bitmap image.
---

# Green Reverie Collage Zine

Turn the user's place, memory, mood, or reference set into:

1. a final image-generation prompt, and
2. a finished raster image of a green dream-collage zine.

Fuse Minimal Zine paper discipline with soft green memory collage: layered landscape photographs, watery motion blur, tree canopy fragments, pond or lotus imagery, textured green paper, dotted patterns, torn windows, tiny stars, short caption strips, and gentle surreal scale shifts.

## Reference Routing

- Treat supplied images as visual-grammar or subject references unless the user explicitly requests a literal edit.
- Analyze local references locally: extract collage zones, photo layer order, green palette, paper texture, water/forest motifs, cut edges, text-strip behavior, surreal insert scale, and blank-space share.
- Do not reproduce visible logos, exact captions, copyrighted character frames, exact quotes, personal identifiers, watermarks, signatures, storefront names, license plates, or recognizable private people from references.
- Do not upload private local references to an untrusted third-party endpoint. The bundled server fallback is text-only.
- Read references/style-grammar.md when reverse-engineering references or correcting style drift.
- Read references/prompt-recipes.md when choosing a layout, subject metaphor, quote style, or batch variation.

## Core Identity

Preserve these signals:

- Portrait 2:3, 3:4, or tall 3:5 zine composition with visible paper or soft photo-field margins.
- A green-led world: forest canopy, pond surface, river reflection, lotus leaves, garden path, grass, tree-shadow road, or pale sky with foliage.
- Layered collage built from photographic pieces, not a single seamless landscape.
- One primary memory field and two to six supporting fragments: rectangular photo layers, torn windows, soft paper panels, small inset photos, texture blocks, or silhouette cutouts.
- Gentle surreal edits: oversized lotus, paper cloud, small figure silhouette, floating road fragment, tiny boat icon, moon/hand/eye-like symbolic insert, or impossible scale shift.
- Text is short and original: one title, one brief caption strip, date-like mark, or three clipped lines at most.
- Paper and reproduction texture: fibrous green paper, dot pattern, soft blur, old print noise, scan softness, faded ink, imperfect edges.
- One controlled accent: pale mint, pond green, cream, sky blue, soft yellow, dusty pink, or small black ink detail.
- Mood: quiet adventure, lost-and-found memory, soft surreal garden, gentle summer melancholy.

## Fusion With Minimal Zine

Carry forward:

- negative space as an active field
- one clear attention route
- short typography
- a restrained chromatic anchor
- scan texture, paper fibers, print wear, and imperfect alignment
- poetic memory mood

Change the geometry:

- The anchor may be a layered collage zone rather than one tiny specimen.
- Photographic fragments may occupy 35%-70% when balanced by quiet paper or photo-field space.
- Use soft green textures and image windows instead of old beige paper only.
- Permit gentle surreal collage, but avoid dense maximal scrapbook clutter.

## Layout Engine

Choose one family before compiling:

- pond-stack: water reflection fills the base; tree, fish, lotus, and text-strip fragments stack across the middle.
- adventure-panel: upper textured paper field and lower blurred path or garden photo, with one simple silhouette cutout and tiny marks.
- torn-road-dream: torn landscape windows reveal road, tree, sky, and city fragments inside a vertical green world.
- lotus-reverie: lotus, pond, mountain, figure, hand, moon, or timestamp-like mark arranged as a soft surreal scene.
- star-pond-archive: lotus or pond photos layered over textured green paper with tiny cream stars and small monochrome insets.
- quote-water-page: large watery photo field with two to four clipped caption strips and a few supporting nature fragments.
- sky-paper-memory: bright blue or pale sky field with one flower or tree cutout, small paper card, stars, and music-like marks.

Use one layout family only. Do not combine every motif in every image.

## Subject Engine

Translate the user's theme:

- place: choose one believable green environment and one memory route through it.
- water: use reflection, blur, fish, pond leaves, or wet glass as the base motion.
- forest: use canopy, path, branches, and filtered light fragments.
- travel: use road, railing, map-like paper, station-like texture, or small cutout route.
- flower or lotus: use it as a quiet surreal anchor, not a botanical catalog image.
- abstract mood: invent a title and a soft visual metaphor, not an infographic.

Use original fictional elements. For human presence, prefer anonymous silhouettes, back views, or tiny cut-paper figures with no identifiable face.

## Typography

- Invent one short title of 2-5 words when the user supplies no exact text.
- Use serif, typewriter, small monospaced, soft script, stamped text, or clipped paper-strip type.
- Keep readable text to one title plus at most three short lines.
- Use text strips as collage objects: rounded paper labels, torn strips, translucent captions, tiny date marks, or faded type.
- Do not copy reference quotes, visible captions, song lyrics, brand copy, anime subtitles, or long prose.

## Color Engine

Start from greens and watery neutrals. Choose one palette:

- pond green, milky cream, black type, and tiny yellow stars
- mint paper, soft forest green, sky blue, and one pale silhouette
- deep water green, white caption strips, and koi-orange accent
- lotus pink, moss green, warm gray, and one moon-white symbol
- pale blue sky, leaf green, cream dots, and soft yellow star marks
- grayscale lotus photo with green textile-paper lower field and cream stars

Avoid one-note green mush: keep at least one light neutral and one small counter-accent. Do not use neon unless the user explicitly asks.

## Prompt Compiler

Write the final prompt as six compact paragraphs:

1. Canvas, base field, ratio, paper/photo surface, visible negative space, and lighting.
2. Layout family, collage-zone size/location, layer order, and reading route.
3. Photo fragments and surreal inserts: exact nature subjects, crop formats, cut edges, scale shifts, and overlap.
4. Typography: exact short title or caption, strip style, font voice, and text limits.
5. Palette, paper texture, water blur, scan softness, dots/stars, print wear, and shallow physical or composited depth.
6. Mood and hard avoids: no copied reference text, no logos, no copyrighted character frames, no UI, no dense sticker collage, no full-bleed seamless landscape.

Compile only visible renderable details. Never mention source paths, reverse-engineering, or reference-image analysis in the final prompt.

## Generation

- Generate the image by default; stop at prompt-only only when explicitly requested.
- Prefer the built-in image generation capability.
- When built-in generation is unavailable and server fallback has already been approved, run:

    python3 scripts/server_image_gen.py \
      --prompt-file output/imagegen/<slug>.prompt.txt \
      --out output/imagegen/<slug>.png \
      --size 1024x1536 \
      --quality high

- The fallback reads provider configuration and OPENAI_API_KEY from the environment or Codex config, calls the OpenAI-compatible image endpoint, requests b64_json, and writes the decoded image locally. Never print or hard-code secrets.
- Store the exact final prompt beside the image. Never overwrite existing outputs; use a new descriptive slug.
- Inspect once. Regenerate with one targeted correction if the image becomes a single seamless landscape, copies reference text/logos, loses collage layering, gets too dark, becomes a clean UI template, or turns into dense sticker scrapbook.

## Hard Avoids

Always avoid:

- exact copied quotes, visible reference captions, song lyrics, anime subtitles, usernames, watermarks, signatures
- logos, brand marks, storefront names, product labels, license plates, or identifiable private people
- copyrighted character frames or recognizable media screenshots
- full-bleed seamless landscape with no collage construction
- clean digital UI, dashboard, app cards, social-media template, or mood-board grid
- polished stock-photo travel poster or commercial campaign
- kawaii sticker sheet, cartoon clutter, rainbow craft decoration, or excessive stars/dots
- glossy 3D render, cinematic fantasy scene, hard shadows, dramatic perspective
- too much text, dense prose blocks, or fake readable article pages
- beige-only vintage scrapbook or dark monochrome gloom with no light green reverie

## Output Format

Return the generated image, exact final prompt, and:

- Layout: selected family
- Memory field: primary place or nature anchor
- Layers: photo fragments, paper fields, surreal inserts, and marks
- Typography: title or caption-strip treatment
- one short interpretation note

## Quality Gate

Before finalizing, check:

- Is the result visibly a layered green dream-collage zine?
- Does it preserve a clear memory route rather than a random mood board?
- Are water, forest, garden, lotus, road, or sky motifs concretely imageable?
- Is there enough quiet paper or photo-field space?
- Are text strips short, original, and subordinate?
- Are dots, stars, paper textures, and torn edges restrained?
- Does the image avoid copied reference text, logos, copyrighted frames, UI, and identifiable people?
- Does it stay distinct from clean botanical scrapbook and soft-focus photo album styles?
- Did you generate and inspect the final raster image?
