import numpy as np
import random
# reemplazamiento elitismo
lista = [0, 1, 2, 3, 4, 5, 6, 7] # son los valores en los que puede estar la reyna
poblacion = np.empty((50,8))
for i in range(50):
    random.shuffle(lista)
    for j in range(8):
        poblacion[i, j] = lista[j]


def fitness(conjunto):
    conteo = 0
    for i in range(8):
        for j in range(i+1, 8):
            con1 = np.abs(conjunto[i]- conjunto[j])
            con2 = np.abs(i - j)
            if con1 == con2:
                conteo +=1
    return conteo

hij1 = ([0,1,2,3,7,6,5,4])
hij2 = ([7,4,1,0,5,2,6,3])
print(len(hij1))

def reemplazamiento(hijo1, hijo2):
    nueva_pobl = poblacion
    pob_revuelta = np.append(nueva_pobl, [hijo1], axis=0)
    pob_revuelta = np.append(pob_revuelta, [hijo2], axis=0)
    lista_fitness = ([])
    lis_remover = ([])
    lista = ([])
    for i in range(52):
        lista_fitness.append(fitness(pob_revuelta[i,:]))
    lista_fitness = sorted(lista_fitness)
    for i in range(50,52):
        for j in range(52):
            if lista_fitness[i] == fitness(pob_revuelta[j, :]):
                lis_remover.append(pob_revuelta[j,:])
                lista.append(j)
    nueva_pobl = pob_revuelta
    pob_revuelta = np.delete(nueva_pobl, lista[0], axis=0)
    pob_revuelta = np.delete(pob_revuelta, lista[1], axis=0)
    nueva_pobl = pob_revuelta
    return nueva_pobl

m = reemplazamiento(hij1, hij2)
print(m)
