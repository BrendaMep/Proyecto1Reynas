import random
import numpy as np


def intersect(a, b):
    return list(set(a) & set(b))

def cruza_ext(padre1,padre2):
    # construccion de tabla de extremos
    tabla = ([[0],[1],[2],[3],[4],[5],[6],[7]])
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
    lista = ([0, 1, 2, 3, 4, 5, 6, 7])
    current_element = random.choice(lista)
    print(current_element)
    cruza = []
    cruza.append(current_element)
    for i in range(8):
        lista2 = ([])
        lista3 = ([])
        num = ([])
        if current_element in tabla_extremos[i]:
            tabla_extremos[i].remove(current_element)
            if current_element in tabla_extremos[i]:
                tabla[i].remove(current_element)
        newtab_ext = tabla_extremos
        print(newtab_ext)
        for j in range(len(lista)):
            rep_elem = ([])  # lista que tiene las repeticiones de la lista de los extremos de curre_element
            for k in range(8):
                if current_element == padre1[k]:
                    #print(newtab_ext[k])
                    for x in newtab_ext[k]:
                        rep_elem.append(newtab_ext[k].count(x))
                        maximo = max(rep_elem)
                        #print(maximo)
                        if 1 < maximo:
                            for m in range(8):
                                if maximo == newtab_ext[k].count(x):
                                    cruza.append(x)
                                    current_element = x
                        else:
                            current_element = random.choice(lista)

                            #for k in range(len(lista2)):
                             #   num.append(len(lista2[k]))
                              #  minimo = min(num)
                               # if minimo == len(lista2[k]):
                                #    lista3.append(lista2[k])
                                 #   if len(lista3) != 1:
                                  #       current_element = random.choice(lista)
                                   # else:
                                    #   current_element = random.choice(lista)
                 #print(num)


        print(cruza)
    return cruza







p1 = np.array([7,1,2,3,4,5,6,0])
p2 = np.array([1,4,3,7,0,2,6,5])
cruza_ext(p1,p2)

