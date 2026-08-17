# Gravity Poem Poster Structure

## Reverse-engineered source DNA

- Tall vertical poster with vast gray-beige paper field.
- The upper half is almost empty, carrying only paper grain, scratches, and age marks.
- The poem begins as tiny, widely spaced horizontal lines around the lower middle.
- Several larger Chinese keywords descend from the poem lines.
- Words are repeated as gray ghost copies, like misprints, memory, or afterimages.
- The final word lands on a small yellow rectangle or torn-paper label.
- The accent block is the only strong color.
- Mood is spare, literary, tired, intimate, and quietly severe.

## Layout families

- **low-center-fall:** small poem lines sit slightly below center; keywords fall vertically beneath them.
- **central-axis-drop:** one clear vertical centerline; words stack down the axis with fading echoes.
- **diagonal-drift:** keywords slip diagonally down-left or down-right, suggesting uncertainty.
- **yellow-anchor:** one final word sits inside or on top of a yellow block; all other words are black or gray.
- **split-weight:** two keyword clusters sit apart, then converge into one final highlighted word.
- **ghost-column:** repeated low-opacity copies create a column of fading text below one bold keyword.

## Typography behavior

- Small poem lines: tiny Songti/Ming-style or typewriter-like Chinese, wide tracking, charcoal gray.
- Primary keywords: larger black Chinese serif or rough printed type, not brush calligraphy.
- Echoes: repeated copies in pale gray, slightly offset downward, sometimes blurred or broken.
- Final anchor: one bold word or two-character phrase on a yellow label.

## Paper and color

- Background: warm gray, oatmeal, old book paper, concrete-like fiber, or handmade paper.
- Ink: black, charcoal, smoky gray.
- Accent: muted yellow, old label yellow, ochre, or faded tape yellow.
- Optional defects: tiny black dust, xerox specks, faint crease, horizontal paper seam, light scratches.

## Text strategy

- If user supplies exact text, use 1-3 short lines as the small poem.
- If text is too long, excerpt the strongest phrase and choose keywords.
- If no text is supplied, invent a short Chinese fragment and a two-character anchor.
- Do not ask generated-image models to render long paragraphs perfectly.

## Prompt recipe

1. Canvas and paper: vertical ratio, negative space, aged texture.
2. Poem lines: tiny horizontal lines, placement, tracking, phrase.
3. Keyword fall: selected words, scale, path, repetition, ghosting.
4. Accent and defects: yellow block, ink decay, xerox dust, paper seam.
5. Mood and avoids: quiet literary tone plus hard constraints.

## Hard avoids

- Full-page poem typesetting
- Decorative calligraphy scroll
- Big commercial headline
- Photo collage, objects, flowers, portraits, or illustrations
- Bright multicolor palette
- Clean digital white background
- Dense paragraphs
- Neon, glitch, UI, or poster-ad styling

## Example prompt skeleton

```text
Tall vertical 9:16 poster on aged gray handmade paper, 85% empty space, faint fibers, scratches, xerox dust, and one soft horizontal crease.

Near the lower middle, place three tiny widely tracked Chinese poem lines in charcoal gray, quiet and worn, like small letterpress text.

Below the poem, let 3 selected keywords fall downward along a slight diagonal: first bold black, then repeated pale gray echo copies with small offsets and fading opacity.

Place the final two-character word on one small muted yellow label block, slightly torn and imperfect; add ink smudge, dust, and print wear.

Sparse literary zine mood. Avoid full-page text, calligraphy scroll, collage objects, bright colors, clean digital typography, logos, and commercial poster hierarchy.
```
