import numpy as np
import random
#funcion fitness

def fitness(individuo): # cada elemento de la poblacion
    conteo = 0
    for i in range(8):
        for j in range(i+1, 8):
            con1 = np.abs(individuo[i]- individuo[j])
            con2 = np.abs(i - j)
            if con1 == con2:
                conteo +=1
    return conteo
