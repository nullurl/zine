---
name: cinema-portrait-film-zine
description: Generate prompts and finished raster images for cinematic real-person film portrait photography with Fujifilm, Ricoh GR, Leica, Hasselblad, Kodak, and CineStill camera/film feel, natural skin texture, analog grain, shallow depth of field, warm natural light, muted earthy palettes, and intimate nostalgic mood. Use when the user gives a person, mood, season, location, camera aesthetic, film simulation, or reference image and wants a vertical realistic film-cinema portrait rather than a paper zine poster, a storybook illustration, a botanical veil, a fashion ad, or a calendar planner.
---

# Cinema Portrait Film Zine

Turn the user's person, mood, season, location, or reference image into:

1. a final image-generation prompt, and
2. a generated raster image made from that prompt.

Use the `imagegen` skill for generation or editing. Prefer the local configured CLI/API path when the user explicitly asks for local image generation, image-gen CLI, model/API controls, or pptoken.

## Style Thesis

Create vertical cinematic film-still portraits that feel like a single frame pulled from a 35mm, compact street camera, or medium-format art-house film. The subject is a believable person in a natural or lived-in environment, lit by real directional light, captured with camera-specific perspective, natural skin texture, shallow depth of field, and restrained analog grain. The mood is intimate, nostalgic, and quietly observant — never posed, never commercial. This skill is the photographic-portrait counterpart to `gc-minimal-zine-poster-v0-1`: keep its prompt-compiler discipline, but replace sparse paper-anchor logic with full-frame realistic human photography, camera behavior, film color, and human presence.

## Reference-Derived Structure

Use these rules as the core visual grammar:

- **Frame:** vertical portrait, typically 3:4 to 3:5. Full-frame photograph, no border, no mockup, no paper overlay, no UI element.
- **Subject:** one person, usually female but not required. Framed from waist-up, bust-up, or full-body. The subject is the compositional anchor but does not fill the entire frame — environment and breathing space matter equally.
- **Gaze:** subject may look at camera, look away, or be seen in profile or from behind. The gaze should feel natural and unforced, as if caught mid-moment rather than directed.
- **Environment:** natural or semi-natural setting — garden, field, forest edge, window interior, rooftop, street, coastline, or domestic space. The environment is soft-focused but identifiable, not abstract blur.
- **Depth:** shallow depth of field. Subject is in focus; foreground and background fall out of focus smoothly. Bokeh should be organic and rounded, not clinical or geometric.
- **Light:** warm natural light — golden hour, window light, overcast softness, or dappled shade. Light has direction and falls across the subject's face or body. No studio softbox, no flash, no flat lighting. Backlighting and rim light are welcome when natural.
- **Color palette:** muted earth tones — warm amber, honey, burnt sienna, olive, sage, dusty rose, faded teal, warm ivory, soft brown. Skin tones are warm and natural, never airbrushed. One accent color may push through (warm orange, deep green, muted blue) but the overall temperature is warm and restrained.
- **Skin realism:** skin is clean but not erased. Preserve pore softness, slight uneven tone, faint under-eye structure, tiny moles/freckles when natural, real lip texture, real lash roots, and mild facial asymmetry. Avoid waxy face, plastic skin, oily highlights, over-sharpened pores, crunchy AI speckle, and beauty-filter smoothness.
- **Camera behavior:** camera brand or film simulation must affect perspective, focus behavior, color, contrast, highlight rolloff, shadow density, and moment selection. Do not use camera names as decorative labels.
- **Texture:** visible but restrained analog film grain across the entire image. Slight halation in highlights, gentle color shift in shadows (warm blacks, faint green-blacks, or cool cyan shadows). The image should not read as digital — it should feel like a real scan or camera file with optical softness, not AI texture.
- **Mood:** intimate, nostalgic, quiet, observant, tender, slightly melancholic. Like a memory of a person in a place, caught at the right moment.

## Anti-Uncanny Natural Portrait Rules

When the user asks for natural portrait photography or rejects AI-face / uncanny-valley results, shift from polished cinematic beauty toward believable human photography.

Build the image in this order:

1. **Person state first:** define what the person is doing, reacting to, or noticing before defining beauty, outfit, camera, or film color.
2. **Moment and body mechanics:** use relaxed shoulders, slight head turn, imperfect posture, a real hand task, wind-disrupted hair, squinting, half-smile, thinking face, or a gaze pulled by something off-camera. Avoid static standard standing poses.
3. **Face variation:** every generated person must have at least three non-template traits: different eye shape, eye distance, face length, brow shape, nose shape, mouth shape, jaw, cheekbone structure, or expression temperament.
4. **Skin as camera texture:** use soft matte / satin matte skin with slight uneven tone, faint under-eye structure, small pores, real lip texture, visible lash roots, small moles or freckles only when natural, and mild asymmetry. Do not request ultra-detailed pores, glossy beauty skin, or porcelain skin.
5. **Hair realism:** hair should have separated strands, flyaways, uneven direction, and breathable volume. Avoid plastic hair clumps, greasy shine, over-sharpened edges, and perfect wig-like outlines.
6. **Camera before filter:** camera names must imply shooting distance, lens perspective, timing, contrast, highlight rolloff, and skin rendering. Do not use Fujifilm, Ricoh, Leica, Hasselblad, Kodak, or CineStill as decorative style labels.
7. **Effects last:** grain, halation, color shift, blur, flare, chromatic aberration, or optical softness can support the photo only after the person and moment already feel real. Keep effects off the central face.

Hard avoid extra:

- identical AI-template face, doll-like eyes, over-perfect white porcelain face, sharp little chin template, influencer face, commercial stock model face
- mechanical smile, empty direct stare, eight-teeth smile by default, perfectly centered standard half-body portrait
- face with no expression muscles, wax statue face, plastic skin, repeated pore pattern, greasy forehead/nose/cheeks/chin, mirror-like facial highlights
- beauty-filter blur, heavy retouch, fake skin texture overlay, crunchy skin noise, dirty grain on the face, over-sharpened pores
- treating “luminous skin” as oily skin; facial highlights should be tiny and localized, mainly in eyes and lips, not broad reflective patches

## Visual DNA

Use this as prompt material:

- **Subject modes:** young woman in linen dress, person in coat and scarf, figure in summer cotton, someone in transitional clothing (spring/autumn), bare-shoulder or collarbone-visible intimate framing, person with windblown hair, figure from behind walking away.
- **Environment modes:** wildflower field, garden path, forest clearing, window-lit room, rooftop at dusk, coastal cliff, old street, cafe interior, staircase, meadow, orchard.
- **Light modes:** golden-hour backlight, window-light from left or right, dappled shade through leaves, overcast even softness, sunset rim, candle-warm interior, blue-hour cool ambient.
- **Camera feel modes:** Fujifilm Classic Chrome, Fujifilm Classic Negative, Fujifilm Nostalgic Negative, Fujifilm Eterna/Cinema, Ricoh GR Positive Film, Ricoh GR Negative Film, Ricoh GR Hi-Contrast B&W, Leica M street color, Hasselblad medium-format calm, Kodak Gold warm consumer film, Portra 400 warm portrait, CineStill 800T halation.
- **Film stock modes:** Portra 400 warmth, CineStill 800T halation, Fuji Pro 400H greenish neutral, Fujifilm Classic Chrome subdued documentary color, Fujifilm Classic Negative stronger contrast and nostalgic color separation, Fujifilm Nostalgic Negative amber highlights and soft cyan shadows, Ricoh GR Positive Film punchy street contrast, Ricoh GR Negative Film muted everyday color, expired film color shift, black-and-white Tri-X grain, warm Kodak Gold consumer grain.
- **Skin texture modes:** clean-matte natural skin, light pore softness, mild asymmetry, real lips and lash roots, subtle under-eye structure, no waxy retouch, no crunchy AI texture.
- **Color systems:**
  - warm-amber-honey: amber, honey, burnt sienna, olive, warm ivory
  - sage-dusty-rose: sage green, dusty rose, muted teal, warm cream
  - faded-teal-warm: faded teal, warm brown, soft orange, ivory
  - monochrome-warm-bw: warm black-and-white, silver highlights, deep soft blacks
  - blue-hour-cool: muted blue, warm skin, cool ambient, soft purple
- **Depth modes:** f/1.4 razor-thin focus plane, f/2.0 subject-in-focus background-soft, f/2.8 subject-plus-immediate-foreground, f/4 environmental portrait with more context.

## Prompt Compiler

Write the final image prompt as four compact paragraphs:

1. **Frame, person, and state:** aspect ratio, vertical portrait, who the person is, what they are doing or reacting to, framing (bust-up/waist-up/full-body), gaze direction, imperfect posture or gesture, clothing and texture.
2. **Environment and depth:** setting, what surrounds the subject, foreground and background elements, depth-of-field description, bokeh quality, how focus separates subject from environment.
3. **Camera, light, and color:** camera feel, lens perspective, light source and direction, time of day, warm or cool temperature, chosen palette, skin tone rendering, any rim/backlight, color proportions.
4. **Film texture, skin, and mood:** film stock or simulation, grain character, halation or color shift, natural skin texture, analog scan or camera-file feel, emotional temperature, hard avoids.

Make the prompt concrete and imageable. Specify the person, the place, the camera feel, the lens behavior, the light, the palette, skin texture, and film texture. Do not write style essays into the generation prompt.

## Variation Engine

Choose one option from each axis before writing the prompt.

### Framing

- **bust-up:** chest to head, intimate close range
- **waist-up:** waist to head, classic portrait
- **full-body:** entire figure in environment, more context
- **profile:** side view, face in profile
- **from-behind:** figure seen from behind, face not visible or partially visible
- **detail-fragment:** hand, shoulder, hair, or neckline close-up

### Environment

- **wildflower-field:** tall grass and wildflowers, natural and unmanicured
- **garden-path:** cultivated garden, paths, hedges, flowers
- **forest-clearing:** trees, filtered light, mossy or leafy ground
- **window-interior:** indoor, window light, domestic objects, curtain or sill
- **rooftop-dusk:** urban rooftop, sky, distant buildings, evening
- **coastal-cliff:** seaside, wind, open sky, rocks or grass
- **old-street:** narrow old-world street, stone or brick, shade
- **cafe-interior:** small cafe, warm interior light, cups, wood textures
- **meadow-orchard:** open meadow with fruit trees, dappled light

### Light

- **golden-hour-backlight:** sun low behind subject, warm rim, lens flare possible
- **window-side:** single window light from one side, soft gradient shadow
- **dappled-shade:** light filtering through leaves, moving pattern on subject
- **overcast-even:** gray-day softness, no harsh shadows, even and gentle
- **sunset-rim:** warm rim light at sunset, subject partially silhouetted
- **blue-hour-ambient:** cool ambient twilight, warm skin by contrast
- **candle-warm-interior:** warm low-interior light, intimate and golden

### Camera Feel

- **fujifilm-classic-chrome:** subdued documentary color, slightly cool shadows, warm skin, gentle contrast, magazine-photo restraint
- **fujifilm-classic-negative:** nostalgic higher contrast, warm highlights, cyan-green shadows, rich but not oversaturated street color
- **fujifilm-nostalgic-negative:** amber highlight rolloff, soft cyan shadows, relaxed medium contrast, tender memory tone
- **fujifilm-eterna:** low contrast cinematic color, soft highlight rolloff, subdued saturation, movie still calm
- **ricoh-gr-positive-film:** 28mm candid street perspective, strong but clean contrast, punchy reds/yellows, quick everyday snapshot rhythm
- **ricoh-gr-negative-film:** 28mm natural everyday perspective, muted color, soft contrast, quiet casual realism
- **ricoh-gr-hi-bw:** high-contrast black-and-white street snapshot, deep blacks, crisp subject separation, visible fine grain
- **leica-m-street:** 35mm or 50mm rangefinder feel, decisive moment, weighted shadows, rich microcontrast without digital harshness
- **hasselblad-medium-format:** calm medium-format portrait, wider tonal latitude, smooth color transitions, more environmental breathing room

### Film Stock

- **portra-400:** warm natural skin tones, fine grain, slightly warm overall
- **cinestill-800t:** halation in highlights, slight blue shift, cinematic night feel
- **fuji-pro-400h:** greenish neutral, soft pastel skin, clean but analog
- **fujifilm-classic-chrome-film:** subdued blues and greens, warm skin, quiet editorial contrast
- **fujifilm-classic-negative-film:** nostalgic color separation, deeper shadows, warm highlights, lived-in everyday color
- **fujifilm-nostalgic-negative-film:** amber cream highlights, soft cyan shadows, gentle low-contrast memory tone
- **ricoh-gr-positive-film:** compact-camera street punch, clean contrast, realistic colors, not glossy
- **ricoh-gr-negative-film:** muted casual color, soft contrast, quiet daily-life realism
- **expired-color-shift:** shifted colors, muted and unpredictable, faded warmth
- **tri-x-bw:** classic black-and-white, silver highlights, deep soft blacks, visible grain
- **kodak-gold-warm:** consumer warm grain, saturated but faded, nostalgic

### Skin Realism

- **clean-matte:** clean satin-matte skin, natural pores, no oily highlights
- **soft-natural:** gentle skin softness, visible facial structure, no beauty-filter blur
- **documentary-real:** slight uneven tone, under-eye structure, small asymmetries, believable real face
- **warm-translucent:** warm natural skin, subtle blush, tiny localized highlights only on eyes/lips
- **mature-texture:** preserve age lines, hand texture, and real facial character when age implies it

### Color System

- **warm-amber-honey:** amber, honey, burnt sienna, olive, warm ivory
- **sage-dusty-rose:** sage green, dusty rose, muted teal, warm cream
- **faded-teal-warm:** faded teal, warm brown, soft orange, ivory
- **monochrome-warm-bw:** warm black-and-white, silver highlights, deep blacks
- **blue-hour-cool:** muted blue, warm skin, cool ambient, soft purple

### Mood

- **intimate:** close, personal, private moment
- **nostalgic:** memory-like, looking back, tender distance
- **quiet:** still, calm, unhurried, contemplative
- **melancholic:** slightly sad beauty, bittersweet, wistful
- **observant:** watching, noticing, present but detached
- **dreamy:** soft, hazy, half-awake, unreal

## Generation Workflow

1. Parse the user's content.
   - Identify the person, mood, season, location, light preference, and any reference image role.
   - If no person description is given, invent one that fits the mood. If no mood is given, default to nostalgic.
   - If a reference image is provided, use it to determine framing, environment, palette, and film texture rather than copying its literal content.

2. Select a variation recipe.
   - Pick framing, environment, light, camera feel, film stock, skin realism, color system, and mood from the Variation Engine.
   - Ensure the choices form a coherent atmosphere. For example, golden-hour-backlight pairs well with wildflower-field, fujifilm-nostalgic-negative, portra-400, and warm-translucent skin; old-street pairs well with ricoh-gr-positive-film, ricoh-gr-positive-film stock, and documentary-real skin.
   - Do not default to the same recipe every time. Vary across runs.

3. Write the final image prompt.
   - Use the Prompt Compiler to compile the user's content into the four-paragraph prompt shape.
   - Specify the person, place, camera feel, lens perspective, light, palette, film stock, skin texture, and mood concretely. Keep it decisive.
   - Add realism constraints when generating faces: natural asymmetry, non-template face traits, expression muscles, real lash roots, lips with texture, soft matte skin, slight uneven tone, and subtle pore softness. Do not ask for heavy grain, ultra-detailed pores, glossy skin, porcelain skin, or extreme sharpness.
   - For anti-uncanny requests, make the person do a small believable action and avoid perfect direct-eye-contact beauty posing.
   - Specify in-image text only if the user provides it. The image should be textless.

4. Generate the image.
   - Use the `imagegen` skill by default.
   - If the user asks for local CLI, pptoken, or a specific model/API, follow that path.
   - Do not stop after prompt-only unless the user explicitly asks for prompt-only.
   - Inspect the result at thumbnail scale and at face scale. If the image reads as digital/crisp/over-saturated, tighten the camera-feel, highlight-rolloff, and analog-texture wording and regenerate once. If the face has waxy skin, oily highlights, over-sharpened pores, or crunchy AI noise, regenerate once with stronger `clean natural skin texture, soft matte skin, subtle pore softness, no AI texture artifacts, no plastic skin, no crunchy noise` wording. If the subject is too posed or commercial, strengthen the candid-mid-moment language and regenerate once.

5. Return the image and prompt.

## Hard Avoids

Always avoid:

- studio product photography, flat even lighting, or flash-on-camera look
- airbrushed or over-retouched skin, plastic-smooth texture, beauty-filter aesthetic
- waxy AI face, oily skin highlights, crunchy noise, over-sharpened pores, fake pore pattern, repeated skin texture, plastic hair, glassy oversized eyes
- posed/commercial portrait hierarchy, headshot, LinkedIn, or fashion-editorial drama
- sparse paper zine poster with 70%-90% negative space (use `gc-minimal-zine-poster-v0-1` instead)
- full-bleed painterly storybook scene with architecture and tiny figures (use `luminous-garden-storybook-zine` instead)
- misted botanical veil with no human subject (use `dream-bloom-veil-zine` instead)
- calendar grid or planner layout (use `monthly-memory-planner-zine` instead)
- 3D rendering, CGI, CGI-painting, or plastic texture
- cartoon, anime, kawaii, or flat illustration
- text blocks, headlines, commercial poster hierarchy, or logo
- neon, cyberpunk, high-contrast HDR, or oversaturated color
- heavy dirty film damage, excessive grain, gray-yellow retro filter, muddy green shadows, or low-quality scan artifacts
- using Fujifilm, Ricoh, Leica, or Hasselblad names as visible logos or text in the image
- wide cinematic landscape aspect ratio unless explicitly requested
- multiple people or group shots — this skill is about one subject

## Output Format

```markdown
**生成图**

![Cinema Portrait Film Zine image](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Recipe: [framing / environment / light / camera feel / film stock / skin realism / color / mood]
- [one short note about the content interpretation]
```

If generated images render directly without a file path, show the image normally and still include the final prompt.

## Quality Gate

Before finalizing, check:

- Did the prompt use the four-paragraph Prompt Compiler?
- Did the run choose a variation recipe across framing, environment, light, camera feel, film stock, skin realism, color, and mood?
- Is the structure materially different from recent visible outputs?
- Is the image a vertical portrait with a human subject as anchor?
- Does the subject feel caught mid-moment rather than posed?
- If this is a natural or anti-uncanny request, did the prompt define the person's state or action before styling?
- Does the face avoid template traits through at least three concrete differences in eyes, face shape, mouth, jaw, brow, nose, or expression temperament?
- Is the depth of field shallow with organic bokeh?
- Is the light warm, natural, and directional (not flat or studio)?
- Does the selected camera feel change perspective, contrast, color, and moment selection rather than acting as a brand label?
- Is the color palette muted earth tones with no neon or high-chroma primaries?
- Does the whole image carry restrained analog film grain without crunchy AI noise?
- Is skin realistic: soft matte, natural pores, mild asymmetry, real eyes/lips/lashes, no waxy texture?
- Does the mood read as intimate, nostalgic, or quietly observant?
- Did the prompt avoid studio lighting, airbrushed skin, waxy AI face, crunchy texture, paper zine, storybook, botanical veil, planner, 3D, cartoon, neon, and commercial hierarchy?
- Is there only one person in the frame?
- Did you actually generate the image?

## Example Requests

- "用 cinema-portrait-film-zine 做一张关于黄昏麦田里的女孩"
- "用 cinema-portrait-film-zine 做一张窗边侧光的怀旧人像"
- "用 cinema-portrait-film-zine 做一张黑白胶片森林人像"
- "用这张参考图做一张同风格的海边人像"
- "用 cinema-portrait-film-zine 做一张蓝调黄昏屋顶人像"
- "用 cinema-portrait-film-zine 做一张富士 Classic Negative 的街边回头人像"
- "用 cinema-portrait-film-zine 做一张理光 GR 日常抓拍感人像"
