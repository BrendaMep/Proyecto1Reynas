import numpy as np
import random
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
    mejor_ind = lis_fit[0]
    return mejor_ind



