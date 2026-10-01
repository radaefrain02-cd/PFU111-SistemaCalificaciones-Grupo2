nombre = input("Ingrese nombre del estudiante: ")
while nombre == "":
    print("ERROR: El nombre no puede estar vacío.")
    nombre = input("Ingrese nombre del estudiante: ")

c1 = float(input("Ingrese la calificación 1: "))
while c1 < 0 or c1 > 100:
    print("ERROR: La calificación debe estar entre 0 y 100.")
    c1 = float(input("Ingrese nuevamente la calificación 1: "))

c2 = float(input("Ingrese la calificación 2: "))
while c2 < 0 or c2 > 100:
    print("ERROR: La calificación debe estar entre 0 y 100.")
    c2 = float(input("Ingrese nuevamente la calificación 2: "))

c3 = float(input("Ingrese la calificación 3: "))
while c3 < 0 or c3 > 100:
    print("ERROR: La calificación debe estar entre 0 y 100.")
    c3 = float(input("Ingrese nuevamente la calificación 3: "))

promedio = (c1 + c2 + c3) / 3

if promedio >= 51:
    estado = "Aprobado"
else:
    estado = "Reprobado"

print("Estudiante:", nombre)
print("Promedio:", promedio)
print("Estado:", estado)