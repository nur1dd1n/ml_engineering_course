import keras 
from keras.datasets import mnist
from keras import Sequential
import numpy as np
import matplotlib.pyplot as plt

(x_train, y_train),(x_test, y_test)=mnist.load_data()

print("Обучающие изображения:", x_train.shape)
print("Обучающие метки:", y_train.shape)
print("Тестовые изображения:", x_test.shape)
print("Тестовые метки:", y_test.shape)

plt.figure(figsize=(8, 4))

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_train[i], cmap="gray")
    plt.title(f"Цифра: {y_train[i]}")
    plt.axis("off")

plt.tight_layout()
plt.show()

x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

x_train = x_train[..., np.newaxis]
x_test = x_test[..., np.newaxis]

print(x_train.shape)
print(x_test.shape)







model = keras.Sequential([
    keras.layers.Input(shape=(28, 28, 1)),

    # Первый свёрточный слой
    keras.layers.Conv2D(
        filters=64,
        kernel_size=(3, 3),
        activation="relu"
    ),

     # Уменьшаем размер карты признаков
    keras.layers.MaxPooling2D(pool_size=(2, 2)),

    # Второй свёрточный слой
    keras.layers.Conv2D(
        filters=128,
        kernel_size=(3, 3),
        activation="relu"
    ),

    # Ещё одно уменьшение размера
    keras.layers.MaxPooling2D(pool_size=(2, 2)),

    # Преобразуем признаки в вектор
    keras.layers.Flatten(),

    # Полносвязный слой
    keras.layers.Dense(64, activation="relu"),

    # 10 классов: цифры от 0 до 9
    keras.layers.Dense(10, activation="softmax"),

    keras.layers.Dropout(0.3)
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

history = model.fit(
    x_train,
    y_train,
    epochs=10,
    batch_size=64,
    validation_split=0.1
)
# Проверяем модель на тестовых данных
test_loss, test_accuracy = model.evaluate(
    x_test,
    y_test,
    verbose=0
)

print("Ошибка:", test_loss)
print("Точность:", test_accuracy)
print(f"Точность в процентах: {test_accuracy * 100:.2f}%")
index = 25

image = x_test[index]

prediction = model.predict(
    image[np.newaxis, ...],
    verbose=0
)

predicted_digit = np.argmax(prediction[0])

plt.imshow(image.squeeze(), cmap="gray")
plt.title(f"Предсказание: {predicted_digit}")
plt.axis("off")
plt.show()

print("Правильный ответ:", y_test[index])
print("Предсказание модели:", predicted_digit)
print(
    "Оценка уверенности:",
    f"{prediction[0][predicted_digit] * 100:.2f}%"
)