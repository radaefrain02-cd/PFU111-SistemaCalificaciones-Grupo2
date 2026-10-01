# Sistema de Registro de Calificaciones - PFU111

Este programa en Python permite registrar estudiantes, ingresar sus 3 calificaciones, calcular el promedio final y determinar si aprueban o reprueban.

## Descripcion del Programa
El programa pide el nombre del estudiante y 3 notas entre 0 y 100. Calcula el promedio y si la nota es mayor o igual a 51, muestra que el estudiante esta Aprobado, de lo contrario muestra Reprobado. Tambien permite registrar varios estudiantes seguidos en bucle.

## Funcionalidades
- Registro del nombre del estudiante.
- Ingreso de 3 calificaciones parciales.
- Calculo del promedio redondeado a 2 decimales.
- Determinacion del estado final (Aprobado o Reprobado).
- Permitir registrar multiples estudiantes de forma continua.

## Validaciones
- Se valida que el nombre del estudiante no quede vacio ("").
- Se asegura que cada calificacion ingresada este dentro del rango permitido de 0 a 100. Si esta fuera de rango, el programa solicita nuevamente el dato.

## Manejo de Errores
- Se utilizan bloques try-except para capturar el error ValueError cuando el usuario ingresa texto o letras en lugar de numeros en las calificaciones.
- El programa detecta la entrada invalida, informa el error al usuario y vuelve a pedir la nota sin cerrarse inesperadamente.

## Pruebas Realizadas
- Prueba 1: Datos validos (ingreso de nombre normal y notas correctas).
- Prueba 2: Calificacion negativa (ingreso de valores como -10).
- Prueba 3: Calificacion superior al maximo (ingreso de valores como 150).
- Prueba 4: Nombre vacio (presionar Enter sin escribir texto).
- Prueba 5: Entrada inesperada (ingresar letras en lugar de numeros).

## Historial de Commits
### Commit 1: feat: crear version inicial del sistema de calificaciones
Se creo la estructura base del programa. Pedia el nombre y las 3 notas con float(), calculaba el promedio dividiendo entre 3 y mostraba el estado con un if basico sin validaciones.

### Commit 2: agregar validacion de entradas
Se agregaron bucles while para controlar las entradas. Se valido que el nombre no quede vacio ("") y que las notas 1, 2 y 3 estuvieran en el rango permitido de 0 a 100.

### Commit 3: fix: corregir errores detectados durante las pruebas
Se mejoro la validacion de las notas utilizando bloques try/except con ValueError para evitar que el programa se rompa si se ingresan letras en lugar de numeros. Se mantuvieron las reglas para que la nota siga entre 0 y 100.

### Commit 4: refactor: modularizar el codigo con funciones
Se organizo el programa creando la funcion registrar_estudiante() para permitir registrar mas estudiantes. Se agrego el formato de 2 decimales para el promedio y un bucle principal para preguntar si se desea registrar a otro estudiante (s/n).

## Tecnologias Utilizadas
- Lenguaje de programacion: Python 3
- Control de versiones: Git
- Plataforma de alojamiento: GitHub
