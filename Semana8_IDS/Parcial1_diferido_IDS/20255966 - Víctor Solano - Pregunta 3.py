palabra = input().lower()
última_letra = str(input()).lower()

palabra = palabra[::-1]
palabra = palabra[:1:]

resultado = palabra == última_letra
print(resultado)