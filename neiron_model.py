import tensorflow as tf
import keras
import numpy as np

x = np.array([1,2,3,4,5], dtype=float)
y = np.array([2,4,6,8,10], dtype=float)

model = keras.Sequential([
    keras.layers.Dense(1, input_shape=[1])
])

model.compile(optimizer="adam", loss="mse")
model.fit(x, y, epochs=200)

print(model.predict(np.array([6])))

# Что тут происходит
# Dense(1) → 1 нейрон
# input_shape=[1] → один вход
# optimizer="adam" → как менять веса
# loss="mse" → ошибка

history = model.fit(x, y, epochs=200)

import matplotlib.pyplot as plt
plt.plot(history.history['loss'])
plt.show()