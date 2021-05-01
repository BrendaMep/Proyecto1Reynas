import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from FuncionSeleccionPadres import selec_padres
from FuncionAptitud import fitness
from FuncionAptitud import aptitud
from FuncionMutacion import mut_insercion
from FuncionRemplazamiento import reemplazamiento



m_individuo = ([])   # va a contener el mejor individuo por genercion
p_individuo = ([])   # va a contener el peor individuo por generacion
ind_promedio = ([])  # va a contener el individuo promedio
des_estdar = ([])    # va a contener el  la desviacion estardar



# Genera la población
lista = [0, 1, 2, 3, 4, 5, 6, 7]  # son los valores en los que puede estar la reyna
poblacion = np.empty((50, 8))
for i in range(50):
    random.shuffle(lista)
    for j in range(8):
        poblacion[i, j] = lista[j]

mejor_ind = aptitud(poblacion)
m_individuo.append(mejor_ind)
print(mejor_ind)


padres = selec_padres(poblacion)   # se da la seleccion de padres
