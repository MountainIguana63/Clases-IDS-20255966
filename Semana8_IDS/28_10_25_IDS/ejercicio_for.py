valores = [[1,3,6],
           [2,7,4],
            [6,5,9],
            [1,10,20]]
mayores = []
minimo = int(input("digite el mínimo: "))
for v in valores:
    for valorcito in v:
        if valorcito > minimo:
            mayores.append(valorcito)
print(mayores)