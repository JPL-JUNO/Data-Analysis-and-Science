"""
@Description: Example: Random Forest for Classifying Digits
@Author: Stephen CUI
@Time: 2023-04-17 10:23:43
"""

from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
digits = load_digits()
digits.keys()
fig = plt.figure(figsize=(6, 6))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1,
                    hspace=.05, wspace=.05)
for i in range(64):
    ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
    ax.text(0, 7, str(digits.target[i]))

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
X_train, X_test, y_train, y_test = train_test_split(digits.data,
                                                    digits.target,
                                                    random_state=0)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

from sklearn import metrics
print(metrics.classification_report(y_pred, y_test))

from sklearn.metrics import confusion_matrix
import seaborn as sns
mat = confusion_matrix(y_test, y_pred)
fig = plt.figure()
sns.heatmap(mat.T, square=True, annot=True,
            fmt='d', cbar=False, cmap='Blues')
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.xticks([])
plt.yticks([])
