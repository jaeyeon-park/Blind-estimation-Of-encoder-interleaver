from bitstring import Bits, BitArray
from toyEncoder import hamming74
from fractions import Fraction
import toyInterleaver as interleaver
import numpy as np

def gaussianElimination(mat):
	try:
		(rows, cols) = mat.shape
		rank = 0
		for col in range(0,cols):
			for row in range(0,rows):
				if col > row : break
				if mat[row][col] == True:
					rank +=1
					tmp = np.copy(mat[col])
					mat[col] = mat[row]
					mat[row] = tmp
					for belowRow in range(col+1,rows):
						if mat[belowRow][col] == True:
							mat[belowRow] ^= mat[row]
					break
		return rank
	except:
		print("shrotage bits")
		return 0

def generateMat(bits,rows,cols):
	mat = np.array([bits[rows*i:rows*(i+1)] for i in range(0,cols)])
	return mat.transpose()

def analyzePeriod(bits,maxPeriod):
	result = []
	for row in range(1,maxPeriod):
		mat = generateMat(bits,row,row+1)
		print(mat)
		rank = gaussianElimination(mat)
		if rank == 0 :return result
		rho = Fraction(rank,row)
		approximation = round(float(rho),3)
		result.append((row,rank,rho))
		print("interleaver period:{} / rank:{} / rho:{}({})".format(row,rank,rho,approximation))
	return result

def test():
	h74 = hamming74()
	bits = h74.generateRandBits(2000)
	mat = interleaver.generateBlockInteleavingMat(7,2)
	interleavedBits = interleaver.interleave(bits,mat)
	result = analyzePeriod(bits,100)

def main():
	h74 = hamming74()
	bits = h74.generateRandBits(2)
	mat = interleaver.generateBlockInteleavingMat(7,2)
	res = interleaver.interleave(bits,mat)
	print(mat)
	print(bits)
	print(res)
	
	
	



if __name__ == "__main__":
	#main()
	test()