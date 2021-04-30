import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from FuncionSeleccionPadres import selec_padres
from FuncionFitnes import fitness
from FuncionMutacion import mut_insercion


 # Genera la población
lista = [0, 1, 2, 3, 4, 5, 6, 7]  # son los valores en los que puede estar la reyna
poblacion = np.empty((50, 8))
for i in range(50):
    random.shuffle(lista)
    for j in range(8):
        poblacion[i, j] = lista[j]

padres =selec_padres(poblacion)
padre1 = padres[0]
padre2 = padres[1]

# SE cruza


#Aqui se muta


# aqui se reemplaza
hij1= mut_insercion(padre1)
hij2 = mut_insercion(padre2)



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
            plt.plot(x)  # Dibuja el gráfico
            plt.title("Mejor individuo")  # Establece el título del gráfico
            plt.xlabel("generaciones")  # Establece el título del eje x
            plt.ylabel("coliciones")  # Establece el título del eje y
            plt.plot(x)
            plt.show()
        return poblacion


gener_po(50)