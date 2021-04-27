import numpy as np
import random

# seleccion de padres
def selec_padres(conjunto):
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


selec_padres(poblacion)

