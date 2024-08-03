import numpy as np

'''
Aqui, encaremos o fato que, os arrays são matrizes e, como tais, as operações usuais com matrizes se encaixam nos arrays.

'''

m1 =  np.array([[1.,2.,3.],[4.,5.,6.]]) # matriz 2x3

m2 = m1**2 # Essencialmente, m1*m1
print(m2)

m3 = m2 - m1

print(m3)

m4 = 3*m3
print(m4)