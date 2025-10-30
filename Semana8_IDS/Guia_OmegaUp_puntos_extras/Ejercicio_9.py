"""Descripción
Ves a Ivan conectado en el Facebook y quieres saludarlo pero para poder ademas presumirle 
que tu ya sabes C/C++ realizas un programa que lo salude cada ves que lo veas conectado.

Entrada
Una unica y simple entrada en la que dira 'conectado' o 'desconectado'.

Salida
Imprimir Ola Ivan si esta conectado e imprimir Ol.. si no."""
estado = str(input())
if estado == "conectado":
    print("Ola Ivan")
else:
    print("Ol..")