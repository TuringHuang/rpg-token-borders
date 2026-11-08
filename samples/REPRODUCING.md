# Reproducing the sample images

Copyright (C) The Battle for Wesnoth Project. Sample artwork and derivatives: GPL v2 or later; see [COPYING](COPYING).

Use [compose_samples.py](compose_samples.py) with the upstream portrait directory at the commit recorded in [sources.json](sources.json):

```sh
python -m pip install Pillow==12.3.0
python compose_samples.py /path/to/wesnoth/data/core/images/portraits out/
```

Byte-identical output was verified on Linux x86_64 (glibc) with Python 3.13 and the Pillow 12.3.0 wheel. On other platforms the faint noise layer (Pillow effect_noise uses the C library rand()) and WebP encoding can differ slightly; the composition is otherwise the same.

The script generates `bryn.webp`, `wren.webp`, `oren.webp`, `vex.webp` and `maera.webp`. For the verified environment, compare output SHA-256 values with `modifiedSha256` in [sources.json](sources.json).

`hero-poster.webp` is composed from `bryn.webp` and the public-domain Iron Bulwark frame ([frames/](frames/)).
