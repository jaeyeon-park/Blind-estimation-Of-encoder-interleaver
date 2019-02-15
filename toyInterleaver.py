from bitstring import Bits, BitArray
import random

def generateBlockInteleavingMat(rows,cols):
	mat=[]
	for col in range(0,cols):
		for row in range(0,rows):
			mat.append( cols*row + col )	
	return mat
	

def generateRandMat(rows,cols):
	upper = rows*cols-1
	[random.randrange(0,upper) for i in range(0,rows*cols)]
	
def interleave(bits,permutationMat):
	def unitInterleave(bits):
		return Bits([bits[idx] for idx in permutationMat])
	res = BitArray()
	pos = 0
	lenOfMat = len(permutationMat)
	while(len(bits)>=pos+lenOfMat):
		res.append(unitInterleave(bits[pos:pos+lenOfMat]))
		pos += lenOfMat
	return res
	
		
