import numpy as np
import random
from FuncionAptitud import fitness


# reemplazamiento elitismo

def reemplazamiento(num_generacion):
    pob_revuelta = poblacion
    po_hijos = pobl_hijos
    for i in range(50):
        pob_revuelta = np.append(pob_revuelta, [po_hijos[i,:]], axis=0) # contiene a la poblacion de padres e hijos
    lista_fitness = ([])
    lis_remover = np.empty((50,8))
    for i in range(100):
        lista_fitness.append(fitness(pob_revuelta[i,:]))
    lista_fitness = sorted(lista_fitness)
    for j in range(100):
        for i in range(50):
            if lista_fitness[i] == fitness(pob_revuelta[j, :]):
                lis_remover[i] = pob_revuelta[j]

    return lis_remover

