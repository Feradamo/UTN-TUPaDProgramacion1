# EJERCICIO 1
# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

# edadUsuario = int(input("Ingrese edad: "))
# if edadUsuario > 18:
#     print("Es mayor de edad")    

# ----------------------------------------------------------------------------------------------

# EJERCICIO 2
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”

# notaUsuario = int(input("Ingrese una nota: "))
# if notaUsuario >= 6:
#     print("Aprobado")   
# else:
#     print("Desaprobado") 

# # ----------------------------------------------------------------------------------------------  

# EJERCICIO 3
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

# numeroUsuario = int(input("Ingrese un número: "))
# if numeroUsuario % 2 == 0: 
#     print("Ha ingresado un número par")
# else:
#     print("Por favor, ingrese un número par")

# # ----------------------------------------------------------------------------------------------  

# EJERCICIO 4

# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

# edadUsuario = int(input("Ingrese edad: "))
# if edadUsuario < 12:
#     print("Niño/a") 
# elif edadUsuario >= 12 and edadUsuario < 18:
#     print("Adolescente") 
# elif edadUsuario >= 18 and edadUsuario < 30:
#     print("Adulto/a joven") 
# elif edadUsuario >= 30:
#     print("Adulto/a") 

# # ----------------------------------------------------------------------------------------------  

# EJERCICIO 5

# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

# contrasenia = input("Ingrese una contraseña: ")
# contrasenia_length = len(contrasenia)
# if contrasenia_length >= 8 and contrasenia_length <= 14: 
#     print("Ha ingresado una contraseña correcta") 
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# # ----------------------------------------------------------------------------------------------  

# EJERCICIO 6

# import random
# from statistics import mode, median, mean
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# # Moda única (valor más común) de datos discretos o nominales.
# moda = mode(numeros_aleatorios)
# # Mediana (valor central) de los datos.
# mediana = median(numeros_aleatorios)
# # Media aritmética («promedio») de los datos.
# media = mean(numeros_aleatorios)

# if media > mediana and mediana > moda:
#     print("Sesgo positivo o a la derecha")
# elif media < mediana and mediana < moda:
#     print("Sesgo negativo o a la izquierda")
# elif media == mediana == moda:
#     print("Sin sesgo")
# else:
#     print("No se cumple ninguna condición")

# # ----------------------------------------------------------------------------------------------  

# EJERCICIO 7

# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

# palabra = input("Ingrese una palabra: ")
# ultima_letra = palabra[len(palabra) - 1] 
# if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
#     print(f"{palabra}!")
# else:
#     print(palabra)

# # ----------------------------------------------------------------------------------------------  

# EJERCICIO 8

#  Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# nombre = input("Ingrese su nombre: ")
# opcion = int(input("Ingrese un número segun la opcion correspondiente \n" 
# "1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. \n"
# "2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. \n"
# "3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. \n"))

# if opcion == 1: 
#     print(nombre.upper())
# elif opcion == 2:
#     print(nombre.lower())
# elif opcion == 3:
#     print(nombre.title())

# # ----------------------------------------------------------------------------------------------  

# EJERCICIO 9

# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# magnitud_terremoto = float(input("Ingrese magnitud de un terremoto: "))

# if magnitud_terremoto >= 7:
#     print("Extremo, (puede causar graves daños a gran escala)")
# elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
#     print("Muy Fuerte, (puede causar daños significativos)")
# elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
#     print("Fuerte, (puede causar daños en estructuras débiles)")
# elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
#     print("Moderado, (sentido por personas, pero generalmente no causa daños)")
# elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
#     print("Leve, (ligeramente perceptible)")
# elif magnitud_terremoto < 3:
#     print("Muy leve, (imperceptible)")

# # ----------------------------------------------------------------------------------------------  

# EJERCICIO 10

# Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

# temporada = ""
# dia = int(input("Qué día del mes es:"))
# mes = int(input("Número del mes (1-12):"))
# hemisferio = input("En qué hemisferio te encuentras (N/S):").upper()

# if mes >= 12 and dia >= 21 or mes >= 3 and dia <= 20 or mes == 1 or mes == 2:
#     if hemisferio == "N":
#         temporada = "Invierno"
#     else:
#         temporada = "Verano"

# if mes >= 3 and dia >= 21 or mes >= 6 and dia <= 20 or mes == 4 or mes == 5:
#     if hemisferio == "N":
#         temporada = "Primavera"
#     else:
#         temporada = "Otoño"

# if mes >= 6 and dia >= 21 or mes >= 9 and dia <= 20 or mes == 7 or mes == 8:
#     if hemisferio == "N":
#         temporada = "Verano"
#     else:
#         temporada = "Invierno"

# if mes >= 9 and dia >= 21 or mes >= 12 and dia <= 20 or mes == 10 or mes == 11:
#     if hemisferio == "N":
#         temporada = "Otoño"
#     else:
#         temporada = "Primavera"

# print(f"Usted se encuentra en: {temporada}")





