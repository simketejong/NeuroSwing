import numpy as np
from numpy import loadtxt
import sys
import os
import time 

while True:
    X = np.loadtxt("/tmp/Test_Input.dat", delimiter=",")
    syn0=np.load('./syn0.npy')
    syn1=np.load('./syn1.npy')

    l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
    l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
    Print str(l2)
    time.sleep(0.1)
