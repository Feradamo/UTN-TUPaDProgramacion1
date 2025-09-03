# EJERCICIO 1

# Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for x in range(0, 100 + 1):
    print(x)

# -----------------------------------------------------------------------------------------------

# EJERCICIO 2

# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# numero_entero = int(input("Ingrese un número entero: "))
# digitos = len(str(abs(numero_entero)))
# print("La cantidad de dígitos es:", digitos)

# Solicito un número entero al usuario
print("Ingrese un número entero")
# Almaceno el valor absoluto del entero
numero_entero = abs(int(input()))
# Inicializo variables de control
flag = True # controla la ejecución del bucle
count = 0   # conteo de dígitos
# Recorro potencias de 10 para evaluar la cantidad de dígitos
while flag:
    divisor = 10 ** count
    if numero_entero // divisor >= 1:
        count += 1
    elif numero_entero == 0:
        count += 1 
        flag = False
    else:
        flag = False
# Imprimo el resultado
print("La cantidad de dígitos es igual a: ", count) 

# -----------------------------------------------------------------------------------------------

# EJERCICIO 3

# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# Centinela del bucle
flag = False
while not flag:
    # Solicito números al usuario
    print("Ingrese el primer número entero: ")
    primer_numero_entero = int(input())
    print("Ingrese el segundo número entero: ")
    segundo_numero_entero = int(input())
    # Evaluo si son identicos
    if primer_numero_entero == segundo_numero_entero:
        print("Los números son identicos")
        print("Intentelo nuevamente")
        continue
    else:
        # Establezco un órden
        numero_mayor = max(primer_numero_entero, segundo_numero_entero)
        numero_menor = min(primer_numero_entero, segundo_numero_entero)
        # Compruebo si son consecutivos
        if numero_mayor - 1 == numero_menor:
            print("Los números son consecutivos")
            print("Intentelo nuevamente")
        else:
            flag = True # Si todo es correcto salgo del bucle
acumulador = 0 # Acumulador de sumas
# Sumo números dentro del rango excluyendo ambos números
for numero in range(numero_menor + 1, numero_mayor):
    acumulador += numero
# Devuelvo resultado
print("El número acumulado es igual a: ", acumulador)

# -----------------------------------------------------------------------------------------------

# EJERCICIO 4

# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0

flag = True # bandera del bucle
acumulador = 0 # contenedor de suma
while flag:
    print("Ingrese un número entero: ")
    numero_entero = int(input())
    if numero_entero == 0: # controla la ejecución del bucle
        flag = False
    acumulador += numero_entero # sumo numeros
    print("Llevas acumulado ---> ", acumulador)
# Devuelvo resultado
print("El número acumulado es igual a: ", acumulador)

# -----------------------------------------------------------------------------------------------

# EJERCICIO 5

# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numeros_aleatorios = random.randint(0, 9) # numero aleatorio entre 0 y 9
flag = True # bandera del bucle
intentos = 0 # suma de intentos
while flag:
    # Solicito número al usuario
    print("Ingrese un número entero entre 0-9: ")
    numero_entero = int(input())
    # Evaluo si se encuentra dentro del rango permitido
    if numero_entero < 0 or numero_entero > 9:
        print("El número ingresado esta fuera de rango")
    # Si es diferente al numeros_aleatorios
    elif numeros_aleatorios != numero_entero:
        print("\n Haz fallado intentalo nuevamente \n")
        intentos += 1 # Sumo intento
    else:
        # Si el resultado es correcto salgo del bucle
        flag = False 
# Devuelvo resultado
print("FELICITACIONES!!!")
print("El número de intentos es igual a: ", intentos)

# -----------------------------------------------------------------------------------------------

# EJERCICIO 6

# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# Set de variables
inico = 100
fin = 0
# Pinto los numeros entre inicio y fin -1
for numero in range(inico, fin - 1, -1):
    if numero % 2 == 0:
        print(numero)

# -----------------------------------------------------------------------------------------------

# EJERCICIO 7

# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario

while True:
    # Solicito número al usuario
    print("Ingrese un número entero mayor a 0: ")
    numero_entero = int(input())
    # Si es correcto salgo de bucle
    if numero_entero > 0:
        break
acumulador = 0 # Acumulador de suma
# Sumo números dentro del rango
for numero in range(0, numero_entero + 1):
    acumulador += numero
# Devuelvo resultado
print("El número acumulado es igual a: ", acumulador)

# -----------------------------------------------------------------------------------------------

# EJERCICIO 8

# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).