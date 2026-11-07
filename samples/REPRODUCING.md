# Reproducing the sample images

Copyright (C) The Battle for Wesnoth Project. Sample artwork and derivatives: GPL v2 or later; see [COPYING](COPYING).

## What can be reproduced exactly

The six WebP files at this directory's root are the actual distributed files, not re-encoded previews. Copy them for byte-identical reuse and verify against [sources.json](sources.json). The transparent originals and their metadata are included under `originals/`.

No original prototype composition script, exact crop rectangle list or separate background layers were retained. The following is a reconstruction recipe for **the same operations and visual framing**, not a claim that an independently redrawn background will reproduce the original compressed bytes. Preserve your new background layer and crop parameters when making further edits.

## Transparent original → background → portrait crop

Use an editor with layers and alpha support, such as GIMP. Work in sRGB.

1. Create a 640 × 640 image with a background layer. Open the corresponding `originals/<name>.webp` as a separate layer above it; do not flatten its transparent alpha first.
2. Paint a soft background using the palette and light placement below. Use a broad linear gradient for the dark base, then a large radial gradient on a separate layer for the colored light; blur the light so that no hard edges compete with the portrait. These backgrounds are additions made for RPG Token Maker, not part of the original Wesnoth artwork.
3. Scale the portrait uniformly (keep the aspect ratio). Translate it to match the landmarks below, using the supplied `<name>.webp` as a reference layer at reduced opacity. Adjust the portrait layer, not the 640 × 640 canvas. Keep the character unrotated. Crop to the canvas once positioned.
4. Hide the reference layer, retain your editable layers, and export a 640 × 640 WebP. Choose your own WebP quality if recreating it; the original portrait encoder settings were not retained. The included distributed WebP remains the exact reference.

| Sample | Background reconstruction | Portrait crop landmarks in the supplied 640px square |
|---|---|---|
| Bryn | Cool dark blue/gray base; muted warm brown light | Face and helmet in the upper half, white beard and shoulder armor below; exclude most of the axe and lower body |
| Wren | Dark teal/charcoal upper-left fading to warm ochre light on the right | Hood touches the top edge, face in the upper-center/right, chest fills the lower half, bow clips the right edge |
| Oren | Very dark blue/purple base; violet light in the upper-right | Head in the left-center, tall staff/fire in the right half; crop out the lower body |
| Vex | Dark brown/black base; muted ochre light at upper-right | Hood close to the top, eyes in the upper half, dagger crossing the lower half; hands clip the lower/right edges |
| Maera | Muted olive/tan base; pale warm light behind the head | Hair touches the top edge, face in the upper-center, pale robe fills the lower half; staff clips the left edge |

The portrait crop and the live Token Maker crop are separate stages. Do not bake the live framing values below into these 640px portrait files.

## Current live token framing

These values apply to a 512px token rendering surface, with `x`/`y` offsets in pixels. They are unchanged from the accepted sample composition.

| Sample | Frame | x | y | scale | Bottom caption |
|---|---|---:|---:|---:|---|
| Bryn | 17, Iron Bulwark | -34 | 72 | 1.85 | off |
| Wren | 12, Azure Rope | 4 | 92 | 1.65 | Wren |
| Oren | 12, Azure Rope | 130 | 54 | 2.15 | Oren |
| Vex | 12, Azure Rope | -36 | 130 | 1.75 | Vex |
| Maera | 12, Azure Rope | -42 | 116 | 1.65 | Maera |

## Hero poster from the supplied Bryn portrait

The included frame and alpha opening mask are sufficient to reproduce the poster composition without the application code. On a transparent 512 × 512 Canvas 2D surface, use image smoothing and these steps:

1. Load `bryn.webp`, `frames/mask-17.png` and `frames/theGreatNacho-17.webp`.
2. The frame's normalized opening bounds are `{width:0.7021484375,height:0.7041015625,x:-0.00244140625,y:0.00146484375}`. Thus `clipW=512*width`, `clipH=512*height`, `cx=256+512*x`, `cy=256+512*y`.
3. Compute `s=max(clipW/640,clipH/640)*1.85`, `w=h=640*s`. Draw Bryn at `(cx-w/2-34, cy-h/2+72, w, h)`.
4. Set `globalCompositeOperation='destination-in'` and draw the mask across `(0,0,512,512)`. This removes the portrait outside the opening.
5. Restore `globalCompositeOperation='source-over'` and draw the unchanged frame across `(0,0,512,512)`. Do not add a caption, tint, or stage/checkerboard background.
6. Export the transparent PNG, then encode WebP at quality 86. The existing poster used Sharp/libwebp. Different browser rasterizers or encoder versions can differ by pixels/bytes; use the supplied file when exact identity is needed.

For frame 12, use its corresponding mask and normalized bounds `{width:0.8408203125,height:0.83984375,x:-0.00048828125,y:-0.0009765625}` with the table's transform. The frame originals were retrieved from [Tokenizer commit 58cc7dad7d8b60411e8003b527ae6f6b06a67889](https://github.com/MrPrimate/tokenizer/tree/58cc7dad7d8b60411e8003b527ae6f6b06a67889/img/thegreatnacho). Their permission statement is retained in [frames/LICENSE.md](frames/LICENSE.md). Frame masks were derived by detecting the enclosed transparent opening; their supplied PNGs fix the exact contours.
