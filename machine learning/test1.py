#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 17:21:59 2018

@author: ckl41
"""


# -*- coding: utf-8 -*-
import numpy as np

import os

import pickle

from itertools import count

import matplotlib.pyplot as plt


with open('mnist.pkl', 'rb') as mnist_pickle:
    mnist = pickle.load(mnist_pickle, encoding='bytes')
    
mnist['data'] = mnist['data'].astype(np.float32) # convert the uint8s to floats
mnist['data'] /= 255 # scale to be from 0 to 1
mnist['target'] = mnist['target'].astype(np.int32) # convert the uint8s to int32s

def set_mnist_pos_neg(positive_label, negative_label):
    positive_indices = [i for i, j in zip(count(), mnist['target']) if j == positive_label]
    negative_indices = [i for i, j in zip(count(), mnist['target']) if j == negative_label]

    positive_images = mnist['data'][positive_indices]
    negative_images = mnist['data'][negative_indices]

    fig = plt.figure()
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(positive_images[0].reshape(28,28), cmap='gray', interpolation='nearest')
    ax.set_xticks([])
    ax.set_yticks([])
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(negative_images[0].reshape(28,28), cmap='gray', interpolation='nearest')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()
    
    return positive_images, negative_images

positive_images, negative_images = set_mnist_pos_neg(1, 0)





# N is batch size; D_in is input dimension;
# H is hidden dimension; D_out is output dimension.
N, D_in, H, D_out = 64, 784, 100, 1

# Create random input and output data
x = np.random.randn(N, D_in)
y = np.random.randn(N, D_out)

x = np.concatenate([positive_images[0:30,:],negative_images[0:34,:]],axis=0)
y= np.array([1 for i in range(30)] + [0 for i in range(34)])
y=np.split(y,64)

rng = np.random.RandomState(1)
X = np.dot(rng.rand(2, 2), rng.randn(2, 200)).T
plt.scatter(X[:, 0], X[:, 1])
plt.axis('equal');

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(x)


'''
# Randomly initialize weights
w1 = np.random.randn(D_in, H)
w2 = np.random.randn(H, D_out)

learning_rate = 1e-6
for t in range(500):
    # Forward pass: compute predicted y
    h = x.dot(w1)
    h_relu = np.maximum(h, 0)
    y_pred = h_relu.dot(w2)

    # Compute and print loss
    loss = np.square(y_pred - y).sum()
    print(t, loss)

    # Backprop to compute gradients of w1 and w2 with respect to loss
    grad_y_pred = 2.0 * (y_pred - y)
    grad_w2 = h_relu.T.dot(grad_y_pred)
    grad_h_relu = grad_y_pred.dot(w2.T)
    grad_h = grad_h_relu.copy()
    grad_h[h < 0] = 0
    grad_w1 = x.T.dot(grad_h)

    # Update weights
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2


x = np.concatenate([positive_images[30:60,:],negative_images[34:34+34,:]],axis=0)
y= np.array([1 for i in range(30)] + [0 for i in range(34)])
y=np.split(y,64)

h = x.dot(w1)
h_relu = np.maximum(h, 0)
y_pred = h_relu.dot(w2)

'''
