"""
@Description: What Is Machine Learning?
@Author: Stephen CUI
@Time: 2023-04-10 09:23:35
"""

import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')
from matplotlib.pyplot import Axes


def format_plot(ax: Axes, title: str) -> None:
    # ax.xaxis.set_major_formatter(plt.NullFormatter())
    # ax.yaxis.set_major_formatter(plt.NullFormatter())
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    plt.grid()
    ax.set_xlabel('feature 1', color='gray')
    ax.set_ylabel('feature 2', color='gray')
    ax.set_title(title, color='gray')


def save_plot(name, extension='png', dpi=300):
    plt.savefig('../Figures/Ch37-' + name + '.' + extension,
                dpi=dpi)


from sklearn.datasets import make_blobs
from sklearn.svm import SVC

X, y = make_blobs(n_samples=50, centers=2,
                  random_state=0, cluster_std=.6)
clf = SVC(kernel='linear')
clf.fit(X, y)

X2, _ = make_blobs(n_samples=80, centers=2,
                   random_state=0, cluster_std=.8)

X2 = X2[50:]
y2 = clf.predict(X2)


fig, ax = plt.subplots(figsize=(8, 6))
point_style = dict(cmap='Paired', s=50)
ax.scatter(X[:, 0], X[:, 1], c=y, **point_style)
format_plot(ax, 'Input Data')
ax.axis([-1, 4, -2, 7])
# fig.savefig('../Figures/Ch37-classification-1.png')
# save_plot('classification-1')

xx = np.linspace(-1, 4, 10)
yy = np.linspace(-2, 7, 10)
xy1, xy2 = np.meshgrid(xx, yy)
Z = np.array([clf.decision_function([t])
             for t in zip(xy1.flat, xy2.flat)]).reshape(xy1.shape)
fig, ax = plt.subplots(figsize=(8, 6))
line_style = dict(levels=[-1.0, 0.0, 1.0],
                  linestyles=['dashed', 'solid', 'dashed'],
                  colors='gray', linewidths=1)
ax.scatter(X[:, 0], X[:, 1], c=y, **point_style)
ax.contour(xy1, xy2, Z, ** line_style)
format_plot(ax, 'Model Learned from Input Data')
ax.axis([-1, 4, -2, 7])


fig, ax = plt.subplots(1, 2, figsize=(16, 6))
fig.subplots_adjust(left=.0625, right=.95, wspace=.1)

ax[0].scatter(X2[:, 0], X2[:, 1], c='gray', s=50)
ax[0].axis([-1, 4, -2, 7])

ax[1].scatter(X2[:, 0], X2[:, 1], c=y2, **point_style)
ax[1].contour(xy1, xy2, Z, **line_style)
ax[1].axis([-1, 4, -2, 7])
format_plot(ax[0], 'Unknown Data')
format_plot(ax[1], 'Predicted Data')

from sklearn.linear_model import LinearRegression

rng = np.random.RandomState(seed=42)
X = rng.randn(200, 2)
y = np.dot(X, [-2, 1]) + .1 * rng.randn(X.shape[0])


model = LinearRegression()
model.fit(X, y)

X2 = rng.randn(100, 2)
y2 = model.predict(X2)

fig, ax = plt.subplots()
points = ax.scatter(X[:, 0], X[:, 1], c=y, s=50,
                    cmap='viridis')
format_plot(ax, 'Input Data')
ax.axis([-4, 4, -3, 3])


from mpl_toolkits.mplot3d.art3d import Line3DCollection

points = np.hstack([X, y[:, np.newaxis]]).reshape(-1, 1, 3)
segments = np.hstack([points, points])
segments[:, 0, 2] = -8

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], y, c=y, s=35,
           cmap='viridis')
ax.add_collection3d(Line3DCollection(segments, color='gray', alpha=.2))
ax.scatter(X[:, 0], X[:, 1], -8 + np.zeros(X.shape[0]),
           c=y, s=10, cmap='viridis')

ax.patch.set_facecolor('white')
ax.view_init(elev=20, azim=-70)
ax.set_zlim3d(-8, 8)
ax.xaxis.set_major_locator(plt.NullLocator())
ax.yaxis.set_major_locator(plt.NullLocator())
ax.zaxis.set_major_locator(plt.NullLocator())
ax.set(xlabel='feature 1', ylabel='feature 2', zlabel='label')


fig, ax = plt.subplots()
pts = ax.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='viridis', zorder=2)

xx, yy = np.meshgrid(np.linspace(-4, 4),
                     np.linspace(-3, 3))
Xfit = np.vstack([xx.ravel(), yy.ravel()]).T
yfit = model.predict(Xfit)

zz = yfit.reshape(xx.shape)
ax.pcolorfast([-4, 4], [-3, 3], zz, alpha=.5,
              cmap='viridis', norm=pts.norm, zorder=1)
ax.axis([-4, 4, -3, 3])
format_plot(ax, 'Input Data with Linear Fit')


fig, ax = plt.subplots(1, 2, figsize=(16, 6))
fig.subplots_adjust(left=.0625, right=.95, wspace=.1)

ax[0].scatter(X2[:, 0], X2[:, 1], c='gray', s=50)
ax[0].axis([-4, 4, -3, 3])

ax[1].scatter(X2[:, 0], X2[:, 1], c=y2, s=50,
              cmap='viridis', norm=pts.norm)
ax[1].axis([-4, 4, -3, 3])
format_plot(ax[0], 'Unknown Data')
format_plot(ax[1], 'Predicted Labels')


from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

X, y = make_blobs(n_samples=100, centers=4,
                  random_state=42, cluster_std=1.5)

model = KMeans(4, random_state=0, n_init='auto')
y = model.fit_predict(X)

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(X[:, 0], X[:, 1], s=50, color='gray')
format_plot(ax, 'Input Data')

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(X[:, 0], X[:, 1], s=50, c=y, cmap='viridis')
format_plot(ax, 'Learned Cluster Labels')


from sklearn.datasets import make_swiss_roll

X, y = make_swiss_roll(200, noise=.5, random_state=42)
X = X[:, [0, 2]]

fig, ax = plt.subplots()
ax.scatter(X[:, 0], X[:, 1], color='gray', s=30)

format_plot(ax, 'Input Data')


from sklearn.manifold import Isomap
model = Isomap(n_neighbors=8, n_components=1)
y_fit = model.fit_transform(X).ravel()

fig, ax = plt.subplots()
pts = ax.scatter(X[:, 0], X[:, 1], c=y_fit, cmap='viridis', s=30)
cb = plt.colorbar(pts, ax=ax)

format_plot(ax, 'Learned Latent Parameters')
cb.set_ticks([])
cb.set_label('Latent Variable', color='gray')
