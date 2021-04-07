# Cruza a los extremos.
import random
import numpy as np
ale_inicial = random.randrange(8)

def cruza_ext(p1,p2):
    for i in range(8):
        if i in range(7):
            elemen = np.array([p1[i - 1], p1[i + 1], p2[p1[i] - 1], p2[p1[i] + 1]])
            print(elemen)
        else:
            elemen = np.array([p1[6], p1[0], p2[0], p2[0]])
            print(elemen)


p1 = np.array([0,1,2,3,4,5,6,7])
p2 = np.array([1,4,2,7,0,3,6,5])
cruza_ext(p1,p2)