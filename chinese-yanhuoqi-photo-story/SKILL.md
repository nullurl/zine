---
name: 烟火气影像
description: "【烟火气影像 / chinese-yanhuoqi-photo-story】 Generate Chinese yanhuoqi street-life photography, editorial scenery images, or poster-like photo stories with captions. Use when the user asks for 中国烟火气, 人间烟火, 老城生活, 市井人文, 街巷日常, 早市夜市, 小店摊位, 胡同巷子, 骑楼水巷, 县城街头, 老人小孩, 桥, 轮渡, 广场, or warm human documentary scenes. Supports single images and batches; every image must receive a concise Chinese caption, and poster/cover outputs may use ivory Song/Ming-style title typography."
---

# Chinese Yanhuoqi Photo Story

## Overview

Create Chinese street-life images where warmth comes from ordinary human use of space: food steam, shop light, wet pavement, bicycles, waiting, carrying, eating, closing, greeting, crossing, repairing, sweeping, and returning.

The skill should generalize from scene to scene. Do not reuse the same place twice as a template. Abstract the image through active relationships: heat against shadow, human scale against architecture, trace against clean ground, work against rest, motion against stillness, and care against hurry.

## Required Reference

Read [yanhuoqi-grammar.md](references/yanhuoqi-grammar.md) before generating or reverse-prompting. It defines the reusable smoke-and-life visual grammar, caption rules, and anti-cliche checks.

## Workflow

1. Parse the request into image count, ratio, location type, time, season, and whether typography is wanted.
2. If the user gives no count, produce one image. If the user gives a count, produce exactly that many independent images.
3. Decide the mode:
   - Photo-only: no text inside the image; captions are delivered beside the image.
   - Poster/cover/editorial typography: caption or title may appear inside the image.
4. For each image, choose one everyday human action, one spatial carrier, and at least three evidence layers from the reference.
5. Write one concise Chinese caption before generating. The caption should be poetic but grounded, usually 8-18 Chinese characters.
6. Generate the image as photorealistic documentary scenery unless the user explicitly asks for poster, cover, or typography.
7. If making a poster or cover, include the caption as an ivory Song/Ming-style title and keep typography sparse.
8. Save every final image and list each image with its caption.

## Image Defaults

- Ratio: 3:4 vertical unless the user specifies otherwise.
- Style: realistic documentary photography, cinematic but not commercial.
- Camera: human-height street observation with foreground occlusion, edge crop, and layered depth.
- Palette: source-led neutrals, warm practical light, damp stone, old plaster, wood, steel, steam, and muted fabric colour.
- People: small or medium scale, natural actions, not posing.
- Atmosphere: lived-in, tactile, warm, and restrained.
- Emotional core: ordinary dignity, everyday motion, quiet exchange, and a place that feels used rather than staged.

## Caption Rules

- Write one caption per image.
- Prefer concrete verbs and sensory nouns: 蒸, 等, 亮, 回, 坐, 收摊, 拎菜, 推车, 下雨, 起锅.
- Keep the caption tied to the scene. Do not write abstract slogans detached from the image.
- Avoid fake place claims, invented festivals, institutional names, and sentimental overstatement.
- For poster text, use ivory Song/Ming-style title typography by default.
- The caption is mandatory even when the image has no text inside it.
- Deliver the caption in the final response next to the file path so the user never receives a naked image.

## Hard Avoids

- tourism advertisement;
- postcard scenery;
- generic guochao ornament;
- red seal, ink splash, decorative border by default;
- staged models facing camera;
- over-clean ancient town;
- excessive lanterns;
- high saturation, HDR, glossy commercial lighting;
- random unreadable text or pseudo-English.

## Delivery

Return the finished image paths and show each image with its caption. If a batch was created, preserve the user's order. Never omit the caption line.
