"""
@Description: Choosing the Covariance Type
@Author(s): Stephen CUI
@Time: 2023-04-19 17:07:27
"""

from sklearn.mixture import GaussianMixture
from Ch48_GMM import draw_ellipse
import matplotlib.pyplot as plt
import numpy as np


fig, axes = plt.subplots(1, 3, figsize=(14, 4), sharex=True, sharey=True)
fig.subplots_adjust(wspace=.05)

rng = np.random.RandomState(5)
X = np.dot(rng.randn(500, 2), rng.randn(2, 2))

for i, cov_type in enumerate(['diag', 'spherical', 'full']):
    model = GaussianMixture(1, covariance_type=cov_type).fit(X)
    axes[i].scatter(X[:, 0], X[:, 1], alpha=.5)
    axes[i].set_title('covariance_type={}'.format(
        cov_type), size=14, family='monospace')
    draw_ellipse(model.means_[0], model.covariances_[0], axes[i], alpha=.2)
    axes[i].xaxis.set_major_locator(plt.NullLocator())
    axes[i].yaxis.set_major_locator(plt.NullLocator())
plt.savefig('../Figures/fig48-8.png', dpi=300)
