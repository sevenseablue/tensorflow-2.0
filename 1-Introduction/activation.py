#

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 101)

y_sigmoid = tf.nn.sigmoid(x)
y_relu = tf.nn.relu(x)


plt.figure(1)
plt.subplot(121)
plt.plot(x, y_relu, c='red', label='relu')
plt.ylim(-1, 5)
plt.legend(loc='best')

plt.subplot(122)
plt.plot(x, y_sigmoid, c="red", label = "sigmoid")
plt.ylim(-0.3, 1.3)
plt.legend(loc='best')

plt.show()

