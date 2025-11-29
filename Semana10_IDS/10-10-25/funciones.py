#Este modula va a contener funciones

#Una función tiene 2 tiempos, una definición y una llamada

#Vamos a definir una función
def mi_funcion():
    """Esta funcion imprime un saludo"""
    print("Hola mundo")
    print("amigo usuario")
    print("¡gracias por usar nuestro sistema!")

#Vamos a recibir información desde afuera de la función
def capturar_nombre():
    """Esta función recibe valores por medio de input"""
    nombre_input = input("Escriba su nombre ")
    apellido_input = input("Digite su apellido ")
    nombre_completo = f"{nombre_input.capitalize()} {apellido_input.capitalize()}"
    print(nombre_completo)

def capturar_usuario(nombre, edad):
    """Esta función recibe valores por medio de argumentos"""
    nombre_usuario = nombre
    edad_usuario = edad
    texto = f"El usuario {nombre_usuario.title()} tiene {edad_usuario} años de edad."
    print(texto)

#Llamando la funcion capturar_usuario()
capturar_usuario(input("ingrese su nombre: "), input("Edad: "))
