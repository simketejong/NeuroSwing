import numpy as np
from numpy import loadtxt
import sys
import os
import time
l2_error = 1
while True:
    while ((os.path.isfile("/tmp/Input.dat")) & (os.path.isfile("/tmp/Output.dat")):
        X = np.loadtxt("/tmp/Input.dat")
        y = (np.loadtxt("/tmp/Output.dat"))

        file = open("/tmp/WegDat.txt", "a")
        file.write("delete dat files")
        file.close()

        if os.path.isfile('./syn0.npy'):
            syn0=np.load('./syn0.npy')
        else:
            syn0 = 2*np.random.random((7,50)) - 1

        if os.path.isfile('./syn1.npy'):
            syn1=np.load('./syn1.npy')
        else:
            syn1 = 2*np.random.random((50,2)) - 1

        teller = 0
        os.remove("/tmp/WegDat.txt")
        while (teller < 100000):
            l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
            l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
            l2_delta = (y - l2)*(l2*(1-l2))
            l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))
            syn1 += l1.T.dot(l2_delta)
            syn0 += X.T.dot(l1_delta)
            l2_error = y - l2
            print "Error:" + str(np.mean(np.abs(l2_error)))
            teller = teller + 1
            print "teller" + str(teller)
    np.save('./syn0', syn0)
    np.save('./syn1', syn1)
time.sleep(60)

