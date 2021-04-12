# Cruza a los extremos.
import random
import numpy as np

def cruza_ext(padre1,padre2):
    elemen = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(8):
        if i in range(7):
            for j in range(8):
                if j in range(7) and padre1[i] == padre2[j]:
                    elemen[i] = [padre1[i - 1], padre1[i + 1], padre2[j - 1], padre2[j + 1]]
                    print(elemen)
                if j == 7 and padre1[i] == padre2[j]:
                    elemen[i] = [padre1[i - 1], padre1[i + 1], padre2[j - 1], padre2[0]]
                    print(elemen)
        else:
            for j in range(8):
                if j in range(7) and padre1[i] == padre2[j]:
                    elemen[i] = [padre1[6], padre1[0], padre2[j - 1], padre2[j + 1]]
                    print(elemen)
                if padre1[7] == padre2[7]:
                    elemen[i] = [padre1[6], padre1[0], padre2[6], padre2[0]]
                    print(elemen)


p1 = np.array([7,1,2,3,4,5,6,0])
p2 = np.array([1,4,3,7,0,2,6,5])
cruza_ext(p1,p2)