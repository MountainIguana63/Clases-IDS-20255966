agente = "encargado"
platillo = []
prezio = []

agente_usuario = input("Favor ingrese el nombre del agente: ").lower()
while agente != agente_usuario:
    print("Agente no registrado")
    agente_usuario = input("Favor ingrese el nombre del agente: ").lower()
menu_inicio = True
while menu_inicio is True:
    menu = int(input("1.Creación de plastillos, 2.Consulta de platillos y precios, 3. Colocar un pedido, 4. Salir: "))
    if menu == 1:
        platilloT = input("Ingrese el nombre del platillo a crear: ").lower()
        precioT = float(input("Ingrese el precio del platillo a crear: "))
        platillo.append(platilloT)
        prezio.append(precioT)
    elif menu == 2:
        if platillo == []:
            print("Actualmente no hay platillos ingresados")
        else:
            for x in range(len(platillo)):
                print(f"{platillo[x].capitalize()}: ${prezio[x]:.2f}")
    elif menu == 3:
        existe = False
        while existe == False:
            platilloOrdenar = (input("Indique el nombre del platillo para su orden: ")).lower()
            for y in range(len(platillo)):
                if platillo[y].lower() == platilloOrdenar:
                    print(f"Usted ha elegido {platillo[y]} con un precio de ${prezio[y]:.2f}")
                    existe = True
                elif existe == False:
                    print("El platillo ingresado no existe.")
    elif menu == 4:
        menu_inicio = False