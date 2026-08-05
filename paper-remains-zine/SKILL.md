---
name: 纸本遗迹
description: "Generate prompts and finished raster images for sparse torn-paper relic posters. Use when the user provides a theme, phrase, memory, object, reference image, or text fragment and wants aged fibrous paper, torn scraps, envelope corners, label fragments, stamp marks, one controlled accent color, and a large quiet paper field."
---

# Paper Remains Zine

Turn the user's theme, phrase, memory, object, or reference set into:

1. a final image-generation prompt, and
2. a finished vertical raster poster.

Fuse Minimal Zine negative-space discipline with paper residue: torn scraps, tape seams, envelope edges, stamp marks, photocopy wear, and one small accent shape.

## Reference Routing

- Treat supplied images as visual-grammar or subject references unless the user explicitly asks for a literal edit.
- Analyze local references locally: extract paper tone, scrap scale, tear shape, stamp geometry, accent color, text placement, and blank-space ratio.
- Do not reproduce visible brands, exact addresses, logos, watermarks, private text, or distinctive copied phrases from references.
- Do not upload private local references to an untrusted third-party endpoint. The bundled server fallback is text-only.
- Read [references/style-grammar.md](references/style-grammar.md) when reverse-engineering a reference or correcting style drift.
- Read [references/prompt-recipes.md](references/prompt-recipes.md) when choosing a layout or translating an abstract theme.

## Core Identity

Preserve these signals:

- Portrait 3:4 or 4:5 poster with a wide off-white or cream paper field.
- One compact paper-remnant cluster, usually centered or slightly low.
- 70%-92% of the canvas should read as quiet paper.
- Materials: torn paper, deckled scraps, translucent tape, envelope fragments, label stubs, stamp circles, photocopy residue, cut-out arrows, brush blocks, or torn receipt pieces.
- One small saturated accent is allowed and should be visible at thumbnail scale.
- Text is short, Chinese or mixed Chinese/English, and looks printed, stamped, or typewritten.
- Matte scan look, paper fibers, dust specks, mild wear, and shallow relief.
- Mood: quiet, conceptual, residual, slightly poetic, like a recovered note or broken notice.

## Fusion With Minimal Zine

Carry forward:

- huge negative space
- one attention cluster
- short text with material presence
- matte print softness and paper texture
- one controlled chromatic anchor

Change the geometry:

- Replace the tiny isolated specimen with torn-paper traces and document residue.
- Let the scrap cluster feel found, not decorative.
- Keep the composition sparse and editorial, not scrapbook-like.

## Layout Engine

Choose one family before compiling:

- single-remnant: one torn paper cluster floats in a large field.
- envelope-window: a torn envelope or flap reveals a smaller interior paper.
- stamp-trace: stamp circles, seals, or postmarks organize the cluster.
- split-cutout: two or three torn scraps overlap with a small color seam.
- margin-remainder: scraps gather off-center with text drifting in the margins.
- block-and-trace: one bold color block or arrow meets faint remnants and type.

Use one family only.

## Color Engine

Start from paper neutrals: warm white, cream, oatmeal, light gray, or faded kraft.
Choose one accent:

- cobalt or ultramarine for sharp conceptual tension
- vermilion or tomato red for urgency
- amber or marigold for warmth
- violet or indigo for memory or dream logic

The accent may appear as a brush block, arrow, stamp, tape strip, or torn print block. Do not reduce it to a tiny dot unless the user explicitly asks for that.

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

## Typography System

- Use one short Chinese line, or one Chinese line plus one small English line.
- Optional date or tiny descriptor is allowed.
- Type can be serif, typewriter, stamped, or rough print.
- Keep text subordinate to paper remnants.
- Do not ask the image model to render long paragraphs or copied article text.

## Prompt Compiler

Write the final prompt as five compact paragraphs:

1. Canvas, paper tone, blank-space ratio, and scan feel.
2. Cluster layout, torn materials, overlap, edges, tape, stamps, and scale.
3. Typography, title line, optional date, and one accent color or block.
4. Texture, wear, dust, print defects, and physical depth.
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

- The fallback reads provider configuration and OPENAI_API_KEY from the environment or Codex config, calls the OpenAI-compatible image endpoint, requests b64_json, and writes the decoded image locally. Never print or hard-code secrets.
- Store the exact final prompt beside the image. Never overwrite existing outputs; use a new descriptive slug.
- Inspect once. Regenerate with one targeted correction if the scraps become scrapbook clutter, the accent disappears, the text dominates, or the result becomes a clean poster template.

## Hard Avoids

Always avoid:

- full-bleed collage with no quiet paper field
- scrapbook stickers, lace, Polaroids, ribbons, or cute journaling
- postcard frames, UI cards, social templates, or dashboard styling
- glossy 3D mockup, hard drop shadows, dramatic perspective, luxury ad lighting
- commercial headline hierarchy, CTA, logo lockup, packaging, or brand campaign feeling
- cartoon, anime, neon, cyberpunk, fashion-drama styling
- long readable paragraphs, watermarks, social handles, private identifiers, or copied sign text
- too many accent colors or a flat beige board with no focal point

## Output Format

Return the generated image, exact final prompt, and:

- Layout: selected family
- Materials: scraps, tape, stamps, envelope, or block accent
- Typography: title and small text treatment
- one short interpretation note

## Quality Gate

Before finalizing, check:

- Is the canvas mostly quiet paper?
- Is there one compact paper-remnant cluster?
- Are tears, tape, stamps, or envelope fragments visible?
- Is the accent small but clearly legible?
- Is the text short and secondary?
- Does the scan feel matte, fibrous, and worn?
- Does the image avoid scrapbook clutter, UI, glossy mockup, and commercial styling?
- Did you generate and inspect the final raster image?
