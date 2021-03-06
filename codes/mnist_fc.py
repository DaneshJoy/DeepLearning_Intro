# -*- coding: utf-8 -*-
"""MNIST_FC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17keDkKP7tpKwV8ibgYzYQjaBTLR1eDSE

## MNIST Classification Using **Dense** Layers
"""

import tensorflow as tf
from tensorflow.keras import datasets, utils, models, layers, optimizers, losses
import numpy as np
import matplotlib.pyplot as plt

"""Data Preparation"""

(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()
print("train_images dimentions: ", train_images.ndim)
print("train_images shape: ", train_images.shape)

# Preprocessing

X_train = train_images.reshape(60000, 784)
X_test = test_images.reshape(10000, 784)

# Normalizing (0-1)
X_train = X_train.astype('float32') / 255
X_test =  X_test.astype('float32') / 255

Y_train = utils.to_categorical(train_labels)
Y_test = utils.to_categorical(test_labels)

print(train_labels[0])
print(Y_train[0])

for i in range(5):
    plt.subplot(1,5,i+1)
    plt.imshow(train_images[i], cmap='gray')
    plt.title(train_labels[i])
    plt.axis('off')

"""Model Creation"""

myModel = models.Sequential()
myModel.add(layers.Dense(500, activation='relu', input_shape=(784,)))
myModel.add(layers.Dropout(0.2))
myModel.add(layers.Dense(100, activation='relu'))
myModel.add(layers.Dropout(0.2))
myModel.add(layers.Dense(10, activation='softmax'))

myModel.summary()
myModel.compile(optimizer=optimizers.SGD(lr=0.001), loss=losses.categorical_crossentropy)

"""Training"""

# Train our model
history = myModel.fit(X_train, Y_train, batch_size=128, epochs=20, validation_split=0.2)

losses = history.history['loss']
val_losses = history.history['val_loss']

plt.plot(losses)
plt.plot(val_losses)
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend(['loss', 'val_loss'])

# Evaluation
test_loss = myModel.evaluate(X_test, Y_test)
print("test loss: ", test_loss)

test_labels_p = myModel.predict(X_test)
test_labels_p = np.argmax(test_labels_p, axis=1)
print("True labels: ", test_labels[0:10])
print("Pred labels: ", test_labels_p[0:10])