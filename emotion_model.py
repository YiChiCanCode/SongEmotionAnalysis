"""
@author: Su, Yiming,
Original author: Sayak, Ritayan
"""
import pickle

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

data = pd.read_csv('Emotion_features.csv')
feature = data.loc[:, 'tempo':]
featureName = list(feature)

for name in featureName:
    feature[name] = (feature[name] - feature[name].min()) / (feature[name].max() - feature[name].min())

array = np.array(data)

features = feature.values
labels = data.loc[:, 'class'].dropna()
test_size = 0.20
random_seed = 42

train_d, test_d, train_l, test_l = train_test_split(features, labels, test_size=test_size, random_state=random_seed)

# for i in range(1, 11):
#     print(i)
#     kNN = KNeighborsClassifier(n_neighbors=i)
#     kNN.fit(train_d, train_l)
#     result = kNN.score(test_d, test_l)
#     print(result)

kNN = KNeighborsClassifier(n_neighbors=6)
kNN.fit(train_d, train_l)


filename = 'knn_model.sav'
pickle.dump(kNN, open(filename, 'wb'))




