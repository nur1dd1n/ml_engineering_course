from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import plot_tree

df = pd.read_csv("students2.csv")

X = df[["hours", "attendance", "homework", "score"]]
y = df["passed"]

model_knn = KNeighborsClassifier(n_neighbors=5)
model_Dtree = DecisionTreeClassifier(random_state=42)
model_logic = LogisticRegression()

model_knn.fit(X,y)
model_Dtree.fit(X,y)
model_logic.fit(X,y)

new_student = [[6, 80, 7, 65]]

print(model_Dtree.predict(new_student))
print(model_knn.predict(new_student))
print(model_logic.predict(new_student))

plt.scatter(df["hours"], df["passed"])
plt.xlabel("Hours")
plt.ylabel("Passed")
plt.show()
plot_tree(model_Dtree)