# Cruza a los extremos.
import random
import numpy as np
ale_inicial = random.randrange(8)

def cruza_ext(p1,p2):
    matrix_zeros = np.zeros(2,4)

p1 = np.array([0,1,2,3,4,5,6,7])
p2 = np.array([1,4,2,7,0,3,6,5])
for i in range(8):
    elemen = np.array([p1[i-1], p1[i+1],p2[i-1],p2[i+1]])
    print(elemen)
