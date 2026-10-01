nombre = input("Ingrese nombre del estudiante: ")
c1 = float(input("Ingrese su calificacion 1: "))
c2 = float(input("Ingrese su calificacion 2: "))
c3 = float(input("Ingrese su calificacion 3: "))

promedio = (c1+c2+c3) / 3

if promedio >= 51:
    estado = "Aprobado"
else:
    estado = "Reprobado"

print("Estudiante:", nombre)
print("Promedio:", promedio)
print("Estado:", estado)