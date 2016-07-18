import numpy as np
from numpy import loadtxt
import sys
import os
import time

l2_error = 1

class File(file):
    def head(self, lines_2find=1):
        self.seek(0)                            #Rewind file
        return [self.next() for x in xrange(lines_2find)]

    def tail(self, lines_2find=1):  
        self.seek(0, 2)                         #go to end of file
        bytes_in_file = self.tell()             
        lines_found, total_bytes_scanned = 0, 0
        while (lines_2find+1 > lines_found and
               bytes_in_file > total_bytes_scanned): 
            byte_block = min(1024, bytes_in_file-total_bytes_scanned)
            self.seek(-(byte_block+total_bytes_scanned), 2)
            total_bytes_scanned += byte_block
            lines_found += self.read(1024).count('\n')
        self.seek(-total_bytes_scanned, 2)
        line_list = list(self.readlines())
        return line_list[-lines_2find:]

check=os.path.getmtime('./syn0.npy')
syn0=np.load('./syn0.npy')
syn1=np.load('./syn1.npy')

f=File('/tmp/Input.dat', 'r')
X = np.loadtxt(f.tail(1))

l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))


while True:
	f=File('/tmp/Input.dat', 'r')
	X = np.loadtxt(f.tail(1))
	X[6] = l2[0]

  	if check != os.path.getmtime('./syn0.npy'):
		syn0=np.load('./syn0.npy')
		syn1=np.load('./syn1.npy')
		print "Load data"

	l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
	l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
	#print str(l2[1])
	print "%0.5f %0.5f" % (((l2[0])), ((l2[1])))
#X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
#y = np.array([[0,1,1,0]]).T