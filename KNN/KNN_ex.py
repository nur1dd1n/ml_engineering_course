from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd

# X = [[1], [2], [3], [4], [5]]
# y = [0, 0, 0, 1, 1]

# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(X, y)

# scaler = StandardScaler()
# X = scaler.fit_transform(X)

# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(X, y)

# new = scaler.transform([[3.5]])
# print(model.predict(new))

# print(model.predict([[3.5]]))

# plt.scatter([1,2,3,4,5], y)
# plt.scatter([3.5], [0.5], s=200)
# plt.show()

data = {
    "hours": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "score": [45, 50, 55, 60, 65, 70, 75, 82, 88, 95],
    "level": [
        "Beginner",
        "Beginner",
        "Beginner",
        "Intermediate",
        "Intermediate",
        "Intermediate",
        "Intermediate",
        "Advanced",
        "Advanced",
        "Advanced"
    ]
}

new_student = [[7.5, 78]]

df = pd.DataFrame(data)

X = df[["hours", "score"]]
y = df["level"]

model = KNeighborsClassifier(n_neighbors = 7)

model.fit(X,y)
new_student = pd.DataFrame({"hours": [7.5], "score": [78]})

prediction = model.predict(new_student)
print(prediction[0])
plt.scatter(df["hours"], df["score"])
plt.scatter(7.5, 78)
plt.xlabel('Hours')
plt.ylabel('score')
plt.show()