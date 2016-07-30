import numpy as np
from numpy import loadtxt
import sys
import os, stat
import time

l2_error = 1

# Input Learning file
InputFile="/tmp/Input.dat"
# Output Learning file
OutputFile="/tmp/Output.dat"
# Tell php GolfClub.php that you are finish with learning
# so that he can delete te Input/ Otput files.
# This is done for timing
FinishFile="/tmp/WegDat.txt"
HowOldFile=0
#These are only swing data
SwingInputFile="/tmp/SwingInput.dat"
SwingOutputFile="/tmp/SwingOutput.dat"
Semaphore="/tmp/GolfSwing_Semaphore.lck"
learn=1000
ScaleAble=100000
while True:
    if os.path.isfile(Semaphore):
        os.remove(Semaphore)
    time.sleep(0.1)
    while (((os.path.isfile(InputFile)) & (os.path.isfile(OutputFile))) | ((os.path.isfile(SwingInputFile)) & (os.path.isfile(SwingOutputFile)))):
        if (ScaleAble > (os.path.getsize(InputFile))):
            learn = learn + 10
        else:
            learn = learn - 10
        if os.path.isfile(Semaphore):
            os.remove(Semaphore)
        time.sleep(0.1)
        file = open(Semaphore, "w")
        file.write("lock")
        file.close()
        time.sleep(1)
        if ((os.path.isfile(InputFile)) & (os.path.isfile(OutputFile))):
            if HowOldFile == os.stat(InputFile)[stat.ST_MTIME]:
                if ((os.path.isfile(InputFile)) & (os.path.isfile(OutputFile))):
                    if ((os.path.isfile(SwingInputFile)) & (os.path.isfile(SwingOutputFile))):
                        X = np.loadtxt(SwingInputFile)
                        y = (np.loadtxt(SwingOutputFile))
                        status="Learning old swing files"
                else:
                    X = np.loadtxt(InputFile)
                    y = (np.loadtxt(OutputFile))
                    status="Learning old files, no update"
                    HowOldFile=os.stat(InputFile)[stat.ST_MTIME]
            else:        
                X = np.loadtxt(InputFile)
                y = (np.loadtxt(OutputFile))
                status="Learing Live data"
                HowOldFile=os.stat(InputFile)[stat.ST_MTIME]
        else:
            X = np.loadtxt(SwingInputFile)
            y = (np.loadtxt(SwingOutputFile))
            status="Learning old swing files"

        file = open(FinishFile, "a")
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
        teller=0
        if os.path.isfile(Semaphore):
            os.remove(Semaphore)
        time.sleep(1)
        os.remove(FinishFile)
        while (teller < learn):
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
            print str(status)
            #print str((os.path.getsize(InputFile)))
            #print len(str(X))
        #print str(ScaleAble)
        print str(learn)
        #ScaleAble=(os.path.getsize(InputFile))
        np.save('./syn0', syn0)
        np.save('./syn1', syn1)
    time.sleep(0.1)

