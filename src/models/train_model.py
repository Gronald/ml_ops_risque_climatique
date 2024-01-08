import pandas as pd
from joblib import dump
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("data/raw/base.csv",sep=";")

data_oot = data.loc[data.annee >2000]

data_train = data.loc[data.annee <= 2000]

X = data_train[['latitude','longitude','annee']]
y = data_train['risque']

clf = KNeighborsClassifier()

parameters = {'n_neighbors': [5, 10, 15]}

grid = GridSearchCV(clf, parameters, n_jobs=-1,cv=10)

grid.fit(X, y)

estimator = grid.best_estimator_

dump(estimator, "models/model.joblib")

