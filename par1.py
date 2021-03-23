import numpy as np
import random

# Funcion de generacion de poblacion.

def poblacion(z):
    reynas = np.zeros([0, 8, z])
    for n in range(0, z):
        for m in range(0,8):
            posicion = random.randrange(8)
            reynas[0, m, n] = posicion
            print(reynas)
    return reynas

poblacion(8)
reynas = np.zeros([0, 8, 1])
print(reynas)

