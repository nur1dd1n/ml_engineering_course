from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

# hours = [[1], [2], [3], [4], [5]]
# scores = [50, 55, 65, 70, 75]

# df = pd.read_csv("students_pandas.csv")

# X = df[["hours"]]
# Y = df["score"]

# model = LinearRegression()
# model.fit(X, Y)

# print(model.predict([[7]]))



# plt.scatter(hours, scores)
# plt.plot(hours, model.predict(hours))
# plt.show()


from sklearn.linear_model import LogisticRegression


hours = [[1], [2], [3], [4], [5], [6]]
passed = [0, 0, 0, 1, 1, 1]  # 0 - нет, 1 - да

X_train, X_test, y_train, y_test = train_test_split(
    hours, passed, test_size=0.3, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

print(model.predict([[2]]))
print(model.predict([[5]]))

print(model.predict_proba([[4]]))

print(model.score(X_test, y_test))

import pandas as pd

df = pd.read_csv("exam.csv")

X = df[["hours"]]
Y = df["passed"]

model = LogisticRegression()
model.fit(X, Y)

print(model.predict([[4]]))