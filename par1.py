import numpy as np
import random

# Funcion de generacion de poblacion.
lista = [0, 1, 2, 3, 4, 5, 6, 7] # son los valores en los que puede estar la reyna
poblacion = np.empty((50,8))
for i in range(50):
    random.shuffle(lista)
    for j in range(8):
        poblacion[i, j] = lista[j]

def fitness(individuo): # cada elemento de la poblacion
    conteo = 0
    for i in range(8):
        for j in range(i+1, 8):
            con1 = np.abs(individuo[i]- individuo[j])
            con2 = np.abs(i - j)
            if con1 == con2:
                conteo +=1
    return conteo


lista_ataques = ([]) #contiene los ataques de cada elemento de la poblacion
for i in range(50):
    lista_ataques.append(fitness(poblacion[i]))
print(lista_ataques)
print(len(lista_ataques))

