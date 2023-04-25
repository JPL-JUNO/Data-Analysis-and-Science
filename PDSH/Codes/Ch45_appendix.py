"""
@Description: 
@Author: Stephen CUI
@Time: 2023-04-17 11:17:44
"""

from Ch45_introduction_to_PCA import draw_vector
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.RandomState(seed=42)
X = (rng.rand(2, 2) @ rng.randn(2, 200)).T
pca = PCA(n_components=2, whiten=True)
pca.fit(X)
fig, ax = plt.subplots(1, 2, figsize=(16, 6))
fig.subplots_adjust(left=.0625, right=.95, wspace=.1)
ax[0].scatter(X[:, 0], X[:, 1], alpha=.5)
for length, vector in zip(pca.explained_variance_, pca.components_):
    v = vector * 2 * np.sqrt(length)
    draw_vector(pca.mean_, pca.mean_ + v, ax=ax[0])

ax[0].axis('equal')
ax[0].set(xlabel='x', ylabel='y', title='input')

X_pca = pca.transform(X)
ax[1].scatter(X_pca[:, 0], X_pca[:, 1], alpha=.2)
draw_vector([0, 0], [0, 3], ax=ax[1])
draw_vector([0, 0], [3, 0], ax=ax[1])
ax[1].axis('equal')
ax[1].set(xlabel='component 1',
          ylabel='component 2',
          xlim=(-5, 5), ylim=(-3, 3.1))
