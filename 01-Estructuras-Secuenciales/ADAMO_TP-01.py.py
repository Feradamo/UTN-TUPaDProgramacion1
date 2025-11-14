# EJERCICIO 1
# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola mundo!")

# -----------------------------------------------------------------------------------------------

# EJERCICIO 2
# Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# -----------------------------------------------------------------------------------------------

# EJERCICIO 3
# Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_de_residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}")

# -----------------------------------------------------------------------------------------------

# EJERCICIO 4
# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
PI = 3.14
radio_del_circulo = float(input("Ingrese radio del circulo en cm: "))
area = radio_del_circulo ** 2 * PI
print(area, "cm2")

# -----------------------------------------------------------------------------------------------

# EJERCICIO 5
# Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

cantidad_de_segundos = int(input("Ingrese cantidad de segundos: "))
equivalente_a_horas = round(cantidad_de_segundos / 3600, 2) # 60 segundos x 60 minutos = 3600s
print(f"{cantidad_de_segundos} segundos equivalen a {equivalente_a_horas} hrs")

# -----------------------------------------------------------------------------------------------

# EJERCICIO 6
# Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
numero = int(input("Ingrese un número: ")) 

print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

# -----------------------------------------------------------------------------------------------

# EJERCICIO 7
# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero_1 = int(input("Ingrese el primer número: ")) 
numero_2 = int(input("Ingrese el segundo número: ")) 

suma = numero_1 + numero_2
division = numero_1 / numero_2
multiplicacion = numero_1 * numero_2
resta = numero_1 - numero_2

print(f"La suma es igual a {suma}")
print(f"La division es igual a {division}")
print(f"La multiplicacion es igual a {multiplicacion}")
print(f"La resta es igual a {resta}")

# -----------------------------------------------------------------------------------------------

# EJERCICIO 8
# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo.

altura = float(input("Ingrese su altura en m: "))
peso = float(input("Ingrese su peso en kg: "))
indice_de_masa_corporal = peso / ( altura ** 2 )
print(f"Tu índice de masa corporal es: {round(indice_de_masa_corporal, 2)}")
# -----------------------------------------------------------------------------------------------

# EJERCICIO 9
# Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

grados_celsius = float(input("Ingrese temperatura en grados Celsius: "))
grados_en_fahrenheit = grados_celsius * 9/5 + 32
print(f"{grados_celsius}°C equivalen a {grados_en_fahrenheit}°F")

# -----------------------------------------------------------------------------------------------

# EJERCICIO 10
# Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

numero_1 = int(input("Ingrese el primer número: ")) 
numero_2 = int(input("Ingrese el segundo número: ")) 
numero_3 = int(input("Ingrese el tercer número: ")) 
suma = numero_1 + numero_2 +numero_3
promedio = suma / 3
print(f"El promedio de los números ingresados es igual a: {promedio}")