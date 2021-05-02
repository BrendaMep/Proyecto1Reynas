import numpy as np
import random
import statistics


#funcion fitness
def fitness(individuo): # cada elemento de la poblacion
    conteo = 0
    for i in range(8):
        for j in range(i+1, 8):
            con1 = np.abs(individuo[i]- individuo[j])
            con2 = np.abs(i - j)
            if con1 == con2:
                conteo +=1
    return conteo


#funcion de aptitud , cada poblacion nos da el mejor

def aptitud(poblacion):
    lis_fit = ([])
    for i in range(50):
        lis_fit.append(fitness(poblacion[i,:]))
    lis_fit = sorted(lis_fit)
    print(lis_fit)
    mejor_ind = lis_fit[0]
    return mejor_ind

def peor(poblacion):
    lis_fit = ([])
    for i in range(50):
        lis_fit.append(fitness(poblacion[i, :]))
    lis_fit = sorted(lis_fit)
    peor_ind = lis_fit[49]
    return peor_ind

def promedio(poblacion):
    lis_fit = ([])
    for i in range(50):
        lis_fit.append(fitness(poblacion[i, :]))
    suma = 0
    for j in range(50):
        suma += lis_fit[j]
    prom = suma / 50
    return prom


def desviacion(poblacion):
    lis_fit = ([])
    for i in range(50):
        lis_fit.append(fitness(poblacion[i, :]))
    de = statistics.stdev(lis_fit)
    return de

