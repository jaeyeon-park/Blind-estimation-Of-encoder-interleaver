# Implementation of Blind estimation of encoder and interleaver Characteristics
## Introduction
This code is implementation of blind estimation of encoder and interleaver characteristics.  
The purpose of this Implementation is to find out the coderate of encoder and period of interleaver.  

## Example
`example.py` shows how it works.
it uses hamming74 encoder and block interleaver that Each is implemented in `toyEncoder.py` and `toyInterleaver.py` to test.  

## How it works
Basic Idea is to reduce the rank of matrix that filled by unknown bitstream by syncing interleaving period.  

1. make matrix(called Z) which is filled by unknown bitstream. the size of matrix is n by m. (n = period, m > n).  
2. when n is the multiple of real interleaving period, the rank of Z is will be reduce radically. if we define rho as rank(z) over n, rho will be radically reduced. In other cases, rho will be maintained around 1.  
3. if we sync the first bit where interleaving start, rho is converged to coderate. (it will be minimum value.)  

- `estimtateInterleavingPeriod(bits,maxPeriod)` in `operation.py`  
: it checks rhos by making Z matrix in each period under maxPeriod.  
- `estimateCoderate(bits,period)` in `operation.py`  
: it find how many bits should be skipped to sync and coderate under assumption that period is real interleaving period.

## Reference
_Blind Estimation of Encoder and Interleaver Characteristics in a Non Cooperative Context_   
_(Gilles BUREL and Roland GAUTIER,2003)_  
(link : http://pagesperso.univ-brest.fr/~gburel/publis/Articles/post/2003_11_ciit_Interleaver.pdf)


