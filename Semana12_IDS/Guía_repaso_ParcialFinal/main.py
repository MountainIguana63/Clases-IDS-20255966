#Este modulo administra el funcionamiento

#importamos los modulos importantes
import modulo_datos
import modulo_funciones as fn

menu = True

while menu:
    print("""---------- Menú Principal ----------
          1. Registrar Estudiante
          2. Inscribir en curso
          3. Generar reportes
          4. Salir""")
    opcion = input("Elija la opción: ")
    if opcion == "1":
        fn.registrar_estudiante()
    elif opcion == "2":
        print("Eligio 2")
    elif opcion == "3":
        print("Eligio 3")
    elif opcion == "4":
        menu = False
        print("Gracias por elegir nuestro servicio.")
    else:
        print("Opción no es válida")