"""¡Felicidades! 🎉

De parte del Competitive Coding Club (C3) te hemos seleccionado para unirte a nuestro equipo de ingenieros 
de software para nuestra nueva plataforma educativa en desarrollo.

Lastimosamente, nuestro CTO (Rober) no está disponible, así que el liderazgo del proyecto quedó en manos de 
Pleites.

Mientras él escribe los problemas para la próxima Copa Salvadoreña de Programación, te ha encargado algo muy 
importante: el sistema de creación de usuarios y cuentas para las competencias del C3.

Entrada
Recibirás 2 cadenas (strings), una por línea:

El nombre del competidor, que siempre tendrá al menos 5 caracteres (garantizado).
El apellido del competidor.
Procesamiento
Con estos datos, deberás construir la cuenta siguiendo las indicaciones del presi, ChrisM:

Nick: Toma los primeros 5 caracteres del nombre, agrega el primer carácter del apellido, y convierte todo a 
minúscula.

Pin: Calcula el pin como:

len(nombre) * 1000 + len(apellido)

Luego aplícale un módulo 10000 (% 10000) para mantenerlo en 4 dígitos.

ID: Une las partes con el formato: "C3-" + nick + "-" + pin"""

nombre = input().lower()
apellido = input().lower()
nombre2 = nombre[:5:]
apellido2 = apellido[:1:]

Nick = nombre2+apellido2


pin = len(nombre) * 1000 + len(apellido)
pin = pin% 10000

ID = f"C3-{Nick}-{pin}"

print(f"Nick: {Nick}")
print(f"Pin: {pin}")
print(f"ID: {ID}")