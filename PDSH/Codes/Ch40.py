"""
@Description: Feature Engineering
@Author: Stephen CUI
@Time: 2023-04-11 10:20:48
"""

data = [
    {'price': 850000, 'rooms': 4, 'neighborhood': 'Queen Anne'},
    {'price': 700000, 'rooms': 3, 'neighborhood': 'Fremont'},
    {'price': 650000, 'rooms': 3, 'neighborhood': 'Wallingford'},
    {'price': 600000, 'rooms': 2, 'neighborhood': 'Fremont'}
]

from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer(sparse=False, dtype=int)
vec.fit_transform(data)
vec.get_feature_names_out()


vec = DictVectorizer(sparse=True, dtype=int)
vec.fit_transform(data)

from sklearn.preprocessing import OneHotEncoder

X = [['Male', 1], ['Female', 3], ['Female', 2]]
ohe = OneHotEncoder(sparse_output=False, dtype=int)
ohe.fit_transform(X)


from sklearn.feature_extraction import FeatureHasher
fh = FeatureHasher(n_features=5, dtype=int)
fh.fit_transform(data).toarray()

# text features
sample = ['problem of evil',
          'evil queen',
          'horizon problem']
from sklearn.feature_extraction.text import CountVectorizer
vec = CountVectorizer()
X = vec.fit_transform(sample)
import pandas as pd
pd.DataFrame(X.toarray(), columns=vec.get_feature_names_out())


from sklearn.feature_extraction.text import TfidfVectorizer
vec = TfidfVectorizer()
X = vec.fit_transform(sample)
pd.DataFrame(X.toarray(), columns=vec.get_feature_names_out())


import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5])
y = np.array([4, 2, 1, 3, 7])
plt.plot(x, y, 'ko', label='origin data')

from sklearn.linear_model import LinearRegression
X = x[:, np.newaxis]
model = LinearRegression().fit(X, y)
yfit = model.predict(X)
plt.plot(x, yfit, label='degree = 1')

from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=3, include_bias=False)
X2 = poly.fit_transform(X)
print(X2)


model = LinearRegression().fit(X2, y)
yfit = model.predict(X2)
plt.plot(x, yfit, label='degree = 3')

plt.legend()


from numpy import nan
X = np.array([[nan, 0, 3],
              [3, 7, 9],
              [3, 5, 2],
              [4, nan, 6],
              [8, 8, 1]])
y = np.array([14, 16, -1, 8, -5])

from sklearn.impute import SimpleImputer
imp = SimpleImputer(strategy='mean')
X2 = imp.fit_transform(X)
print(X2)

model = LinearRegression().fit(X2, y)
model.predict(X2)


from sklearn.pipeline import make_pipeline

model = make_pipeline(SimpleImputer(strategy='mean'),
                      PolynomialFeatures(degree=2),
                      LinearRegression())
model.fit(X, y)
print(y)
print(model.predict(X))
