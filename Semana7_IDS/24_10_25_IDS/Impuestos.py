print("BIENVENIDO A EL PROGRAMA SUPER CHACHI PARA CALCULAR CUANTO DINERO SE TE ROBARÁ... ¡DIGO! SE TE COBRARÁ DE IMPUESTOS :D")

monto = float(input("Ingrese su monto ganado: "))
Tipo_de_venta = int((input("¿La venta fue local(1) o internacional(2)? Introduzca el número correspondiente: ")))

if Tipo_de_venta == 1:
    if monto > 500:
        print("Se te cobrara 10% en impuestos")
    else:
        if monto > 200:
            print("Se te cobraran 8% en impuestos")
        else:
            if monto > 50:
                print("Se te cobraran 6% en impuestos")
            else: 
                if monto <= 50:
                    print("No se te cobraran impuestos")
elif Tipo_de_venta == 2:
        if monto > 500:
            print("Se te cobrara 14% en impuestos")
        else:
            if monto > 200:
                print("Se te cobraran 12% en impuestos")
            else:
                if monto > 50:
                    print("Se te cobraran 10% en impuestos")
                else: 
                    if monto <= 50:
                        print("No se te cobraran impuestos")
else:
    print("Porfavor indroduzca una opción válida")