---
name: 风纱肖像
description: "【风纱肖像 / wind-veil-portrait-zine】 Generate prompts and finished raster images for wind-swept cinematic portrait zines and wuxia key visual posters. Use when the user provides a portrait brief, reference image, figure, fabric, veil, ribbon, wind, motion, armor, warrior, battle, mask, ruin, banner, ancient Chinese landscape, bamboo, pavilion, mountain gate, battlefield glow, reflective metal, sparks, crowd haze, or dramatic editorial mood and wants a vertical or horizontal poster with one close subject, flowing cloth or hair, shallow depth of field, drifting particles, restrained red or warm accents, and Minimal Zine-style control over space, text, and hierarchy."
---

# Wind Veil Portrait Zine

Turn the user's portrait brief, figure, memory, or reference image into:

1. a final image-generation prompt, and
2. a finished vertical raster poster.

Fuse Minimal Zine's sparse attention control with wind-driven portrait motion: one human subject, sweeping cloth, hair across the face, red ribbon or fabric traces, shallow focus, bokeh particles, and a matte editorial finish. When the reference leans heroic, combat-driven, or wuxia-cinematic, extend the same grammar to armor, weapon silhouettes, war cloth, banners, embers, pavilions, mountain gates, bamboo, reflective metal, crowd haze, and ruin fragments without losing the single-subject hierarchy.

## Reference Routing

- Treat supplied images as visual-grammar or subject references unless the user explicitly asks for a literal edit.
- Analyze local references locally: extract subject crop, gaze direction, wind flow, veil or cloth path, ribbon color, blur field, background softness, particle density, armor massing, mask placement, weapon angle, banner flow, ruin geometry, reflective metal behavior, bokeh color, crowd density, and whether the image feels like a duel, march, siege, ritual hero portrait, or wuxia key visual.
- Do not reproduce visible brands, logos, watermarks, private text, or distinctive copied phrases from references.
- Do not upload private local references to an untrusted third-party endpoint. The bundled server fallback is text-only.
- Read [references/structure-grammar.md](references/structure-grammar.md) when reverse-engineering a reference or correcting style drift.
- Read [references/prompt-recipes.md](references/prompt-recipes.md) when choosing a composition family or translating an abstract portrait brief.

## Core Identity

Preserve these signals:

- Portrait 3:4 or 4:5 vertical poster with a single dominant figure cluster.
- Horizontal 16:9 or 21:9 key visual posters are allowed when the user asks for a main visual, landscape fusion, or scene-rich wuxia poster.
- The subject is close, wind-swept, and partially obscured by hair, veil, or fabric.
- Motion is diagonal and layered: foreground streaks, midground cloth, subject, then soft background blur.
- Texture feels photographic and tactile: wind, skin, cloth folds, dust, spray, floating fibers, shallow depth of field, luminous backlight, and wet reflective armor or lacquered surfaces when present.
- Heroic variants may add armor plates, leather straps, talisman masks, weapon hilts, metal trims, skull charms, torn banners, or city-ruin silhouettes as long as the face stays the anchor.
- Wuxia variants may add ancient Chinese roofs, tiled eaves, mountain gates, bamboo groves, stone bridges, lanterns, flags, ink-wash mountains, river mist, carved wood, lacquer, silk embroidery, jade ornaments, and sword tassels when they help the image feel like a unified scene.
- Battlefield-glow variants may add dense bokeh embers, teal haze, molten gold reflections, violet shadow, black lacquer armor, translucent fabric shells, and layered crowd silhouettes while keeping one facial anchor.
- Typography is short and secondary: a small title, micro caption, or vertical fragment tucked into an edge or quiet area.
- Color stays restrained: ivory cloth, black hair, warm skin, pale sky, and one strong red or crimson motion accent.
- For richer Chinese atmosphere, allow vermilion, cinnabar, bronze gold, jade green, ink black, indigo sky, and warm parchment cream as supporting tones, but keep one accent dominant.
- For combat references, allow bronze, gold, teal-gray sky, soot, ash, ember sparks, dark jade shadows, molten orange, violet-black, and deep cyan reflections as supporting tones, but keep one accent dominant.
- Mood is cinematic, intimate, tense, poetic, and airy rather than glossy or commercial.

## Fusion With Minimal Zine

Carry forward:

- one clear attention cluster
- large portions of atmosphere or negative space
- short text treated as part of the composition
- controlled color anchoring
- sparse, editorial framing

Change the geometry:

- Replace static object clusters with wind-driven figure flow.
- Let fabric and ribbon act like the "material" layer from Minimal Zine.
- Let microtype or a short title behave like a quiet registration mark, not a headline.
- For battle-heavy references, let armor edges, weapon shafts, banners, or ruin beams become the diagonal structure that carries the motion.
- For wuxia key visuals, let landscape architecture and mountain depth share the same diagonal rhythm as cloth and weapon motion.
- For reflective-battle references, let glossy metal, wet highlights, and spark showers become the same structural language as cloth and motion blur.

## Layout Engine

Choose one family before compiling:

- closeup-sweep: face and shoulder dominate; wind and cloth sweep diagonally across the frame.
- veil-crossing: translucent fabric crosses the face and splits the composition into near/far layers.
- ribbon-orbit: red ribbon or cloth fragments orbit the subject and create motion arcs.
- backlit-fragment: strong backlight silhouettes hair and cloth while the face stays softly modelled.
- edge-cut portrait: the subject is cropped by the frame edge and appears in motion rather than posed.
- particle-storm: floating dust, spray, snow, or petals intensify the motion field.
- armored-vanguard: close warrior portrait with armor mass, blade or staff angle, and wind-raked banners in the background.
- mask-and-ember: the face is partly covered by a talisman, mask, scarf, or mouth guard while embers and sparks fill the near field.
- ruin-procession: the subject sits before broken city or temple forms, with layered banners and distant silhouettes creating scale.
- wuxia-key-visual: one featured heroine or hero fused with a broader Chinese landscape, so roofs, gates, pavilions, mountains, mist, banners, and weapon arcs share the frame with the close face.
- landscape-hero: the subject stays close in the foreground while the scene opens wide around them with rivers, cliffs, courtyards, or mountain passes.
- glow-siege: dense battle-light, ember bokeh, reflective armor, and distant crowd silhouettes form the scene around one human anchor.
- blade-screen: one sword or staff slices the frame diagonally as the foreground structure, with the face and armor partially revealed behind it.
- iridescent-vanguard: glossy wet armor, lacquer sheen, and teal-gold reflections dominate the materials while the face remains readable.
- crowd-haze-hero: the subject stands out of a blurred war crowd or army haze, with many distant figures reduced to atmosphere.

Use one family only.

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

Write the final prompt as five compact paragraphs:

1. Canvas, aspect ratio, atmosphere, and overall light.
2. Subject pose, crop, gaze, hair, armor, and veil or cloth movement.
3. Foreground and background motion materials, blur logic, weapon or banner angle, architecture or landscape depth, reflective material behavior, and exact layout family.
4. Typography, title placement, color accent, and print or scan texture.
5. Mood and hard avoids.

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

- The fallback reads provider configuration and `OPENAI_API_KEY` from the environment or Codex config, calls the OpenAI-compatible image endpoint, requests `b64_json`, and writes the decoded image locally. Never print or hard-code secrets.
- Store the exact final prompt beside the image. Never overwrite existing outputs; use a new descriptive slug.
- Inspect once. Regenerate with one targeted correction if the face becomes too centered, the cloth loses motion, the red accent disappears, or the result becomes a fashion ad, studio headshot, or over-clean beauty portrait.

## Hard Avoids

Always avoid:

- static centered headshot composition
- clean studio background, beauty-ad polish, or product-campaign framing
- glossy 3D render, heavy HDR, over-sharpened skin, or synthetic fashion lighting
- anime, cartoon, neon cyberpunk, or cute illustration
- busy scrapbook decoration, lace overload, and decorative sticker clutter
- large commercial headline, logo lockup, CTA, or long readable text
- washed-out cloth with no motion, or a motion blur so heavy the face disappears
- flat, toy-like fantasy costume design with no photographic air
- generic tourist postcard scenery with a pasted-in person
- plastic-looking armor, clean game-asset gloss, or uniformly synthetic highlights

## Output Format

Return the generated image, exact final prompt, and:

- Layout: selected family
- Motion: hair, cloth, ribbon, or particle path
- if present, armor, weapon, banner, or ruin path
- if present, roofline, gate, bamboo, mountain, river mist, or pavilion path
- if present, spark field, crowd haze, reflective armor, or blade-screen path
- Accent: selected color and form
- one short interpretation note

## Quality Gate

Before finalizing, check:

- Is there one close subject with clear facial focus?
- Do hair, veil, cloth, or ribbons create a strong diagonal flow?
- Do armor, banners, weapon shafts, or ruin fragments reinforce the same flow when present?
- Is the portrait still readable through occlusion and motion?
- Is the red or warm accent visible without taking over?
- Does the image retain a matte photographic feel rather than a beauty ad?
- Is the text short, sparse, and physically integrated?
- Did you generate and inspect the final raster image?
