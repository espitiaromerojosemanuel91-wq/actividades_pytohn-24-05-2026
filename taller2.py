# 1. Creamos la lista de compras vacia
lista_compras = []

# 2. Iniciamos el bucle while para el menu interactivo
while True:
    print("\nLISTA DE COMPRAS")
    print("1. Agregar item a la lista")
    print("2. Eliminar item de la lista")
    print("3. Ver la lista completa")
    print("4. Salir")
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        item = input("Ingrese el nombre del articulo a agregar: ")
        lista_compras.append(item)  # Agrega al final de la lista
        print(f"{item} ha sido agregado correctamente.")
        
    elif opcion == "2":
        item = input("Ingrese el nombre del articulo a eliminar: ")
        if item in lista_compras:
            lista_compras.remove(item)  # Elimina el articulo de la lista
            print(f"{item} ha sido eliminado correctamente.")
        else:
            print(f"El articulo {item} no esta en la lista.")
            
    elif opcion == "3":
        print("\nItems en tu lista de compras:")
        if len(lista_compras) == 0:
            print("La lista esta vacia.")
        else:
            # Recorremos la lista para mostrar cada elemento ordenado
            for i, articulo in enumerate(lista_compras, 1):
                print(f"{i}. {articulo}")
                
    elif opcion == "4":
        print("Programa finalizado. gracias por comprar!")
        break  # Rompe el bucle while para salir del programa
        
    else:
        print("Opcion invalida. Intente de nuevo.")

