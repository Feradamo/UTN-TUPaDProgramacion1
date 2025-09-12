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