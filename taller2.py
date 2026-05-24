# 1. Creamos la lista de compras vacía
lista_compras = []
# 2. Iniciamos el bucle while para el menú interactivo
while True:
    print("\n--- LISTA DE COMPRAS ---")
    print("1. Agregar ítem a la lista")
    print("2. Eliminar ítem de la lista")
    print("3. Ver la lista completa")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        item = input("Ingrese el nombre del artículo a agregar: ")
        lista_compras.append(item)  # Agrega al final de la lista
        print(f"'{item}' ha sido agregado correctamente.")
    elif opcion == "2":
        item = input("Ingrese el nombre del artículo a eliminar: ")
        if item in lista_compras:
            lista_compras.remove(item)  # Elimina el artículo de la lista
            print(f"'{item}' ha sido eliminado correctamente.")
        else:
            print(f"El artículo '{item}' no está en la lista.")
    elif opcion == "3":
        print("\nItems en tu lista de compras:")
        if len(lista_compras) == 0:
            print("La lista está vacía.")
        else:
            # Recorremos la lista para mostrar cada elemento ordenado
            for i, articulo in enumerate(lista_compras, 1):
                print(f"{i}. {articulo}")
    elif opcion == "4":
        print("Programa finalizado. ¡gracias por comprar!")
        break  # Rompe el bucle while para salir del programa
    else:
        print("Opción inválida. Intente de nuevo.")
