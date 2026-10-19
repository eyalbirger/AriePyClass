import numpy as np
import math
import random
import scipy
from scipy import ndimage
import h5py
import matplotlib.pyplot as plt
from PIL import Image
import sys
sys.path.append(r"unit10/c1w2_utils.py")
import unit10.c1w2_utils

train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset() 
index = 25 # change index to get a different picture
plt.imshow(train_set_x_orig[index])
plt.show()
print ("y = " + str(train_set_y[index]) + ", it's a '" + 
classes[np.squeeze(train_set_y[index])].decode("utf-8") +  "' picture.")

m_train = len(train_set_x_orig)
m_test = len(test_set_x_orig)
num_px = train_set_x_orig.shape[1] * train_set_x_orig.shape[0]


print ("Number of training examples: m_train = " + str(m_train))
print ("Number of testing examples: m_test = " + str(m_test))
print ("Height/Width of each image: num_px = " + str(num_px))
print ("Each image is of size: (" + str(num_px) + ", " + str(num_px) + ", 3)")
print ("train_set_x shape: " + str(train_set_x_orig.shape))
print ("train_set_y shape: " + str(train_set_y.shape))
print ("test_set_x shape: " + str(test_set_x_orig.shape))
print ("test_set_y shape: " + str(test_set_y.shape))



"""
#m = len(y)
#n = x.shape[0]

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def perceptron(X, W, B):
    Z = (W@X)+B
    return sigmoid(Z)

alpha = 0.0001
def calcJ(X,Y,W, b):
    n = X.shape[1]
    m = len(Y)

    J = 0
    DW = np.zeros(n)
    Db = 0
    
    for i in range(m):
        
        diff=0
        y_hat = perceptron(X[i], W, b)

        diff = y_hat-Y[i]

        
        #J = J + diff ** 2
        J = 

        Db = Db + diff * 2
        for j in range (n):
            DW[j] = DW[j] + diff * X[i,j] * 2


    return J/m, DW/m, Db/m

def train(X, Y, iterations, alpha):

    w = np.zeros(len(X[0]))
    for i in range(len(X[0])):
        w[i] = random.randint(-26, 26)

    b = random.randint(-10, 10)

    for i in range(iterations):
        J, Da, Db = calcJ(X, Y, w, b)
        w -= Da*alpha
        b -= Db*alpha
    return w, b

def addaptive_train(X, Y, alpha, iter):
    lengthW = len(X[0])
    w = np.zeros(lengthW) #יוצר מערך של אפסים באורך של שורה אחת של איקס
    alphaW = np.zeros(lengthW)

    for i in range(lengthW):
        w[i] = random.randint(-26, 26)
        alphaW[i] = alpha

    b = random.randint(-10, 10)
    alphaB = alpha

    
    for i in range(iter):
        J, Dw, Db = calcJ(X, Y, w, b)

        for j in range(lengthW):
            if Dw[j]*alphaW[j] > 0:# אז כזה אם הנגזרת חיובית או שלילית
                alphaW[j] *= 1.1
            else:
                alphaW[j] *= 0.9
            if alphaB*Db > 0:
                alphaB *= 1.1
            else: 
                alphaB *= 0.9
        for j in range(lengthW):
            w[j] -= Dw*alphaW
        b -= Db*alphaB
    return w, b




W, B = train(x, y, 1000000, alpha)
for i in range (len(W)):
    print(f"W={W[i]},", end=" ")
print()
print("B = ", B)

"""