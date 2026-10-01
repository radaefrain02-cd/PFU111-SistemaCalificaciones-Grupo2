def registrar_estudiante():
    nombre = input("Ingrese nombre del estudiante: ")
    while nombre == "":
        print("ERROR: El nombre no puede estar vacío.")
        nombre = input("Ingrese nombre del estudiante: ")

    while True:
        try:
            c1 = float(input("Ingrese la calificación 1: "))
            if c1 >= 0 and c1 <= 100:
                break
            print("ERROR: La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("ERROR: Debe ingresar un número.")

    while True:
        try:
            c2 = float(input("Ingrese la calificación 2: "))
            if c2 >= 0 and c2 <= 100:
                break
            print("ERROR: La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("ERROR: Debe ingresar un número.")

    while True:
        try:
            c3 = float(input("Ingrese la calificación 3: "))
            if c3 >= 0 and c3 <= 100:
                break
            print("ERROR: La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("ERROR: Debe ingresar un número.")

    promedio = (c1 + c2 + c3) / 3

    if promedio >= 51:
        estado = "Aprobado"
    else:
        estado = "Reprobado"

    print()
    print("Estudiante:", nombre)
    print(f"Promedio: {promedio:.2f}")
    print("Estado:", estado)


seguir = "s"

while seguir == "s" or seguir == "S":
    print()
    print("--- Registro de estudiante ---")
    registrar_estudiante()
    print()
    seguir = input("¿Desea registrar otro estudiante? (s/n): ")

print("Programa finalizado.")