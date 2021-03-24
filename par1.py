import numpy as np
import random

# Funcion de generacion de poblacion.

def posicion(x, y, z):   # marca en cual fila se encuentra una reyna
    reyna = np.zeros([1, 8, z])
    for n in range(0, z):
        for i in range(8):
            p = random.randrange(8)
            reyna[0, i, n] = p
    return reyna

poblacion = posicion(1,8,10)
print(poblacion[:,:,2])