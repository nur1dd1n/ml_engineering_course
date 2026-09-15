from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv(university.csv)

days_prep = [[100], [150], [200], [250], [300], [350]]
accepted = [0, 0, 0, 1, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(
    days_prep, accepted, test_size=0.3, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

print(model.predict([[250]]))
print(model.predict([[260]]))

print(model.predict_proba([[270]]))

print(model.score(X_test, y_test))

import pandas as pd

df = pd.read_csv("university.csv")

X = df[["days_prep"]]
Y = df["accepted"]

model = LogisticRegression()
model.fit(X, Y)

print(model.predict([[4]]))

plt.scatter(X, Y)
plt.plot(X, model.predict(X))
plt.xlabel("days of prep")
plt.ylabel("Accepted")
plt.show()