# importamos json
import json

# importamos os para borrar pantalla
import os

# importamos datatime para la hora de creacion de la copia de respaldo
from datetime import datetime

# importamos glob para la opcion 3 de la tienda
import glob

# mostramos el menu
def menu():
    print('''
==================================================
==             tienda MENU SENA CBA             ==
==================================================
=                                                =
= 1). Cargar Datos                               =
= 2). Copia de Respaldo                          =
= 3). Reparar Datos                              =
= 4). Grabar Nuevos Productos                    =
= 5). Borrar Productos                           =
= 6). Comprar Productos                          =
= 7). Imprimir Factura                           =
= 0). Cerrar App                                 =
=                                                =
==================================================      
''')


# creamos la entrada del dato
    try:
        option = int(input("Seleccione la opcion que necesita: "))
        return option

    except ValueError:
        print("CARACTER INVALIDO...")

# funcion para crear una copia de respaldo
def copiar_respaldo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as file:
            data = json.load(file)
            # Obtener la fecha y hora actual para el nombre del archivo
            fecha_hora_actual = datetime.now().strftime('%Y%m%d_%H%M%S')
            nombre_copia = f"{nombre_archivo.split('.')[0]}_copia_{fecha_hora_actual}.json"
            with open(nombre_copia, 'w') as copy_file:
                json.dump(data, copy_file, indent=4)
            print(f"Copia de respaldo '{nombre_copia}' creada correctamente.")
    except FileNotFoundError:
        print(f"No se encontró el archivo '{nombre_archivo}'.")

# creamos la pregunta de volver o no al menu
def ask_again():
    while True:
        return_menu = input("¿Desea volver al menú? (si/no): ").lower()
        if return_menu == "si":
            os.system("cls")
            return True
        elif return_menu == "no":
            return False
        else:
            print("Carácter inválido, por favor responda con 'si' o 'no'...")

# funciones para guardar y caragar archivos en json
def cargar_productos_desde_json(datos):
    try:
        with open(datos, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_productos_en_json(lista_productos, datos):
    with open(datos, 'w') as file:
        json.dump(lista_productos, file, indent=4)

# muestra la tabla con los productos para la opcion 1,4 y 5

def mostrar_productos(productos):
    print("="*79)
    print(f"|{'PRODUCTOS DISPONIBLES TIENDA SENA CBA':^77}|")
    print("="*79)
    print(f"| {'Codigo':<12}{'Descripción':<24}{'Inventario':<14}{'Precio de Venta':<26}|")
    print("="*79)
    
    for producto in productos:
        print(f"| {producto['codigo_producto']:<12}{producto['nombre_producto']:<24}{producto['inventario_producto']:<14}{producto['precio_producto']:<26}|")
    
    print("="*79)

def mostrar_carrito(productos_carrito, nombre_cliente, documento_cliente, direccion_cliente):
    print("=" * 79)
    print(f"|{'FACTURA DE ' + nombre_cliente:^77}|")
    print("=" * 79)
    print(f"| Documento: {documento_cliente:<65}|")
    print(f"| Dirección: {direccion_cliente:<65}|")
    print("=" * 79)
    print(f"| {'Código':<12}{'Descripción':<24}{'Cantidad':<14}{'Precio':<12}{'Subtotal':<14}|")
    print("=" * 79)
    
    total = 0
    for producto in productos_carrito:
        codigo = producto['codigo_producto']
        descripcion = producto['nombre_producto']
        cantidad = producto['cantidad_producto']
        precio = producto['precio_producto']
        subtotal = producto['subtotal_producto']
        total += subtotal
        print(f"| {codigo:<12}{descripcion:<24}{cantidad:<14}{precio:<12.2f}{subtotal:<14}|")
    
    print("=" * 79)
    print(f"| {'TOTAL':<52}{total:<24}|")
    print("=" * 79)

def mostrar_productos_comprados(productos_carrito):
    print("=" * 40)
    print(f"| {'Código':<18}{'Valor':<19}|")
    print("=" * 40)
    
    for producto in productos_carrito:
        descripcion = producto['nombre_producto']
        valor = producto['subtotal_producto']
        print(f"| {descripcion:<18}{valor:<19}|")
    
    print("=" * 40)

# Función para listar las copias de respaldo disponibles
def listar_copias_respaldo():
    copias = glob.glob('datos_copia_*.json')
    if not copias:
        print("No existen copias de respaldo disponibles.")
        return None
    else:
        print("Copias de respaldo disponibles:")
        for i, copia in enumerate(copias, start=1):
            print(f"{i}. {copia}")
        return copias

# Función para cargar una copia de respaldo seleccionada
def cargar_copia_respaldo(copias):
    try:
        seleccion = int(input("Seleccione el número de la copia de respaldo a cargar: "))
        if 1 <= seleccion <= len(copias):
            copia_seleccionada = copias[seleccion - 1]
            with open(copia_seleccionada, 'r') as file:
                productos = json.load(file)
                print(f"Copia de respaldo '{copia_seleccionada}' cargada correctamente.")
                return productos
        else:
            print("Selección inválida.")
            return None
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")
        return None









