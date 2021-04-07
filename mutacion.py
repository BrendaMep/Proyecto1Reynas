import numpy as  np
import random

# mutacion por insercion

def mut_insercion(hijo):
    mutado = hijo
    matrix_zeros = np.zeros((1,8))
    posicion1 = random.randrange(7) # nos dara el numero de una columna al azar.
    posicion2 = random.randrange(8)
    print(posicion1)
    print(posicion2)

    if posicion1 < posicion2:
        for i in range(0, posicion1 + 1):
            matrix_zeros[0, i] = mutado[i]
        for i in range(posicion1 + 1, posicion1 + 2):
            matrix_zeros[0, i] = mutado[posicion2]
        for i in range(posicion1 + 1, posicion2):
            matrix_zeros[0, i + 1] = mutado[i]
        for i in range(posicion2 + 1, 8):
            matrix_zeros[0, i] = mutado[i]
        hijo_mut = matrix_zeros
        print(hijo_mut)
    else:
        for i in range(0, posicion2):
            matrix_zeros[0, i] = mutado[i]
        for i in range(posicion1, posicion1 + 1):
            matrix_zeros[0, i] = mutado[i]
        for i in range(posicion1 + 1, 8):
            matrix_zeros[0, i] = mutado[i]
        for i in range(posicion1 + 1, posicion1 + 2):
            matrix_zeros[0, i] = mutado[posicion2]
        for i in range(posicion2 + 1, posicion1):
            matrix_zeros[0, i] = mutado[i]
        for i in range(posicion1 + 1, posicion1 + 2):
            matrix_zeros[0, posicion2] = mutado[i]
        hijo_mut = matrix_zeros
        print(hijo_mut)


m = np.array([0,1,2,3,4,5,6,7])
mut_insercion(m)
