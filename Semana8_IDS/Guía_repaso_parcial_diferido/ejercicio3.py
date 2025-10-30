"""¡Otra vez!

En la ESEN, estamos experimentando demasiados problemas con las contraseñas. Esta vez, la víctima es
 el pobre OOF.

Al igual que con la contraseña de Alvin, Issem es el malandro que ha hackeado y encriptado la contraseña de 
Steam de OOF. No obstante, esta vez no se llegó a un acuerdo con el Señor Oscuro, por lo que podemos esperar 
que la recuperación de la contraseña no será tan sencilla como la vez pasada.

Afortunadamente, con la ayuda del coco de Rober Polanski, hemos sido capaces de descifrar la forma de recuperar
 la contraseña, siendo así:

Polanski encontró 2 palabras escondidas (A y B).
La primera parte de la contraseña, son los primeros 
 caracteres de A, donde 
 representa el tamaño de la cadena 
.
La segunda parte de la contraseña, son los últimos 
 caracteres de B, donde 
 representa el tamaño de la cadena 
.
¿Puedes ayudar a que OOF recupere su cuenta de Steam?

Entrada
La primera línea contiene un único entero X, los caracteres que tienes que tomar en cuenta. La segunda línea 
presenta una cadena de caracteres A. La última línea contiene una cadena de caracteres B.

Salida
Imprime una única cadena de caracteres, la contraseña recuperada

Restricciones
El tamaño de A y B siempre será a lo sumo 100 caracteres X siempre será un divisor del tamaño de A y B, aunque
 dichas cadenas no tengan el mismo tamaño."""

X = int(input())
A = input()
B = input()

Afinal = len(A) // X
Bfinal = len(B) // X

AHoySi = A[:Afinal]      # prefijo de A
BHoySi = B[-Bfinal:]     # sufijo de B

print(AHoySi + BHoySi)