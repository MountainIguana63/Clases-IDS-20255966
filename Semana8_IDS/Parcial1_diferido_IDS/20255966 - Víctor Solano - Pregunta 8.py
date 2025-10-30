DUI = input()

largo = len(DUI)
noveno = DUI[8]
entero = DUI[9]

entero = (entero).isnumeric()

largof = largo == 10
novenof = noveno == "-"
enterof = entero == True
respuesta_final = largof is True and novenof is True and enterof is True
print(respuesta_final)