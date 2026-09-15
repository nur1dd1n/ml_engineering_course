from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

# days = [[1],[2],[3],[4],[5]]
# mm = [[15],[20],[25],[30],[35]]

df = pd.read_csv("plant_growth.csv")

X = df[["days"]]
Y = df[["mm"]]

model = LinearRegression()
model.fit(X,Y)

print(model.predict([[7]]))

plt.scatter(X, Y)
plt.plot(X, model.predict(X))
plt.xlabel("Days")
plt.ylabel("Growth (mm)")
plt.show()