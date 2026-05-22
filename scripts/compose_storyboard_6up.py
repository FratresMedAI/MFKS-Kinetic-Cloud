#!/usr/bin/env python3
"""Compose mkfs_puck_storyboard_6up.png from individual frame PNGs."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ASSETS = Path(__file__).resolve().parent.parent / "assets"
FRAMES = [
    ("mkfs_puck_frame01_launch.png", "Frame 1 — Launch"),
    ("mkfs_puck_frame02_flight.png", "Frame 2 — Flight"),
    ("mkfs_puck_frame03_setback.png", "Frame 3 — Setback @ R_open"),
    ("mkfs_puck_frame04_skirt_peel.png", "Frame 4 — Skirt Peel"),
    ("mkfs_puck_frame05_drag_spread.png", "Frame 5 — Drag Spread"),
    ("mkfs_puck_frame06_cloud.png", "Frame 6 — Terminal Cloud @ 350 ft"),
]


def main() -> None:
    cell_w, cell_h = 960, 720
    label_h = 48
    header_h = 72
    cols, rows = 3, 2
    sheet_w = cols * cell_w
    sheet_h = header_h + rows * (cell_h + label_h)
    sheet = Image.new("RGB", (sheet_w, sheet_h), (24, 28, 32))
    draw = ImageDraw.Draw(sheet)
    try:
        title_font = ImageFont.truetype("arial.ttf", 36)
        label_font = ImageFont.truetype("arial.ttf", 22)
    except OSError:
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default()

    draw.text(
        (24, 18),
        "MKFS Puck Cutaway Storyboard — PUCK-A / PUCK-B",
        fill=(230, 230, 230),
        font=title_font,
    )

    for i, (fname, label) in enumerate(FRAMES):
        row, col = divmod(i, cols)
        x = col * cell_w
        y = header_h + row * (cell_h + label_h)
        img = Image.open(ASSETS / fname).convert("RGB")
        img.thumbnail((cell_w, cell_h), Image.Resampling.LANCZOS)
        ox = x + (cell_w - img.width) // 2
        oy = y + (cell_h - img.height) // 2
        sheet.paste(img, (ox, oy))
        draw.text((x + 16, y + cell_h + 8), label, fill=(200, 200, 200), font=label_font)

    out = ASSETS / "mkfs_puck_storyboard_6up.png"
    sheet.save(out, optimize=True)
    print(f"Wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
