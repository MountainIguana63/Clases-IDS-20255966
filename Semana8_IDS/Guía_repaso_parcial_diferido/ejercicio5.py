"""Contexto:
Alvin le pidió a sus ayudantes favoritos (ya los conoces) que le entregaran un reporte acerca del desempeño de 
los estudiantes de Introducción al Desarrollo de Software.

Ellos ya calificaron, pero están demasiado ocupados en sus otras actividades, como organizar competencias, 
escribir problemas y debatir sobre Kirby. Por eso necesitan tu ayuda para generar el resumen estadístico 
automáticamente.

Entrada
Recibirás 6 datos de tipo float, cada uno en una línea independiente.

Estos representan las notas de los estudiantes ya calificadas. Puedes usar una lista para almacenarlas.

Salida
Debes calcular y mostrar en líneas separadas lo siguiente, con formato de 2 decimales en todos los valores 
numéricos:

El máximo
El mínimo
La diferencia entre el máximo y el mínimo
La suma total de las 6 notas
El promedio de las 6 notas
Cada línea debe seguir estrictamente el formato indicado:

La palabra del campo (escríbela exactamente igual), seguida de dos puntos, un espacio y el número con dos 
decimales. Presta mucha atención a las mayúsculas, los acentos y los espacios, ya que cualquier diferencia 
hará que tu programa no produzca la salida correcta.

Nota: El orden de las líneas es obligatorio y el formato de dos decimales debe aplicarse incluso a los números 
enteros para mantener la coherencia."""

A = float(input())
B = float(input())
C = float(input())
D = float(input())
E = float(input())
F = float(input())

Lista = [A,B,C,D,E,F]
suma = A+B+C+D+E+F
promedio = suma/6
maxi = max(Lista)
mini = min(Lista)
diferencia = maxi - mini

print(f"Maximo: {maxi:.2f}")
print(f"Minimo: {mini:,.2f}")
print(f"Diferencia: {diferencia:,.2f}")
print(f"Suma: {suma:,.2f}")
print(f"Promedio: {promedio:,.2f}")