# -*- coding: utf-8 -*-
"""
这个练习的代码来自 ReLU 的练习，应用一个 dropout 层。
用 ReLU 层和 dropout 层构建一个模型，
keep_prob值设为 0.5。打印这个模型的 logits。
注意: 由于 dropout 会随机丢弃单元，每次运行代码输出会有所不同。
"""

import tensorflow as tf

hidden_layer_weights = [
    [0.1, 0.2, 0.4],
    [0.4, 0.6, 0.6],
    [0.5, 0.9, 0.1],
    [0.8, 0.2, 0.8]]
out_weights = [
    [0.1, 0.6],
    [0.2, 0.1],
    [0.7, 0.9]]

# Weights and biases
weights = [
    tf.Variable(hidden_layer_weights),
    tf.Variable(out_weights)]
biases = [
    tf.Variable(tf.zeros(3)),
    tf.Variable(tf.zeros(2))]

# Input
features = tf.Variable([[0.0, 2.0, 3.0, 4.0], [0.1, 0.2, 0.3, 0.4], [11.0, 12.0, 13.0, 14.0]])

# TODO: Create Model with Dropout
# 定义一个placeholder用来存放drop_out的数量比例
keep_prob = tf.placeholder(tf.float32)

# 定义hidden layer和activation过程
hidden_layer = tf.add(tf.matmul(features, weights[0]), biases[0])
hidden_layer = tf.nn.relu(hidden_layer)

# Drop out ！！！
hidden_layer = tf.nn.dropout(hidden_layer, keep_prob)

# 输出
logits = tf.add(tf.matmul(hidden_layer, weights[1]), biases[1])

# TODO: Print logits from a session
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(logits, feed_dict={keep_prob: 0.5}))