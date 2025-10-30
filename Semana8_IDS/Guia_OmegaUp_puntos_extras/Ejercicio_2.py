"""Descripción
Leer un numero entero S y mostrar como salida el numero par posterior y el número impar anterior.

Entrada
Un número entero S.

Salida
El número par posterior y el número impar anterior al número entero leído."""

numero = int(input())

if numero % 2 == 0:
    print(numero+2)
    print(numero-1)
else:
    print(numero+1)
    print(numero-2)