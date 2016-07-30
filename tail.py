import subprocess
import numpy as np
from numpy import loadtxt
import sys
import os
import stat, time

l2_error = 1
maxL0 = 0
maxL1 = 0

syn0=np.load('./syn0.npy')
syn1=np.load('./syn1.npy')

HowOldFile=os.stat("./syn1.npy")[stat.ST_MTIME]
vorige=0
HowOldDataFile=0
f = subprocess.Popen(['tail','-F','/tmp/Test_Input.dat'],\
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)

while True:
	line = line = f.stdout.readline()
	X = np.fromstring(line,dtype=float,sep=" ")
	if len(X) == 7:
		X[6] = vorige
		if os.stat("./syn1.npy")[stat.ST_MTIME] > HowOldFile:
			time.sleep(1)
			syn0=np.load('./syn0.npy')
			syn1=np.load('./syn1.npy')
			HowOldFile=os.stat("./syn1.npy")[stat.ST_MTIME]
		l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
		l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
		vorige=l2[0]
		if l2[0] > maxL0:
			maxL0 = l2[0]
		if l2[1] > maxL1:
			maxL1 = l2[1]
		print "Feedback=%f Swing=%f Max_Feedback=%f  Max_Swing=%f Input ->>> %s" % (((l2[0])), ((l2[1])), maxL0 , maxL1, X)