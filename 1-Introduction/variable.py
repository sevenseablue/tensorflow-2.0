import tensorflow as tf

with tf.name_scope("my") as my:
    variable = tf.Variable(1)
print(variable)

variable = variable + 1
print(variable)

variable = tf.Variable(2)
variable.assign_add(1)
print(variable)
