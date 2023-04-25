"""
@Description: k-Means on Digits
@Author(s): Stephen CUI
@Time: 2023-04-18 17:05:15
"""

from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

digits = load_digits()
assert digits.data.shape == (1797, 64)
kmeans = KMeans(n_clusters=10, n_init='auto', random_state=0)
clusters = kmeans.fit_predict(digits.data)
assert kmeans.cluster_centers_.shape == (10, 64)
fig, ax = plt.subplots(2, 5, figsize=(8, 3))
centers = kmeans.cluster_centers_.reshape(10, 8, 8)
for axi, center in zip(ax.flat, centers):
    axi.set(xticks=[], yticks=[])
    axi.imshow(center, interpolation='nearest', cmap=plt.cm.binary)


from scipy.stats import mode
# clusters 中的数字只是用来表示类的，并不表明其真实的那个值，
# 比如说 1 只是表明所有的 1 是一类并不意味着是 1 这一类
labels = np.zeros_like(clusters)
for i in range(10):
    mask = (clusters == i)
    labels[mask] = mode(digits.target[mask], axis=0, keepdims=False)[0]
from sklearn.metrics import accuracy_score
accuracy_score(digits.target, labels)

from sklearn.metrics import confusion_matrix
import seaborn as sns
mat = confusion_matrix(digits.target, labels)
fig = plt.figure()
ax = sns.heatmap(mat.T, square=True, annot=True, fmt='d',
                 cbar=False, cmap='Blues', xticklabels=digits.target_names,
                 yticklabels=digits.target_names)
ax.tick_params(left=False, bottom=False)
ax.set_xlabel('True Label')
ax.set_ylabel('Predicted Label')


from sklearn.manifold import TSNE
tsne = TSNE(n_components=2, init='random',
            learning_rate='auto', random_state=0)
digits_proj = tsne.fit_transform(digits.data)
kmeans = KMeans(n_clusters=10, random_state=0, n_init='auto')
clusters = kmeans.fit_predict(digits_proj)
labels = np.zeros_like(clusters)
for i in range(10):
    mask = (clusters == i)
    labels[mask] = mode(digits.target[mask], axis=0, keepdims=False, )[0]
accuracy_score(digits.target, labels)
