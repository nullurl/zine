#!/usr/bin/env python3
"""Build a paired proof by mapping one paper master onto a body portrait."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paper", required=True)
    parser.add_argument("--body", required=True)
    parser.add_argument("--body-out", required=True)
    parser.add_argument("--paired-out", required=True)
    return parser.parse_args()


def clean_body(body: Image.Image) -> Image.Image:
    rgb = body.convert("RGB")
    arr = np.asarray(rgb, dtype=np.float32)

    # Replace the complete footprint of the old tattoo. Tracking only its dark
    # pixels leaves a second jellyfish visible beneath the transferred master.
    footprint = Image.new("L", rgb.size, 0)
    draw = ImageDraw.Draw(footprint)
    draw.ellipse((286, 292, 704, 694), fill=255)
    draw.polygon(
        [(304, 500), (682, 470), (660, 870), (620, 1120),
         (584, 1308), (352, 1308), (306, 1080), (286, 760)],
        fill=255,
    )
    footprint_strength = np.asarray(
        footprint.filter(ImageFilter.GaussianBlur(24)), dtype=np.float32
    ) / 255.0
    arm_guard = Image.new("L", rgb.size, 0)
    ImageDraw.Draw(arm_guard).polygon(
        [(354, 278), (526, 238), (650, 292), (702, 410),
         (690, 650), (658, 890), (620, 1135), (582, 1318),
         (382, 1318), (338, 1110), (314, 870), (286, 650),
         (300, 430)],
        fill=255,
    )
    arm_strength = np.asarray(
        arm_guard.filter(ImageFilter.GaussianBlur(3.5)), dtype=np.float32
    ) / 255.0
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]
    luminance = arr @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
    skin = (
        (luminance > 72)
        & (r > 95)
        & (g > 58)
        & (b > 40)
        & (r > b * 1.16)
        & (g > b * 0.90)
    )
    mask = footprint_strength * arm_strength
    hard = (footprint_strength > 0.002) & (arm_strength > 0.08)
    repaired = fit_skin_surface(arr, hard, skin)
    alpha = np.power(np.clip(mask, 0.0, 1.0), 0.82)[..., None]

    # Reintroduce a restrained pore-like grain so the repaired skin does not
    # become a flat painted patch under the transferred tattoo.
    rng = np.random.default_rng(1387)
    grain = rng.normal(0.0, 1.55, repaired.shape).astype(np.float32)
    repaired = np.clip(repaired + grain, 0, 255)
    clean = arr * (1.0 - alpha) + repaired * alpha
    return Image.fromarray(np.uint8(np.clip(clean, 0, 255)), "RGB")


def fit_skin_surface(arr: np.ndarray, mask: np.ndarray, skin: np.ndarray) -> np.ndarray:
    h, w = mask.shape
    yy, xx = np.mgrid[0:h, 0:w]
    roi = (xx > 255) & (xx < 745) & (yy > 260) & (yy < 1320)
    luminance = arr @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
    valid = roi & skin & ~mask & (luminance > 112) & (luminance < 244)
    if valid.sum() < 5000:
        valid = roi & skin & ~mask

    left = np.full((h, 3), np.nan, dtype=np.float32)
    right = np.full((h, 3), np.nan, dtype=np.float32)
    fallback = np.full((h, 3), np.nan, dtype=np.float32)
    bounds = np.full((h, 2), np.nan, dtype=np.float32)

    for row in range(h):
        target_x = np.flatnonzero(mask[row])
        if target_x.size == 0:
            continue
        lo, hi = int(target_x[0]), int(target_x[-1])
        bounds[row] = (lo, hi)
        valid_x = np.flatnonzero(valid[row])
        if valid_x.size:
            fallback[row] = np.median(arr[row, valid_x], axis=0)
        left_x = valid_x[valid_x < lo]
        right_x = valid_x[valid_x > hi]
        if left_x.size >= 4:
            left[row] = np.median(arr[row, left_x[-48:]], axis=0)
        if right_x.size >= 4:
            right[row] = np.median(arr[row, right_x[:48]], axis=0)

    def fill_rows(values: np.ndarray) -> np.ndarray:
        result = values.copy()
        rows = np.arange(h)
        for channel in range(3):
            known = np.isfinite(result[:, channel])
            if known.sum() < 2:
                fallback_known = np.isfinite(fallback[:, channel])
                result[:, channel] = np.interp(
                    rows, rows[fallback_known], fallback[fallback_known, channel]
                )
            else:
                result[:, channel] = np.interp(
                    rows, rows[known], result[known, channel]
                )
            radius = 32
            offsets = np.arange(-radius, radius + 1, dtype=np.float32)
            kernel = np.exp(-0.5 * (offsets / 13.0) ** 2)
            kernel /= kernel.sum()
            padded = np.pad(result[:, channel], radius, mode="edge")
            result[:, channel] = np.convolve(padded, kernel, mode="valid")
        return result

    left = fill_rows(np.where(np.isfinite(left), left, fallback))
    right = fill_rows(np.where(np.isfinite(right), right, fallback))
    repaired = arr.copy()

    for row in range(h):
        if not np.isfinite(bounds[row, 0]):
            continue
        lo, hi = bounds[row]
        span = max(1.0, hi - lo)
        t = np.clip((np.arange(w, dtype=np.float32) - lo) / span, 0.0, 1.0)
        surface = left[row][None, :] * (1.0 - t[:, None]) + right[row][None, :] * t[:, None]
        shoulder = np.exp(-0.5 * ((row - 500.0) / 260.0) ** 2)
        cross_section = np.maximum(np.sin(np.pi * t), 0.0)
        highlight = (7.0 + 5.0 * shoulder) * cross_section ** 1.7
        surface += highlight[:, None] * np.array([1.0, 0.86, 0.72], dtype=np.float32)
        repaired[row] = np.clip(surface, 0, 255)

    # Add a neutral, correlated high-frequency texture. It preserves the
    # photographic surface without reintroducing fragments of the old tattoo.
    rng = np.random.default_rng(8241)
    texture = rng.normal(0.0, 1.0, (h, w)).astype(np.float32)
    texture_l = np.uint8(np.clip(texture * 28.0 + 128.0, 0, 255))
    smooth_texture = np.asarray(
        Image.fromarray(texture_l, "L").filter(ImageFilter.GaussianBlur(1.25)),
        dtype=np.float32,
    ) / 28.0 - (128.0 / 28.0)
    texture = (texture - smooth_texture)[..., None]
    repaired = np.clip(repaired + texture * np.array([1.9, 1.7, 1.45]), 0, 255)
    return repaired


def diffuse_fill(arr: np.ndarray, mask: np.ndarray) -> np.ndarray:
    filled = arr.copy()
    known = ~mask
    fill = filled.copy()

    for _ in range(900):
        frontier = mask & (
            np.roll(known, 1, axis=0)
            | np.roll(known, -1, axis=0)
            | np.roll(known, 1, axis=1)
            | np.roll(known, -1, axis=1)
        )
        if not frontier.any():
            break

        total = np.zeros_like(fill)
        count = np.zeros(mask.shape, dtype=np.float32)
        for shifted_known, shifted_fill in [
            (np.roll(known, 1, axis=0), np.roll(fill, 1, axis=0)),
            (np.roll(known, -1, axis=0), np.roll(fill, -1, axis=0)),
            (np.roll(known, 1, axis=1), np.roll(fill, 1, axis=1)),
            (np.roll(known, -1, axis=1), np.roll(fill, -1, axis=1)),
        ]:
            total += shifted_fill * shifted_known[..., None]
            count += shifted_known.astype(np.float32)

        fill[frontier] = total[frontier] / count[frontier, None]
        known[frontier] = True
        mask[frontier] = False

    smooth = Image.fromarray(np.uint8(np.clip(fill, 0, 255)), "RGB")
    smooth = smooth.filter(ImageFilter.GaussianBlur(1.8))
    return np.asarray(smooth, dtype=np.float32)


def extract_master(paper: Image.Image) -> Image.Image:
    rgb = np.asarray(paper.convert("RGB"), dtype=np.float32)
    luminance = rgb @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
    border = np.concatenate(
        [luminance[:80].ravel(), luminance[-80:].ravel(),
         luminance[:, :80].ravel(), luminance[:, -80:].ravel()]
    )
    paper_white = float(np.percentile(border, 68))
    delta = np.clip(paper_white - luminance, 0.0, 255.0)
    local_energy = np.asarray(
        Image.fromarray(np.uint8(delta), "L").filter(ImageFilter.GaussianBlur(1.35)),
        dtype=np.float32,
    )
    support = (delta > 34.0) | ((delta > 7.0) & (local_energy > 10.5))
    darkness = np.clip((delta - 5.5) / 155.0, 0.0, 1.0)
    alpha = np.where(support, np.power(darkness, 0.78) * 248.0, 0.0)
    alpha[alpha < 5.0] = 0.0
    alpha_image = Image.fromarray(np.uint8(np.clip(alpha, 0, 255)), "L")
    strong = Image.fromarray(np.uint8(delta > 42.0) * 255, "L")
    bbox = strong.getbbox()
    if bbox is None:
        raise RuntimeError("No ink mark found in paper master")
    padding = 42
    bbox = (
        max(0, bbox[0] - padding), max(0, bbox[1] - padding),
        min(paper.width, bbox[2] + padding), min(paper.height, bbox[3] + padding),
    )
    alpha_image = alpha_image.crop(bbox)
    ink = Image.new("RGB", alpha_image.size, (12, 10, 9))
    ink.putalpha(alpha_image)
    return ink


def place_master(clean: Image.Image, master: Image.Image) -> Image.Image:
    target_height = 900
    target_width = max(1, round(master.width * target_height / master.height))
    tattoo = master.resize((target_width, target_height), Image.Resampling.LANCZOS)
    tattoo = curve_to_upper_arm(tattoo)
    tattoo = tattoo.rotate(-1.0, resample=Image.Resampling.BICUBIC, expand=True)
    alpha = tattoo.getchannel("A").filter(ImageFilter.GaussianBlur(0.55))
    tattoo.putalpha(alpha)
    result = clean.convert("RGB")
    x = 280
    y = 306
    return embed_tattoo(result, tattoo, x, y)


def curve_to_upper_arm(tattoo: Image.Image) -> Image.Image:
    arr = np.asarray(tattoo.convert("RGBA"))
    h, w = arr.shape[:2]
    curved = np.zeros((h, w + 38, 4), dtype=np.uint8)
    for y in range(h):
        t = y / max(1, h - 1)
        shift = int(round(16 * np.sin((t - 0.08) * np.pi) - 11 * t))
        curved[y, 19 + shift : 19 + shift + w] = arr[y]
    return Image.fromarray(curved, "RGBA")


def embed_tattoo(base: Image.Image, tattoo: Image.Image, x: int, y: int) -> Image.Image:
    base_arr = np.asarray(base.convert("RGB"), dtype=np.float32)
    tattoo_arr = np.asarray(tattoo.convert("RGBA"), dtype=np.float32)
    h, w = tattoo_arr.shape[:2]
    x0, y0 = max(0, x), max(0, y)
    x1, y1 = min(base.width, x + w), min(base.height, y + h)
    if x1 <= x0 or y1 <= y0:
        return base

    tx0, ty0 = x0 - x, y0 - y
    tx1, ty1 = tx0 + (x1 - x0), ty0 + (y1 - y0)
    crop = base_arr[y0:y1, x0:x1]
    ink = tattoo_arr[ty0:ty1, tx0:tx1, :3]
    alpha = tattoo_arr[ty0:ty1, tx0:tx1, 3:4] / 255.0
    strength = np.clip(alpha * 0.98, 0, 0.93)

    luminance = crop @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
    local_light = (luminance[..., None] - 120.0) / 190.0
    ink_color = ink * (0.62 + np.clip(local_light, -0.12, 0.15))
    multiplied = crop * (1.0 - strength) + ink_color * strength

    pores = crop - np.asarray(
        Image.fromarray(np.uint8(np.clip(crop, 0, 255)), "RGB").filter(ImageFilter.GaussianBlur(1.1)),
        dtype=np.float32,
    )
    multiplied = np.clip(multiplied + pores * alpha * 0.22, 0, 255)
    crop[:] = multiplied
    base_arr[y0:y1, x0:x1] = crop
    return Image.fromarray(np.uint8(np.clip(base_arr, 0, 255)), "RGB")


def paired_canvas(paper: Image.Image, body: Image.Image) -> Image.Image:
    panel_size = (760, 1024)
    left = ImageOps.fit(paper.convert("RGB"), panel_size, Image.Resampling.LANCZOS, centering=(0.5, 0.5))
    right = ImageOps.fit(body.convert("RGB"), panel_size, Image.Resampling.LANCZOS, centering=(0.5, 0.46))
    canvas = Image.new("RGB", (1536, 1024), (244, 240, 232))
    canvas.paste(left, (0, 0))
    canvas.paste(right, (776, 0))
    return canvas


def main() -> None:
    args = parse_args()
    paper = Image.open(args.paper)
    body = Image.open(args.body)
    clean = clean_body(body)
    matched_body = place_master(clean, extract_master(paper))
    paired = paired_canvas(paper, matched_body)
    body_out = Path(args.body_out)
    paired_out = Path(args.paired_out)
    body_out.parent.mkdir(parents=True, exist_ok=True)
    paired_out.parent.mkdir(parents=True, exist_ok=True)
    matched_body.save(body_out, format="PNG")
    paired.save(paired_out, format="PNG")
    print(f"Wrote {body_out}")
    print(f"Wrote {paired_out}")


if __name__ == "__main__":
    main()
