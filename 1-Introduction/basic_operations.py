import tensorflow as tf

a=tf.ones([2,3])
print(a)

a = tf.Variable(a)
b = a.read_value()
a[0,0].assign(10)
print(a)
print(b)

print(b is a)

