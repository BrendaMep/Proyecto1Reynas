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

-1.Crear una tabla de extremos

-2.Creamos un individuo vacio llamado cruza

-3.Se elige aleatoriamente un extremo que llamamos
curre_element y se le agrega a cruza

-4.Removemos el curre-.element de dotas las listas.

-5.Examinamos la lista que le corresponde a 
curre_element, dentro de este paso se realiza lo 
siguiente.

    -Si existe un elemento que pertenezca a los dos padres 
    seleccionamos a curre_element como ese elemento.
    -De otro modo de selecciona como curre_element
    la entrada con la lista mas pequeña
    -Se selecciona como curre_element un numero 
    aleatorio (3)
    -Terminamos al encontrar un curre_element en 
    una lista vacia y el tamaño del hijo es 8 
Para esta parte se tuvo algunos problemas, crei que
podia resolverlos yo sola y no fue asi :(

##Mutacion.
En esta etapa se utilizo la mutacion por insercion
Una inserción es un tipo de mutación que implica 
la adición de material genético. Una mutación 
por inserción puede ser pequeña e involucrar 
un único par de bases de ADN, o grande e 
involucrar un fragmento de un cromosoma.
----
Se mencionara los pasos que se realizaron:

    -1 Seleccionar al azar dos posiciones del hijo
    que vamos a mutar, posicion1 y posicion2.

    -2 Se crea un vector vacio, en cual se le van
    a ir agregando los elementos del hijo a mutar

    -3 Para todos los elementos que esten antes o iguales que
    la posicion1 se agregan a al cevtor vacio.
    
    -4 Al vector vacio se le agrega el elemento de
    posicion2

    -5 Si existen elementos entre posicion1 y posicion2
    se agragan

    -6 Por ultimo se agregan los elemenos que estan despues
    de posicion2.

## Remplazamiento
Para el remplazamiento se utilizo el metodo 
de Elitismo, se creo una nueva poblacion que 
constaba de 52 elementos, despues se ordenaron
de menor a mayor  de acuerdo a las colisiones que tuviera 
cada elemento de la nueva poblacion.
---
Una vez ordenados de forma creciente, solo se seleccionan
los primeros 50 elementos , dejando asi los peores elementos
de la nueva poblacion.
---------------
Al estar realizando este reemplazamiento, nos garantiza
que la convergencia al individuo ideal sea mas rapido, 
ya que siempre nos quedamos con solos los individuos que 
tienen menor colisiones.
