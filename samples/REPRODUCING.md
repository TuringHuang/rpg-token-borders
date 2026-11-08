# Reproducing the sample images

Copyright (C) The Battle for Wesnoth Project. Sample artwork and derivatives: GPL v2 or later; see [COPYING](COPYING).

Use [compose_samples.py](compose_samples.py) with the upstream portrait directory at the commit recorded in [sources.json](sources.json):

```sh
python -m pip install Pillow==12.3.0
python compose_samples.py /path/to/wesnoth/data/core/images/portraits out/
```

Byte-for-byte verification used Pillow 12.3.0 with glibc-compatible noise. Native Windows noise can differ.

The script generates `bryn.webp`, `wren.webp`, `oren.webp`, `vex.webp` and `maera.webp`. Compare output SHA-256 values with `modifiedSha256` in [sources.json](sources.json).

`hero-poster.webp` is composed from `bryn.webp` and the public-domain Iron Bulwark frame ([frames/](frames/)).
