import numpy as np
import random

def gener_po(num_generacion):
    lista = [0, 1, 2, 3, 4, 5, 6, 7]  # son los valores en los que puede estar la reyna
    poblacion = np.empty((50, 8))
    for i in range(50):
        random.shuffle(lista)
        for j in range(8):
            poblacion[i, j] = lista[j]
        for n in range(num_generacion):
            lista_fitness = ([])
            suma = 0
            for k in range(50):
                lista_fitness.append(fitness(poblacion[k, :]))
            maximo = max(lista_fitness)
            minimo = min(lista_fitness)
            for j in range(50):
                suma += lista_fitness[j]
            promedio = suma // 50
            x = ([])
            p = ([])
            r = ([])
            for m in range(50):
                if lista_fitness[maximo] == fitness(poblacion[m, :]):
                    x.append(poblacion[m, :])
                if lista_fitness[minimo] == fitness(poblacion[m, :]):
                    p.append(poblacion[m, :])
                if lista_fitness[promedio] == fitness((poblacion[m, :])):
                    r.append(poblacion[m, :])
            # print("Mejor individuo", p[0], lista_fitness[minimo], "Peor individuo", x[0], lista_fitness[maximo],
            #     "Individuo promedio", r[0], promedio)
            tabla1 = pd.DataFrame({'Mejor individuo': [p[0]], 'Peor individuo': [x[0]]})
            print(tabla1)
            tabla2 = pd.DataFrame({'min coliciones': [lista_fitness[minimo]], 'max coliciones': [lista_fitness[maximo]],
                                   'coliciones promedio': [promedio]})
            print(tabla2)
            poblacion = reemplazamiento(n)
            plt.plot(x)  # Dibuja el gráfico
            plt.title("Mejor individuo")  # Establece el título del gráfico
            plt.xlabel("generaciones")  # Establece el título del eje x
            plt.ylabel("coliciones")  # Establece el título del eje y
            plt.plot(x)
            plt.show()
        return poblacion


gener_po(50)
