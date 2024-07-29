from funciones import *


#-----------------------------------------------------------clase producto---------------------------------------------------------------
# creamos la clase producto
class Producto:
    def __init__(self, codigo_producto, nombre_producto, inventario_producto, precio_producto):
        self.__codigo_producto = codigo_producto.zfill(6) # definimos los atributos
        self.__nombre_producto = nombre_producto # definimos los atributos
        self.__inventario_producto = inventario_producto # definimos los atributos
        self.__precio_producto = precio_producto # definimos los atributos

# creamos setter y getter
    def set_codigo_producto(self, value):
        self.__codigo_producto = value.zfill(6)
# creamos get codigo producto
    def get_codigo_producto(self):
        return self.__codigo_producto
# creamos set nombre producto
    def set_nombre_producto(self, value):
        self.__nombre_producto = value
# creamos el get de nombre producto
    def get_nombre_producto(self):
        return self.__nombre_producto
# creamos el set de inventarioproducto
    def set_inventario_producto(self, value):
        self.__inventario_producto = value
# creamos el get de inventario producto
    def get_inventario_producto(self):
        return self.__inventario_producto
# creamos set precio producto
    def set_precio_producto(self, value):
        self.__precio_producto = value
# creamos get precio producto
    def get_precio_producto(self):
        return self.__precio_producto
# creamos data para agregar al json
    def data(self):
        return {
            "codigo_producto": self.__codigo_producto,
            "nombre_producto": self.__nombre_producto,
            "inventario_producto": self.__inventario_producto,
            "precio_producto": self.__precio_producto
        }        

#-----------------------------------------------------------clase productos venta---------------------------------------------------------------
class ProductosVenta:
    def __init__(self, lista_productos):
        self.__lista_productos = lista_productos
# creamos set lista productos
    def set_lista_productos(self, value):
        self.__lista_productos = value
# creamos get lista productos
    def get_lista_productos(self):
        return self.__lista_productos
# metodos propios
# revisa cuantas unidades existen de un producto
    def verificar_existencia(self, codigo_producto, cantidad):
        codigo_producto = codigo_producto.zfill(6)
        for prod in self.__lista_productos:
            if prod['codigo_producto'] == codigo_producto:
                if prod['inventario_producto'] >= cantidad:
                    return True
                else:
                    print(f"No hay suficientes unidades disponibles para '{prod['nombre_producto']}'.")
                    return False
        print(f"No se encontró ningún producto con código '{codigo_producto}'.")
        return False
# resta los productos comprados con los de la tinda
    def reducir_inventario(self, codigo_producto, cantidad):
        codigo_producto = codigo_producto.zfill(6)
        for prod in self.__lista_productos:
            if prod['codigo_producto'] == codigo_producto:
                prod['inventario_producto'] -= cantidad
                break
# agrega los datos al carrito
    def agregar_al_carrito(self, codigo_producto, cantidad):
        codigo_producto = codigo_producto.zfill(6)
        for prod in self.__lista_productos:
            if prod['codigo_producto'] == codigo_producto:
                nombre_producto = prod['nombre_producto']
                precio_producto = prod['precio_producto']
                subtotal = cantidad * precio_producto
                producto_carrito = ProductoCarrito(codigo_producto, nombre_producto, cantidad, precio_producto, subtotal)
                return producto_carrito.data()
        return None
# borra el producto por medio del codigo
    def borrarproductos(self, codigo):
        codigo = codigo.zfill(6)
        productos_restantes = [prod for prod in self.__lista_productos if prod['codigo_producto'] != codigo]
        if len(productos_restantes) < len(self.__lista_productos):
            self.__lista_productos = productos_restantes
            print(f"Producto con código '{codigo}' eliminado correctamente.")
        else:
            print(f"No se encontró ningún producto con código '{codigo}'.")
# pregunta si esta seguro de borrar
    def verificarborrarproductos(self, codigo):
        codigo = codigo.zfill(6)
        for prod in self.__lista_productos:
            if prod['codigo_producto'] == codigo:
                nombre_producto = prod['nombre_producto']
                while True:
                    confirmacion = input(f"¿Está seguro de borrar el producto '{nombre_producto}'? (si/no): ").lower()
                    if confirmacion == 'si':
                        self.borrarproductos(codigo)
                        break
                    elif confirmacion == 'no':
                        break
                    else:
                        print("Caracter inválido. Por favor responda 'si' o 'no'.")
                break
        else:
            print(f"No se encontró ningún producto con código '{codigo}'.")

# agrega un nuevo producto
    def agregar_producto(self, producto):
        codigo_nuevo = producto.get_codigo_producto()
        codigos_existentes = [prod['codigo_producto'] for prod in self.__lista_productos]

        if codigo_nuevo in codigos_existentes:
            print(f"El código de producto '{codigo_nuevo}' ya existe. No se puede agregar.")
        else:
            self.__lista_productos.append(producto.data())
            print(f"Producto '{producto.get_nombre_producto()}' agregado correctamente.")

#-----------------------------------------------------------clase producto carrito---------------------------------------------------------------

class ProductoCarrito:
    def __init__(self, codigo_producto, nombre_producto, cantidad_producto, precio_producto, subtotal_producto):
        self.__codigo_producto = codigo_producto
        self.__nombre_producto = nombre_producto
        self.__cantidad_producto = cantidad_producto
        self.__precio_producto = precio_producto
        self.__subtotal_producto = subtotal_producto

# creamos set codigo producto
    def set_codigo_producto(self, value):
        self.__codigo_producto = value
# creamos get codigo producto
    def get_codigo_producto(self):
        return self.__codigo_producto
# creamos set nombre producto
    def set_nombre_producto(self, value):
        self.__nombre_producto = value
# creamos get nombre producto
    def get_nombre_producto(self):
        return self.__nombre_producto
# creamos set cantidad producto
    def set_cantidad_producto(self, value):
        self.__cantidad_producto = value
# creamos get cantidad producto
    def get_cantidad_producto(self):
        return self.__cantidad_producto
# creamos set precio producto
    def set_precio_producto(self, value):
        self.__precio_producto = value                         
# creamos get precio producto
    def get_precio_producto(self):
        return self.__precio_producto
# creamos set subtotal precio
    def set_subtotal_precio(self, value):
        self.__subtotal_producto = value
# creamos get subtotal precio
    def get_subtotal_precio(self):
        return self.__subtotal_producto

# metodos propios
    def data(self):
        return {
            "codigo_producto": self.__codigo_producto,
            "nombre_producto": self.__nombre_producto,
            "cantidad_producto": self.__cantidad_producto,
            "precio_producto": self.__precio_producto,
            "subtotal_producto": self.__subtotal_producto
        }

#-----------------------------------------------------------clase carrito compra---------------------------------------------------------------

class CarritoCompra:
    def __init__(self, documento_cliente, nombre_cliente, direccion_cliente, productos_carrito):
        self.__documento_cliente = documento_cliente
        self.__nombre_cliente = nombre_cliente
        self.__direccion_cliente = direccion_cliente
        self.__productos_carrito = productos_carrito

# creamos set documento cliente 
    def set_documento_cliente(self, value):
        self.__documento_cliente = value
# creamos get documento cliente 
    def get_documento_cliente(self):
        return self.__documento_cliente
# creamos set nombre cliente
    def set_nombre_cliente(self, value):
        self.__nombre_cliente = value
# creamos get nombre cliente 
    def get_nombre_cliente(self):
        return self.__nombre_cliente
# creamos set direccion cliente
    def set_direccion_cliente(self, value):
        self.__direccion_cliente = value
# creamos get direccion cliente
    def get_direccion_cliente(self):
        return self.__direccion_cliente
# creamos set productos carritos
    def set_productos_carrito(self, value):
        self.__productos_carrito = value
# creamos get productos carrito
    def get_productos_carrito(self):
        return self.__productos_carrito

# metodos propios  
    def documentocliente(self):
        while True:
            documento = input("Ingrese su número de documento: ")
            if documento.isdigit() and 7 <= len(documento) <= 10:
                self.set_documento_cliente(documento)
                print(f"Documento {documento} registrado correctamente.")
                break
            else:
                print("Su documento tiene errores, revíselo.")

    def nombrecliente(self):
        while True:
            nombre = input("ingrese su nombre: ")  
            nombre_con_espacion = nombre.replace(" ", "")  
            if nombre_con_espacion.isalpha():
                self.set_nombre_cliente(nombre)
                print(f"El Nombre '{nombre}' ha sido registrado correctamente.")
                break
            else:
                print("Digite el nombre correctamente.")

    def direccioncliente(self):
        direccion = input("Ingrese su dirrecion: ")
        self.set_direccion_cliente(direccion)
        print(f"la direccion {direccion} se agrego correctamente.")


    def validar_codigo_producto(self, codigo_producto):
        if codigo_producto.isdigit() and len(codigo_producto) == 6:
            return True
        return False

    def validar_cantidad(self, cantidad):
        if cantidad.isdigit() and int(cantidad) > 0:
            return True
        return False

    def validar_codigo_producto(self, codigo_producto):
        if codigo_producto.isdigit() and 1 <= len(codigo_producto) <= 6:
            return True
        return False

    def validar_confirmacion(self, confirmacion):
        return confirmacion in ['si', 'no']

    def nuevo_producto(self, productos_venta):
        while True:
            codigo_producto = input("Ingrese el código del producto: ")
            while not self.validar_codigo_producto(codigo_producto):
                print("Código de producto inválido. Debe ser un número de entre 1 y 6 dígitos.")
                codigo_producto = input("Ingrese el código del producto: ")

            codigo_producto = codigo_producto.zfill(6)  # Rellenar con ceros a la izquierda, para así pasar el filtro de 6 dígitos

            cantidad = input("Ingrese la cantidad a comprar: ")
            while not self.validar_cantidad(cantidad):
                print("Cantidad inválida. Debe ser un número entero positivo.")
                cantidad = input("Ingrese la cantidad a comprar: ")

            cantidad = int(cantidad)
            if productos_venta.verificar_existencia(codigo_producto, cantidad):
                producto_agregado = productos_venta.agregar_al_carrito(codigo_producto, cantidad)
                if producto_agregado:
                    self.__productos_carrito.append(producto_agregado)
                    productos_venta.reducir_inventario(codigo_producto, cantidad)  # Reducir el inventario
                    # Guardar los productos actualizados en el archivo JSON
                    guardar_productos_en_json(productos_venta.get_lista_productos(), 'datos.json')
                    print(f"Producto '{producto_agregado['nombre_producto']}' agregado al carrito.")
                else:
                    print(f"No se pudo agregar el producto '{codigo_producto}' al carrito.")

            agregar_otro = input("¿Desea agregar otro producto? (si/no): ").lower()
            while not self.validar_confirmacion(agregar_otro):
                print("Respuesta inválida. Por favor, responda 'si' o 'no'.")
                agregar_otro = input("¿Desea agregar otro producto? (si/no): ").lower()

            if agregar_otro == 'no':
                break
    
    def listaproductos(self):
        return self.__productos_carrito
