---
name: deckled-light-overlay-zine
description: "Generate prompts and finished raster images for deckled paper photo-overlay zines. Use when the user gives a flower, tree, bamboo, garden, city skyline, sunset, street light, natural scene, photo, mood, sentence, or content brief and wants a vertical poster with an aged cream-paper upper layer, ragged deckled torn lower edge, real full-color photo revealed underneath, xerox or halftone botanical/urban print on the paper layer, sparse typewriter captions, timestamp labels, registration crosses, tiny specimen marks, and quiet archival light."
---

# Deckled Light Overlay Zine

Turn the user's content into both:

1. a final image-generation prompt, and
2. a generated raster image made from that prompt.

## Source Grammar

Use this visual grammar as the style core:

- **Two-layer structure:** the upper 55%-70% is aged cream paper; the lower 30%-45% is a real color photograph visible beneath a ragged torn paper edge.
- **Deckled edge:** the lower edge of the paper layer is irregular, fibrous, scalloped, and shadowed, like handmade paper torn across the poster.
- **Photo reveal:** the bottom photo shows the real scene in full color: sunflowers at sunset, bamboo canopy, rose branch, plum blossoms, blue-sky tree, city afterglow, or night garden light.
- **Paper print:** the upper paper reinterprets the same subject as a faded xerox, halftone, ink drawing, risograph print, translucent silhouette, or small overprinted panel.
- **Accents:** one restrained color accent may stay vivid in the paper print: sunflower yellow, bamboo green, cherry-blossom pink, rose red, violet petals, cyan sky, or deep blue tree canopy.
- **Typography:** tiny typewriter captions such as `AFTERGLOW / 19:42`, `WIND WRITES / 15:31`, `ONE BRANCH / 07:12`, `GARDEN AIR / 06:58`; optional archive number, single letter, vertical code, or `R`.
- **Marks:** registration crosses, thin arrows, dotted guide lines, faded numerals, tiny falling leaves or petals, and small stamp-like fragments.
- **Mood:** botanical archive, natural light record, torn-paper field poster, gentle specimen page, memory held between print and real photo.

## Mode Policy

Use **Standard Mode** for all generation. Compile only the visual details that should become pixels. Do not include analysis prose, source filenames, or process notes inside the final image prompt.

## Standard Mode Prompt Compiler

Every prompt must describe a single finished vertical poster image, not a UI, website, mockup template, or loose moodboard.

### First-Principles Fields

1. **Canvas and Layer Split**
   - Tall vertical 9:16 or 3:5 poster.
   - Upper layer: warm cream or tea-stained paper with fibers, stains, faint fold lines, and aged print texture.
   - Lower layer: real color photograph revealed below the torn edge.
   - The torn paper edge crosses horizontally around 55%-70% down the canvas and casts a subtle shadow.

2. **Main Subject**
   - Convert the user's content into one field-observed subject: flowers, bamboo, tree branches, leaves, skyline, sunset, street light, garden lamp, skyward tree, or city edge.
   - The lower photo should show the subject realistically, with natural light and depth.
   - The upper paper should echo or abstract the same subject as a print, illustration, crop, or specimen.

3. **Upper Paper Treatment**
   - Use faded black xerox, halftone, risograph grain, ink-stamp botanical lines, translucent paper cutout, or distressed photo-transfer.
   - Let part of the subject cross the paper as a sparse printed motif, not a dense full-bleed illustration.
   - Add one small photo-transfer panel or color-wash patch only when it supports the subject.
   - Preserve large blank cream-paper space.

4. **Lower Photo Reveal**
   - Place the real photo beneath the torn edge, occupying the bottom band.
   - Use vivid but natural light: sunset red, blue sky, glowing lamp, green foliage, pink blossoms, or city silhouettes.
   - The bottom photo can be softly out of focus near the edges, but must clearly show the subject.

5. **Typography System**
   - Use tiny typewriter or monospaced serif text.
   - Include one short uppercase title with a time code, formatted like `GARDEN AIR / 06:58`.
   - Optional archive elements: vertical number, `No. 0005`, isolated letters, `R`, `M_`, or small date-like codes.
   - Text should be sparse and integrated with the print; no large marketing headline.

6. **Color Logic**
   - Paper base stays warm cream, beige, or tea-stained.
   - Ink support is black, gray, faded charcoal, or sepia.
   - Use one subject color accent in the paper print, matching the lower photo: yellow, green, pink, red, violet, blue, or orange.
   - Avoid multi-color poster graphics; color should feel like a print artifact or natural photo leak.

7. **Registration and Specimen Marks**
   - Add 1-3 small crosshair registration marks, thin arrows, tiny numerals, faint vertical codes, falling petals/leaves, or specimen dots.
   - These marks should look like archival print calibration, not a UI overlay.

8. **Reproduction Texture**
   - Aged paper fibers, deckled torn paper thickness, soft shadow under torn edge, halftone dots, xerox wear, letterpress bleed, dust, faint stains, and low-contrast scan grain.
   - Keep a handmade physical-poster feeling.

9. **Emotional Temperature**
   - Quiet, light-filled, archival, botanical, time-stamped, gently nostalgic, observational.
   - The viewer should feel the same scene exists twice: once as a real moment, once as a paper memory.

10. **Hard Avoids**
   - Avoid clean digital collage, website mockup, commercial poster, glossy photo frame, scrapbook clutter, stickers, tape overload, full-bleed photo with no paper layer, fantasy forest, neon glow, 3D render, cinematic drama, thick borders, large sans headline, or long readable paragraphs.

### Standard Prompt Shape

Write the final Standard Mode prompt as four compact paragraphs:

1. canvas, aged upper paper, torn lower edge, lower photo reveal, overall split ratio
2. subject transformation between lower real photo and upper xerox/halftone paper print
3. typewriter caption, time code, archive marks, registration crosses, small specimen details
4. texture, color logic, mood, lighting, and avoid-list

Prefer precise placement and material instructions. If the user supplies no text, invent one short uppercase title and one time code.

## Variation Engine

Before writing the prompt, choose one option from each axis. For multiple images, vary at least three axes per image.

### Layout Family

- **sunset-flower-reveal:** torn cream paper above, bright flower field and sunset photo below.
- **bamboo-wind-sheet:** sparse bamboo print on the paper, green bamboo photo beneath.
- **single-branch-spring:** diagonal blossom branch print above, soft blossom photo below.
- **rose-over-wall:** rose branch printed near upper right, real rose photo below the torn edge.
- **garden-air-corner:** flower print grows from lower-left paper, real garden photo below.
- **midnight-garden-light:** dark floral transfer on paper, glowing lamp and flowers below.
- **blue-veins-tree:** blue tree-canopy print above, inverted or high-contrast tree photo below.
- **first-light-trunk:** upward tree trunk print on paper, blue sky and blossoms beneath.
- **city-afterglow:** skyline and sunflower print on paper, sunset city flower photo below.

### Subject Anchor

- sunflower skyline
- bamboo leaves
- cherry or plum blossom branch
- red rose over wall
- pink garden rose
- violet daisies
- tangled spring branches
- blue tree canopy
- white blossoms against sky
- city lights or afterglow

### Paper Print Treatment

- black xerox botanical line
- halftone flower transfer
- risograph color patch
- translucent photo-transfer rectangle
- ink-stamp branch silhouette
- distressed skyline silhouette
- blue cyanotype-like canopy
- faded grayscale specimen
- overprinted torn photo fragment

### Lower Photo Treatment

- crisp botanical photo
- soft-focus blossom background
- sunset city silhouette
- low-angle sky photo
- night garden lamp glow
- green canopy photo
- high-contrast inverted tree photo
- warm afterglow field photo

### Typography Mode

- title and time code
- vertical archive number
- tiny `No. 0005`
- isolated letter stamp
- `R` recorder mark
- small monospaced caption
- sparse date code
- typewriter words along right edge

### Mark Mode

- crosshair registration marks
- thin diagonal arrows
- falling printed petals
- tiny leaves in the air
- dotted specimen guide
- faint folded paper line
- red or gray calibration ticks
- small square print blocks

### Color Mode

- sunflower yellow and sunset red
- bamboo green and cream
- cherry pink and pale gray
- rose red and charcoal
- violet petals and pale blue
- cyanotype blue and tea stain
- lamp gold and midnight green
- skyline black and orange sky

### Mood Mode

- afterglow
- wind writes
- one branch
- over the wall
- garden air
- midnight garden
- lightward
- tangled spring
- blue veins
- first light

## Workflow

1. Determine mode.
   - Use Standard Mode.

2. Parse the user's content.
   - Identify the subject, mood, exact text if supplied, and any reference image role.
   - Convert abstract content into one scene that can exist as both lower photo and upper paper print.
   - If no text is supplied, invent a short uppercase title and time code matching the scene.

3. Select a variation recipe.
   - Pick layout, subject anchor, paper print treatment, lower photo treatment, typography mode, mark mode, color mode, and mood.
   - Keep the torn paper edge and lower photo reveal non-negotiable.
   - If the composition becomes busy, remove marks first; keep paper texture, subject print, type caption, and photo reveal.

4. Write the final image prompt.
   - Use the four-paragraph Standard Prompt Shape.
   - Specify the split ratio, torn edge position, paper print placement, lower photo subject, caption location, and color accent.
   - Keep exact in-image text short because image models distort long text.

5. Generate the image.
   - Use the built-in image generation capability by default.
   - Do not stop after prompt-only unless the user explicitly asks for prompt-only.
   - If the result lacks the torn paper/photo split, becomes a simple full-bleed photo, or turns into scrapbook clutter, tighten the deckled edge, upper-paper, lower-photo, and sparse archive mark constraints and regenerate once.

6. Return the image and prompt.

## Negative Constraints

Always avoid:

- full-bleed single photo with no torn paper overlay
- clean digital collage, website mockup, UI, app screen, vector template
- commercial poster, ad headline, logo lockup, CTA
- scrapbook clutter, stickers, tape overload, washi tape collage, cute stationery
- glossy photo frame, product mockup, 3D render, CGI, cinematic spotlight
- fantasy forest, neon glow, cyberpunk color, magical creature scene
- thick decorative border, large modern sans headline, long clean paragraphs
- too many unrelated photos or motifs
- overly colorful graphic design not tied to the lower photo subject

## Output Format

````markdown
**生成图**

![Deckled Light Overlay Zine image](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Mode: Standard
- Recipe: [layout / subject / paper print / lower photo / typography / marks / color / mood]
- [one short note about how the user's content became the torn-paper photo overlay]
````

If generated images render directly without a file path, show the image normally and still include the final prompt.

## Quality Gate

Before finalizing, check:

- Did the prompt create a vertical poster with an aged cream paper upper layer?
- Is the lower edge of the paper visibly ragged, deckled, fibrous, and shadowed?
- Is a real color photo revealed below the torn edge?
- Does the upper paper echo the same subject as xerox, halftone, risograph, ink print, or photo transfer?
- Is there a sparse typewriter title with time code or archive mark?
- Are crosshair marks, arrows, tiny numerals, petals, leaves, or specimen marks present but restrained?
- Does the palette stay paper-based with one subject-driven color accent?
- Does the image feel archival and physical rather than a clean digital collage?
- Did the prompt avoid UI, commercial, full-bleed photo, scrapbook, 3D, neon, and long text aesthetics?
- Did you actually generate the image?

## Example Requests

- "Use $deckled-light-overlay-zine to turn sunflowers at sunset into a torn-paper archive poster."
- "用 $deckled-light-overlay-zine 做一张关于竹影和风的图"
- "Use $deckled-light-overlay-zine to make a rose over the wall poster with timestamp."
