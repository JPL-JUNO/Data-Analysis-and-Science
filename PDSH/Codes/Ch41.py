"""
@Description: In Depth: Naive Bayes Classification
@Author: Stephen CUI
@Time: 2023-04-11 15:03:01
"""


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.datasets import make_blobs
X, y = make_blobs(100, 2, centers=2, random_state=2, cluster_std=1.5)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu')

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X, y)

rng = np.random.RandomState(0)
# 生成[-6, 8]\times [-14, 4]上的均匀分布
X_new = [-6, -14] + [14, 18] * rng.rand(2000, 2)
y_new = model.predict(X_new)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu')
lim = plt.axis()
plt.scatter(X_new[:, 0], X_new[:, 1], c=y_new, s=20, alpha=.1, cmap='RdBu')
plt.axis(lim)

# 怎么求的概率，使用 类似于 softmax 那种变换吗？因为后验概率的计算中，分母是不能计算的吧！！！
yprob = model.predict_proba(X_new)
yprob[-8:].round(2)


from sklearn.datasets import fetch_20newsgroups

data = fetch_20newsgroups()
data.target_names

categories = ['talk.religion.misc',
              'soc.religion.christian', 'sci.space', 'comp.graphics']
train = fetch_20newsgroups(subset='train', categories=categories)
test = fetch_20newsgroups(subset='test', categories=categories)
print(train.data[5][48:])

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

model = make_pipeline(TfidfVectorizer(),
                      MultinomialNB())
model.fit(train.data, train.target)
labels = model.predict(test.data)

from sklearn.metrics import confusion_matrix
mat = confusion_matrix(test.target, labels)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=train.target_names, yticklabels=train.target_names,
            cmap='Blues')
plt.xlabel('true label')
plt.ylabel('predicted label')


def predict_category(s, train=train, model=model):
    pred = model.predict([s])  # return an array containing the index of label
    return train.target_names[pred[0]]


predict_category('sending a payload to the ISS')
predict_category('discussing the existence of God')
predict_category('determining the screen resolution')
