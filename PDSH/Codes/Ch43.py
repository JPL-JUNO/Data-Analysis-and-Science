"""
@Description: In Depth: Support Vector Machines
@Author: Stephen CUI
@Time: 2023-04-12 16:52:19
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
plt.style.use('ggplot')


from sklearn.datasets import make_blobs
X, y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=.6)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')

xfit = np.linspace(-1, 3.5)
plt.plot([.6], [2.1], 'x', color='red', markeredgewidth=2, markersize=10)
for m, b, in [(1, .65), (.5, 1.6), (-.2, 2.9)]:
    plt.plot(xfit, m * xfit + b, '-k')
plt.xlim(-1, 3.5)

fig = plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
for m, b, d in [(1, .65, .33), (.5, 1.6, .55), (-.2, 2.9, .2)]:
    yfit = m * xfit + b
    plt.plot(xfit, yfit, '-k')
    plt.fill_between(xfit, yfit - d, yfit + d,
                     edgecolor='none', color='lightgray', alpha=.5)
plt.xlim(-1, 3.5)

from sklearn.svm import SVC
from matplotlib.pyplot import Axes
model = SVC(kernel='linear', C=1e10)
model.fit(X, y)


def plot_svc_decision_function(model: SVC, ax: Axes = None, plot_support: bool = True):
    if ax is None:
        ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    x = np.linspace(xlim[0], xlim[1], 30)
    y = np.linspace(ylim[0], ylim[1], 30)
    Y, X = np.meshgrid(y, x)
    xy = np.vstack([X.ravel(), Y.ravel()]).T
    P = model.decision_function(xy).reshape(X.shape)
    ax.contour(X, Y, P, colors='k',
               levels=[-1, 0, 1], alpha=.5,
               linestyles=['--', '-', '--'])
    if plot_support:
        ax.scatter(model.support_vectors_[:, 0],
                   model.support_vectors_[:, 1],
                   s=300, linewidth=1, edgecolors='black', facecolors='none')
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)


fig = plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn')
plot_svc_decision_function(model)

# model.support_vectors_


def plot_svm(N=10, ax=None):
    X, y = make_blobs(n_samples=200, centers=2,
                      random_state=0, cluster_std=.6)
    X = X[:N]
    Y = y[:N]
    model = SVC(kernel='linear', C=1e10)
    model.fit(X, Y)
    ax = ax or plt.gca()
    ax.scatter(X[:, 0], X[:, 1], c=Y, s=50, cmap='autumn')
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 6)
    plot_svc_decision_function(model, ax)


fig, ax = plt.subplots(1, 2, figsize=(16, 6))
fig.subplots_adjust(left=.0625, right=.95, wspace=.1)
for axi, N in zip(ax, [60, 120]):
    plot_svm(N, axi)
    axi.set_title('N={}'.format(N))
