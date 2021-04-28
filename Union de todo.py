import random
import numpy as np
import pandas as pd


 # Genera la población
lista = [0, 1, 2, 3, 4, 5, 6, 7]  # son los valores en los que puede estar la reyna
poblacion = np.empty((50, 8))
for i in range(50):
    random.shuffle(lista)
    for j in range(8):
        poblacion[i, j] = lista[j]
#Seleccion de padres

def fitness(conjunto):
    conteo = 0
    for i in range(8):
        for j in range(i+1, 8):
            con1 = np.abs(conjunto[i]- conjunto[j])
            con2 = np.abs(i - j)
            if con1 == con2:
                conteo +=1
    return conteo

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
padres =selec_padres(poblacion)
padre1 = padres[0]
padre2 = padres[1]

#Aqui se muta

def mut_insercion(hijo):
    mutado = hijo
    matrix_zeros = ([])
    posicion1 = random.randrange(7) # nos dara el numero de una columna al azar.
    posicion2 = random.randrange(8)
    if posicion1 == posicion2:
        posicion1 = random.randrange(7)
    posicion1 = posicion1
            # aqui comienza la mutacion.
    if posicion1 < posicion2:
        for i in range(0,posicion1+1):
            matrix_zeros.append(mutado[i])
        for i in range(posicion2, posicion2+1):
            matrix_zeros.append(mutado[i])
        for i in range(posicion1+1,posicion2):
            matrix_zeros.append((mutado[i]))
        for i in range(posicion2+1,8):
            matrix_zeros.append(mutado[i])
    if posicion2 < posicion1:
        for i in range(0,posicion2):
            matrix_zeros.append(mutado[i])
        for i in range(posicion1,posicion1+1):
            matrix_zeros.append(mutado[i])
        for i in range(posicion2,posicion2+1):
            matrix_zeros.append(mutado[i])
        for i in range(posicion2+1,posicion1):
            matrix_zeros.append(mutado[i])
        for i  in range(posicion1+1, 8):
            matrix_zeros.append(mutado[i])
    mutado = matrix_zeros
    return mutado

# aqui se reemplaza

def reemplazamiento(num_generacion):
    hijo1 = mut_insercion(padre1)
    hijo2 = mut_insercion(padre2)
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


def gener_po(num_generacion):
    lista = [0, 1, 2, 3, 4, 5, 6, 7]  # son los valores en los que puede estar la reyna
    poblacion = np.empty((50, 8))
    for i in range(50):
        random.shuffle(lista)
        for j in range(8):
            poblacion[i, j] = lista[j]
        for n in range(num_generacion):
            lista_fitness = ([])
            suma = 0
            for k in range(50):
                lista_fitness.append(fitness(poblacion[k, :]))
            maximo = max(lista_fitness)
            minimo = min(lista_fitness)
            for j in range(50):
                suma += lista_fitness[j]
            promedio = suma // 50
            x = ([])
            p = ([])
            r = ([])
            for m in range(50):
                if lista_fitness[maximo] == fitness(poblacion[m, :]):
                    x.append(poblacion[m, :])
                if lista_fitness[minimo] == fitness(poblacion[m, :]):
                    p.append(poblacion[m, :])
                if lista_fitness[promedio] == fitness((poblacion[m, :])):
                    r.append(poblacion[m, :])
            # print("Mejor individuo", p[0], lista_fitness[minimo], "Peor individuo", x[0], lista_fitness[maximo],
            #     "Individuo promedio", r[0], promedio)
            tabla1 = pd.DataFrame({'Mejor individuo': [p[0]], 'Peor individuo': [x[0]]})
            print(tabla1)
            tabla2 = pd.DataFrame({'min coliciones': [lista_fitness[minimo]], 'max coliciones': [lista_fitness[maximo]],
                                   'coliciones promedio': [promedio]})
            print(tabla2)
            poblacion = reemplazamiento(n)
        return poblacion


gener_po(50)