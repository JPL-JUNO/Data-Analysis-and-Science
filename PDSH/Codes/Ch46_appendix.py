"""
@Description:
@Author(s): Stephen CUI
@Time: 2023-04-18 10:24:55
"""

from mpl_toolkits.mplot3d.art3d import Line3DCollection
from sklearn.neighbors import NearestNeighbors
import numpy as np
import matplotlib.pyplot as plt
from Ch46_manifold_learning import make_hello, make_hello_s_curve

X = make_hello()
colorsize = dict(c=X[:, 0], cmap='rainbow')
XS = make_hello_s_curve(X)
rng = np.random.RandomState(42)
ind = rng.permutation(len(X))
lines_MDS = [(XS[i], XS[j]) for i in ind[:100] for j in ind[100:200]]
nbrs = NearestNeighbors(n_neighbors=100).fit(XS).kneighbors(XS[ind[:100]])[1]
lines_LLE = [(XS[ind[i]], XS[j]) for i in range(100) for j in nbrs[i]]
titles = ['MSD Linkages', 'LLE Linkages (100-NN)']
fig, ax = plt.subplots(1, 2, figsize=(16, 6),
                       subplot_kw=dict(projection='3d'))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0, wspace=0)
for axi, title, lines in zip(ax, titles, [lines_MDS, lines_LLE]):
    axi.scatter3D(XS[:, 0], XS[:, 1], XS[:, 2], **colorsize)
    axi.add_collection(Line3DCollection(lines, lw=1, color='black',
                                        alpha=.05))
    axi.view_init(elev=10, azim=-80)
    axi.set_title(title, size=18)

plt.savefig('../Figures/fig46-7.png', dpi=300)
