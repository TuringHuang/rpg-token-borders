#!/usr/bin/env python3
"""Compose the RPG Token Maker sample portraits from Battle for Wesnoth art.

This is the script that produced bryn.webp, wren.webp, oren.webp, vex.webp
and maera.webp. Parameters below are the exact values used.

What it does to each original portrait:
  1. Finds the head near the top of the transparent portrait and crops a
     square head-and-shoulders frame around it (zoom / dx / dy per image).
  2. Paints a new background: a vertical colour gradient, a few blurred
     coloured light blobs, and a faint noise texture.
  3. Adds a soft drop shadow behind the figure and composites the figure
     on top, then saves a 640 x 640 WebP (quality 84).

hero-poster.webp is not made here: it is a snapshot of the live Hero canvas
(bryn.webp inside the public-domain TheGreatNacho "Iron Bulwark" frame).

Reproducibility: verified to recreate all five published WebP files
byte-for-byte with Pillow 12.3.0. Other Pillow versions may differ
slightly in the faint noise layer or WebP encoding.

Requirements: Python 3, Pillow.
Usage:
  git clone --depth 1 --filter=blob:none --sparse https://github.com/wesnoth/wesnoth
  cd wesnoth && git sparse-checkout set data/core/images/portraits && cd ..
  python3 compose_samples.py wesnoth/data/core/images/portraits out/

Original art: Copyright (C) The Battle for Wesnoth Project, GPL v2 or later.
Modifications (backgrounds, cropping) and this script: GPL v2 or later.
"""
import os
import random
import sys

from PIL import Image, ImageDraw, ImageFilter

SIZE = 640

# name, source portrait, gradient top, gradient bottom,
# light blobs [(cx, cy, radius, rgb, alpha)], zoom, dx, dy
SAMPLES = [
    ("wren", "elves/ranger+female", (28, 44, 46), (150, 96, 52),
     [(.8, .75, .35, (240, 170, 80), 150), (.2, .2, .3, (60, 110, 90), 120)], 1.15, -0.2, 0.02),
    ("bryn", "dwarves/fighter", (52, 50, 56), (24, 22, 26),
     [(.25, .2, .35, (220, 140, 60), 110), (.8, .8, .3, (90, 90, 110), 90)], 1.15, 0, 0),
    ("oren", "humans/mage-silver", (26, 22, 46), (10, 8, 20),
     [(.7, .25, .32, (140, 110, 230), 120), (.2, .8, .3, (60, 40, 120), 110)], 1.2, -0.11, 0),
    ("vex", "humans/assassin+female", (46, 32, 22), (14, 10, 8),
     [(.8, .2, .3, (240, 180, 90), 110), (.2, .7, .35, (90, 30, 30), 90)], 1.2, 0, 0),
    ("maera", "humans/mage-white+female", (210, 190, 150), (90, 70, 40),
     [(.5, .1, .4, (255, 245, 210), 160), (.2, .8, .3, (150, 110, 60), 80)], 1.25, 0.32, 0.02),
]


def background(size, top, bottom, blobs):
    im = Image.new("RGB", (size, size))
    d = ImageDraw.Draw(im)
    for y in range(size):
        t = y / size
        d.line([(0, y), (size, y)], fill=tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3)))
    lay = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    dl = ImageDraw.Draw(lay)
    for cx, cy, r, col, a in blobs:
        dl.ellipse([cx * size - r * size, cy * size - r * size, cx * size + r * size, cy * size + r * size], fill=col + (a,))
    lay = lay.filter(ImageFilter.GaussianBlur(size * 0.08))
    im = Image.alpha_composite(im.convert("RGBA"), lay)
    noise = Image.effect_noise((size, size), 40).convert("L").filter(ImageFilter.GaussianBlur(1.2))
    return Image.blend(im, Image.merge("RGBA", (noise, noise, noise, Image.new("L", (size, size), 255))), 0.05)


def head_box(im):
    """Return the head's horizontal centre, the top of the figure and its height."""
    a = im.split()[3]
    x0, y0, x1, y1 = a.getbbox()
    h = y1 - y0
    band = a.crop((x0, y0, x1, y0 + int(h * 0.18))).getbbox()
    return x0 + (band[0] + band[2]) / 2, y0, h


def compose(src_path, out_path, top, bottom, blobs, zoom, dx, dy):
    p = Image.open(src_path).convert("RGBA")
    cx, y0, h = head_box(p)
    crop = int(h * 0.78 / zoom)
    hx, hy = cx + dx * crop, y0 + crop * 0.42 + dy * crop
    box = (int(hx - crop / 2), int(hy - crop * 0.42), int(hx + crop / 2), int(hy + crop * 0.58))
    fig = Image.new("RGBA", (crop, crop), (0, 0, 0, 0))
    fig.paste(p.crop(box), (0, 0))
    fig = fig.resize((SIZE, SIZE), Image.LANCZOS)
    out = background(SIZE, top, bottom, blobs)
    shadow = fig.split()[3].filter(ImageFilter.GaussianBlur(14)).point(lambda v: int(v * .45))
    out.paste((0, 0, 0, 255), (10, 14), shadow)
    out = Image.alpha_composite(out, fig)
    out.convert("RGB").save(out_path, "WEBP", quality=84)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    portraits, out_dir = sys.argv[1], sys.argv[2]
    os.makedirs(out_dir, exist_ok=True)
    for name, src, top, bottom, blobs, zoom, dx, dy in SAMPLES:
        random.seed(name)
        compose(os.path.join(portraits, src + ".webp"), os.path.join(out_dir, name + ".webp"), top, bottom, blobs, zoom, dx, dy)
        print("wrote", name)


if __name__ == "__main__":
    main()
