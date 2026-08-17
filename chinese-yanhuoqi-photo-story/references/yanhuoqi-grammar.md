# Yanhuoqi Grammar

## Core Definition

`烟火气` is not decoration. It is the visible evidence that ordinary life has recently happened, is happening, or is about to happen.

The image should make the viewer infer people through use: warm food, damp thresholds, bicycles, stools, plastic basins, shop awnings, kitchen steam, mended walls, handwritten prices, old doors, laundry, market crates, waiting figures, and worn paths.

Do not treat this as a fixed old-city look. The same grammar can move across hutong, canal bridge, county street, ferry landing, arcade lane, market edge, or neighborhood square as long as the life signals remain credible.

## Five Evidence Layers

Use at least three in every image, and prefer four when the scene can carry them.

1. **Heat:** steam, stove glow, lamp, soup, tea, roasted food, breakfast stall.
2. **Trace:** footprints, tire marks, wet stone, worn threshold, oil marks, rainwater, snow slush.
3. **Use:** stools, baskets, bicycles, carts, umbrellas, awnings, tables, shop shutters.
4. **Human action:** waiting, eating, carrying vegetables, pushing a cart, closing a stall, opening a door, chatting, sheltering from rain.
5. **Local material:** grey brick, plaster wall, old tile, arcade columns, canal stone, mountain-city steps, county street signs, wood doors.

## Spatial Carriers

Choose one carrier per image:

- northern hutong or old brick lane;
- Jiangnan canal lane or wet stone bridge;
- southwest mountain-city stairs;
- Lingnan arcade street;
- county market street;
- railway-station side street;
- old residential courtyard;
- morning food alley;
- night market back lane;
- riverside old town.

## Abstract Visual DNA

When the request is broad, reduce the scene to a relationship instead of a named place.

- heat against shadow;
- human scale against architecture;
- trace against clean ground;
- work against rest;
- motion against stillness;
- shelter against exposure;
- distance against closeness;
- clean gesture against worn surface;
- waiting against passing;
- care against hurry.

## Human Motifs

Prefer small actions that imply an entire day:

- opening a shutter;
- wiping a table;
- holding a steaming bowl;
- mending a tire;
- leaning on a bicycle;
- carrying greens or tofu;
- tying a scarf;
- sweeping a threshold;
- chatting across a doorway;
- taking a rest on a low stool;
- helping a child adjust clothing;
- waiting by a bridge or landing.

## Scene Patterns

Do not use all patterns at once. Pick one.

### Morning Opens

Breakfast steam, shop shutters lifting, bicycles passing, pale light, damp pavement.

Caption examples:
- 热气先醒了
- 巷口开锅
- 早市亮起来

### Rain Holds

Umbrellas, wet stone, shop light reflection, people waiting under awnings.

Caption examples:
- 雨把巷子留住
- 灯在水里亮着
- 等一阵雨停

### Evening Closes

Stalls packing up, warm lamps, tired figures, carts, last customers.

Caption examples:
- 收摊的人慢下来
- 灯下还有一碗热的
- 天黑前回去

### Winter Returns

Snow or slush, warm doorway, small figure carrying food or pushing bicycle.

Caption examples:
- 雪停以后回家
- 灯还给人留着
- 路冷，饭热

### County Street

Mixed signage, small shops, scooters, plastic stools, repair shops, vegetable baskets.

Caption examples:
- 县城慢慢热起来
- 街边坐一会儿
- 买菜的人经过

### Bridge / Landing

Bridge railings, water, boats, steps, crossings, handoffs, pauses, reflected light.

Caption examples:
- 桥边等一会儿
- 走到水那边去
- 这边也有日子过

## Typography Mode

Use typography only when the user asks for poster, cover, editorial image, or text on image.

Default typography:
- ivory Song/Ming-style Chinese title;
- 1 short title line or 2 stacked title lines;
- optional small caption or English line;
- no fake metadata blocks;
- no QR code;
- no random English filler.

When the user asks for scenery photo only, generate no text inside the image and provide captions outside the image.

## Caption Synthesis

Every output must have a caption, even when the image itself has no text.

Rules:

- one caption per image;
- 8-18 Chinese characters is the default range;
- use concrete verbs, objects, and spatial cues;
- keep it tied to one visible act;
- avoid slogans, moralizing, or generic praise;
- if the scene is quiet, let the caption stay quiet;
- if the scene is active, let the caption move.

Good caption shapes:

- [place cue] + [light or weather cue];
- [action] + [simple result];
- [small object] + [human state];
- [spatial cue] + [everyday verb].

Examples:

- 桥边晒会儿太阳
- 早市还没散
- 灯下有一碗热的
- 风一吹，巷子醒了

## Prompt Formula

Create a 3:4 vertical photorealistic Chinese street-life documentary image. Scene: [spatial carrier]. Human action: [one everyday action]. Evidence layers: [heat], [trace], [use], [local material]. Mood: warm human life inside restrained real surroundings. Composition: human-height camera, foreground occlusion, edge crop, layered depth, small natural figures, no posing. Lighting: warm practical light against cool ambient shadow, soft controlled highlights, weighted but readable dark areas. Palette: muted local colours, old wall texture, damp ground, warm lamps, natural skin and fabric tones. Avoid: tourism advertisement, postcard, generic guochao ornament, high saturation, HDR, fake ancient palace, excessive lanterns, red seals, ink splashes, watermark, logo, random text, or blank scenes with no human evidence.

## Quality Gate

Reject or regenerate if:

- it looks like a scenic spot ad;
- people pose for the camera;
- the place is too clean or theatrical;
- there is no evidence of use;
- the caption could fit any unrelated image;
- the image depends on red lanterns or antique decoration instead of lived activity;
- text appears when the user requested plain photos.
- the scene reads like a generic old-town postcard rather than current life.
