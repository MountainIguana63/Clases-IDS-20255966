"""Hay un estreno en el cine, la cola para entrar es larga, el dueño quiere saber cuantos van entrar porque 
la pelicula es clasificación B15 que no es recomendada para menores de 15 años. Apoya al dueño creando un 
programa que determine la cantidad que ingresaron a ver la pelicula.

Entrada
Una variable entera A que representa la cantidad de personas que hay en la fila y las edades de cada una de 
las personas de la fila.

Salida
Un valor entero que representa la cantidad de personas que ingresaron a la sala a ver la pelicula."""

fila = int(input())
lista = []
pasan = 0
for personas in range(fila):
    n = int(input())
    lista.append(n)
for pelones in lista:
    if pelones >= 15:
        pasan = pasan + 1
print(pasan)