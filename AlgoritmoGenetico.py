import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from FuncionSeleccionPadres import selec_padres
from FuncionAptitud import peor
from FuncionAptitud import aptitud
from FuncionMutacion import muta_insercion
from FuncionRemplazamiento import reemplazamiento
from FuncionAptitud import promedio
import statistics
from FuncionAptitud import desviacion



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


for k in range(50):
    padres = selec_padres(poblacion)   # se da la seleccion de padres
    #cruza
    pobl_hijos = muta_insercion()
    poblacion = reemplazamiento(k)

    mejor = aptitud(poblacion)
    m_individuo.append(mejor)
    no_bueno = peor(poblacion)
    p_individuo.append(no_bueno)
    media = promedio(poblacion)
    ind_promedio.append(media)
    pro_des = desviacion(poblacion)
    des_estdar.append(pro_des)


# tabla con los datos


