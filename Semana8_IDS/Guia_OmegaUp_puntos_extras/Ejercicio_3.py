"""Descripción del Problema
Un alumno desea saber si obtendrá su premio al estudio en el presente semestre por lo que captura en un programa sus 
6 calificaciones, en donde calcula su promedio y determina si obtiene el premio por un promedio mayor a 9.5.

Entrada
Recibirás en seis líneas diferentes un número con decimales 
donde para la 
sima línea será la calificación para la materia 

Salida
Deberas mostrar "Gana Premio :)" en caso que su promedio para las seis materias sea mayor a 9.5. 
En caso contrario "No Gana Premio :("."""

calificacion1 = float(input())
calificacion2 = float(input())
calificacion3 = float(input())
calificacion4 = float(input())
calificacion5 = float(input())
calificacion6 = float(input())

promedio = calificacion1 + calificacion2 + calificacion3 + calificacion4 + calificacion5 + calificacion6
promedio = promedio / 6

if promedio > 9.5:
    print("Gana Premio :)")
else:
    print("No Gana Premio :(")