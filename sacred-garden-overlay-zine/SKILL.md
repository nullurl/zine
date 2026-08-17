---
name: sacred-garden-overlay-zine
description: "Generate sacred garden overlay zine prompts and matching raster images. Use when the user gives a theme, mood, place, memory, temple, statue, lotus pond, forest, water reflection, devotional object, or photo reference and wants a dark luminous analog poster with green forest glow, temple or Buddhist architecture, stone statues, lotus leaves, water-ripple double exposure, scratched film texture, deep vignette, and mystical garden archive aesthetics."
---

# Sacred Garden Overlay Zine

Turn the user's content into both:

1. a final image-generation prompt, and
2. a generated raster image made from that prompt.

## Source Grammar

Use this visual identity:

- vertical 3:5 or 4:5 analog photo-zine poster; horizontal 16:9 is allowed only when the chosen scene is a reclining statue or pond panorama
- dark, devotional, humid garden atmosphere with luminous green, teal, gold, black, violet, and faded cream
- strong vignette or black edges; bright center glow, sky hole, temple skylight, glowing flower, or water reflection as the light source
- sacred anchors: Buddhist statue, reclining figure, stone guardian, temple interior, pagoda ceiling, shrine wall, lotus pond, canal garden, forest canopy, mossy path
- double-exposure overlays: water ripples, pond reflections, leaf shadows, lotus petals, temple icon grids, eyes, scratches, dust, film damage
- surfaces feel aged, scratched, scanned, damp, smoky, low-contrast, and imperfect
- composition is quiet and immersive, not decorative; the scene should feel discovered, half-submerged, or remembered

The style should feel like a sacred garden apparition captured on damaged film, not a clean travel photo, not a fantasy render, and not a generic temple poster.

## Mode Policy

Use **Standard Mode** for all generation. Use the Standard Mode Prompt Compiler below to convert the user's content into compact, imageable prompts.

Use prompt-only output only when the user explicitly asks for prompt-only.

## Standard Mode Prompt Compiler

Default generation should compile only visible image instructions.

### First-Principles Fields

Every prompt must answer these rendering questions in this order:

1. **Canvas:** What is the frame?
   - tall vertical 3:5 or 4:5 analog photo poster by default; use 16:9 only for reclining statue, lotus pond, or wide temple tableau; no mockup, no UI.

2. **Sacred Place:** What is the underlying space?
   - choose one concrete place from the user's content: forest canopy, canal under trees, lotus pond, temple interior, shrine ceiling, stone statue courtyard, Buddhist hall, mossy garden, night pond, or rain-soaked path.

3. **Primary Anchor:** What object carries attention?
   - one strong anchor: luminous canopy opening, ornate temple oculus, standing statue, reclining Buddha-like statue, lotus blossom, stone guardian pair, glowing pond flower, eye reflected in water, or shrine architecture.

4. **Overlay Layer:** What double-exposure layer changes the reality?
   - choose one or two: water ripple rings, leaf reflections, lotus leaves, translucent flower petals, carved icon pattern, eye texture, scratches, rain marks, black branches, or mottled film haze.

5. **Light Geometry:** Where does light come from?
   - bright green canopy center, turquoise sky hole, gold temple lamps, glowing lotus, milky water reflection, pale statue body, or small warm shrine lights; surround it with heavy dark edges.

6. **Color Logic:** What palette controls the mood?
   - deep green-black shadows with acid green bloom; teal sky with antique gold interior; violet-black pond with pale lotus; cream stone with mint haze; copper-gold shrine lights against turquoise oculus.

7. **Surface Damage:** What physical process defines the image?
   - scratched film scan, dust specks, worn emulsion, light leaks, chemical stains, low-resolution softness, haze, green color cast, cyan/red bleed, and uneven exposure.

8. **Composition Density:** How much is visible?
   - immersive full-frame scene with one clear anchor; dense texture is allowed but must not become clutter. Keep the image readable at thumbnail scale.

9. **Typography:** Should text appear?
   - default to no text. If requested, use one tiny low-contrast caption or date-like mark near an edge; never add a headline.

10. **Emotional Temperature:** What should the viewer feel first?
   - sacred, damp, hidden, nocturnal, glowing, meditative, uncanny, archival, half-dream, ritual garden memory.

11. **Hard Avoids:** What must not appear?
   - clean travel brochure, glossy tourism poster, fantasy game environment, polished 3D render, neon cyberpunk, cute illustration, commercial layout, UI, dense typography.

### Standard Prompt Shape

Write the final Standard Mode prompt as four compact paragraphs:

1. canvas + sacred place + primary anchor + light geometry
2. overlay layers + blend behavior + composition placement
3. palette + surface damage + analog scan texture
4. mood + typography policy + avoid-list

Use precise nouns and material terms. Do not describe the references or the skill; describe the image to generate.

## Variation Engine

Before writing the prompt, choose one option from each axis. Vary the structure, not only color.

### Layout Family

- **canopy-glow:** upward-looking forest canopy with black trunks around a bright green center
- **canal-green-dream:** tree tunnel and canal reflection under luminous green haze
- **temple-oculus:** ornate gold temple interior looking up to a turquoise sky opening
- **statue-bird-haze:** standing stone statue with dark bird or wing shape, mint film fog
- **lotus-night-pond:** dark lotus pond with one glowing flower and scratched lily pads
- **guardian-ripple-overlay:** stone guardian or carved posts seen through water-ripple reflections
- **flower-tree-monochrome:** monochrome tree canopy overlaid with glowing white flowers
- **reclining-lotus-shrine:** reclining pale statue in darkness with giant translucent lotus and shrine icon patterns
- **eye-lotus-water:** giant eye blended with lotus pond leaves and one glowing blossom
- **wide-devotional-tableau:** horizontal dark shrine or pond panorama with central sacred figure

### Sacred Place

- dense forest canopy
- tree-lined canal
- lotus pond at night
- temple interior under an oculus
- carved Buddhist shrine wall
- stone statue courtyard
- mossy guardian gate
- damp garden path
- dark pond with floating leaves
- shadowed hall with shrine lights

### Primary Anchor

- luminous green canopy opening
- ornate gold central pagoda or shrine tower
- stone statue holding a bird
- reclining pale devotional statue
- glowing lotus blossom
- stone guardian pair
- eye reflected under lotus leaves
- turquoise temple skylight
- black tree arch over water
- small warm lamps around a sacred structure

### Overlay Layer

- circular water-ripple rings
- translucent lotus leaves
- pale lotus petals behind a statue
- reflected tree branches
- carved icon grid
- giant eye texture
- white flower silhouettes
- scratched emulsion streaks
- rain specks and dust
- green chemical fog

### Light Treatment

- acid green bloom through leaves
- turquoise sky hole surrounded by gold
- violet-black pond with one glowing flower
- pale statue body emerging from black
- mint haze behind stone
- small gold lamps sparkling through scratches
- milky water reflection across the frame
- overexposed center fading into dark corners

### Palette Mode

- black-brown shadows, luminous leaf green, faded yellow highlights
- antique gold architecture, turquoise sky, warm lamp specks
- mint-grey statue, cream fog, black base
- violet-black water, emerald lily pads, pink-white lotus glow
- forest green canal, pale yellow mist, brown vignette
- grayscale canopy, white flower glow, blue-black reflection
- dark shrine black, dusty pink lotus, chalk white statue
- olive water reflection, stone grey guardians, pale green leaf haze

## Workflow

1. Parse the user's content.
   - Identify the main subject, place, spiritual or memory mood, and any supplied reference role.
   - If the content is abstract, translate it into one sacred place plus one anchor plus one overlay layer.
   - If the user supplies a photo, decide whether it should become the sacred place, primary anchor, or overlay texture.

2. Select a variation recipe.
   - Choose layout, sacred place, primary anchor, overlay layer, light treatment, and palette from the Variation Engine.
   - Keep one clear anchor even when the texture is dense.
   - Use 16:9 only for wide devotional tableau, reclining statue, or pond panorama; otherwise use vertical 3:5 or 4:5.

3. Write the final image prompt.
   - Use the Standard Prompt Shape.
   - Specify the light source, dark-edge behavior, overlay scale, and analog damage.
   - Default to no text.
   - Make the image feel photographic and damaged, not illustrated or rendered.

4. Generate the image.
   - Use the available image generation capability by default.
   - Do not stop after prompt-only unless the user asks for prompt-only.
   - If the result becomes a clean temple photo, fantasy concept art, or ordinary forest scene, tighten the prompt and regenerate once with stronger `scratched analog film`, `double exposure`, `dark vignette`, `water-ripple overlay`, and `luminous green/gold center` wording.

5. Return the image and prompt.

## Negative Constraints

Always avoid:

- clean travel photography, tourism poster, postcard, brochure layout
- glossy architecture render, fantasy game environment, cinematic VFX spectacle
- bright neon cyberpunk, synthetic gradients, colorful commercial lighting
- cute cartoon, anime, kawaii illustration, sticker collage
- product ad, logo, CTA, brand campaign, headline poster
- clean paper stationery, scrapbook clutter, washi tape, UI screenshot
- perfectly sharp stock photo realism with no scratches or film damage
- overly literal horror, gore, monsters, jump-scare mood
- long readable typography or large slogan
- flat vector temple iconography

## Output Format

````markdown
**生成图**

![Sacred Garden Overlay Zine style poster](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Mode: Standard
- Recipe: [layout / sacred place / primary anchor / overlay layer / light treatment / palette]
- [one short note about the content interpretation]
````

If generated images render directly without a file path, show the image normally and still include the final prompt.

## Quality Gate

Before finalizing, check:

- Did the run use the Standard Mode Prompt Compiler?
- Did the run choose a recipe across layout, sacred place, primary anchor, overlay layer, light treatment, and palette?
- Is the image an analog photo-zine poster rather than a clean travel photo?
- Is there a sacred garden, temple, statue, lotus pond, canal, shrine, or forest setting?
- Is one primary anchor readable at thumbnail scale?
- Are water ripples, reflections, lotus leaves, flower petals, carved icons, eye texture, or film damage used as overlay layers?
- Does the image have heavy dark edges or black shadows plus one luminous green, teal, gold, cream, or lotus-pink light source?
- Are scratches, dust, haze, stains, light leak, or worn film texture visible?
- Is typography absent or tiny and low-contrast unless requested otherwise?
- Did the prompt avoid tourism poster, fantasy render, neon, cartoon, scrapbook, UI, commercial ad, and text-heavy aesthetics?
- Did you actually generate the image?

## Example Requests

- "用 $sacred-garden-overlay-zine 做一张关于寺庙雨夜的绿光海报"
- "Use $sacred-garden-overlay-zine to turn a memory of a lotus pond into a dark ritual garden poster."
- "用这张森林照片做一张水纹叠印的神圣花园 zine"
- "Use $sacred-garden-overlay-zine prompt-only for a reclining statue with a giant lotus behind it."
