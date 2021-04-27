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
# aqui comienza la mutacion.

    if posicion1 < posicion2:
        for i in range(0, posicion1 + 1):  # los lugares que son <= posicion1 permanecen es su lugar
            matrix_zeros[0, i] = mutado[i]

        for i in range(posicion1 + 1, posicion1 + 2): # el concecutivo de posicion 1 es posicion2
            matrix_zeros[0, i] = mutado[posicion2]

        for i in range(posicion1 + 1, posicion2): # los x entre las 2 posiciones
            matrix_zeros[0, i + 1] = mutado[i]

        for i in range(posicion2 + 1, 8): # los que estan despues de posicion2 permanecen en su lugar
            matrix_zeros[0, i] = mutado[i]
        mutado = matrix_zeros
        return mutado
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
        mutado = matrix_zeros
    return mutado
