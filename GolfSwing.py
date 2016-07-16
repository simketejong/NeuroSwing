import numpy as np
from numpy import loadtxt
import sys
import os
#import os.path

#X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
#y = np.array([[0,1,1,0]]).T
##FirstLayer = random.randint(size=(4, 100))
##SecondLayer = random.randint(size=(4, 100))

X = np.loadtxt("Learn_Input.dat", delimiter=",")
y = np.loadtxt("Learn_Output.dat", delimiter=",")

if os.path.isfile('./syn0.npy'):
    syn0=np.load('./syn0.npy')
else:
    syn0 = 2*np.random.random((4,5)) - 1

if os.path.isfile('./syn1.npy'):
    syn1=np.load('./syn1.npy')
else:
    syn1 = 2*np.random.random((3,2)) - 1

print "x" + str(X)
print "y" + str(y)

##print "syn0" + str(syn0)
##print "syn1" + str(syn1)
##sys.exit()
l2_error = 1
teller = 0
while (np.mean(np.abs(l2_error)) > 0.01):
    l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
    l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
    l2_delta = (y - l2)*(l2*(1-l2))
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))
    syn1 += l1.T.dot(l2_delta)
    syn0 += X.T.dot(l1_delta)
    l2_error = y - l2
    ##print "x" + str(X)
    ##print "y = " + str(y)
##    print "l2 = " + str(l2)
    print "Error:" + str(np.mean(np.abs(l2_error)))
    teller = teller + 1
    print "teller" + str(teller)
#    print "syn0" + str(syn0)
np.save('./syn0', syn0)
np.save('./syn1', syn1)

