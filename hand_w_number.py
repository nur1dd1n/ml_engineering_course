from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization
from keras.datasets import mnist
from keras.activations import relu
from keras.optimizers import Adam
from keras import utils
from keras.preprocessing import image
import numpy as np
import pandas as pd
import pylab
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split





(x_train_org, y_train_org), (x_test_org, y_test_org) = mnist.load_data()


x_train = x_train_org.reshape(60000, 784)
x_test = x_test_org.reshape(10000, 784)

x_train = x_train.astype('float32')
x_train = x_train / 255
x_test = x_test.astype('float32')
x_test = x_test / 255


y_train = utils.to_categorical(y_train_org, 10)
y_test = utils.to_categorical(y_test_org, 10)

x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=10000, random_state=42)

results = []

for n in [50000, 10000, 500]:
    model = Sequential()
    model.add(Dense(800, input_dim=784, activation="relu"))
    model.add(Dense(400, activation="relu"))
    model.add(Dense(10, activation="softmax"))
    model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

    history = model.fit(x_train[:n], y_train[:n], batch_size=128, epochs=15,validation_data=(x_val, y_val), verbose=1)

    test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
    results.append(['Basic',
                    n,
                    history.history['val_accuracy'][-1],
                    test_accuracy])

    print(history.history['val_accuracy'][-1])
    print(test_accuracy)

model.save_weights('model.weights.h5')
model.load_weights('model.weights.h5')

model = Sequential()
model.add(Dense(800, input_dim=784, activation="relu"))
model.add(BatchNormalization())
model.add(Dropout(0.3))

model.add(Dense(400, activation="relu"))
model.add(BatchNormalization())
model.add(Dropout(0.3))

model.add(Dense(200, activation="relu"))
model.add(BatchNormalization())
model.add(Dropout(0.2))

model.add(Dense(10, activation="softmax"))

model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(x_train,y_train, batch_size=128, epochs=15, validation_data=(x_val, y_val), verbose=1)

test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)

results.append(['New',
                50000,
                history.history['val_accuracy'][-1],
                test_accuracy])

table = pd.DataFrame(results, columns=['Arch',
                                       'Number of Ex', 
                                       'Accuracy of test', 
                                       'Accuracy of test'])

print(table)
table.to_csv('result.csv', index=False)


n=125
plt.imshow(Image.fromarray(x_train_org[n]).convert('RGB'))
plt.show()

x = x_test[n]
print(x.shape)
x = np.expand_dims(x, axis=0)
print(x.shape)

prediction = model.predict(x)
print(prediction)
sum(prediction[0])

pred = np.argmax(prediction)
print(pred)
print(y_test_org[n])

