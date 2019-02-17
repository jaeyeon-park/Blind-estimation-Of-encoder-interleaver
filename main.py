from bitstring import Bits, BitArray
from fractions import Fraction
import toyInterleaver as interleaver
import toyEncoder as enc
import matrixOp as mop
import numpy as np

def analyzePeriod(bits,maxPeriod):
	result = []
	for row in range(1,maxPeriod):
		if row*(row+1) > len(bits) : 
			print("bits shortage to generate {} by {} matrix".format(row,row+1))
			break
		testMat = mop.generateMat(bits,row,row+1)
		rank = mop.gaussianElimination(testMat)
		if rank == 0 :return result
		rho = Fraction(rank,row)
		approximation = round(float(rho),3)
		result.append((row,rank,rho))
		print("interleaver period:{} / rank:{} / rho:{}({})".format(row,rank,rho,approximation))
	return result

def main():
	h74 = enc.hamming74()
	bits = h74.generateBlocks(2000) #it means 100 blocks. (7bits/1block) -> generate 700bits
	imatrix = interleaver.generateBlockInteleavingMat(7,2)
	interleavedBits = interleaver.interleave(bits,imatrix)
	result = analyzePeriod(bits,100)
	
if __name__ == "__main__":
	main()