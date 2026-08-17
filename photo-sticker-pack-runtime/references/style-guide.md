# Style Guide

Use this reference before drafting every `image_gen` prompt.

| Element | Requirement |
| --- | --- |
| Default ink | `#2E429B` |
| Fixed white | `#FFFFFF` |
| Source canvas | 1024 × 1024, transparent RGBA final output |
| Safe area | Keep content at least 64 px from the outer edge |
| Die-cut | Approximately 32 px continuous white border, with transparent exterior |
| Language | Generate illustrations without text; add captions locally in post-processing |

Preserve only visible, generation-relevant cues: hairstyle, face shape, glasses, clothing silhouette, visible expression, and unambiguous accessories. Use a recognizable stylized likeness, not a photorealistic portrait. Omit uncertain details and never add a brand, identity claim, or sensitive inference.

Use minimalist cobalt monoline and flat fills: clean curves, small expressive face details, tight readable composition, and high recognizability at sticker size. Do not use gradients, texture, photo detail, multicolor fills, realistic skin rendering, complicated shadows, cast shadows, glow, a sticker sheet, cropping, logos, watermarks, or model-rendered lettering.

Present the completed pack as an asymmetric editorial sticker sheet on white paper: varied large/medium/small anchors, natural whitespace, slight mixed rotations, content-aware visible bounds, collision-free rotated bounding boxes, and a subtle alpha-silhouette shadow. The shadow belongs to the gallery presentation only, never to generated art or downloadable PNG/SVG masters.

Use this built-in `image_gen` prompt frame, replacing angle-bracketed values only with visible facts:

```text
Use case: stylized-concept
Asset type: one sticker illustration source
Input images: Image 1 is the subject reference; Image 2 is style-only and its people, brand, and words must not be copied.
Subject: preserve <visible subject profile>; perform <one action> with <one accessory>.
Style/medium: clean commercial die-cut illustration; cobalt and white only; broad flat shapes; blocky simplified forms; uniform 8–12 px-equivalent monoline contours; uniform stroke weight; hairstyle as one solid readable silhouette with at most a few structural divisions.
Accessory color translation: preserve the visible accessory by shape and pose, but translate every non-white source color into cobalt; the only third color is the flat #00FF00 backdrop.
Detail budget: one clear facial expression, minimal fingers, no flyaway hairs, no individual hair strands, no tiny fabric folds, no hatching, no highlights, no gradients, no texture, no micro-decoration.
Composition/framing: one centered isolated sticker subject, generous padding, no crop, no sticker sheet.
Scene/backdrop: perfectly flat solid #00FF00 chroma-key background.
Text (verbatim): ""
Constraints: text-free generated art; no text, no letters, no logo, no watermark, no shadow, no gradient, no texture, no extra person; do not use #00FF00 in the subject.
```

The artwork palette is strict: cobalt and white only, apart from the temporary flat `#00FF00` backdrop. Keep accessory identity through its simplified shape and pose, never by retaining a source color.

The deterministic generation-time quality gate uses these inclusive acceptance boundaries: visible coverage 3–72%, forbidden-palette pixels at most 1% of visible pixels, at most 12% unsupported fine ink removed by a 3×3 opening, at most 8% of ink in disconnected components no larger than 192 px, ink density at least 1.5% of visible pixels, and at least 48 px transparent border clearance. There is no upper ink-density rejection because a clean solid-cobalt accessory or clothing silhouette is valid. The fine-ink and small-component limits target one-pixel whiskers and specks without treating ordinary face, glasses, bridge, mouth, or broad flat fills as excessive detail.

Use this **simplified retry** frame after a quality failure. Keep the same visible identity cues, but use a face/upper-body subject or one simple accessory silhouette, fewer contours, the same cobalt-and-white-only palette, and the same clean-line detail exclusions above.

## Kind-specific Subject and Composition variants

Keep the shared style, backdrop, `Text (verbatim): ""`, and text-free constraints above for every variant.

### `character_accessory`

Subject: preserve <visible protagonist profile>; <one action> with <one visible accessory>.

Composition/framing: one centered protagonist and one accessory, full or three-quarter body as needed, generous padding, no crop.

### `character_accessory_text`

Subject: preserve <visible protagonist profile>; <one action> with <one visible accessory>.

Composition/framing: one centered protagonist and one accessory with clear negative space for local caption placement. The image_gen result is still text-free; render its planned caption only in local post-processing.

### `accessory_text`

Subject: <one visible accessory> only, no person.

Composition/framing: one centered isolated accessory, generous padding, and clear negative space for local caption placement. The image_gen result remains text-free.

### `character_expression`

Subject: preserve <visible protagonist profile>; show one clear face/upper-body expression only, with no required accessory.

Composition/framing: centered face or upper body, generous padding, no crop, no text.

Use `#00FF00` only as a temporary background key. The deterministic post-process creates the final fixed-white and recolorable-ink layers.

The SVG master is a two-layer asset: fixed `#FFFFFF` for white subject areas and die-cut border, and `currentColor` for blue ink, fills, and local text. Keep both layers independent so the gallery never recolors white or regenerates the image.
