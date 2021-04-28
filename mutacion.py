import numpy as  np
import random

# mutacion por insercion

def mut_insercion(hijo):
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
        for i  in range(posicion1+1, 8):
            matrix_zeros.append(mutado[i])
    mutado = matrix_zeros
    return mutado