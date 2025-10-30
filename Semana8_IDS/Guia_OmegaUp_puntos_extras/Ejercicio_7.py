"""Descripción
En sumalandia, tampoco saben siquiera saber de dos números cual es el mayor. Tu misión es hacer un 
programa que lea dos números enteros 
, 
 y devuelva el mayor.

Entrada
Se leeran dos números 
, 
.

Salida
Se imprimirá el entero con el mayor."""
one, two = map(int, input().split()) 

if one > two:
    print(one)
else:
    print(two)