import numpy as  np
import random

# mutacion por insercion

def mut_insercion(hijo):
    mutado = hijo
    matrix_zeros = np.zeros((1,8))
    posicion1 = random.randrange(7) # nos dara el numero de una columna al azar.
    posicion2 = random.randrange(8)

    if posicion2 == posicion1:
        posicion2 = random.randrange(8)

    minimo = min(posicion1, posicion2)
    maximo = max(posicion1, posicion2)
    if minimo == posicion2:
        for i in range(0, minimo):
            matrix_zeros[0, i] = mutado[i]
        print(matrix_zeros[:,:])
        for i in range(minimo+1, posicion1):
            matrix_zeros[0, i] = mutado[i]

    else:
        for i in range(0, minimo+1):
            matrix_zeros[0, i] = mutado[i]
        if i == posicion2 :
            matrix_zeros[0,minimo+1] = mutado[posicion2]
        for i in range(minimo+1,posicion2):
            matrix_zeros[0,i] = mutado[posicion1+i]
        for i in range(posicion2,8):
            matrix_zeros[0, i ] = mutado[i]
        print(matrix_zeros[:, :])


m = np.array([0,1,2,3,4,5,6,7])
mut_insercion(m)