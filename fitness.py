import numpy as np
import random
#funcion fitness

def fitness(poblacion):
    conteo = 0
    for i in range(8):
        for j in range(i+1, 8):
            con1 = np.abs(poblacion[i]- poblacion[j])
            con2 = np.abs(i - j)
            if con1 == con2:
                conteo +=1
    return conteo
