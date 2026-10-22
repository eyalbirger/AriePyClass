import numpy as np
import random
import scipy
from scipy import ndimage
import h5py
import matplotlib.pyplot as plt
from PIL import Image
import unit10.c1w2_utils as c1w2

train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = c1w2.load_dataset() 
index = 25 # change index to get a different picture
plt.imshow(train_set_x_orig[index])
#plt.show()
print ("y = " + str(train_set_y[index]) + ", it's a '" + 
classes[np.squeeze(train_set_y[index])].decode("utf-8") +  "' picture.")

# exe 1
num_of_pics_train = len(train_set_x_orig) # m
num_of_pics_test = len(test_set_x_orig)

num_px = len(train_set_x_orig[index]) #


print(f"num of training pics: {num_of_pics_train}")
print(f"num of testing pics: {num_of_pics_test}")
print(f"height: {num_px}, width: {num_px}")
print(f"each image is of size: ({num_px}, {num_px}, 3)") # height by width by 3(rgb)

print(f"train set x shape: {str(train_set_x_orig.shape)}")
print(f"train set y shape: {str(train_set_y.shape)}")
print(f"test set x shape: {str(test_set_x_orig.shape)}")
print(f"test set y shape: {str(test_set_y.shape)}")

# exe 2

train_set_x_flatten = train_set_x_orig.reshape(train_set_x_orig.shape[0], -1)
test_set_x_flatten = test_set_x_orig.reshape(test_set_x_orig.shape[0], -1)

print(f"train set x flatten: {str(train_set_x_flatten.shape)}")
print(f"test set x flatten: {str(test_set_x_flatten.shape)}")

train_set_x = (train_set_x_flatten / 255).T
test_set_x = (test_set_x_flatten / 255).T
#train_set_x = []
#for pic in train_set_x_flatten:
#    train_set_x.append(pic/255)


# exe 3
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

print(f"sigmoid([0, 2]) = {str(sigmoid(np.array([0, 2])))}")


# exe 4
def initialize_with_zeros(dim):
    w = np.zeros((dim, 1))
    return w, 0

#W, B = initialize_with_zeros(n)
#print(f"W = {str(W)}")
#print(f"b = {str(b)}")


# exe 5
def perceptron(X, W, B):
    Z = W.T @ X + B
    return sigmoid(Z)


def forward_propagation(X, Y, w, b):
    m = X.shape[1]
    A = perceptron(X, w, b)

    j = -np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A))
    return j/m


x = train_set_x
y = train_set_y

n = x.shape[0]
w, b = initialize_with_zeros(n)
print("--------------------")
print(f"X shape: {x.shape}")
print(f"W shape: {w.shape}")
print("-----------------------------------------------------------\n")
print(f"cost: {forward_propagation(x, y, w, b)}")