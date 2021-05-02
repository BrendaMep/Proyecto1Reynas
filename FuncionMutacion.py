import numpy as np
import random

lista = [0, 1, 2, 3, 4, 5, 6, 7] # son los valores en los que puede estar la reyna
poblacion = np.empty((50,8))
for i in range(50):
    random.shuffle(lista)
    for j in range(8):
        poblacion[i, j] = lista[j]
print(poblacion)


# mutacion por insercion
# mutacion por insercion
def muta_hijo(hijo):
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
        for i in range(posicion1+1, 8):
            matrix_zeros.append(mutado[i])
    mutado = matrix_zeros
    return mutado


def muta_insercion(poblacion):
    pob_muta = np.empty((50,8))
    for i in range(50):
        pob_muta[i,:] = muta_hijo(poblacion[i,:])
    print(pob_muta)
    return pob_muta
