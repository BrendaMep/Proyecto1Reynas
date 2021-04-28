### Proyecto de reinas
En este proyecto se implementa un algoritmo genetico que deberia 
resolver el problema de 0 colisiones entre reinas en un tablero
de ajedrez. Este esta dividido por etapas, las cuales describiremos
detalladamente mas adelante.

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
la cual esta dada por:
-
$$E=mc^2$$





#####H5 header
######H6 header