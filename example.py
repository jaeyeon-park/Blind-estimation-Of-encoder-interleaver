from bitstring import Bits, BitArray
import toyInterleaver as interleaver
import toyEncoder as enc
import operation as op
import math

(PERIOD_IDX,RANK_IDX,RHO_IDX) = (0,1,2)

def main():
	print(
		"""
----Blind estimation of block Interleaver Period and coderate (k/n)----
This code is example to show how to run it
In this code, Hamming 74 block code and random pkg of python is used to generate codewords
		""")
	numOfBlocks = int(input("number of blocks to generate bits (7bits/1block) : "))
	maxPeriod = int(input("max interleaving period to test : "))
	h74 = enc.hamming74()
	bits = h74.generateBlocks(numOfBlocks)
	imatrix = interleaver.generateBlockInteleavingMat(7,2)	# interleaving period is multiple of codeword length 7
	interleavedBits = interleaver.interleave(bits,imatrix)
	periodCandidates = op.estimateInterleavingPeriod(bits,maxPeriod)
	coderateCandidates = op.estimateCoderate(bits,14)	# '14' can be found by function - estimationInterleavingPeriod
	

if __name__ == "__main__":
	main()