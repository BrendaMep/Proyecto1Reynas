import numpy as np
import random
#funcion fitness

lista = [0, 1, 2, 3, 4, 5, 6, 7] # son los valores en los que puede estar la reyna
poblacion = np.empty((50,8))
for i in range(50):
    random.shuffle(lista)
    for j in range(8):
        poblacion[i, j] = lista[j]
    print(poblacion[i,:])

def fitness(poblacion):
    conteo = 0
    for i in range(8):
        for j in range(i+1, 8):
            con1 = np.abs(poblacion[i]- poblacion[j])
            con2 = np.abs(i - j)
            if con1 == con2:
                conteo +=1
    return conteo

Aptitud = ([])
for i in range(50):
    Aptitud.append(fitness(poblacion[i,:]))
maximo = max(Aptitud)
print(maximo)
