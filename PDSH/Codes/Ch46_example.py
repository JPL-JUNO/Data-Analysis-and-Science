"""
@Description: Example: Visualizing Structure in Digits
@Author(s): Stephen CUI
@Time: 2023-04-18 11:14:19
"""

from sklearn.datasets import fetch_openml
from sklearn.manifold import Isomap
import numpy as np
import matplotlib.pyplot as plt
from Ch46_manifold_learning import plot_components
plt.style.use('ggplot')
mnist = fetch_openml('mnist_784', parser='auto')
assert mnist.data.shape == (70_000, 784)

mnist_data = np.asarray(mnist.data)
mnist_target = np.asarray(mnist.target, dtype=int)
fig, ax = plt.subplots(6, 8, subplot_kw=dict(xticks=[], yticks=[]))
for i, axi in enumerate(ax.flat):
    axi.imshow(mnist_data[1250 * i].reshape(28, 28), cmap='gray_r')

data = mnist_data[::30]
target = mnist_target[::30]
model = Isomap(n_components=2)
proj = model.fit_transform(data)
fig = plt.figure()
plt.scatter(proj[:, 0], proj[:, 1], c=target,
            cmap='jet')
plt.colorbar(ticks=range(10))
plt.clim(-.5, 9.5)


data = mnist_data[mnist_target == 1][::4]
fig = plt.figure()
fig, ax = plt.subplots(figsize=(10, 10))
model = Isomap(n_neighbors=5, n_components=2, eigen_solver='dense')
plot_components(data, model, images=data.reshape((-1, 28, 28)),
                ax=ax, thumb_frac=.05, cmap='gray_r')
