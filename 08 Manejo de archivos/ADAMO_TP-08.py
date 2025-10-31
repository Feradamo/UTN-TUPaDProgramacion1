# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.

# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.

def mostrar_productos():
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            linea = linea.strip().split(",")
            print("------------------------------------------------------------------")
            print(f"Producto: {linea[0]} | Precio: ${linea[1]} | Cantidad: {linea[2]}")
            print("------------------------------------------------------------------")
        print("\n")

def solicitar_campo(campo):
    return input(f"Ingrese {campo} de producto:  ")

def agregar_producto():
    campos = ["Nombre","Precio","Cantidad"]
    nuevo_producto = ""
    for i in range(len(campos)):
        nuevo_producto += solicitar_campo(campos[i])
        nuevo_producto += "," if i < len(campos) - 1 else ""
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nuevo_producto}\n")
        
def cargar_productos():
    productos = []
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            producto = {
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            }
            productos.append(producto)
    return productos

def buscar_por_nombre(productos):
    print("\n")
    nombre_del_producto = solicitar_campo("nombre")
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre_del_producto.lower():
            encontrado = producto
            break
    if encontrado:
        print("------------------------------------------------------------------")
        print("Producto encontrado:", encontrado) 
        print("------------------------------------------------------------------")
    else:
        print("------------------------------------------------------------------")
        print("No se encontró el producto.")
        print("------------------------------------------------------------------")
    print("\n")

def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    print("------------------------------------------------------------------")
    print("Los productos se han guardado correctamente")
    print("------------------------------------------------------------------")
    print("\n")

def init():
    mostrar_productos()
    agregar_producto()
    productos = cargar_productos()
    buscar_por_nombre(productos)
    guardar_productos(productos)

init()