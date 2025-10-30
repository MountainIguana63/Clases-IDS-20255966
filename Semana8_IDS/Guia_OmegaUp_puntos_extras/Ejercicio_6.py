"""Descripción
Bodoque es un conejo que ha sufrido muchos desamores por distintas razones (aunque no quiso decir por qué). 
Ahora, ha vuelto a enamorarse, pero su amigo "
" le ha advertido que no se ilusione demasiado rápido. Según él, Bodoque siempre se emociona demasiado y acaba 
saliendo lastimado.

Por eso, 
 quiere tu ayuda para saber si esta vez el amor de Bodoque tiene posibilidades de funcionar. Ha descubierto 
 que Bodoque toma en cuenta la cantidad de letras en los nombres de sus enamoramientos para decidir si debe 
 ilusionarse o no. Si el nombre cumple con ciertas condiciones, él se deja llevar por la emoción.

¡Ayuda a 
 a evitar que Bodoque sufra otro desarrollo de personaje innecesario!

Entrada
Se te dará una lista N de nombres, los cuales son los amores de Bodoque, y dependiendo de la cantidad de 
letras le dirás lo siguiente:

Salida
Dependiendo de la cantidad de letras, dirás lo siguiente:

Si el nombre tiene * 6 letras o menos, imprimirás: "No vale la pena".
Si el nombre tiene * 8 letras o mas, imprimirás:"Si aguanto otro desarrollo de personaje".
Si el nombre tiene ** mas de 6 pero menos de 8, imprimirás: "Dios no creo aguantar esta vez"."""

cantidad_nombres = int(input())
nombres = []
letras = []

for n in range(cantidad_nombres):
    nombre_de_la_afortunada_WUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU = (input())
    TunTunTunSahur = len(nombre_de_la_afortunada_WUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU)
    letras.append(TunTunTunSahur)
    nombres.append(nombre_de_la_afortunada_WUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU)

for x in letras:
    if x <= 6:
        print("No vale la pena")
    elif x >= 8:
        print("Si aguanto otro desarrollo de personaje")
    elif x == 7:
        print("Dios no creo aguantar esta vez")

    




