# EJERCICIO 1

# Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

# Devuelve Hola mundo!
def imprimir_hola_mundo():
    print("Hola mundo!")
# Invoco función
imprimir_hola_mundo()

# -----------------------------------------------------------------------------------------------

# EJERCICIO 2

# Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá 
# devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

# Saluda nombre de usuario.
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
# Valida nombre de usuario.
def validar_datos(nombre_de_usuario):
    return True if nombre_de_usuario != "" else False
# Solicita nombre de usuario.
def solicitar_datos():
    print("Ingresa tu nombre de usuario: ")
    nombre_de_usuario = input()
    return nombre_de_usuario
# Almacena nombre de usuario
nombre_de_usuario = solicitar_datos()
# Verifica si los datos son válidos
esValido = validar_datos(nombre_de_usuario)
# Invoco función saludar
saludar_usuario(nombre_de_usuario) if esValido else print("Entrada vacia, intentelo nuevamente")

# -----------------------------------------------------------------------------------------------

# EJERCICIO 3

# Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Solicita nombre de usuario.
def solicitar_datos():
    nombre = apellido = edad = residencia = ""
    print("Ingresa tu nombre: ")
    nombre = input()
    print("Ingresa tu apellido: ")
    apellido = input()
    print("Ingresa tu edad: ")
    edad = int(input())
    print("Ingresa tu lugar de residencia: ")
    residencia = input()
    return [[nombre, "string"], [apellido, "string"], [edad, "number"], [residencia, "string"]]
# Valida datos string y númericos
def validar_datos(datos_del_usuario):
    for dato in datos_del_usuario:
        if dato[1] == "string" and dato[0] == "":
            return False
        elif dato[1] == "number" and dato[0] < 1:
            return False
    return True
# Saluda nombre de usuario.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
# Almacena nombre de usuario
datos_del_usuario = solicitar_datos()
# Verifica si los datos son válidos
sonValidos = validar_datos(datos_del_usuario)
# Si son válidos invoca función
if sonValidos:
    informacion_personal("Fernando", "Adamo", 34, "Buenos aires")
else:
    print("Algunas de las entradas es inválida o se encuentra vacia, intentelo nuevamente")

# ----------------------------------------------------------------------------------------------- 

# EJERCICIO 4

# Crear dos funciones: calcular_area_circulo(radio) que reciba el 
# radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como 
# parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones 
# para mostrar los resultados.

import math
PI = math.pi
# Calcula el area.
def calcular_area_circulo(radio):
    return (radio ** 2) * PI
# Calcula el perimetro.
def calcular_perimetro_circulo(radio):
     return radio * 2 * PI
# Valida radio del circulo.
def validar_datos(radio_del_circulo):
    return True if radio_del_circulo > 0 else False
# Solicita radio del circulo.
def solicitar_datos():
    print("Ingresa radio del circulo en centimetros: ")
    radio_del_circulo = int(input())
    return radio_del_circulo
# Variable que alcena radio 
radio_del_circulo = solicitar_datos()
# Verifica el dato es válido
esValido = validar_datos(radio_del_circulo)
# Si es válido invoco funciones
if esValido:
    areDeCirculo = calcular_area_circulo(radio_del_circulo)
    perimetro_circulo = calcular_perimetro_circulo(radio_del_circulo)
    print(f"El valor de area es: {round(areDeCirculo, 2)}cm²")
    print(f"El valor de perimetro es: {round(perimetro_circulo, 2)}cm")
else:
    print("El número tiene que ser mayor a 0, intentelo nuevamente")

# ----------------------------------------------------------------------------------------------- 

# EJERCICIO 5

# Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos 
# y mostrar el resultado usando esta función.

# Conversión de valores
def segundos_a_horas(segundos):
    segundos_en_una_hora = 60 * 60
    return segundos / segundos_en_una_hora
# Valida segundos ingresados.
def validar_dato(segundos):
    return True if segundos > 0 else False
# Solicita cantidad de segundos.
def solicitar_datos():
    print("Ingresa cantidad de segundos: ")
    segundos = int(input())
    return segundos

# Almacena nombre de usuario
segundos = solicitar_datos()
# Verifica si los datos son válidos
sonValidos = validar_datos(datos_del_usuario)
# Si son válidos invoca función
if sonValidos:
    cantidad_en_horas = segundos_a_horas(segundos)
    print(f"La cantidad es {round(cantidad_en_horas, 2)}hr{ 's' if cantidad_en_horas > 2 else '' } ")
else:
    print("El número ingresado es invalido, intentelo nuevamente")


# ----------------------------------------------------------------------------------------------- 

# EJERCICIO 6

# Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero,cantidad_de_multiplicaciones = 10):
    for i in range(1, cantidad_de_multiplicaciones + 1):
        print(f"{numero} x {i} = {i * numero}")
# Valida número ingresado.
def validar_dato(numero):
    return True if numero > 0 else False
# Solicita cantidad de segundos.
def solicitar_datos():
    print("Ingresa número a multiplicar: ")
    return int(input())
# Almacena nombre de usuario
numero = solicitar_datos()
# Verifica si el dato es correcto
esValido = validar_dato(numero)
# Invoco función multiplicar
tabla_multiplicar(numero) if esValido else print("Entrada vacia, intentelo nuevamente")

# ----------------------------------------------------------------------------------------------- 

# EJERCICIO 7

# Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

# Operaciones aritmeticas
def suma(a, b): return f"La SUMA de a + b es igual a {a + b}"
def resta(a, b): return f"La RESTA de a - b es igual a {a - b}"
def multiplicacion(a, b): return f"La MULTIPLICACIÓN de a * b es igual a {a * b}"
def division(a, b): return f"La DIVISIÓN de a / b es igual a {a / b}"
# Retonar conjunto de operaciones
def operaciones_basicas(a, b):
    return (suma(a, b), resta(a, b), multiplicacion(a, b), division(a, b))
# Solicitar números ingresados.
def solicitar_numeros_usuario():
    a = int(input("Ingrese el primer número: \n"))
    b = int(input("Ingrese el segundo número: \n"))
    return (a, b)
# Validar números ingresados.
def validar_datos(numeros):
    a = numeros[0]
    b = numeros[1]
    def mayor_a_cero(numero):
        return True if numero > 0 else False
    return mayor_a_cero(a) and mayor_a_cero(b)
# Mostrar resultados
def muestro_resultados(resultados):
    for resultado in resultados:
        print(resultado)
# Verifica si el dato es correcto
numeros_del_usuario = solicitar_numeros_usuario()
sonValidos = validar_datos(numeros_del_usuario)
# Si son validos muestro resultado
if sonValidos:
    resultados = operaciones_basicas(numeros_del_usuario[0], numeros_del_usuario[1])
    muestro_resultados(resultados)
else:
    print("Alguno de los valores ingresados es menor o igual a 0")


# ----------------------------------------------------------------------------------------------- 

# EJERCICIO 8

# Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar 
# a la función para mostrar el resultado con dos decimales.
#  IMC = Peso (kg) / Estatura² (m²)

# Calcula el  IMC
def calcular_imc(peso, altura):
    return peso / (altura**2)
# Valida número ingresado.
def validar_dato(numero):
    return True if numero > 0 else False
# Solicita datos de entrada.
def solicitar_datos(tipo, textoDeEntrada = ""):
    if tipo == "peso":
        textoDeEntrada = "Ingresa tu peso en KGs"
    else:
        textoDeEntrada = "Ingresa tu altura en Mts"
    return float(input(f" {textoDeEntrada}: "))
# Variables para peso y altura
peso = solicitar_datos("peso")
altura = solicitar_datos("altura")
# Valida datos e invoca función de IMC
if validar_dato(peso) and validar_dato(altura):
    IMC = calcular_imc(peso, altura)
    print(f"El valor de IMC es de: {round(IMC, 2)}")
else:
    print("Alguna de las entradas es incorrecta, intentelo nuevamente")


# ----------------------------------------------------------------------------------------------- 

# EJERCICIO 9

# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

# Realiza la conversión
def celsius_a_fahrenheit(celsius):
    return (celsius * 1.8) + 32
# Valida número ingresado.
def validar_dato(numero):
    return True if numero > 0  else False
# Solicita datos de entrada.
def solicitar_dato():
    return float(input(f"Ingrese temperatura en grados Celsius: "))
# Variable que almacena celsius.
celsius = solicitar_dato()
# Valida datos e invoca función de celsius_a_fahrenheit
if validar_dato(celsius):
    temperatura_en_farenheit = celsius_a_fahrenheit(celsius)
    print(f"La temperatura en Farenheit es de: {round(temperatura_en_farenheit, 2)}F")
else:
    print("La entrada es incorrecta, intentelo nuevamente")

# ----------------------------------------------------------------------------------------------- 

# EJERCICIO 10

# Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

# Realiza el calculo de promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3
# Valida número ingresado.
def validar_dato(numero):
    return True if numero > 0  else False
# Solicita datos de entrada.
def solicitar_dato(letra):
    return int(input(f"Ingrese número {letra}: "))
# Variables que almacenan números.
a = solicitar_dato("a")
b = solicitar_dato("b")
c = solicitar_dato("c")
# Valida datos e invoca función calcular_promedio
if validar_dato(a) and validar_dato(b) and validar_dato(c):
    promedio = calcular_promedio(a, b, c)
    print(f"El promedio es de: {round(promedio, 2)}")
else:
    print("Alguna de las entradas es incorrecta, intentelo nuevamente")