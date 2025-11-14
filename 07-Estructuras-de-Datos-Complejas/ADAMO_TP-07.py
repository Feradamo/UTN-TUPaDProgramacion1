# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

# Diccionario de frutas
precios_frutas = {
    'Banana': 1200, 
    'Ananá': 2500, 
    'Melón': 3000, 
    'Uva': 1450
}
# Añade nuevas frutas
precios_frutas["Naranaja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
# Pinta diccionario actualizado
print(precios_frutas)

# -----------------------------------------------------------------------------------------------

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

# Actualiza precios de frutas
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

# -----------------------------------------------------------------------------------------------

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

# Obtiene keys y devuelve lista
frutas = list(precios_frutas.keys()) 
# Pinta lista
print(frutas)

# -----------------------------------------------------------------------------------------------

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

# Variables del programa
maximo_de_usuarios = 5
numeros_telefonicos = {}

# Valida datos de entrada
def validar_contacto(key, value):
    return key != "" and value.isdigit()
# Solicita datos al usuario
def solicitar_contacto():
    key = input("Ingrese un nombre de contacto:  ")
    value = input("Ingrese un número de contacto:  ")
    return (key, value)
# Carga 5 usuarios
def cargar_cinco_usuarios():
    counter = 0
    while counter < maximo_de_usuarios:
        print("\n")
        print(f"Ingrese contacto número {counter + 1}")
        key, value = solicitar_contacto()
        es_valido = validar_contacto(key, value)
        # Si son validos se agregan a numeros_telefonicos
        if es_valido:
            numeros_telefonicos[key] = value
            counter += 1
        else:
            print("\n")
            print("------------------------------------")
            print("El contacto ingresado es invalido!")
            print("Intentelo nuevamente!")
            print("------------------------------------")
            print("\n")
# Busca contacto en numeros_telefonicos
def busqueda_contacto():
    print("\n")
    nombre = input("Ingrese el nombre del contacto a buscar:  ")
    if nombre in numeros_telefonicos:
        print(f"El número de telefoo asociado a {nombre} es: {numeros_telefonicos[nombre]}")
    else:
        print("El nombre ingresado no existe!")
# Funcion de inicio
def init():
    cargar_cinco_usuarios()
    print(numeros_telefonicos)
    busqueda_contacto()
# Dispara funcion de inicio
init()

# -----------------------------------------------------------------------------------------------

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

# Solicta frase al usuario
def solicita_frase():
    return input("Ingrese una frase!")
# Convierte la misma en un set
def convierte_en_set(conjunto_de_palabras):
    return set(conjunto_de_palabras)
# Muestra palabras unicas
def muestra_palabras_unicas(palabras_unicas):
    for palabra in palabras_unicas:
        print(palabra)
# Muestra cantidad de veces
def muestra_cantidad_de_veces(conjunto_de_palabras):
    diccionario_de_cantidades = {}
    for palabra in conjunto_de_palabras:
        diccionario_de_cantidades[palabra] = conjunto_de_palabras.count(palabra)
    print(diccionario_de_cantidades)
# Funcion de inicio
def init():
    frase = solicita_frase()
    conjunto_de_palabras = frase.split(" ")
    palabras_unicas = convierte_en_set(conjunto_de_palabras)
    muestra_palabras_unicas(palabras_unicas)
    muestra_cantidad_de_veces(conjunto_de_palabras)
# Dispara funcion de inicio
init()

# -----------------------------------------------------------------------------------------------

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
alumnos = {}
maximo_de_alumnos = 3
cantidad_de_notas = 3

# Devuelve nombre
def ingresar_nombre():
    return input("Ingrese nombre:  ")
# Devuelve notas
def ingresar_notas():
    notas = []
    for nota in range(cantidad_de_notas):
        nota = input("Ingrese nota:  ")
        notas.append(int(nota))
    return tuple(notas)
# Solicita cantidad de alumnos
def cargar_x_cantidad_de_alumnos():
    counter = 0
    while counter < maximo_de_alumnos:
        name = ingresar_nombre()
        notas = ingresar_notas()
        alumnos[name] = notas
        counter += 1
    print("////////////////")
    print(alumnos)
    print("////////////////")
# Muestra promedio
def mostrar_promedio():
    resultado = ""
    counter = 1
    for alumno in alumnos: 
        nombre = alumno
        notas = list(alumnos[alumno])
        promedio = sum(notas) / cantidad_de_notas
        resultado += f"El promedio de {nombre} es igual a: {round(promedio, 2)}"
        resultado += "\n" if counter < maximo_de_alumnos else ""
        counter += 1
    print("////////////////")
    print(resultado)
    print("////////////////")
# INIT ejercicio
def init():
    cargar_x_cantidad_de_alumnos()
    mostrar_promedio()

# INIT
init()

# -----------------------------------------------------------------------------------------------

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

aprobados_parcial_1 = {101, 105, 110, 115, 120}
aprobados_parcial_2 = {105, 110, 112, 125, 130}
# Muestra los que aprobaron ambos parciales
def aprobaron_ambos_parciales():
    print(aprobados_parcial_1 & aprobados_parcial_2)
# Muestra los que aprobaron uno de los dos
def uno_de_los_dos():
    print(aprobados_parcial_1 ^ aprobados_parcial_2)
# Muestra los que aprobaron al menos uno
def al_menos_uno():
    print(aprobados_parcial_1 | aprobados_parcial_2)

# Conjunto de funciones
aprobaron_ambos_parciales()
uno_de_los_dos()
al_menos_uno()

# -----------------------------------------------------------------------------------------------

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

# Funcion de productos
def stock_de_productos():
    stock_de_productos = {"martillo": 10, "pinza": 2, "destornillador": 20, "clavos": 200}
    # Consulta stock
    def consultar_stock(producto):
        if producto in stock_de_productos:
            stock = stock_de_productos[producto]
            print(f"El stock de {producto} es: {stock}")
        else: 
            print("El producto solicitado no existe!!")
    # Agrega unidades
    def agregar_unidades(producto, cantidad):
        if producto in stock_de_productos:
            stock_de_productos[producto] = cantidad 
        print(stock_de_productos)
    # Agrega nuevo producto
    def agregar_nuevo_producto(producto, cantidad):
        stock_de_productos[producto] = cantidad 
        print(stock_de_productos)
    # Conjunto de funciones
    consultar_stock("martillo")
    agregar_unidades("martillo", 14)
    agregar_nuevo_producto("alicate", 11)
# Dispara funcion de productos
stock_de_productos()

# -----------------------------------------------------------------------------------------------

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.

# Diccionario de ejemplo
agenda = {
    ("lunes", "10:00"): "Reunion",
    ("martes", "15:00"): "Clase de ingles",
}
# Consulta actividades
def consultar_actividad(dia, horario):
    if (dia, horario) in agenda:
        print(agenda[(dia, horario)])
    else:
        print("El valor ingresado no existe!!")
# Dispara la funcion
consultar_actividad("lunes", "10:00")

# -----------------------------------------------------------------------------------------------

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores

# Diccionario de ejemplo
original = {"Argentina": "Buenos aires", "Chile": "Santiago"}
# Invierte diccionario key -> value
def invertir_diccionario(diccionario):
    nuevo_diccionario = {}
    for elemento in diccionario:
        key = diccionario[elemento]
        value = elemento
        nuevo_diccionario[key] = value
    return nuevo_diccionario
# Muestro en terminal
print(invertir_diccionario(original))