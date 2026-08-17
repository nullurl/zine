---
name: 字体包装编辑
description: "【字体包装编辑 / font-packaging-editorial-poster】 Generate type-dense bilingual editorial promotional poster prompts and matching raster images from a user theme, product, exhibition, travel idea, food concept, photo, or visual brief. Use when the user wants font-packaging style layouts, oversized Chinese/English display typography, poster-design footer metadata, dense microcopy, halftone or scan textures, duotone photographic anchors, expressive calligraphy, pastel illustrated campaign posters, cultural exhibition posters, or reverse-engineered prompt structures based on gc-minimal-zine-poster-v0-1 but with commercial editorial typography."
---

# Font Packaging Editorial Poster

## Overview

Transform the user's content into a compact image-generation prompt, then generate a raster poster unless the user explicitly asks for prompt-only. This style borrows the recipe discipline and quality gate of `gc-minimal-zine-poster-v0-1`, but flips the visual identity from sparse quiet zine into type-forward font-packaging promotion: huge bilingual titles, image anchors, microcopy systems, bottom metadata bars, and visible print texture.

## Source DNA

Use this reverse-engineered identity:

- **Canvas:** vertical promotional poster, usually 3:4, 4:5, or 5:7; full-frame printed sheet; no mockup.
- **Type hierarchy:** one dominant headline occupying 20%-45% of the canvas. Use large Chinese characters, oversized English serif/condensed sans, italic script, calligraphy, or playful bubble lettering. Text is a graphic material, not only readable information.
- **Bilingual system:** combine Chinese display text with English subtitles, short slogans, event labels, dates, locations, category captions, and tiny footer metadata.
- **Image anchor:** one strong subject: mountain ridge, sea flowers, classical garden, portrait, ancient tree, dessert bowl, ink-calligraphy mass, product/venue/photo crop. The subject can be full-width, central, or embedded in rectangular blocks.
- **Packaging marks:** small logos, year marks, copyright-like footer rows, layout/promotion labels, poster-design badge, tiny paragraphs, itemized side notes. These should look like generic design-system metadata, not real brand claims unless supplied by the user.
- **Print texture:** halftone dots, risograph grain, horizontal scanlines, washed photo texture, posterized duotone, noisy paper, overprint edges, imperfect ink.
- **Color:** high-chroma but controlled. Common palettes: blue/purple mountain with white type and pink ridge outline; cyan/pink seaside pastel; neon yellow/black classical layout; pink/black exhibition poster; pale yellow/cobalt tree poster; candy pink/sky-blue dessert; orange/yellow/green neo-oriental ink.

Do not copy the sparse 70%-90% blank-paper rule from `gc-minimal-zine-poster-v0-1`. Keep its prompt compiler structure, variation selection, old-print constraints, and generated-image workflow, but allow dense typography and commercial editorial composition.

## Workflow

1. Parse the input.
   - Identify the subject, audience, mood, scene type, event/product category, required wording, and any supplied photo role.
   - If the user gives no text, invent a short bilingual title pair and generic supporting labels that fit the subject.
   - If the user supplies exact copy, preserve it as much as image generation allows, but warn silently through prompt structure by keeping text short and graphic.

2. Choose a recipe.
   - Select one layout family, one type system, one image treatment, and one color palette from the Variation Engine.
   - Change the composition grammar across batches, not just the color.
   - Let the headline and image compete intentionally; this style should feel designed, layered, and promotional.

3. Compile the prompt.
   - Use the Prompt Compiler field order.
   - Specify canvas, headline scale, Chinese/English type behavior, image anchor, microcopy zones, footer metadata, print texture, palette, and hard avoids.
   - Do not request long perfectly readable body copy; specify "tiny semi-legible metadata" where dense text is needed.

4. Generate the image.
   - Use built-in image generation by default.
   - If the output lacks a strong type hierarchy or bottom packaging details, tighten the prompt and regenerate once.
   - If the result becomes a clean corporate flyer, regenerate once with stronger halftone, risograph, overprint, and experimental typography language.

5. Return the generated image, final prompt, and recipe.

## Prompt Compiler

Write final prompts as four compact paragraphs:

1. **Canvas and campaign identity:** poster ratio, theme/category, print surface, overall mood, dominant palette.
2. **Type hierarchy:** exact large headline behavior, Chinese/English pairing, secondary slogans, side labels, date/location blocks, footer metadata.
3. **Image anchor and composition:** subject, placement, crop, illustration/photo/duotone/ink treatment, overlays, panels, ridge lines or rectangles.
4. **Print texture and avoids:** halftone/scan/risograph defects, paper grain, overprint, and negative constraints.

Use this skeleton:

```text
[Canvas and campaign identity paragraph]

[Type hierarchy paragraph]

[Image anchor and composition paragraph]

[Print texture and avoid-list paragraph]
```

## Variation Engine

Pick one from each group.

Layout families:

- **mountain-packaging:** gradient sky top, giant translucent English word at top, huge white Chinese title across middle, mountain photo band in lower half, colored ridge outline, bottom metadata strip.
- **pastel-seaside-illustration:** large blue Chinese headline, hand-drawn flower/sea illustration center, pink pixel vertical word, halftone sample patches, small bilingual copy blocks.
- **heritage-yellow-sidebar:** classical architecture or garden photo on left, bright yellow vertical panel on right with dense microcopy and black calligraphy, tiny footer captions.
- **exhibition-portrait-type:** oversized serif/italic English headline, scanned portrait block with horizontal lines, pink highlight bars, right-side vertical invitation text, date and venue block.
- **duotone-tree-info-panels:** pale yellow/cobalt duotone tree photo in blocky collage rectangles, large bilingual title at top, many small information cards and vertical Chinese labels.
- **cute-product-lineart:** cream halftone background, playful pink bubble headline, central line-art product/food illustration, blue wavy rules and small benefit words.
- **neo-oriental-ink-brand:** enormous western display headline, green script accent, orange/yellow gradient field, black digital-ink calligraphy mass, small brand-system labels along edges.

Type systems:

- **oversized Chinese display:** 3-6 huge Chinese characters dominate the poster; English subtitle stays smaller.
- **giant English specimen:** one huge English word or phrase is used like a font specimen; Chinese sits above, beside, or around it.
- **calligraphy collision:** black brush characters overlap photo or bright panel; small English serif subtitle anchors it.
- **playful bubble display:** rounded irregular Latin or Chinese lettering; friendly consumer-poster mood.
- **modular info grid:** title plus many rectangular copy cards, vertical labels, dates, and category stamps.

Image treatments:

- duotone photo, posterized photo, scanned portrait, hand-drawn line illustration, ink blur silhouette, halftone patch, collage rectangles, mountain cutout, flower sketch, tree texture.

Color palettes:

- **snow-blue-magenta:** cobalt/purple sky, white title, pink ridge or moon, dark green lower band, yellow accent text.
- **sea-pastel:** white, bright cyan-blue, soft pink, light sky blue, cream, orange/yellow flower accents, green leaves.
- **heritage-yellow-black:** white/green-black photo, fluorescent yellow panel, black calligraphy, tiny red or neutral text.
- **pink-black-gallery:** white field, black serif type, soft pink highlights, warm scanned portrait tones.
- **cobalt-ancient-tree:** pale yellow background, strong cobalt text and photo blocks, faint green shadows.
- **candy-halftone:** cream dot field, bubblegum pink linework, sky blue rules, lime green and orange food accents.
- **oriental-gradient:** ochre, yellow, orange, chartreuse, dark brown/black ink, small green script accent.

## Reverse Prompt Patterns

Use these as compact references. Adapt subject, words, and palette to the user's request.

- **Distant mountains packaging:** vertical poster with cobalt-purple gradient sky, huge translucent "MOUNTAINS" across top, massive white Chinese title over a snow mountain ridge, thin arced English sentence following the ridge, pink contour outline, dark green lower band, yellow center slogan, small travel labels and dense footer metadata.
- **Spring sea flower record:** white poster with oversized bright-blue Chinese calligraphy title across top, smaller English phrase in parentheses, pastel hand-drawn flowers rising from stone wall near center, pale blue sea texture block, pink pixel vertical word, halftone sample rectangles, bilingual microcopy.
- **New Chinese style:** classical garden window and blossom photo on left, high-key white paper, fluorescent yellow vertical information strip on right, dense microcopy, black brush calligraphy, tiny English serif labels along bottom.
- **Women growth exhibition:** white editorial poster, huge black italic serif "GROWS", pink script "SHE", scanned portrait image with horizontal scanlines, pink translucent text highlights, date/venue block at bottom, vertical invitation copy on right.
- **Ancient tree exhibition:** pale yellow poster with cobalt duotone ancient tree collage blocks, bilingual title "WHISPERS OF THE RINGS", vertical Chinese side labels, rectangular info cards, large date block.
- **Sweetness product poster:** cream halftone paper, large pink playful title, central pink line-art dessert bowl with small green/orange accents, blue wavy lines, benefit keywords, tiny product copy at bottom.
- **Boundless ink brand:** warm yellow-orange gradient poster, huge brown "Boundless" headline, green script accent, central black blurred digital-ink calligraphy mass with glitch scratches, small edge labels and footer packaging metadata.

## Text Rules

- Use short display text that image models can approximate: 1-4 big words or 2-6 large Chinese characters.
- Treat dense copy as visual texture: "tiny semi-legible microcopy", "footer metadata row", "design-system labels".
- If exact text matters, keep it large and minimal. Do not ask for long body copy to be perfectly readable.
- Include dates, years, venue, and footer marks only when useful for poster realism; they may be invented unless the user supplies exact content.

## Negative Constraints

Always avoid:

- plain minimalist zine with only one tiny object
- clean corporate flyer, app UI, PowerPoint slide, menu board
- glossy mockup, 3D paper, hard shadows, desk scene
- stock-photo realism without print treatment
- random real brand logos or false sponsors
- overlong perfectly readable paragraphs
- anime, cute mascot character unless the user asks for mascot design
- generic cyberpunk neon, vaporwave grid, luxury fashion ad
- flat vector-only look without halftone, scanline, risograph, or paper texture

## Output Format

````markdown
**生成图**

![Font packaging editorial poster](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Recipe: [layout family / type system / image treatment / palette]
- Source interpretation: [one short note]
````

If the user asks for reverse prompting only, omit image generation and return the analyzed structure plus the final prompt.

## Quality Gate

Before finalizing, check:

- Does the poster have a strong type hierarchy, with one dominant headline occupying 20%-45% of the canvas?
- Does it combine Chinese and English typography unless the user requested one language only?
- Is there a clear image anchor or calligraphy/illustration mass?
- Are microcopy, footer metadata, labels, dates, or packaging marks present enough to read as promotional design?
- Is print texture visible: halftone, scanlines, risograph grain, paper noise, posterized photo, or overprint?
- Does the palette match the selected recipe and avoid one-note beige minimalism?
- Did the prompt avoid clean corporate flyer, stock-photo poster, mockup, random real logo, and long readable body-copy demands?
