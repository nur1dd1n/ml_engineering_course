from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


hours = [[1], [2], [3], [4], [5], [6]]
passed = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier()

model.fit(hours, passed)

print(model.predict([[2]]))  # 0
print(model.predict([[5]]))  # 1

plot_tree(model)
plt.show()