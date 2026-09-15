from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("decisionTree.csv")

X = df[["days_prep"]]
Y = df[["passed"]]

# days_prep = [[100], [150], [200], [250], [300], [350], [400]]
# passed = [0, 0, 0, 0, 1, 1,1]

model = DecisionTreeClassifier()

model.fit(X, Y)

print(model.predict([[170]]))  # 0
print(model.predict([[450]]))  # 1

plot_tree(model)
plt.show()