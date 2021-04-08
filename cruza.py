# Cruza a los extremos.
import random
import numpy as np
ale_inicial = random.randrange(8)

def cruza_ext(p1,p2):
    for i in range(8):
        for j in range(8):
            if i in range(7) or j in range(8):
                if j in range(7):
                    if p1[i] == p2[j]:
                        elemen = np.array([p1[i - 1], p1[i + 1], p2[p1[j] - 1], p2[p1[j] + 1]])
                        print(elemen)
                if j == 7 and p1[i] == p2[j]:
                    elemen = np.array([p1[i - 1], p1[i + 1], p2[6], p2[0]])
                    print(elemen)
            if i == 7 and j in range(8):
                if p1[i] == p2[j]:
                    elemen = np.array([p1[6], p1[0], p2[p1[j] - 1], p2[p1[j] + 1]])
                    print(elemen)

p1 = np.array([0,1,2,3,4,5,6,7])
p2 = np.array([1,4,2,7,0,3,6,5])
cruza_ext(p1,p2)