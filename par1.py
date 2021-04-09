import numpy as np
import random

# Funcion de generacion de poblacion.
lista = [0, 1, 2, 3, 4, 5, 6, 7] # son los valores en los que puede estar la reyna
poblacion = np.empty((50,8))
for i in range(50):
    random.shuffle(lista)
    for j in range(8):
        poblacion[i, j] = lista[j]


hijo1 = poblacion[36,:]
hijo2 = poblacion[12,:]

