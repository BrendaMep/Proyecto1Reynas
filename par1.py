import numpy as np
import random

# Funcion de generacion de poblacion.

def posicion(x, y, z):   # marca en cual fila se encuentra una reyna
    reyna = np.zeros([x, y, z])
    for n in range(0, z):
        for i in range(y):
            columna = random.randrange(y)   #nos dice en cual columna se encuentra
            reyna[x-1, i, n] = columna
    return reyna

posicion(1, 8, 50)
poblacion = posicion(1,8,50)

