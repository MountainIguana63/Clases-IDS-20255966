"""Descripción
El agente secreto JEMI (por sus siglas ya explicadas en otro problema) se ha aventurado en una misión mas por salvar al mundo mientras su esclava busca que darle de comer.

En esta misión, JEMI, tendrá que infiltrarse a la base secreta de sus enemigos. Hasta el momento todo iba de maravilla, solo había un inconveniente: no tenía la contraseña completa para entrar. Solo sabe que la contraseña inicia con "123456789" y que hace falta un dígito (0 - 9). Por suerte, sus compañeros le han mandado el dígito desconocido aunque por motivos de seguridad lo han enviado de manera cifrada como un número en el rango [10, 100].

Problema
Ayuda a JEMI a terminar su misión dándole el dígito que le hace falta. Sabiendo que el dígito es el mismo con el que termina el número dado. (ver ejemplos para mayor claridad).

Entrada
Un entero 
 que es el número cifrado enviado por los compañeros de JEMI.

Salida
Un entero que representa el dígito que JEMI necesita. (Siempre es el número con el que termina 
)"""

numero_codificado = input()
ultima_cifra_de_numero_codificado = len(numero_codificado)
print(ultima_cifra_de_numero_codificado)