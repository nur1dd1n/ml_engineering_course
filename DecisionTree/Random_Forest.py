from sklearn.ensemble import RandomForestClassifier

X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

model = RandomForestClassifier(n_estimators=100)

model.fit(X, y)

print(model.predict([[3.5]]))
print(model.score(X, y))

# n_estimators=100

# означает:

# Создать 100 деревьев.
# max_depth

# Максимальная глубина каждого дерева.

# max_depth=10