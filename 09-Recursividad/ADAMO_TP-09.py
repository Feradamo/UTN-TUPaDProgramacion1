# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

# Devuelve en la terminal el factorial de un número
def factorial_de_un_numero(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial_de_un_numero(numero - 1)
        
# Repite x cantidad de veces
def repetir_x_cantidad(cantidad_de_veces):
    for numero in range(cantidad_de_veces):
        print(factorial_de_un_numero(numero + 1))

# Solicita, valida y retorna un número entero
def solicitar_numero():
    while True:
        numero_ingresado = input("Ingrese un numero entero mayor a 1:  ")
        if not numero_ingresado.isdigit():
            continue
        numero_ingresado = int(numero_ingresado)
        if numero_ingresado <= 1:
            continue
        break
    return numero_ingresado

cantidad_de_veces = solicitar_numero()
repetir_x_cantidad(cantidad_de_veces)

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

# Calcula el Fibonacci en la pociscion n
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Almacena y retorna serie.
def mostrar_serie_fibonacci(hasta_posicion):
    serie = []
    for i in range(hasta_posicion + 1):
        serie.append(fibonacci(i))
    return serie

# Solicita, valida y retorna un número entero.
def solicitar_numero():
    while True:
        numero_ingresado = input("Ingrese un numero entero mayor a 1:  ")
        if not numero_ingresado.isdigit():
            continue
        numero_ingresado = int(numero_ingresado)
        if numero_ingresado <= 1:
            continue
        break
    return numero_ingresado

posicion = solicitar_numero()
serie = mostrar_serie_fibonacci(posicion)
print(serie)

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛 M = 𝑛 ∗ 𝑛 (𝑚−1)
# Prueba esta función en un algoritmo general.

def factorial(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * factorial(base, exponente - 1) 

print(factorial(3, 4))

# 3 * 27
# 3 * 9
# 3 * 3
# 3 * 1
# 3

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

def conversion_a_binario(numero):
    if numero < 2:
        return str(numero)
    else:
        return conversion_a_binario(numero // 2) + str(numero % 2)
    
conversion_a_binario(10)

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
def suma_digitos(n):
    if n == 0:
        return 0
    return (n % 10) + suma_digitos(n // 10)

suma_digitos(10)

# 7) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
def contar_bloques(n):
    if n <= 0:
        return 0
    return n + contar_bloques(n - 1)

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0

    ultimo_digito = numero % 10

    if ultimo_digito == digito:
        conteo_actual = 1
    else:
        conteo_actual = 0
    return conteo_actual + contar_digito(numero // 10, digito)

