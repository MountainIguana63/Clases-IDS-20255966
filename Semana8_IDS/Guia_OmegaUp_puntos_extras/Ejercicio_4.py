"""Descripción
En el siguiente problema recibirá una lista de números y tu tarea será contar cuantos números son 7 y cuantos 
números son 5

Entrada
Un numero entero N que indica cuantos números serán ingresados, seguido de la lista de N números

Salida
Dos números enteros indicando cuantos números son 7 y cuantos números son 5, el primer número indica cuantos 7 
hay y el segundo número indica cuantos 5 hay"""

numeros_a_ingresar = int(input())
seven = 0
five = 0
for n in range(numeros_a_ingresar):
    numero = int(input())
    if numero == 7:
        seven += 1
    elif numero == 5:
        five += 1
print(seven, five)