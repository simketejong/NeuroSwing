import numpy as np
from numpy import loadtxt
import sys
import os
import stat, time

l2_error = 1
maxL0 = 0
maxL1 = 0
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

syn0=np.load('./syn0.npy')
syn1=np.load('./syn1.npy')

HowOldFile=os.stat("./syn1.npy")[stat.ST_MTIME]
vorige=0
HowOldDataFile=0
while True:
	while ((os.path.isfile("/tmp/Test_Input.dat")) & (os.stat("/tmp/Test_Input.dat")[stat.ST_MTIME] > HowOldDataFile)):
		HowOldDataFile=os.stat("/tmp/Test_Input.dat")[stat.ST_MTIME]
		f=File('/tmp/Test_Input.dat', 'r')
	#	X = np.loadtxt(f.tail(1))
		X = np.loadtxt(f)
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
			print str(HowOldDataFile)	
			print "%f %f %f %f" % (((l2[0])), ((l2[1])), maxL0 , maxL1)
#X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
#y = np.array([[0,1,1,0]]).T