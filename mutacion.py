import numpy as  np
import random

# mutacion por insercion

def mut_insercion(hijo):
    mutado = hijo
    matrix_zeros = np.zeros((1,8))
    posicion1 = random.randrange(8) # nos dara el numero de una columna al azar.
    posicion2 = random.randrange(8)


