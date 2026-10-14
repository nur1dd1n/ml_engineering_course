import keras
from keras import Sequential
from keras.layers import Dense
import numpy as np

# x=np.linspace(-10,10,1000)
# y= x ** 2

x = np.array([4,5,7,8], dtype=float)
y = np.array([16,25,49,64], dtype=float)

model = Sequential()
model.add(Dense(10, activation="relu", input_shape=[1]))
model.add(Dense(1))
model.compile(optimizer="adam", loss="mse")
model.fit(x,y, epochs=2000, verbose=0)

print(model.predict(np.array([5,7,8])))
