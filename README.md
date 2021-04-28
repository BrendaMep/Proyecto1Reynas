### Proyecto de reinas
En este proyecto se implementa un algoritmo genetico que deberia 
resolver el problema de 0 colisiones entre reinas en un tablero
de ajedrez. Este esta dividido por etapas, las cuales describiremos
detalladamente mas adelante.
![img_1.png](img_1.png)
Imagen de las reinas con 0 colisiones.

**Table of Contents**

[TOCM]

[TOC]

#Introduccion
Sabemos que los algoritmos geneticos son algoritmos de optimización
búsqueda y aprendizaje
inspirados en los procesos de evolución natural
y evolución genética.
---
 Apartir del problema de las cero coliciones de 8 reinas en un
tablero de ajedrez, se implemento un algoritmo
genetico con los procesos de generacion de poblacion,
seleccion de padres, cruza, mutacion y reemplazamiento
de la poblacion.
----
Acontinuacion se realizo un proceso de 
50 generaciones para observar la evolucion de los 
individuos, asi en cada generacion se 
escogieron los mejores individuos,
es decir los que tenian menos coliciones,
para observar la convergencia hacia el individuo ideal
de cero coliciones.

##Proyecto de reinas
![img_2.png](img_2.png)
## Generacion de la poblacion
Para iniciar se comenzo por crear una poblacion de
50 elementos los cuales solo nos representan la posicion
de la columna en la que se encuentran cada una
de las reinas, cada individuo esta representado 
como un vector que consta de 8 entradas, 
representadas con numeros de 0 a 7, sin repeticion
las cuales fueron generadas aleatoriamente.

##Seleccion de padres.
Para este algoritmo genetico se la seleccion 
de padres fue por medio de la ponderacion de 
aptitud, para ello se obtubo las coliciones
de cada individuo.
----
Una vez obtenidos todos se selecciono el maximo 
para poder obtener la normalizacion de cada uno
la cual esta dada por, la cantidad de coliciones que 
tiene menos el maximo de todas las coliciones, esto se 
necesita para poder obtener la probabilidad de ser
seleccionado y la probabilidad acomulada.
----
Despues se obtuvieron al azar dos numero r1 y r2, 
entre [0,1), para poder seleccionar los padres.

##Cruza
Para este algoritmo se utilizaria el metodo de cruza
de extremos, el cual consiste en:

-Crear una tabla de extremos

-Creamos un individuo vacio llamado cruza

-Se elige aleatoriamente un extremo que llamamos
curre_element y se le agrega a cruza

-Removemos el curre-.element de dotas las listas.

-Examinamos la lista que le corresponde a 
curre_element, dentro de este paso se realiza lo 
siguiente.

    -Si existe un elemento que pertenezca a los dos padres 
    seleccionamos a curre_element como ese elemento.
    -De otro modo de selecciona como curre_element
    la entrada con la lista mas pequeña
-

######H6 header