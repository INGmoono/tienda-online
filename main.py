# importamos el modulo de funciones y clases
from funciones import *
from clases import *
# importamos os para poder borrar la pantalla
import os




def main():
    productos = cargar_productos_desde_json('datos.json')  # Cargamos los productos desde el archivo JSON
    while True:
        option = menu()
        
        if option == 0:
            os.system("cls")
            print('''
+-------------------------------------------------+
|         GRACIAS POR VISITAR LA TIENDA           |
+-------------------------------------------------+''')
            break

        elif option == 1:
            os.system("cls")
            productos = cargar_productos_desde_json('datos.json')
            mostrar_productos(productos)
        

        elif option == 2:
            os.system("cls")
            copiar_respaldo('datos.json')

        elif option == 3:
            os.system("cls")
            copias = listar_copias_respaldo()
            if copias:
                productos = cargar_copia_respaldo(copias)
                if productos:
                    guardar_productos_en_json(productos, 'datos.json')

        elif option == 4:
            os.system("cls")
            mostrar_productos(productos)
            codigo = input("Ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ").upper()
            inventario = int(input("Ingrese las unidades disponibles: "))
            precio = float(input("Ingrese el precio del producto: "))
            nuevo_producto = Producto(codigo, nombre, inventario, precio)
            productos_venta = ProductosVenta(productos)
            productos_venta.agregar_producto(nuevo_producto)
            productos = productos_venta.get_lista_productos()
            guardar_productos_en_json(productos, 'datos.json')  # Guardamos los productos actualizados en el archivo JSON
            
        elif option == 5:
            os.system("cls")
            mostrar_productos(productos)
            codigo = input("Ingrese el código del producto a borrar: ")
            productos_venta = ProductosVenta(productos)
            productos_venta.verificarborrarproductos(codigo)
            productos = productos_venta.get_lista_productos()
            guardar_productos_en_json(productos, 'datos.json') 

        elif option == 6:
            os.system("cls")
            mostrar_productos(productos)
            carrito = CarritoCompra("", "", "", [])
            carrito.documentocliente()
            carrito.nombrecliente()
            carrito.direccioncliente()
            carrito.nuevo_producto(ProductosVenta(productos))
            print("PRODUCTOS COMPRADOS:")
            mostrar_productos_comprados(carrito.listaproductos())        
            
        elif option == 7:
            os.system("cls")
            if carrito:
                mostrar_carrito(carrito.listaproductos(), carrito.get_nombre_cliente(), carrito.get_documento_cliente(), carrito.get_direccion_cliente())
                print("Imprimir Factura")
            else:
                print("No hay productos en el carrito para imprimir una factura.")
            
        else:
            os.system("cls")
            print("Opción no válida, por favor intente nuevamente.")
        
        if not ask_again():
            print("GRACIAS POR VISITAR LA TIENDA...")
            break

if __name__ == "__main__":
    main()

