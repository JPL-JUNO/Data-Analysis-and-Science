"""
@Description: Manifold Learning: 'HELLO'
@Author: Stephen CUI
@Time: 2023-04-17 17:00:02
"""

import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np


def make_hello(N=1000, rseed=42):
    fig, ax = plt.subplots(figsize=(4, 1))
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.axis('off')
    ax.text(.5, .4, 'HELLO', va='center', ha='center', weight='bold', size=85)
    fig.savefig('hello.png')
    plt.close(fig)

    from matplotlib.image import imread
    data = imread('hello.png')[::-1, :, 0].T
    rng = np.random.RandomState(rseed)
    X = rng.rand(4 * N, 2)
    i, j = (X * data.shape).astype(int).T
    mask = (data[i, j] < 1)
    X = X[mask]
    X[:, 0] *= (data.shape[0] / data.shape[1])
    X = X[:N]
    return X[np.argsort(X[:, 0])]


X = make_hello()
colorsize = dict(c=X[:, 0], cmap='rainbow')
plt.scatter(X[:, 0], X[:, 1], **colorsize)
plt.axis('equal')


def rotate(X, angle):
    theta = np.deg2rad(angle)

    R = [[np.cos(theta), np.sin(theta)],
         [-np.sin(theta), np.cos(theta)]]
    return np.dot(X, R)


X2 = rotate(X, 20) + 5
fig = plt.figure()
plt.scatter(X2[:, 0], X2[:, 1], **colorsize)
plt.axis('equal')


from sklearn.metrics import pairwise_distances
D = pairwise_distances(X)
assert D.shape == (1000, 1000)


plt.imshow(D, zorder=2, cmap='viridis', interpolation='nearest')
plt.colorbar()

D2 = pairwise_distances(X2)
assert np.allclose(D, D2)

from sklearn.manifold import MDS
model = MDS(n_components=2,
            normalized_stress='auto', dissimilarity='precomputed',
            random_state=1701)
out = model.fit_transform(D)
fig = plt.figure()
plt.scatter(out[:, 0], out[:, 1], **colorsize)
plt.axis('equal')


def random_project(X, dimension=3, rseed=42):
    assert dimension >= X.shape[1]

    rng = np.random.RandomState(rseed)
    C = rng.randn(dimension, dimension)
    e, V = np.linalg.eigh(np.dot(C, C.T))
    return np.dot(X, V[:X.shape[1]])


X3 = random_project(X, 3)
from mpl_toolkits import mplot3d
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(X3[:, 0], X3[:, 1], X3[:, 2],
             **colorsize)
model = MDS(n_components=2,
            normalized_stress='auto',
            random_state=1701)
out3 = model.fit_transform(X3)
fig = plt.figure()
plt.scatter(out3[:, 0], out3[:, 1], **colorsize)
plt.axis('equal')


def make_hello_s_curve(X):
    t = (X[:, 0] - 2) * .75 * np.pi
    x = np.sin(t)
    y = X[:, 1]
    z = np.sign(t) * (np.cos(t) - 1)
    return np.vstack((x, y, z)).T


XS = make_hello_s_curve(X)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(XS[:, 0], XS[:, 1], XS[:, 2],
           **colorsize)

model = MDS(n_components=2,
            normalized_stress='auto',
            n_jobs=-1,
            random_state=2)
outS = model.fit_transform(XS)
plt.scatter(outS[:, 0], outS[:, 1], **colorsize)
plt.axis('equal')


from sklearn.manifold import LocallyLinearEmbedding
model = LocallyLinearEmbedding(
    n_neighbors=100, n_components=2, method='modified', eigen_solver='dense'
)
out = model.fit_transform(XS)
fig, ax = plt.subplots()
ax.scatter(out[:, 0], out[:, 1], **colorsize)
ax.set_ylim(.15, -.15)


from sklearn.datasets import fetch_lfw_people
faces = fetch_lfw_people(min_faces_per_person=30)
assert faces.data.shape == (2370, 2914)

fig, ax = plt.subplots(4, 8, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(faces.images[i], cmap='gray')

from sklearn.decomposition import PCA
model = PCA(100, svd_solver='randomized').fit(faces.data)
fig = plt.figure()
plt.plot(np.cumsum(model.explained_variance_ratio_))
plt.xlabel('n components')
plt.ylabel('cumulative variance')


from sklearn.manifold import Isomap
model = Isomap(n_components=2)
proj = model.fit_transform(faces.data)
assert proj.shape == (2370, 2)

from matplotlib import offsetbox


def plot_components(data, model, images=None,
                    ax=None, thumb_frac=.05, cmap='gray'):
    ax = ax or plt.gca()
    proj = model.fit_transform(data)
    ax.plot(proj[:, 0], proj[:, 1], '.k')

    if images is not None:
        min_dist_2 = (
            thumb_frac * max(proj.max(axis=0) - proj.min(axis=0))) ** 2
        shown_images = np.array([2 * proj.max(axis=0)])
        for i in range(data.shape[0]):
            dist = np.sum((proj[i] - shown_images) ** 2, axis=1)
            if np.min(dist) < min_dist_2:
                continue
            shown_images = np.vstack([shown_images, proj[i]])
            imagebox = offsetbox.AnnotationBbox(
                offsetbox.OffsetImage(images[i], cmap=cmap),
                proj[i]
            )
            ax.add_artist(imagebox)


fig, ax = plt.subplots(figsize=(10, 10))
plot_components(faces.data, model=Isomap(n_components=2),
                images=faces.images[:, ::2, ::2])
