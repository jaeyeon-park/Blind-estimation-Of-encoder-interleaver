from bitstring import Bits,BitArray
import random

class Enc():
	def __init__(self):
		self.msg=None
	def generateRandBits(self,n):
		bits = '0b'+''.join([str(random.randrange(0,2)) for i in range(0,n)])
		return Bits(bits)
	
class blockEnc(Enc):
	def __init__(self, n,k):
		Enc.__init__(self)
		self.n = n
		self.k = k
	def generateRandBits(self):
		return Enc.generateRandBits(self,self.k)

class hamming74(blockEnc):
	def __init__(self):
		blockEnc.__init__(self,7,4)
	def generateRandBits(self,count):
		bits = BitArray()
		for i in range(0,count):
			msg = blockEnc.generateRandBits(self)
			bits.append(self.addParity(msg))
		return bits
	def addParity(self,bits):
		p1 = str(self.__getParity(bits,[0,1,2]))
		p2 = str(self.__getParity(bits,[1,2,3]))
		p3 = str(self.__getParity(bits,[0,2,3]))
		return Bits('0b'+bits.bin+p1+p2+p3)
	def __getParity(self,bits,indices):
		parity = indices[0]
		for i in indices[1:]:
			parity ^= bits[i]
		return parity