# Cruza a los extremos.
import random
import numpy as np


def cruza_ext(padre1, padre2):
    tabla = [[0], [1], [2], [3], [4], [5], [6], [7]]
    for i in range(8):
        if i in range(7):
            for j in range(8):
                if j in range(7) and padre1[i] == padre2[j]:
                    tabla[i] = [padre1[i - 1], padre1[i + 1], padre2[j - 1], padre2[j + 1]]

                if j == 7 and padre1[i] == padre2[j]:
                    tabla[i] = [padre1[i - 1], padre1[i + 1], padre2[j - 1], padre2[0]]
        else:
            for j in range(8):
                if j in range(7) and padre1[i] == padre2[j]:
                    tabla[i] = [padre1[6], padre1[0], padre2[j - 1], padre2[j + 1]]

                if padre1[7] == padre2[7]:
                    tabla[i] = [padre1[6], padre1[0], padre2[6], padre2[0]]

    tabla_extremos = tabla
    print(tabla_extremos)
    current_element = random.randrange(8)
    print(current_element)
    cruza = []
    remover = [[0], [1], [2], [3], [4], [5], [6], [7]]
    for i in range(8):
        remover[i] = list(tabla_extremos[i])
        if current_element in remover[i]:
            remover[i].remove(current_element)
            if current_element in remover[i]:
                remover[i].remove(current_element)
        if padre1[i] == current_element:
            print(tabla_extremos[i])
            cruza.append(current_element)
            print(cruza)
            for padre1[i] in tabla_extremos[i]:
                print(remover[padre1[i]])


p1 = np.array([7,1,2,3,4,5,6,0])
p2 = np.array([1,4,3,7,0,2,6,5])
cruza_ext(p1,p2)
