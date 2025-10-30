"""Enunciado

Un dragón duerme sobre una cadena de letras. Para que no despierte, debes contar cuántas veces aparece 
la letra z en la cadena.

Entrada:

Una cadena de hasta 100 caracteres en minúsculas.
Salida:

Un número entero con la cantidad de letras z."""

cadena = str(input()).lower()
z = cadena.count("z")

print(z)
