"""
@Description: Example: Eigenfaces
@Author: Stephen CUI
@Time: 2023-04-17 15:53:35
"""

from sklearn.datasets import fetch_lfw_people
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

faces = fetch_lfw_people(min_faces_per_person=60)
print(faces.target_names)
print(faces.images.shape)

pca = PCA(150, svd_solver='randomized', random_state=42)
pca.fit(faces.data)
# eigenfaces
fig, axes = plt.subplots(3, 8, figsize=(9, 4),
                         subplot_kw={'xticks': [], 'yticks': []},
                         gridspec_kw=dict(hspace=.1, wspace=.1))
for i, ax in enumerate(axes.flat):
    ax.imshow(pca.components_[i].reshape(62, 47), cmap='bone')

fig = plt.figure()
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('number of components')
plt.ylabel('cumulative explained variance')


pca = pca.fit(faces.data)
components = pca.transform(faces.data)
projected = pca.inverse_transform(components)

fig, ax = plt.subplots(2, 10, figsize=(20, 4),
                       subplot_kw={'xticks': [], 'yticks': []},
                       gridspec_kw=dict(hspace=.1, wspace=.1))
for i in range(10):
    ax[0, i].imshow(faces.data[i].reshape(62, 47), cmap='binary_r')
    ax[1, i].imshow(projected[i].reshape(62, 47), cmap='binary_r')
ax[0, 0].set_ylabel('full-dim\ninput')
ax[1, 0].set_ylabel('150-dim\nreconstruction')
