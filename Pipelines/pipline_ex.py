from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# pipe = Pipeline([
#     ("scaler", StandardScaler()),
#     ("model", KNeighborsClassifier(n_neighbors=3))
# ])
# pipe.fit(X_train, y_train)
# pipe.predict(X_test)
# pipe.score(X_test, y_test)



X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier(n_neighbors=3))
])

pipe.fit(X_train, y_train)

print(pipe.score(X_test, y_test))
print(pipe.predict([[3.5]]))