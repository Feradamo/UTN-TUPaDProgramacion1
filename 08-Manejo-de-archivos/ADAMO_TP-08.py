# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

def crear_archivo_inicial():
    # Lista de productos
    productos = [
        {
            "nombre": "Mouse",
            "precio": "30.000",
            "cantidad": "2",
        },
        {
            "nombre": "Teclado",
            "precio": "40.000",
            "cantidad": "4",
        },
        {
            "nombre": "Monitor",
            "precio": "70.000",
            "cantidad": "8",
        },
    ]
    # Creas un nuevo archivo
    with open('productos.txt', "w") as archivo:
        # Recorre productos y agrega en el archivo
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

def leer_productos():
    with open('productos.txt', 'r') as archivo:
        for linea in archivo:
            linea = linea.strip().split(",")
            print("------------------------------------------------------------------")
            print(f"Producto: {linea[0]} | Precio: ${linea[1]} | Cantidad: {linea[2]}")
            print("------------------------------------------------------------------")
            print("\n")

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

def agregar_nuevo_producto():
    # Lista de campos
    campos = ["nombre","precio","cantidad"]
    # Producto vacio en formato string
    nuevo_producto = ""
    # Recorre los campos
    for campo in campos:
        while True:
            valor_ingresado = input(f"Ingrese {campo} de nuevo producto: ")
            # Verifica si el valor ingresado esta vacio
            if valor_ingresado != "":
                nuevo_producto += valor_ingresado
                nuevo_producto += ","
                break
    # Escribe una nueva linea y elimina la "," final
    with open("productos.txt", "a") as archivo:
        archivo.write(f'{nuevo_producto.strip(",")}\n')

# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.

def cargar_productos():
    # Lista para almacenar productos
    productos = []
    # Lectura de archivo
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            # Desempaqueto lista
            nombre, precio, cantidad = linea.strip().split(",")
            # Crea nueva entrada
            producto = {
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            }
            # Agrega en lista de productos
            productos.append(producto)
    # Regresa productos
    return productos

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.

def buscar_por_nombre(productos):
    # Solicita nombre de producto a buscar
    while True:
        nombre_del_producto = input(f"Ingrese nombre del producto a buscar:  ")
        if nombre_del_producto != "":
            break
    # Match del producto
    producto_encontrado = ""
    # Recorre productos
    for producto in productos:
        # Se compara nombre de producto con valor ingresado
        if producto["nombre"].lower() == nombre_del_producto.lower():
            producto_encontrado = producto
            # Si se encuentra se sale del bucle
            break
    if producto_encontrado:
        print("------------------------------------------------------------------")
        print("El siguiente producto ha sido encotrando:")
        print(f"{producto_encontrado["nombre"]} | Precio: ${producto_encontrado["precio"]} | Cantidad: {producto_encontrado["cantidad"]}") 
        print("------------------------------------------------------------------")
    else:
        print("------------------------------------------------------------------")
        print("No se encontró el producto.")
        print("------------------------------------------------------------------")

# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.

def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    print("------------------------------------------------------------------")
    print("Los productos se han guardado correctamente")
    print("------------------------------------------------------------------")
    print("\n")

# Crea arvhivo inicial
crear_archivo_inicial()

# Lee productos
leer_productos()

# Agrega nuevo producto
agregar_nuevo_producto()

# Carga los productos en una lista y los devuelve
productos = cargar_productos()

# Busca por nombre
buscar_por_nombre(productos)

# Actualiza productos
guardar_productos(productos)