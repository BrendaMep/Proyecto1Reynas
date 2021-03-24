import numpy as np
import random

def posicion(x, y, z):   # marca en cual fila se encuentra una reyna
    reyna = np.zeros([1, 8, z])
    for n in range(0, z):
        ls_res = [ p = random.randrange(y)  reyna[x-1, i, n] = p]

        for i in range(y):
            p = random.randrange(y)
            reyna[x-1, i, n] = p
    return reyna




poblacion = posicion(1,8,10)
print(poblacion[:,:,2])