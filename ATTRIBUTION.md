# Attribution

This repository is a fork/derivative of:

- Upstream project: https://github.com/jerpint/rubiks_cube_convnet
- Upstream description: "How to train a convnet to solve a rubiks cube"
- Upstream default branch at import time: `master`
- Upstream project-level license: none declared on GitHub at the time this fork was prepared.

The project also bundles MagicCube for cube simulation and visualization:

- MagicCube: https://github.com/davidwhogg/MagicCube
- Bundled license: GNU GPL v2, preserved in `MagicCube/LICENSE.txt`

Local changes in this fork:

- `train_cube.py` was modified as a local experiment around 2023-12-06 to inspect generated cube states and one-hot move labels.
- `test.py` was added as a small Keras `to_categorical` one-hot encoding check.
- `README.md` was annotated to make the upstream source and local modification status explicit.

This fork is kept public primarily as a record of a learning experiment based on the upstream ConvNet Rubik's cube solver.
