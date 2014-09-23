"""Make custom cubehelix colormaps."""

import matplotlib as mpl

mpl.cm.register_cmap(
    name='redcube', data=mpl.cm.revcmap(mpl._cm.cubehelix(s=0, r=0.5, h=1))
)
mpl.cm.register_cmap(
    name='bluecube', data=mpl.cm.revcmap(mpl._cm.cubehelix(s=0.3, r=-0.5, h=1))
)
