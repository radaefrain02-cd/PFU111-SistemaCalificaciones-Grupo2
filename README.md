# Sistema de Calificaciones 
Este programa en Python permite registrar estudiantes, ingresar sus 3 calificaciones, calcular el promedio final y determinar si aprueban o reprueban.

## Descripcion del Programa
El programa pide el nombre del estudiante y 3 notas entre 0 y 100. Calcula el promedio y si la nota es mayor o igual a 51, muestra que el estudiante esta Aprobado, de lo contrario muestra Reprobado. Tambien permite registrar varios estudiantes seguidos en bucle.

## Historial de Commits
### Commit 1: feat: crear version inicial del sistema de calificaciones
Se creo la estructura base del programa. Pedia el nombre y las 3 notas con float(), calculaba el promedio dividiendo entre 3 y mostraba el estado con un if basico sin validaciones.
### Commit 2: agregar validacion de entradas
Se agregaron bucles while para controlar las entradas. Se valido que el nombre no quede vacio ("") y que las notas 1, 2 y 3 estuvieran en el rango permitido de 0 a 100.
### Commit 3: fix: corregir errores detectados durante las pruebas
Se mejoro la validacion de las notas utilizando bloques try/except con ValueError para evitar que el programa se rompa si se ingresan letras en lugar de numeros. Se mantuvieron las reglas para que la nota siga entre 0 y 100.
### Commit 4: refactor: modularizar el codigo con funciones
Se organizo el programa creando la funcion registrar_estudiante() para permiritr registar ams estudiantes. Se agrego el formato de 2 decimales para el promedio y un bucle principal para preguntar si se desea registrar a otro estudiante (s/n).