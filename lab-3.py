# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E2xGxX7Qlo2LMd2XnXlR4hQCorvdOIL6
"""

import tensorflow as tf #: Imports the TensorFlow library,
from tensorflow import keras # Imports the Keras module from TensorFlow
import numpy as np #Imports the NumPy library, which is used for numerical computations 
import matplotlib.pyplot as plt #Imports the Matplotlib library for plotting

model=tf.keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])]) #Creates a sequential model using Keras.
# It consists of a single dense  layer with one unit and an input shape of [1]

for layer in model.layers:
    weights = layer.get_weights() #Retrieves the weights of the layer in the model and assigns them to the weights variable.

model.compile(optimizer='sgd', loss='mse') #Sets the model for training. It specifies the optimizer as stochastic gradient descent (SGD) 
#and the loss function as mean squared error (MSE).
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=np.float32) # Creates a NumPy array xs containing the input data points.
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=np.float32)# Creates a NumPy array ys containing the corresponding target values.

plt.scatter(xs, ys)#a scatter plot of xs versus ys 

model.fit(xs, ys, epochs=500) #Trains the model on the input data xs and target values ys for 500 epochs, adjusting the weights to minimize the MSE loss.
print(model.predict([10.0])) # to predict the output for a new input value of 10.0 and prints the result.