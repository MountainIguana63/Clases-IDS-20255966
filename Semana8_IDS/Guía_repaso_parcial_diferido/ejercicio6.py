"""Contexto
La primera ronda de la Copa Salvadoreña de Programacion ha llegado a su fin. El jurado estaba a punto de 
revisar los resultados del equipo NESE, pero el internet dejo de funcionar!

Afortunadamente, Crijeme tiene anotado cuantos puntos otorga cada problema y el porcentaje de los puntos 
que obtuvo el equipo para cada problema.

Ayuda a determinar cual es el total de puntos que logro el equipo NESE si la competencia consistio de 5 
problemas.

Entrada
Vas a recibir 10 numeros en total.

Los primeros 5 numeros enteros determinan la cantidad de puntos que otorga cada problema.

Los ultimos 5 numeros decimales detereminan el porcentaje que obtuvo cada equipo.

Salida
Un solo numero entero que indique la puntuacion total del equipo NESE."""

p1 = int(input())
p2 = int(input())
p3 = int(input())
p4 = int(input())
p5 = int(input())
r1 = float(input())
r2 = float(input())
r3 = float(input())
r4 = float(input())
r5 = float(input())


a1 = float(p1)*r1
a2 = float(p2)*r2
a3 = float(p3)*r3
a4 = float(p4)*r4
a5 = float(p5)*r5
resultado = a1+a2+a3+a4+a5
resultado = int(resultado)
print(resultado)
