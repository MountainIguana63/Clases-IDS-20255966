""""El software libre es la denominación del software que respeta la libertad de los usuarios 
sobre su producto adquirido y, por tanto, una vez obtenido puede ser usado, copiado, estudiado, 
cambiado y redistribuido libremente."(wikipedia).

Juan se dedica a redistribuir el sofware libre(SL) y cuenta con una cantidad considerable de este 
tipo de software. Para llevar el control de que SL ha sido ya redistribuido ha creado una base de datos 
donde para cada SL guarda un Entero P que indica las veces que sea redistribuido.

El objetivo de Juan es saber cual SL se a redistribuido 3 o mas veces.

Entrada
La primer linea es entero N que indica el numero de SL's registrados y las siguientes N lineas contienen 
un entero Pi que indica el numero de resdistribuciones para un SL.

Salida
Para cada Pi escribir en una linea si Pi >= 3 "Ok" (sin las comillas) en caso contrario escribir "No"
(sin comillas)."""

tuntunsahur = int(input())
balerina = []

for chimpazinis in range(tuntunsahur):
    tralarero = int(input())
    balerina.append(tralarero)
    
for six_seven in balerina:
    if six_seven >= 3:
        print("Ok")
    else:
        print("No")