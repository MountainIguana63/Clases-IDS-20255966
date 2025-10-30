"""Descripción del Problema
Adrián realiza un prototipo de programa para determinar si una empresa tiene saldos positivos onegativos.

Él empieza formando las bases del código escribiendo un número y determinando si es positivo o negativo. Escribra un código querealice esta acción

Entrada
Recibirás un número entero 


Salida
Deberás mostrar "Positivo" en caso de que el número sea Positivo.

Deberás mostrar "Negativo" en caso de que el número sea Negativo."""

numero = int(input())

if numero >= 0:
    print("Positivo")
else:
    print("Negativo")