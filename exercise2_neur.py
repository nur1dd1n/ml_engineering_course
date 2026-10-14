import keras
from keras import Sequential
from keras.layers import Dense
import numpy as np
from sklearn.model_selection import train_test_split

x = np.arange(1, 101, dtype='float32')
y = x ** 3

x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=42)

model1 = Sequential()
model1.add(Dense(4, activation='relu', input_shape=[1]))
model1.add(Dense(1))
model1.compile(optimizer="adam", loss="mse", metrics=['mae'])
model1.fit(x,y, epochs=200, verbose=0)

print(model1.predict(np.array([2,3,4])))

model2 = Sequential()
model2.add(Dense(50, activation='relu', input_shape=[1]))
model2.add(Dense(50, activation='relu'))
model2.add(Dense(1))
model2.compile(optimizer="adam", loss="mse", metrics=['mae'])
model2.fit(x,y, epochs=200, verbose=0)

print(model2.predict(np.array([2,3,4])))

for name, model in [('model1', model1),
                    ('model2', model2)]:
    train_loss, train_mae = model.evaluate(
        x_train, y_train, verbose=0
    )
    val_loss, val_mae = model.evaluate(
        x_val, y_val, verbose=0
    )

    print(name)
    print(f'trainig (MAE): {train_mae:.2f}')
    print(f'validation (MAE): {val_mae:.2f}')
    print()