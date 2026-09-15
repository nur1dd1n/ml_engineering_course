import pandas as pd
import matplotlib.pyplot as plt



# df = pd.read_csv("data.csv")

# plt.plot(df["age"], df["score"])
# plt.show()
# #plt.plot(x, y)
# plt.savefig("plot.png")
# plt.show()

# plt.grid(True)
# plt.xticks [0, 1, 2, 3, 4]

# plt.yticks([0, 1, 2, 3, 4, 5],
# [ '$0m', '$lm', '$2m', '$3m', '$4m', '$5m'])

#plt.bar(left_edges, heights, color=('r', 'g', 'Ь', 'm', 'k'))





#========== Steps for creating AI models in ML ===========

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

hours = [[1], [2], [3], [4], [5]]
scores = [50, 55, 65, 70, 75]  

#Разделение на обучение и тест
X_train, X_test, y_train, y_test = train_test_split(
    hours, scores, test_size=0.2, random_state=42
)

#Обучение модели
model = LinearRegression()
model.fit(X_train, y_train)
#Прогноз
prediction = model.predict([[6]])
print(prediction)

print(model.score(X_test, y_test))