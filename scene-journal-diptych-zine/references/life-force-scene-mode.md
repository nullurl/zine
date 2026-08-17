# Life-Force Upper Scene Mode

## Contents

- [Activation](#activation)
- [Portrait Scene Card](#portrait-scene-card)
- [Upper Photography Rules](#upper-photography-rules)
- [Identity and Face Rules](#identity-and-face-rules)
- [Person-to-Paper Extraction](#person-to-paper-extraction)
- [Prompt Block](#prompt-block)
- [Examples](#examples)
- [Failure Corrections](#failure-corrections)

## Activation

Use this mode only when one person or a small group carries the upper scene, or when the user requests portrait, traveler, family, child, elder, worker, shopkeeper, performer, or people-centered travel imagery.

Keep ordinary bystanders documentary. Do not force every place scene into a portrait.

This mode adapts the photographic priorities of `fantasy-life-force-portrait-photography` to the upper half of the diptych. It does not import full-screen portrait composition, unrelated fashion styling, or a separate color system into the lower journal.

## Portrait Scene Card

Define this card before writing the image prompt:

```text
Person: age range, role, cultural and place fit, identity lock if supplied
Event: one concrete action happening now
Distance: close, medium-close, active medium, or rare environment-led frame
Angle/crop: eye-level, low, tilted, over-shoulder, partial crop, or off-center
Foreground: one event-related object, hand, fabric, plant, glass, rain, steam, water, or architecture edge
Light: one real directional source and its physical effect
Color: one main scene hue + one supporting contrast + natural skin/neutral
Main optical effect: one only
Subtle edge effect: optional, one only
Extraction targets: three to five sources for the lower journal
```

## Upper Photography Rules

Use this priority order:

1. Specific human state.
2. Concrete action.
3. Active camera distance and viewpoint.
4. Foreground depth and accidental crop.
5. Real directional light.
6. Clean, memorable color relationship.
7. One restrained optical effect.

### Action

Show the person doing something tied to the place: lifting tea, opening a door, selecting a book, shielding rain, adjusting hair, handing over an object, stepping across water, laughing after interruption, looking for something, arranging goods, or reacting to wind, light, steam, rain, or another person.

Avoid standard standing, empty smiles, centered half-body portraits, and `a beautiful person at a place`.

### Distance and Framing

- Prefer 24-35 mm close or medium-close perspective when the action benefits from intimacy.
- Include face, hand, and action in medium-close frames.
- Allow cropped head, shoulder, arm, prop, or foreground when the event remains readable.
- Use low angle, tilted horizon, near-lens hand or prop, partial occlusion, or off-center framing one at a time.
- Use an environment-led wide frame only when the place has strong form and the person supplies scale.

### Light and Color

- Start with real sun, side light, backlight, window light, tree-shadow caustics, water reflection, rain sparkle, glass refraction, or fabric shadow.
- Keep highlights near overexposure only on hair, water, glass, cloth edge, or background; keep the face readable.
- Use one main scene hue, one support hue, and natural skin or neutral. The upper image may be colorful, but the lower journal selects only one of these hues as its saturated anchor.
- Keep dark areas open and clean; avoid dirty HDR contrast, muddy yellow grading, and cyberpunk neon.

### Optical Effects

Choose one main effect:

- foreground motion blur
- localized caustic pattern
- soft highlight bloom
- slight camera motion
- water or glass refraction
- gentle background swirl when geometry permits

Optionally add one subtle edge effect:

- slight red-cyan or blue-violet dispersion on hair, glass, water, fabric, metal, or frame edge
- tiny flare outside the face

Never stack effects or cover the eyes, nose, mouth, or primary identity cues.

## Identity and Face Rules

For a supplied person, preserve face, age, body, expression, pose, clothes, action, and relationship to the setting. Upgrade only photography, light, depth, color, and controlled optical treatment unless the user requests a specific edit.

For text-only generation:

- Create an original non-celebrity person appropriate to the requested culture and place.
- Avoid generic stock-model symmetry, oversized eyes, tiny pointed jaw, porcelain skin, and identical faces across a batch.
- Keep mild asymmetry, real bone structure, pores, lip texture, under-eye structure, stray hair, and age-appropriate detail.
- Keep skin soft-matte or satin-matte, not oily, mirrored, plastic, waxy, or over-smoothed.
- Keep children natural and age-appropriate. Keep elders' wrinkles, hands, hair, and age traces visible.

## Person-to-Paper Extraction

Do not make the face the default collage anchor. Extract the event around the person.

| Upper source | Preserve | Lower transformation |
| --- | --- | --- |
| Action prop | silhouette, grip relation, scale | object specimen, torn crop, flat color cutout |
| Gesture or action path | direction, arc, reach, turn | graphite trajectory, arrow, callout, perforated line |
| Clothing or accessory | one distinctive hue, pattern, fold | opaque risograph block, textile-like xerox strip, geometric reduction |
| Moving hair or fabric | contour and direction | ink sweep, line tracing, halftone edge |
| Foreground object | crop, occlusion shape, perspective | torn photo window, translucent overlay, irregular cutout |
| Light pattern | caustic spots, shadow edge, reflection rhythm | pale halftone, stencil dots, rough ink field |
| Environment relation | adjacency, overlap, route, repeated structure | dual panel, contour map, offset geometry |
| Microdata | place, time, weather, short action phrase | typewriter caption, stamp, tiny handwriting |

Use the person's portrait as a small faded photo fragment only when identity or relationship is essential to the memory. Preserve identity if used. Never flatten a supplied person's face into a colored silhouette without explicit permission.

## Prompt Block

Insert this after the upper scene description and before the element manifest:

```text
Human moment: [PERSON] is actively [CONCRETE ACTION], photographed from [DISTANCE / ANGLE] with [FOREGROUND] partly entering or framing the lens. Real [LIGHT SOURCE] creates [PHYSICAL LIGHT EFFECT]. Use [MAIN HUE] + [SUPPORT HUE] + natural skin/neutral. Apply only [MAIN OPTICAL EFFECT] and optional [SUBTLE EDGE EFFECT] on hair, fabric, water, glass, foreground, or frame edge. Keep identity and expression stable, facial features clean, skin softly matte, pores and hair texture real, and the moment candid rather than posed.
```

Then declare the extraction mappings explicitly. At least two should come from action, prop, gesture, clothing, foreground, or light.

## Examples

### Teahouse Pour

Upper: a middle-aged Chengdu visitor lifts a gaiwan lid while steam crosses side light; close medium frame with a bamboo-chair edge in the foreground. Deep green and white support natural skin; steam is the only soft optical effect.

Lower extraction:

- gaiwan -> green-and-black object specimen
- lid-lifting gesture -> graphite upward arc
- sleeve fold -> narrow xerox textile strip
- steam path -> pale halftone curve
- chair diagonal -> registration line

### Rain Umbrella

Upper: a traveler turns while opening a clear umbrella after rain; umbrella rim enters the lens, red cardigan contrasts with cool pavement, sunlight sparkles on droplets, subtle dispersion only on umbrella edges.

Lower extraction:

- umbrella ribs -> radial line diagram
- red cardigan -> one opaque tomato-red block
- raindrop rhythm -> stencil dots
- turning gesture -> curved trajectory
- pavement reflection -> gray halftone window

### Bookstore Selection

Upper: a reader half-turns while pulling a book from a shelf; medium-close off-center frame with one blurred book edge in foreground, warm shelf light and cobalt book spine as the color relationship.

Lower extraction:

- book rectangle -> cobalt risograph cutout
- pulling hand path -> short graphite line
- shelf rhythm -> pale repeated bars
- foreground blur -> torn translucent crop
- warm light -> subdued yellow-gray halftone, not a second saturated anchor

## Failure Corrections

- If the person is merely posing, replace the pose description with one concrete event and a hand-prop interaction.
- If the frame feels distant, move to a close or medium-close 24-35 mm perspective and bring one event-related foreground element near the lens.
- If the face looks synthetic, remove beauty language and restate mild asymmetry, pores, lip texture, under-eye structure, soft-matte skin, and natural expression compression.
- If skin is oily, prohibit mirror highlights on forehead, nose, cheeks, and chin; move highlights to hair, water, glass, or fabric edges.
- If effects cover the face, confine them to foreground, hair, fabric, water, glass, background, and outer frame.
- If the lower journal becomes a portrait scrapbook, remove full-face repeats and extract the action prop, gesture path, clothing color, foreground shape, and light pattern instead.
- If upper color overwhelms the diptych, keep one upper main hue plus one support hue, then carry only the main hue into the lower high-chroma anchor.
