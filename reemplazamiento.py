import numpy as np
import random
# reemplazamiento elitismo
lista = [0, 1, 2, 3, 4, 5, 6, 7] # son los valores en los que puede estar la reyna
poblacion = np.empty((50,8))
for i in range(50):
    random.shuffle(lista)
    for j in range(8):
        poblacion[i, j] = lista[j]
print(poblacion)

def reemplazamiento(hijo1, hijo2):
    rein=np.array([6,2,7,1,4,0,5,3]) # es la reina con cero ataques
    count1 = 0
    count2 = 0
    for i in range(8):
        if hijo1[i] == rein[i]:
            count1 += 1
        if hijo2[i] == rein[i]:
            count2 +=1

    maximo = max(count1,count2)
    if maximo == count1:
        cambio = random.randrange(50)
        print(cambio)
        poblacion[cambio,:]= hijo1
    else:
        cambio = random.randrange(50)
        poblacion[cambio,:] = hijo2
        print(cambio)

hijo1= [0,1,2,3,4,5,6,7]
hijo2= [6,2,7,1,3,5,4,0]
reemplazamiento(hijo1,hijo2)
print(poblacion)
