"""Indicaciones
Después del desastre con el generador automático de correos y el intento de realizar un programa para encontrar 
los correos inválidos, la ESEN se dio cuenta de que el programa era demasiado simple y permitió que muchos correos 
incorrectos pasaran las pruebas.

Por esta razón, la ESEN quiere desarrollar un nuevo programa, más complejo y sofisticado, que les ayude a 
validar de mejor forma los correos y así tenerlos listos para sus alumnos de nuevo ingreso 2026.

Te han asignado la misión de crear este nuevo programa. Tu programa debe recibir un correo a validar e 
imprimir un mensaje que indique si es válido o inválido (True/False). Para que un correo se considere válido, 
debe cumplir las siguientes condiciones:

El correo contiene exactamente un @
Antes y después del @ debe haber al menos 3 caracteres
El correo debe contener al menos un punto
El correo no puede contener espacios
El correo no puede iniciar ni terminar con un punto
Restricciones
Todos los correos tendrán mínimo un arroba, aunque pueden tener varios.

Entrada
Una sola línea con un correo electrónico a validar.

Salida
Una sola línea con un mensaje que indique si el correo cumple todas las condiciones (True) o no (False)."""

correo = input()
arroba = correo.count("@")
punto = correo.count(".")
caracteres1 = correo[:3:]
caracteres2 = correo[::-1]
caracteres2 = caracteres2[:3:]
caracteres1 = caracteres1.count("@")
caracteres2 = caracteres2.count("@")
espacios = correo.count(" ")
final = correo
finalhoysi = final[0]
final2 = correo[-1]

bul1 = arroba == 1
bul2 = punto >= 1
bul3 = caracteres1 == 0
bul4 = espacios <= 0
bul5 = finalhoysi != "."
bul23 = final2 != "."
bul6 = caracteres2 == 0
resultado = bul1 is True and bul2 is True and bul6 is True and bul4 is True and bul5 is True and bul3 is True and bul23 is True
print(resultado)