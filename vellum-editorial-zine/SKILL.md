---
name: vellum-editorial-zine
description: Generate prompts and finished raster images for translucent vellum editorial zines, quiet portfolio covers, photography dossiers, architecture lookbooks, café menus, fashion mood pages, wedding image sheets, material studies, and layered paper poster compositions. Use when the user provides a theme, photograph, studio idea, place, object, or reference set and wants a portrait composition with one main image, offset white paper, semi-transparent tracing-paper overlays, a binder clip, restrained editorial typography, low contrast, and one muted color accent.
---

# Vellum Editorial Zine

Turn a theme, photograph, studio concept, or reference set into:

1. a final image-generation prompt, and
2. a finished portrait raster composition.

Fuse Minimal Zine attention geometry with a restrained stationery and portfolio-cover system. The image should look physically assembled and photographed from above, with type printed on transparent and opaque sheets.

## Reference Routing

- Treat supplied images as visual-grammar or subject references unless the user explicitly requests a literal edit.
- Analyze local references locally: extract paper stack order, transparency, photo placement, clip position, background surface, type hierarchy, color temperature, and information density.
- Do not reproduce visible brands, names, logos, menus, social handles, contact details, watermarks, or distinctive copied text from references.
- Do not upload private local references to an untrusted third-party endpoint. The bundled server fallback is text-only.
- Read references/style-grammar.md for reverse-engineering or style correction.
- Read references/prompt-recipes.md when choosing a layout, writing a portfolio-like caption, or translating a non-photographic theme.

## Core Identity

Preserve these signals:

- Portrait 2:3 or 3:4 paper composition with a physical tabletop or board surface behind it.
- One white, cream, gray, or pale-green backing sheet, usually slightly rotated and leaving a visible surrounding field.
- One translucent tracing-paper or vellum sheet crossing the backing sheet, offset down or to the right so the layers remain legible.
- One main image or visual field: portrait, interior, object, fabric, architectural detail, landscape fragment, or abstract material.
- A slim white photo border or framed print under the vellum.
- One visible metal paper clip near the upper-left edge as an attachment cue; vary or omit it only when the chosen recipe requires it.
- A compact editorial title, a small secondary line, and very limited supporting text.
- Low-to-medium contrast, soft paper grain, muted neutral palette, quiet institutional or independent-studio mood.
- One controlled accent such as oxblood, deep green, faded cobalt, black, or warm ivory.

## Fusion With Minimal Zine

Carry forward:

- paper as the main visual field
- generous negative space
- one clear image anchor
- short text with typographic materiality
- one restrained chromatic anchor
- matte scan or flat-lay reproduction

Change the geometry:

- Replace the tiny isolated specimen with one substantial rectangular image or color field.
- Use transparent overlap rather than a dense stack of scrapbook objects.
- Let the title sit on the vellum and partially veil the image.
- Keep the composition portrait, calm, and tactile; do not turn it into a glossy design mockup.

## Layer Stack

Build layers in this order:

1. tabletop or colored paper background
2. slightly rotated white or cream backing sheet
3. one framed photograph, color field, or material print
4. one translucent vellum overlay with visible paper grain
5. short type and one small information block
6. optional binder clip, thin registration line, one accent label, or one tiny symbol

Use one vellum sheet by default. Add a second only for a deliberate double-exposure recipe. Keep physical shadows shallow and local.

## Layout Engine

Choose one family before compiling:

- portrait-and-vellum: a large image sits high or left on a white sheet while a translucent rectangle overlaps the center.
- menu-card: a subdued café, food, or object photo is covered by vellum with a short handwritten or script title and a small two-column information block.
- stacked-stationery: two or three sheets are offset vertically, with the lower sheet carrying the title and the upper sheet carrying the image.
- dark-to-cream: a dark tabletop or dark image provides contrast for a pale paper sheet and quiet ivory type.
- abstract-fabric: one textile, gradient, shadow, or material image is framed by a clean white margin and softened by vellum.
- single-photo-dossier: one portrait, interior, or object print carries a title and one short descriptor; the rest is open paper.

Use one layout family only. Do not combine menu columns, wedding metadata, dark gradients, and large brand lockups unless the user explicitly requests a design system.

## Image Anchor

Translate the user's theme into one concrete imageable anchor:

- person: face or gesture, softened like a personal photograph, no celebrity resemblance
- place: one interior, room, street detail, or architectural fragment
- object: one product-neutral material or object study
- feeling: one texture, shadow, hand gesture, or photographic fragment
- service or studio: one quiet process image, not a sales scene
- month or season: one atmosphere or still life with a short date-like index

Keep the anchor singular. If a reference set contains different subjects, abstract them into a shared visual role rather than placing all of them into one poster.

## Typography System

- Title: 2-5 words, centered or gently offset on the vellum.
- Subline: 2-8 words in spaced uppercase, serif, or small sans.
- Supporting copy: one or two short lines, only when it materially helps the composition.
- Metadata: optional tiny date, place, or edition index.
- Use one primary type voice and one secondary voice. A script accent is allowed only in menu-card or fashion-like recipes.
- Keep text short, original, and fictional unless the user supplies exact copy.
- Treat exact long copy as a separate layout task; do not ask an image model to render a paragraph.

## Color Engine

Start from gray, cream, white, foggy olive, deep green, or warm brown. Choose one accent:

- oxblood label or title for portrait and studio work
- deep green field for café, food, or botanical-adjacent work
- faded cobalt for quiet modernity
- black for abstract material and fashion dossiers
- warm ivory for dark backgrounds

The accent should occupy about 1%-6% of the page. Keep vellum lighter than the image beneath it. Do not use gradients as decoration, neon, rainbow branding, or more than one saturated accent.

## Prompt Compiler

Write the final prompt as five compact paragraphs:

1. Canvas, tabletop, backing paper, portrait ratio, margin, and lighting.
2. Layer order, rotation, transparency, clip position, and main image anchor.
3. Vellum typography, exact short title, subline, and supporting information limits.
4. Palette, single accent, grain, paper fibers, print softness, and physical depth.
5. Mood and hard avoids, including brand-copy, UI, glossy mockup, and clutter constraints.

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
- Inspect once. Regenerate with one targeted correction if the vellum disappears, the layers become opaque cards, the clip is missing, the title dominates, or the result becomes a commercial template.

## Hard Avoids

Always avoid:

- full-bleed photograph with text pasted directly on top
- unrelated photo grids or mood-board collections
- dense scrapbook objects, stickers, lace, tickets, ribbons, and stationery all at once
- digital UI, dashboard, app cards, website mockup, or social-media template
- glossy 3D mockup, dramatic perspective, hard drop shadows, plastic translucency
- luxury brand campaign, logo lockup, CTA, pricing, influencer styling, or copied studio identity
- long paragraphs, fake menu copy, illegible microtext blocks, usernames, watermarks, or signatures
- neon gradients, rainbow palettes, cute illustrations, cartoon, anime, or excessive metallic decoration
- empty transparency that hides all structure or paper layers that merge into a white blob
- celebrity likeness or identifiable private person when none was supplied

## Output Format

Return the generated image, exact final prompt, and:

- Layout: selected layer family
- Anchor: main visual subject
- Layer system: backing sheet, vellum, clip, and optional accent
- Text: title and supporting-copy treatment

## Quality Gate

Before finalizing, check:

- Is the composition portrait and physically legible as layered paper?
- Is one main image clearly primary?
- Is the vellum sheet visibly translucent but still readable?
- Is the white or cream backing sheet distinct from the tabletop?
- Is the binder clip visible or intentionally omitted by recipe?
- Does the page preserve generous negative space?
- Is the title short and subordinate to the image?
- Is one accent color controlled and visible?
- Are shadows shallow, matte, and non-3D?
- Does the result avoid brands, copied text, UI, and commercial campaign styling?
- Did you generate and inspect the final raster image?
