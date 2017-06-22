import tensorflow as tf
import matplotlib.pyplot as plt

X = [1, 2, 3]
Y = [1, 2, 3]

W = tf.placeholder(tf.float32)
hypothesis = X * W

# cost / loss function
cost = tf.reduce_mean(tf.squre(hypothesis - Y))