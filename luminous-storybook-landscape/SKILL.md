---
name: 流光绘本风景
description: "【流光绘本风景 / luminous-storybook-landscape】 Generate luminous painterly storybook landscape prompts and matching raster images from a user theme, place, fantasy scene, village, city, garden, night market, architectural idea, journey, or visual brief. Use when the user wants cozy illuminated villages, magical floating houses, moonlit towns, flower-framed valleys, enchanted inns, portal gates, canal cities, lantern forests, umbrella gardens, miniature figures, gouache/acrylic brush texture, cinematic horizontal storybook compositions, or reverse-engineered prompt structures based on gc-minimal-zine-poster-v0-1 but converted into full-scene narrative illustration."
---

# Luminous Storybook Landscape

## Overview

Transform the user's content into a compact image-generation prompt, then generate a raster image unless the user explicitly requests prompt-only. This style borrows the recipe discipline and quality-gate rigor of `gc-minimal-zine-poster-v0-1`, but replaces sparse paper collage with full-frame painterly storybook worlds: warm lights, deep blue-green shadows, whimsical architecture, tiny travelers, and textured illustration grain.

## Source DNA

Use this reverse-engineered visual identity:

- **Canvas:** mostly horizontal 4:3 or 16:9 storybook frame. Use vertical only when the reference composition is a tall poster with embedded landscape band.
- **Scene type:** a complete painted environment: village roofs under moonlight, cliffside workshop above town, flower valley looking into the cosmos, lantern inn in a forest, grand open gate to a sunlit field, reflective canal city, candlelit city labyrinth, apartment facade full of lives, umbrella garden in rain, forest lantern procession.
- **Composition:** layered depth with foreground silhouettes or flowers, midground path/water/architecture, and background sky, cliffs, city, forest, or portal. The eye should travel through the frame.
- **Light logic:** many warm orange/yellow windows, lanterns, candles, or reflections against cool blue/teal/green night. Light is small, repeated, and emotionally important.
- **Brushwork:** visible gouache, acrylic, pastel, or screenprint-like paint texture; chunky shapes; grainy edges; soft bloom; rough canvas/paper tooth. Avoid polished digital gradients.
- **Scale and wonder:** oversized moons, impossible cliffs, houses stacked on clouds, giant flowers, tiny wagons, small people, narrow ladders, floating paper lights, palace-scale umbrellas, or city blocks as dollhouse slices.
- **Mood:** quiet adventure, bedtime fantasy, cozy mystery, festival night, rain-glow, enchanted travel, wonder without horror.

Do not default to the paper-negative-space rules of `gc-minimal-zine-poster-v0-1`. Keep its structured prompt compiler, variation selection, and anti-generic quality gate; transform the output into image-rich narrative illustration.

## Workflow

1. Parse the input.
   - Identify subject, place, time of day, emotional tone, architectural motifs, travel direction, weather, and any required story element.
   - If the user supplies only an abstract theme, convert it into one navigable place with a small human-scale action.
   - If a reference image is supplied, preserve its core subject or layout role but repaint it as a luminous storybook environment.

2. Choose a recipe.
   - Select one layout family, one light engine, one motif set, and one palette from the Variation Engine.
   - Prefer horizontal frame and layered depth unless the user asks otherwise.
   - Make the world coherent: one main route, one main architectural anchor, one dominant light source pattern.

3. Compile the prompt.
   - Use the Prompt Compiler field order.
   - Describe pixels only: camera view, scene layers, light, color, brush texture, tiny figures, and avoids.
   - Avoid lore exposition, named franchises, and text-heavy poster instructions unless asked.

4. Generate the image.
   - Use built-in image generation by default.
   - If the result becomes 3D, anime, or overly cinematic realism, regenerate once with stronger gouache/storybook/screenprint wording.
   - If it lacks warm points of light or a clear path through the frame, regenerate once with stronger light and composition instructions.

5. Return the image, prompt, and recipe.

## Prompt Compiler

Write final prompts as four compact paragraphs:

1. **Canvas and viewpoint:** aspect ratio, camera distance, scene type, time/weather, primary place.
2. **Scene structure:** foreground, midground, background, path/water/gate/sky relation, tiny characters and scale contrast.
3. **Light and palette:** warm light sources, cool shadows, accent colors, reflection behavior, atmospheric haze.
4. **Paint process and avoids:** gouache/acrylic/screenprint texture, grain, edges, and hard negative constraints.

Use this skeleton:

```text
[Canvas and viewpoint paragraph]

[Scene structure paragraph]

[Light and palette paragraph]

[Paint process and avoid-list paragraph]
```

## Variation Engine

Pick one layout family, light engine, motif set, and palette.

Layout families:

- **moonlit-rooftop-village:** dense European village rooftops, church spire, crescent moon, warm windows, a magical workshop or house perched above the town.
- **flower-valley-cosmos-window:** green valley path framed by giant flowers and cliffs; sky opens into star field or orange-blue cosmic water above.
- **enchanted-forest-inn:** large dark fantasy inn or temple in blue forest, warm windows and red lanterns, tiny traveler at entrance, misty distant city.
- **sunlit-gate-reveal:** monumental arch or palace gate opens to bright fields, clouds, flowers, and tiny visitors in silhouette.
- **canal-city-reflections:** blue night city with bridges, boats, red doors, warm windows, water reflections, small child or traveler in shadow.
- **candle-labyrinth-hall:** vast architectural interior or plaza filled with thousands of candles, circular path, high dark walls, moonlit doorway.
- **vertical-apartment-dollhouse:** dense city apartment facade with glowing rooms, balconies, staircases, tiny residents, cool night background.
- **rain-umbrella-garden:** oversized patterned umbrellas and hanging tassels over rainy garden paths, saturated red/yellow/blue shapes, soft rainfall lines.
- **letterbox-lantern-procession:** horizontal painted scene embedded inside tall black field or heavy letterbox; lantern procession through forest and water.

Light engines:

- warm window grid against blue night
- lantern trail reflected in water
- moon portal and dark silhouettes
- candle sea with red path
- rain glow through translucent umbrellas
- sunset peach sky behind dark roofs
- cosmic orange-blue sky above green valley

Motif sets:

- crooked roofs, chimneys, church spire, ladders, floating papers
- cliffs, flowers, small wagon, winding path, star field
- forest temple, red lanterns, animal-like roof silhouettes, distant city
- palace gate, floral field, clouds, tiny pilgrims
- canal bridge, boats, red doors, sitting child
- candle labyrinth, dark towers, central figure
- apartment windows, balconies, interior vignettes, exterior stairs
- umbrellas, rain strings, garden path, tiny walkers
- lantern procession, autumn forest, reflective pond

Palettes:

- **deep-teal-warm-window:** navy, teal, moss green, warm amber, tomato red accents.
- **spring-green-cosmos:** meadow green, dark ivy, lavender blue, orange coral sky, cream flowers.
- **forest-blue-lantern:** blue mist, deep green, black roof, warm yellow windows, red lanterns.
- **gate-sunlight:** cobalt door, peach stone, light green field, cream clouds, yellow flowers.
- **canal-blue-red:** midnight blue water, pale stone, red doors, warm window reflections.
- **candle-orange-black:** glowing orange, coral red path, black walls, deep blue vertical shadows.
- **apartment-cyan-coral:** cyan apartments, coral panels, yellow windows, dark blue city.
- **rain-umbrella-saturated:** red, teal, ochre yellow, periwinkle, forest green, rain-blue haze.

## Reverse Prompt Patterns

Use these references for reverse-prompting similar images. Adapt subject, viewpoint, and palette.

- **Floating workshop over village:** horizontal gouache storybook night village, dark rooftops and church spire below, huge pale moonlit cloud, warm workshop house perched on a cliff above town, ladders and ropes, tiny workers, glowing papers drifting in air, crescent moon.
- **Valley window to stars:** horizontal screenprint-like flower valley, winding cream road, tiny wagon, cliffs and giant white flowers in foreground, rectangular opening to starry orange-blue cosmic sea above.
- **Forest inn with lanterns:** wide blue-green forest at night, ornate dark inn with animal-like roof silhouettes, warm windows, red lanterns, tiny traveler on path, distant city lights through trees.
- **Open gate to fields:** monumental shadowed arch framing bright cobalt doors and sunlit field beyond, cream clouds, flower-covered slope, small visitors in silhouette.
- **Reflective canal city:** moonlit blue canal town with white stone buildings, red doors and lantern reflections, boats, bridge, small seated child in dark foreground.
- **Candle labyrinth:** vast dark hall or city square filled with thousands of orange candles in circular maze, red path to a moonlit doorway, tiny central figure.
- **Apartment lives:** tall dense apartment blocks split into warm glowing rooms, cyan and coral panels, visible staircases and balconies, small residents, dark snowy night behind.
- **Umbrella rain garden:** lush rainy fantasy garden packed with giant red, teal, and yellow patterned umbrellas, hanging tassels, tiny walkers, palace domes hidden in mist.
- **Lantern procession letterbox:** horizontal autumn forest scene inside black vertical canvas, robed travelers carrying lanterns above reflective water, orange canopy and blue undergrowth.

## Color and Texture Rules

- Use saturated color, but make it feel painted and printed: broken brush edges, visible canvas tooth, granular pigment, soft overprint.
- Balance cool dark masses with repeated small warm lights. The warm lights should guide the eye.
- Avoid pure black except for silhouettes and letterbox fields; keep shadows textured with blue, teal, green, or brown.
- Use simplified shape language and hand-painted detail, not photographic realism.
- Preserve atmospheric depth with layers, haze, tiny scale cues, and repeated light dots.

## Text Policy

Do not add visible poster text by default. This skill is image-led.

- If the user requests title text, keep it small or use a simple unobtrusive storybook title area.
- Avoid typography-heavy layouts, logos, captions, UI labels, and commercial metadata unless explicitly requested.

## Negative Constraints

Always avoid:

- photorealistic 3D render, cinematic VFX realism, glossy concept art polish
- anime character focus, manga panels, cute sticker style
- commercial poster typography, logos, product ad layout, CTA
- clean vector illustration, flat icon style, UI/game screenshot
- generic dark fantasy horror, gore, threatening mood
- empty landscape without tiny human-scale story details
- smooth digital gradients without brush texture
- over-sharp high-resolution stock-photo detail

## Output Format

````markdown
**生成图**

![Luminous storybook landscape image](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Recipe: [layout family / light engine / motif set / palette]
- Source interpretation: [one short note]
````

If the user asks for reverse prompting only, omit image generation and return the analyzed structure plus the final prompt.

## Quality Gate

Before finalizing, check:

- Did the prompt use the four-paragraph Prompt Compiler?
- Is the composition a full narrative scene, not a sparse paper poster?
- Is there a clear foreground, midground, background, and path/gate/water/sky route through the frame?
- Are warm lights repeated enough to create a cozy focal rhythm?
- Does the image include tiny human-scale story details?
- Is brush/paper/grain texture visible and non-digital?
- Does the palette match the selected recipe?
- Did the prompt avoid 3D, photorealism, anime focus, commercial typography, logos, and generic dark fantasy?
