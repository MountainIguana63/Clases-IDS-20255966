"""Descripción
David hace poco descubrió un videojuego bastante interesante, lo instaló y empezó a practicarlo mucho, 
tanto que se hizo un profesional, sin embargo, a pesar de que sabe que sus combos siempre hacen daño, 
quiere saber cuánto hacen exactamente. Cada combo consta de presionar 6 veces los botones de ataque 
A, B y/o C
 (pueden ser combinados, no necesariamente tiene que ser siempre el mismo durante el combo, o sea, 
 puede ser tanto AABCAB como AAAAAA). Cada botón hace un daño diferente.

Entrada
Un entero N
 con la cantidad de combos que ejecutó David, seguido de enteros 
 que son la cantidad de daño de los ataques 
 y 
. Después 
 líneas con los combos de David.

Salida
El daño de cada combo de David."""

combosN = int(input()) 
dañoA, dañoB, dañoC = map(int, input().split()) 

resultados = [] 

for _ in range(combosN):
    combo = input().strip()
    daño_total = 0

    for letra in combo:
        if letra == "A":
            daño_total += dañoA
        elif letra == "B":
            daño_total += dañoB
        elif letra == "C":
            daño_total += dañoC

    resultados.append(daño_total)


for daño in resultados:
    print(daño)

