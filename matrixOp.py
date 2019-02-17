from bitstring import Bits, BitArray
import numpy as np
def gaussianElimination(mat):
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

def generateMat(bits,rows,cols):
	mat = np.array([bits[rows*i:rows*(i+1)] for i in range(0,cols)])
	return mat.transpose()
