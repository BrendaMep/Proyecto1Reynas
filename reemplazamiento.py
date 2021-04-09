import numpy as np
import random
# reemplazamiento elitismo
def reemplazamiento(hijo1, hijo2):
    poblacion = np.empty((50, 8))
    rein=np.array([6,2,7,1,4,0,5,3]) # es la reina con cero ataques
    count1 = 0
    count2 = 0
    for i in range(8):
        if hijo1[i] == rein[i]:
            count1 += 1
        if hijo2[i] == rein[i]:
            count2 +=1

    maximo = max(count1,count2)
