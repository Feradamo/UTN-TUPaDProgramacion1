# EJERCICIO 1

# Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja
import random
# array que almacenara notas random 
notas_estudiantes = []
# cantidad de notas a crear
cantidad_de_notas = 10
# acumulador para calculo de promedio
promedio = 0    
# variables infinitas para encontrar valores bajo y alto
nota_mas_baja = float('inf')
nota_mas_alta = float('-inf')
for _ in (range(cantidad_de_notas)):
    # creación de número random 1-10
    nota = random.randint(1, 10)
    # acumulación de notas
    promedio += nota
    # Evaluacion de notas altas y bajas
    if nota <  nota_mas_baja:
        nota_mas_baja = nota
    if nota >  nota_mas_alta:
        nota_mas_alta = nota
    # actualizacion de array
    notas_estudiantes.append(nota)
# calculo de promedio
promedio = promedio / cantidad_de_notas
# Resultados por pantalla
print(nota_mas_baja)
print(nota_mas_alta)
print(promedio)
print(notas_estudiantes)

# -----------------------------------------------------------------------------------------------

# EJERCICIO 2

# Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

# Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

# sorted(iterable, *, key=None, reverse=False)

# variable que almacenara la cantidad de productos a cargar
cantidad_de_productos = 5
# Lista contendra los elementos
lista_de_productos = []
# Lista que almacenara los elementos ordenados
lista_ordenada = []
# variable que almacenara el producto a eliminar
producto_a_eliminar = ""
# Recorro cantidad_de_productos veces
for _ in range(cantidad_de_productos):
    print("Ingrese un producto")
    pruducto = input()
    # almaceno en lista_de_productos cada producto
    lista_de_productos.append(pruducto)
# Se realiza el ordenamiento en formato ASC
lista_ordenada = sorted(lista_de_productos)
# Solicito producto al usuario
print("Que producto desea eliminar")
producto_a_eliminar = input()
# Verifico que el producto existe antes de eliminarlo
if producto_a_eliminar in lista_ordenada:
    lista_ordenada.remove(producto_a_eliminar)
else:
    print(f"El producto '{producto_a_eliminar}' no se encuentra en la lista.")
# Printeo valores por pantalla
print(lista_ordenada)

# -----------------------------------------------------------------------------------------------

# EJERCICIO 3

# Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

import random
# array que almacenara cantidad de numeros pares
lista_numeros_pares = []
# array que almacenara cantidad de numeros impares
lista_numeros_impares = []
# cantidad de números a crear
cantidad_de_numeros = 15

for _ in (range(cantidad_de_numeros)):
    # creación de número random 1-100
    numero_random = random.randint(1, 100)
    # El número se almacena en su array correspondiente
    if numero_random % 2 == 0:
        lista_numeros_pares.append(numero_random) 
    else:
        lista_numeros_impares.append(numero_random) 

# Resultados por pantalla: cantida de números pares e impares
print(f"La cantidad de números pares es igual a {len(lista_numeros_pares)}")
print(f"La cantidad de números impares es igual a {len(lista_numeros_impares)}")

# -----------------------------------------------------------------------------------------------

# EJERCICIO 4

# Dada una lista con valores repetidos:
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

datos = [1,3,5,3,7,1,9,5,3]
# array que excluira los numeros repetidos
datos_sin_valores_repetidos = []
# se recorren los datos y si no existen en el array vacio se agregan
for numero in datos:
    if numero not in datos_sin_valores_repetidos:
        datos_sin_valores_repetidos.append(numero)
# Printeo nuevo array
print(datos_sin_valores_repetidos)

# -----------------------------------------------------------------------------------------------

# EJERCICIO 5

# Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

# Lista de estudiantes presentes
array_de_estudiantes = ['alma', 'cinthia', 'lourdes', 'arianna', 'santiago', 'jhonnny', 'guido', 'victor']
# variables de usuario
estudiante = ""
orden = ""
# Solictud de orden al usuario
print("Para manipular la lista ingrese:")
print("'agregar' o 'quitar' segun corresponda")
orden = input()
if orden == "agregar":
    print("Ingresa el nombre del nuevo estudiante")
    estudiante = input()
    # agrego un nuevo estudiante a la lista
    array_de_estudiantes.append(estudiante)
elif orden == "quitar":
    print("Ingresa el nombre del estudiante a quitar")
    estudiante = input()
    # compruebo si el estudiante se encuentra en la lista
    if estudiante in array_de_estudiantes:
        # quito estudiante a la lista
        array_de_estudiantes.remove(estudiante)
    else:
        print(f"El estudiante '{estudiante}' no se encuentra en la lista.")
else:
    print("La acción solicitada es incorrecta")
# Devuelvo array
print(array_de_estudiantes)

# -----------------------------------------------------------------------------------------------

# EJERCICIO 6

# Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).

# SOLUCION 1
lista = [2,3,4,5,6,7,8]
largo_de_lista = len(lista)
elemento_a_copiar = 0
# Almaceno ultima posicion 
ultimo_elemento = lista[largo_de_lista - 1]
# Actualizo posiciones en orden invertido
for indice in range(largo_de_lista, 0, -1):
    # Evito la posicion que no existe
    if indice == largo_de_lista:
        continue
    # Tomo la posicion anterior y actualizo la actual
    elemento_a_copiar = lista[indice - 1]
    lista[indice] = elemento_a_copiar
# Actualizo el primer elemento
lista[0] = ultimo_elemento
# Imprimo lista
print(lista)

# SOLUCION 2
# pop(0) quita y devuelve el ultimo, si recibe arg quite el indice solicitado
# insert(0, x) agrega al inicio
# appen() agrega al final
lista = [2,3,4,5,6,7,8]
ultimo_elemento = lista.pop()
lista.insert(0, ultimo_elemento)
print(lista)

# -----------------------------------------------------------------------------------------------

# EJERCICIO 7

# Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
# semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

# Temperaturas
temperaturas = [
    [19, 18, 20, 19, 19, 22, 20], # máximas
    [12, 13, 14, 14, 13, 16, 17]  # mínimas
]
# Promedios
promedioMinima = 0
promedioMaxima = 0
# Amplitud térmica
mayorAmplitudTermica = 0
# Recorre matriz de temperaturas
for i in range(len(temperaturas)):
    # Variable de fila
    fila = temperaturas[i]
    # Recorre array de temperaturas maximas y minimas
    for j in range(len(fila)):
        # Segunda fila para temperaturas maximas
        if i == 1:
            promedioMaxima += fila[j]
        # Sino fila para temperaturas minimas
        else:
            promedioMinima += fila[j]

# Recorre array de temperaturas
for i in range(len(temperaturas[0])):
    # Variables de temperaturas
    temperaturasMaximas = temperaturas[0][i]
    temperaturasMinimas = temperaturas[1][i]
    # Calculo de amplitud térmica
    amplitudTermica = temperaturasMaximas - temperaturasMinimas

    if amplitudTermica > mayorAmplitudTermica:
        mayorAmplitudTermica = amplitudTermica

# Calulo de promedios
promedioMinima = promedioMinima / len(fila)
promedioMaxima = promedioMaxima / len(fila)

# Muestra valores por pantalla
print(f"El promedio de mínima es igual a : {round(promedioMinima, 1)}°")
print(f"El promedio de máxima es igual a : {round(promedioMaxima, 1)}°")
print(f"La mayor amplitud térmica fue de: {mayorAmplitudTermica}°")

# -----------------------------------------------------------------------------------------------

# EJERCICIO 8

# Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

notas = [
            [2,7,4,6,9], # Matemática
            [6,8,9,7,8], # Programación 
            [7,3,6,7,9], # Organizacion Empresarial
        ]

# Calcula el promedio de cada materia
for i in range(len(notas)):
    fila = notas[i]
    # Reinicia la variable que acumula notas
    acumuladorDeNotas = 0
    # Recorre cada columna
    for j in range(len(fila)):
        columna = fila[j]
        # Suma la nota al acumulador
        acumuladorDeNotas += columna
    # Calcula el promedio de la materia
    promedio = acumuladorDeNotas / len(fila)
    # Muestra el promedio de la materia
    print(f"El promedio de la materia {i + 1} es igual a: {promedio}")

# Calcula el promedio de cada alumno - asumo que son 5 notas
for i in range(len(notas[0])): 
    # Reinicia la variable que acumula notas
    acumuladorDeNotas = 0
    # Recorre cada fila
    for j in range(len(notas)):
        # i es la nota y j es la materia
        columna = notas[j][i]
        # Suma la nota al acumulador
        acumuladorDeNotas += columna
    # Calcula el promedio del alumno
    promedio = acumuladorDeNotas / len(notas)
    # Muestra el promedio del alumno
    print(f"El promedio del alumno {i + 1} es igual a: {round(promedio, 1)}")


# -----------------------------------------------------------------------------------------------

# EJERCICIO 9

# Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

tablero = [
        ["-","-","-"], 
        ["-","-","-"], 
        ["-","-","-"], 
    ]

print("\n---------------------------------------------\n")
print("Antes de comenzar a jugar recuerde ")
print("que las posiciones en el eje 'x' o 'y'")
print("no pueden ser MENORES a 1 ni MAYORES a 3")
print("\n---------------------------------------------\n")

juegoEnProceso = True
jugadorActual = 0
cantidadDeJugadas = 9
jugadas = []

while juegoEnProceso:
    # Evalua si la cantidad de jugadas es igual a la cantidad de posiciones
    if len(jugadas) == cantidadDeJugadas - 1:
        juegoEnProceso = False
        print("El juego ha terminado")
    # Variable que almacena el estado de la jugada
    jugadaValida = False
    # Variable que almacena el valor de la ficha
    ficha = ""
    # Evalua que jugador realiza la accion
    if jugadorActual == 0 or jugadorActual == 1:
        print("---------------------------------------------")
        print("Turno del jugador X\n")
        ficha = "X"
        jugadorActual = 1
    else: 
        print("\n---------------------------------------------")
        print("Turno del jugador O\n")
        ficha = "O"
        jugadorActual = 2
    # Solicita coordenandas al usuario
    while not jugadaValida:
        print("\nIngrese coordenadas en eje 'x'")
        posicionX = int(input()) - 1
        print("\n---------------------------------------------")
        print("\nIngrese coordenadas en eje 'y'")
        posicionY = int(input()) - 1
        print("\n---------------------------------------------")
        # Valida si las coordenandas se encuentran dentro del rango
        if posicionX >= 0 and posicionX <= 2 and posicionY >= 0 and posicionY <= 2:
            # Valida si la posicion se encuentra ocupada
            if tablero[posicionX][posicionY] != "O" and tablero[posicionX][posicionY] != "X":
                jugadaValida = True
            else:
                print("La posicion ya se encuentra ocupada!")        
        else:
            print("Has ingresado un valor de coordenada incorrecto!")
    # Si la jugada es válida updateo el juego
    if jugadaValida:
        # Actualiza el valor de ficha en la matriz
        tablero[posicionX][posicionY] = ficha
        # Actualiza el registro de jugadas
        jugadas.append(ficha)
        # Pinta el tablero
        for x in range(len(tablero)):
            acumulador = ""
            for j in range(len(tablero[x])):
                acumulador += "|" + tablero[x][j] + "|"
            print(acumulador)
        # Cambia al jugador opuesto
        jugadorActual = 2 if jugadorActual == 1 else 1


# -----------------------------------------------------------------------------------------------

# EJERCICIO 10

# Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

# Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.
# Matriz de ventas
ventas = [
    [12, 15, 20, 18, 25, 30, 22],  # Producto 1
    [8,  10, 12, 9,  14, 11, 13],  # Producto 2
    [5,  7,  6,  8,  10, 9,  7],   # Producto 3
    [20, 18, 25, 22, 30, 28, 26]   # Producto 4
]
# Array dias de la semana
diasDeLaSemana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
# Variable que almacenara las ventas totales por dia
ventasTotalesPorDia = []
# Variable que almacenara las ventas totales por producto
ventasTotalesPorProducto = []
# Variable que almacenara la mayor venta por dia y su posicion en el array
mayorVentaPorDia = [0,0]
# Variable que almacenara la mayor venta por producto y su posicion en el array
mayorVentaPorProducto = [0,0]
# Recorre ventas
for i in range(len(ventas)):
    acumulador = 0
    for j in range(len(ventas[i])):
        # Acumulo el valor de ventas
        acumulador += ventas[i][j]
    # Almacena el valor del total por producto
    ventasTotalesPorProducto.append(acumulador)
    # Reponde por pantalla el listado de productos y su total en ventas
    print(f"Cantidad de ventas del producto {i + 1} es igual a: {acumulador}")
# Recorre el array y devuelve el valor y posicion del elemento mas vendido
for i in range(len(ventasTotalesPorProducto)):
    if ventasTotalesPorProducto[i] > mayorVentaPorProducto[0]:
        mayorVentaPorProducto[0] = ventasTotalesPorProducto[i]
        mayorVentaPorProducto[1] = i
# Recorre ventas por dia
for i in range(len(ventas[0])):
    acumulador = 0
    for j in range(len(ventas)):
        # Acumulo el valor de ventas
        acumulador += ventas[j][i]
    # Almacena el valor del total por dia
    ventasTotalesPorDia.append(acumulador)
# Recorre el array y devuelve el valor y posicion del dia con mas ventas
for i in range(len(ventasTotalesPorDia)):
    if ventasTotalesPorDia[i] > mayorVentaPorDia[0]:
        mayorVentaPorDia[0] = ventasTotalesPorDia[i]
        mayorVentaPorDia[1] = i
# Devuelvo resultados por pantalla
print(f"El dia de la semana con mayor ventas fue el dia: {diasDeLaSemana[mayorVentaPorDia[1]]} con un total de {mayorVentaPorDia[0]}")
print(f"El producto {mayorVentaPorProducto[1] + 1} es el mas vendido con un total de {mayorVentaPorProducto[0]}")

# -----------------------------------------------------------------------------------------------