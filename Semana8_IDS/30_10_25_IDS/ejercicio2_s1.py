# Una aplicacion para registrar alumnos

alumnos = []

for a in range(int(input("Digite la cantidad de alumnos a registrar: "))):
    alumno = input("Digite el nombre: ")
    alumnos.append(alumno)
print(alumnos)