
from fractions import Fraction as Fr
from decimal import *
import math
pi = Decimal('3.141592653589793238462643383279502884197169399375105820974944592307816406286')

def factorial(Z):
    if Z == 0:
        return 1
    return Z*factorial(Z-1)

print(Fr(2*(4)*factorial(4)/ Decimal((2*pi)**4)))

'''
def bernoulli_number(n):
    if(n == 1):
        return Fr(-1, 2)
    A = [0]*(n+1)
    for x in range(n+1):
        A[x] = Fr(1, 1+x)
        for j in range(x,0,-1):
            A[j-1] = j*(A[j-1] - A[j])
    return A[0]

print(bernoulli_number(2))
'''


