from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd

X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

model = GradientBoostingClassifier()
model.fit(X, y)

print(model.predict([[3.5]]))

df = pd.read_csv("students.csv")

X = df[["hours", "age"]]
y = df["passed"]

model = GradientBoostingClassifier()
model.fit(X, y)

print(model.predict([[4, 21]]))
