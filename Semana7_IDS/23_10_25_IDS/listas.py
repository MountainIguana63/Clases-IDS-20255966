"""numeros = ["uno","dos","tres","cuatro"]
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
nombre = "Antonio"
print(nombre.lower().count("a"))
print(numeros.count("dos"))"""

nombres = ["Ana", "Antonio", "Ana", "Jose"]
r_a = 0
r_a = r_a + nombres[0].lower().count("a")
r_a = r_a + nombres[1].lower().count("a")
r_a = r_a + nombres[2].lower().count("a")
r_a = r_a + nombres[3].lower().count("a")
print(r_a)
