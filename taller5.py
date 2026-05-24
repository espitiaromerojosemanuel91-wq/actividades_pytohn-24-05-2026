# Mini Sistema de Gestión de Inventario

inventario = []

# Función para agregar productos
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print(" Producto agregado correctamente.\n")


# Función para realizar una venta
def realizar_venta():
    nombre = input("Ingrese el nombre del producto vendido: ")

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():

            print(f"Stock disponible: {producto['cantidad']}")
            cantidad_vendida = int(input("Ingrese la cantidad vendida: "))

            if cantidad_vendida <= producto["cantidad"]:
                producto["cantidad"] -= cantidad_vendida
                print(" Venta realizada correctamente.\n")
            else:
                print(" No hay suficiente stock.\n")

            return

    print(" Producto no encontrado.\n")


# Función para mostrar el inventario
def mostrar_inventario():

    if len(inventario) == 0:
        print(" El inventario está vacío.\n")
        return

    print("\n INVENTARIO ")

    for i, producto in enumerate(inventario, start=1):
        print(f"{i}. Nombre: {producto['nombre']}")
        print(f"   Precio: ${producto['precio']}")
        print(f"   Cantidad: {producto['cantidad']}")
        

    print()


# Menú principal
while True:

    print(" MENÚ INVENTARIO ")
    print("1. Agregar producto")
    print("2. Realizar venta")
    print("3. Mostrar inventario")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()

    elif opcion == "2":
        realizar_venta()

    elif opcion == "3":
        mostrar_inventario()

    elif opcion == "4":
        print(" Saliendo del sistema...")
        break

    else:
        print(" Opción inválida.\n")