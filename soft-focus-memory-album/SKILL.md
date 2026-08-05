---
name: 柔焦记忆
description: Generate prompts and finished raster images for soft-focus digital memory albums, summer day collages, travel recaps, lifestyle photo diaries, friendship memories, café and street snapshots, and cinematic photo boards. Use when the user wants a wide blurred-scene background with a central cluster of overlapping photo windows, thin white frames, dotted or star halftone textures, handwritten titles, short editorial captions, arrows, and a restrained nostalgic color grade.
---

# Soft Focus Memory Album

Turn a memory, day, place, feeling, theme, or reference image set into both:

1. a final image-generation prompt, and
2. a generated landscape raster collage.

This skill fuses minimal-zine attention geometry with a digital photo-album language: the environment becomes a soft-focus emotional background, while a compact set of snapshots carries the readable memory.

## Reference Routing

- Treat supplied images as visual-grammar or subject references unless the user explicitly requests a literal edit.
- Analyze local reference images locally. Extract background treatment, photo count, crop geometry, borders, typography, annotation symbols, palette, and emotional temperature.
- Do not upload private local reference images to an untrusted third-party endpoint. The bundled server fallback is text-only.
- Read `references/style-grammar.md` when reverse-engineering a reference set or correcting style drift.
- Read `references/prompt-recipes.md` for batches, unusual memories, or when the collage structure is unclear.

## Core Identity

Preserve these signals:

- Wide landscape composition, usually 16:9, with a full-frame but heavily blurred environmental background.
- A compact central or slightly offset memory cluster occupying roughly 32%-58% of the canvas.
- Five to nine related photographic windows from the same day, place, or emotional thread.
- Rectangular crops with thin white borders, occasional rounded corners, modest overlaps, and varied aspect ratios.
- One larger anchor photo plus smaller supporting snapshots; every window should belong to one visual story.
- Fine white outlined rectangles, connector lines, arrows, circles, crosshairs, star/round halftone patches, or small geometric markers.
- A handwritten or script-like title paired with a small serif, mono, or editorial caption system.
- One restrained accent color, usually vermilion arrow marks, muted red type, cobalt blue, lemon yellow, or white linework.
- Dreamy memory-board mood: warm, slightly hazy, observational, personal, and more like an edited album page than an advertisement.

## Fusion With Minimal Zine

Carry forward:

- one clear attention cluster
- negative space around the cluster
- sparse visual hierarchy
- short, imperfect text instead of long copy
- one controlled chromatic anchor
- film grain, scan softness, and restrained editorial mood

Change the geometry:

- Use a horizontal 16:9 memory board instead of a vertical paper poster.
- Let the background be a soft-focus place-memory field, never a sharp full-bleed scene.
- Use several photographic fragments inside one cluster instead of one tiny specimen.
- Keep borders, lines, dots, arrows, and captions subordinate to the photos.
- Do not add physical paper stacks, binder hardware, or scrapbook stickers unless the user explicitly asks for them.

## Layout Engine

Choose one layout family before compiling the prompt:

- **centered-memory-board:** one large middle photo with four to seven surrounding crops.
- **left-to-right-day:** snapshots progress from morning on the left to evening on the right.
- **upper-caption-grid:** photo cluster sits below a loose title and tiny editorial header.
- **diagonal-route:** windows follow a diagonal route connected by thin arrows or lines.
- **botanical-interlude:** lifestyle photos are interrupted by one plant or flower window with white frames.
- **split-memory:** two major photo groups separated by an intentional breathing gap.

Keep the cluster coherent. Avoid scattering unrelated photos across the full frame.

## Photo Window Engine

Select one anchor and 4-8 supports:

- anchor: meal, face-free travel scene, landmark, hands, vehicle view, sunset, or place-defining frame
- support: drink, table, flower, window, street detail, clothing detail, object in hand, bench, storefront, sky, or transit fragment

Vary crop sizes, but keep a shared grade. Use one or two windows with a thin white border and one or two borderless translucent overlays. Do not make every image the same size.

## Typography and Annotation

- Use one expressive handwritten/script title of 2-4 words.
- Add one short subline in serif or small mono type.
- Add at most 2-4 tiny captions or tags.
- Use arrows, circles, thin boxes, stars, dots, and short connector lines as visual annotations, not as decoration.
- Keep long lyrics, full paragraphs, usernames, logos, or brand copy out of the prompt. Exact text should be short and invented unless supplied by the user.
- If the reference includes visible social handles or signatures, abstract them into a generic short tag rather than reproducing personal identifiers.

## Color and Image Grade

Choose one grade:

- **summer-olive:** deep leafy green background, warm skin/wood, amber light, muted cream text.
- **golden-afternoon:** olive shadows, honey highlights, faded blue sky, warm white borders.
- **soft-cyan:** cool green-blue background, muted beige objects, one vermilion accent.
- **dusty-pink:** gray-green shadows, blush highlights, cream frames, one cobalt mark.
- **night-window:** dark forest background, low warm lights, white borders, one electric blue or red accent.

Keep the background lower contrast and softer than the photo cluster. Do not make every photo saturated. One accent color should occupy about 1%-5% of the canvas, or 10%-25% of the cluster.

## Color Trend Enhancement

Use this only when the user asks for brighter color, richer color, preserved source color, a named palette mood, or when the draft would otherwise become too gray, beige, dark, or flat. Preserve this skill's layout grammar first; color is an enhancement layer, not a replacement for structure.

Pick one dominant palette and optionally one small adjacent accent. Assign colors to visible roles such as paper field, photo grade, ink, label, material, shadow, highlight, or motion accent. Do not combine more than two palettes unless the user explicitly asks for chaotic or maximal color.

- forest green: #92AD76, #B6CCAA, #E3EBDD, #71906A, #435F45. Use for botanical, tropical, moss, spring, garden, healing, or green-reverie briefs.
- purple luxury: #7B5FA4, #A487C6, #D8C9EE, #9A8AB6, #5B376D. Use for dreamy, ritual, night floral, velvet, memory, or quiet-luxury briefs.
- vintage mocha: #885949, #C87949, #E6BC8C, #D9D2C8, #203A35. Use for cafe, archive, editorial, old-photo, paper, or warm city briefs.
- earth warm brown: #A5673D, #C89A6B, #E8D6C3, #7B5A42, #3D2C22. Use for handmade, soil, leather, textile, relic, desert, or autumn briefs.
- deep sea blue: #0F2E48, #1E4F73, #5C87B2, #AFC5DA, #E6F0F8. Use for ocean, rain, night water, cloud-sea, distance, or cinematic calm.
- mist blue gray: #9FB0C3, #C9D3DF, #EEF2F6, #75879A, #31485D. Use for rain, fog, glass, winter, quiet architecture, or analytical moods.
- sunset orange: #FF9A42, #FFC185, #FFE9D3, #C66A31, #7B3D1E. Use for warm light, cafe lamps, islands, evening, energy, or celebratory accents.
- cream soft pink: #F6D7DE, #FBE9EE, #FFF7F8, #E9C6D1, #C39BAA. Use for bright journaling, tender memory, blossoms, soft albums, or feminine notes.
- sea-salt blue: #A8D8EA, #D8EDF5, #F8FCFD, #7FB8CF, #5A8097. Use for airy coastal, island, pool, travel, summer, or brighter-water requests.
- desert elegant white: #F7F4EE, #E7DED1, #D1C6B8, #A99F91, #736F66. Use as a clean bright base when the image needs lift without saturation.

When brightening a dark output, increase paper/background luminance with desert elegant white, sea-salt blue, or cream soft pink before increasing saturation. When preserving a reference image, keep its main hues first, then harmonize them with the closest palette above.

## Prompt Compiler

Write the final prompt in five compact paragraphs:

1. **Canvas and background**
   - landscape ratio, blurred environmental field, grade, negative-space behavior, and emotional setting.

2. **Memory cluster**
   - layout family, anchor image, support windows, photo count, crop variation, and shared story.

3. **Graphic system**
   - white borders, outlined boxes, connector lines, arrows, circles, dots/stars, translucent overlays, and overlap order.

4. **Typography and color**
   - exact short title, caption style, accent color, image grade, and text limitations.

5. **Texture and avoid list**
   - film grain, soft blur, chromatic restraint, editorial feeling, and explicit anti-identity constraints.

## Generation

- Use built-in image generation by default and do not stop at prompt-only unless explicitly requested.
- When built-in image generation is unavailable and server fallback has already been approved, use `scripts/server_image_gen.py` with the final prompt.
- The fallback reads provider configuration and `OPENAI_API_KEY` from the environment or Codex config, calls `/images/generations`, requests `b64_json`, and writes the image locally. Never hard-code secrets.
- Use a landscape size such as `1536x864` for the default 16:9 composition.
- Inspect the output once. Regenerate with one targeted correction if the photo cluster is too scattered, the background is sharp, the text dominates, or the scene becomes a generic marketing collage.

## Hard Avoids

Always avoid:

- sharp full-bleed background competing with the photo cluster
- commercial campaign layout, logo lockup, CTA, or influencer-ad styling
- generic stock-photo moodboard with unrelated images
- excessive borders, stickers, stars, arrows, circles, or decorative UI widgets
- long readable lyrics, paragraphs, or many usernames
- neon rainbow palette or more than two strong accent colors
- clean app interface, dashboard, card UI, or web design mockup
- glossy 3D collage, cinematic poster drama, fashion campaign polish
- kawaii stickers, emoji, anime, cartoon illustration
- random copy that claims a real brand, person, or organization

## Output Format

````markdown
**生成图**

![Soft Focus Memory Album](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Layout: [layout family]
- Memory thread: [anchor / support windows / grade / annotation system]
- [one short note about the interpretation]
````

## Quality Gate

Before finalizing, check:

- Is the output landscape and visibly a memory album rather than a poster?
- Is the background clearly blurred and lower contrast than the photo cluster?
- Does one coherent cluster contain five to nine related photo windows?
- Is there a clear anchor photo with varied supporting crops?
- Are white frames, lines, dots, arrows, and captions sparse and subordinate?
- Is the title short and visually integrated rather than a huge headline?
- Is one accent color controlled and visible without becoming commercial?
- Do all photos share a believable time/place/color grade?
- Does the output avoid generic stock moodboard, UI card layout, and scrapbook clutter?
- Did you actually generate the image?
