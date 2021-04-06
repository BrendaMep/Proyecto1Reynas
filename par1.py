import numpy as np
import random

# Funcion de generacion de poblacion.

def posicion(x, y, z):   # marca en cual columna se encuentra una reyna
    reyna = np.zeros((x, y, z))
    for n in range(0, z):
        for i in range(y):
            columna = random.choice(range(y))   #nos da una columna aleatoria en la que encontrara la reina
            reyna[x-1, i, n] = columna  # i es la fila y columna la posicion de la reina
    return reyna

posicion(1, 8, 50)
poblacion = posicion(1,8,50)
print(poblacion[:,:,34])
#Funcion seleccion de padres metodo Sobrante estocastico
