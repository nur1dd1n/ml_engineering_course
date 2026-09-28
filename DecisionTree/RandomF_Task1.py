from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import plot_tree

X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [0, 0, 0, 0, 0, 1, 1, 1]

model_RandomF = RandomForestClassifier(n_estimators=200, max_depth=10)
model_knn = KNeighborsClassifier(n_neighbors=4)
model_Dtree = DecisionTreeClassifier(random_state=42)


model_knn.fit(X,y)
model_RandomF.fit(X,y)
model_Dtree.fit(X,y)

print(model_Dtree.predict([[6]]))
print(model_knn.predict([[6]]))
print(model_RandomF.predict([[6]]))
print(model_RandomF.score(X, y))
