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
        if current_element in tabla_extremos[i]:
            tabla_extremos[i].remove(current_element)
            if current_element in tabla_extremos[i]:
                tabla[i].remove(current_element)
    newtab_ext = tabla_extremos
    print(newtab_ext)

    for i in range(len(newtab_ext)):
        lista2 = ([])
        lista3 = ([])
        num = ([])
        if padre1[i] == current_element:
            cruza.append(current_element)
            for j in newtab_ext[i]:
                lista2.append(newtab_ext[j])
            print(lista2)
            m = set(lista2[0])
            for k in range(1,len(lista2)):
                n = set(lista2[k])
                m = intersect(m,n)
            if len(m) != 0:
                for x in m:
                    cruza.append(x)
                    lista.pop(x)
                    current_element = random.choice(lista)
            else:
                for k in range(len(lista2)):
                    num.append(len(lista2[k]))
                    minimo = min(num)
                    if minimo == len(lista2[k]):
                        lista3.append(lista2[k])
                        if len(lista3) != 1:
                             current_element = random.choice(lista)
                        else:
                            current_element = random.choice(lista2[k])
                print(num)
            newtab_ext.remove(newtab_ext[i])
            print(newtab_ext)
    return cruza







p1 = np.array([7,1,2,3,4,5,6,0])
p2 = np.array([1,4,3,7,0,2,6,5])
cruza_ext(p1,p2)

