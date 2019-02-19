from bitstring import Bits, BitArray
from fractions import Fraction
import numpy as np

# matrix Operation 
def generateMat(bits,rows,cols):
	mat = np.array([bits[rows*i:rows*(i+1)] for i in range(0,cols)])
	return mat.transpose()

def gaussianElimination(mat):	#It modifies matrix variable of outside scope
	(rows, cols) = mat.shape
	rank = 0
	for col in range(0,cols):
		for row in range(col,rows):
			if mat[row][col] == True:
				rank +=1
				tmp = np.copy(mat[col])
				mat[col] = mat[row]
				mat[row] = tmp
				for belowRow in range(col+1,rows):
					if mat[belowRow][col]==True: mat[belowRow] ^= mat[col]
				break
	return rank

# Estimation of Interleaving Period and Coderate
def estimateInterleavingPeriod(bits,maxPeriod):
	result = []
	for row in range(1,maxPeriod):
		if row*(row+1) > len(bits) : 
			print("bits shortage to generate {} by {} matrix".format(row,row+1))
			break
		testMat = generateMat(bits,row,row+1)
		rank = gaussianElimination(testMat)
		if rank == 0 :return result
		rho = Fraction(rank,row)
		approximation = round(float(rho),3)
		result.append((row,rank,rho))
		print("interleaving period(estimation):{} / rank:{} / rho:{}({})".format(row,rank,rho,approximation))
	return result

def estimateCoderate(bits,period):
	result = []
	print("Estimated Interleaving period:{}".format(period))
	for shift in range(0,period):
		mat = generateMat(bits[shift:],period,period+1)
		rank = gaussianElimination(mat)
		rho = Fraction(rank,period)
		approximation = round(float(rho),3)
		result.append((shift,rank,rho))
		print("shift:{} / rank:{} / coderate(estimation):{} {}".format(shift, rank, rho, approximation))
	return result