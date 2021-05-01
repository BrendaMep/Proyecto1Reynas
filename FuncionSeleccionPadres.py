import numpy as np
import random
from FuncionAptitud import fitness


lista = [0, 1, 2, 3, 4, 5, 6, 7] # son los valores en los que puede estar la reyna
poblacion = np.empty((50,8))
for i in range(50):
    random.shuffle(lista)
    for j in range(8):
        poblacion[i, j] = lista[j]

def padres(conjunto):
    r1 = random.random()
    r2 = random.random()
    Aptitud = ([])
    A_norm = ([])
    probabilidad = ([])
    prob_acomulada = ([])
    posibles_papas = ([])
    for i in range(50):
        Aptitud.append(fitness(conjunto[i, :]))   # contiene todos los ataques
    maximo = max(Aptitud)                         # es el que tiene mas ataques
    for i in range(50):
        A_norm.append(Aptitud[i]-maximo)
    suma = sum(A_norm)
    for i in range(50):
        probabilidad.append(A_norm[i]/ suma)   # probabilidad de cada individuo de la población
    prob_acomulada = probabilidad
    for i in range(1,50):
        prob_acomulada[i] = prob_acomulada[i] + prob_acomulada[i-1]
    for i in range(50):
        if prob_acomulada[i]>= r1:
            posibles_papas.append(conjunto[i])
    papa1 = posibles_papas[0]
    posibles_papas = ([])
    for i in range(50):
        if prob_acomulada[i]>= r2:
            posibles_papas.append(conjunto[i])
    papa2 = posibles_papas[0]
    return papa1,papa2


def selec_padres(poblacion):
    pob_padres = np.empty((100, 8))
    j =0
    while j in range(100):
        papas = padres(poblacion)
        pob_padres[j]= papas[0]
        pob_padres[j+1]= papas[1]
        j = j+2
    return pob_padres