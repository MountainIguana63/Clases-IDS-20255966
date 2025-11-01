agente = "encargado"
platillo = []
prezio = []

agente_usuario = input("Ingrese el nombre del agente: ")
while agente != agente_usuario:
    print("Agente no registrado”")
    agente_usuario = input("Ingrese el nombre del agente: ")
menu_inicio = True
while menu_inicio is True:
    menu = int(input("1.Creación de plastillos, 2.Consulta de platillos y precios, 3. Colocar un pedido, 4. Salir: "))
    if menu == 4:
        menu_inicio = False
    elif menu == 1:
        a = a