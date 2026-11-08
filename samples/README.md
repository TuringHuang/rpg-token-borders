# RPG Token Maker sample artwork

Copyright (C) The Battle for Wesnoth Project

The five portraits originate from [Battle for Wesnoth](https://www.wesnoth.org/). Each supplied original retains its upstream artist and **GNU GPL v2+** EXIF notice. The modified portraits and `hero-poster.webp` in this directory are likewise released under the **GNU General Public License version 2 or, at your option, any later version (GPL-2.0-or-later)**. You may copy, redistribute and modify them under those terms. They are provided without warranty. Read the complete [GPL v2 license](COPYING).

## Original sources

All five original files are pinned to upstream commit [033012219e737f8c1bca288e16700a8795e67117](https://github.com/wesnoth/wesnoth/commit/033012219e737f8c1bca288e16700a8795e67117), which records the artist and license metadata. Their bytes were also checked against upstream master commit `acac4b91af592765a712919c6c87dad3ade57e28` on 2026-11-08 and are identical. The names Bryn, Wren, Oren, Vex and Maera are labels chosen for RPG Token Maker, not upstream character names.

| Sample | Upstream path at the pinned commit | Original artist |
|---|---|---|
| bryn | [data/core/images/portraits/dwarves/fighter.webp](https://github.com/wesnoth/wesnoth/blob/033012219e737f8c1bca288e16700a8795e67117/data/core/images/portraits/dwarves/fighter.webp) | Phil Barber (thespaceinvader) |
| wren | [data/core/images/portraits/elves/ranger+female.webp](https://github.com/wesnoth/wesnoth/blob/033012219e737f8c1bca288e16700a8795e67117/data/core/images/portraits/elves/ranger+female.webp) | Kathrin Polikeit (Kitty) |
| oren | [data/core/images/portraits/humans/mage-silver.webp](https://github.com/wesnoth/wesnoth/blob/033012219e737f8c1bca288e16700a8795e67117/data/core/images/portraits/humans/mage-silver.webp) | Kathrin Polikeit (Kitty) |
| vex | [data/core/images/portraits/humans/assassin+female.webp](https://github.com/wesnoth/wesnoth/blob/033012219e737f8c1bca288e16700a8795e67117/data/core/images/portraits/humans/assassin+female.webp) | Kathrin Polikeit (Kitty) |
| maera | [data/core/images/portraits/humans/mage-white+female.webp](https://github.com/wesnoth/wesnoth/blob/033012219e737f8c1bca288e16700a8795e67117/data/core/images/portraits/humans/mage-white+female.webp) | Kathrin Polikeit (Kitty) |

Unchanged originals are included under [originals/](originals/). [sources.json](sources.json) includes a source link and commit link for each file, individual authors, modification notices and SHA-256 checksums. The per-image metadata, rather than a blanket assumption about all Wesnoth art, establishes these five files' GPL v2+ status. See also [Wesnoth's licensing policy](https://wiki.wesnoth.org/Wesnoth%3ACopyrights).

## Our modifications and distributed files

- `bryn.webp`, `wren.webp`, `oren.webp`, `vex.webp`, `maera.webp`: added colored backgrounds, enlarged and cropped the original portraits to 640 × 640, encoded as WebP. Imported from the sample-first prototype on 2026-11-07.
- `hero-poster.webp`: a Hero canvas snapshot composed from `bryn.webp` and the public-domain Iron Bulwark frame in [frames/](frames/).
- Documentation and source packaging added on 2026-11-08. All six distributed image files remain byte-for-byte identical to RPG Token Maker's existing sample files; this licensing update does not change the composition.

**These modified images are also GPL v2+.** The root repository's MIT license for its original SVG borders does not replace the license of the Wesnoth originals or these derivatives. TheGreatNacho's separate frame permissions remain intact: the artist allows use in paid or free projects and requests public-domain release of a packaged collection. We preserve the exact statement in [frames/LICENSE.md](frames/LICENSE.md), rather than describing it as an MIT or CC0 grant. The frames/masks are supplied openly without additional restrictions; the resulting Wesnoth-containing composites remain GPL v2+.

## Reuse and reproduction

[compose_samples.py](compose_samples.py) composes the five portraits from the original artwork by adding backgrounds and cropping. Byte-identical output was verified on Linux x86_64 (glibc) with Python 3.13 and the Pillow 12.3.0 wheel. On other platforms the faint noise layer (Pillow effect_noise uses the C library rand()) and WebP encoding can differ slightly; the composition is otherwise the same. See [REPRODUCING.md](REPRODUCING.md) for usage and [sources.json](sources.json) for pinned originals and checksums. Keep these license and modification notices with redistributed copies.

The script does not generate `hero-poster.webp`; it remains the supplied Hero canvas snapshot.
