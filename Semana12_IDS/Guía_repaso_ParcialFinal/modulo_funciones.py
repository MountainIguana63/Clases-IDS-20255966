#Vamos a definir las funciones de nuestro sistema

#importamos las estructuras de datos
import modulo_datos as dat

def registrar_estudiante():
    """Vamos a registrar a un estudiante (carnet, nombre y apellido)"""
    while True:
        carnet_i = input("Ingrese número de carnet: ")
        existe = False
        for c in dat.Estudiantes:
            if c["carnet"] == carnet_i:
             existe = True
        if len(carnet_i) >= 6 and len(carnet_i) <= 10 and existe == False:
            break
        print("El carnet debe entre 6 y 10 carácteres y ser único")
    while True:
        nombre_i = input("Ingrese el nombre: ")
        if len(nombre_i) > 2:
            break
        print("El nombre no debe ser menor a dos caracteres.")
    while True:
        apellido_i = input("Ingrese el apellido: ")
        if len(apellido_i) > 2:
            break
        print("El apellido no debe ser menor a dos caracteres.")
    dat.Estudiantes.append(
        {
            "carnet":carnet_i,
            "nnombre":nombre_i,
            "apellido_i":apellido_i
        }
    )


