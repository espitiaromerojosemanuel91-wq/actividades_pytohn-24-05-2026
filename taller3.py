# Agenda de Contactos con Diccionario
agenda = {}
while True:
    print("\n AGENDA DE CONTACTOS ")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Mostrar contactos")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    # Añadir contacto
    if opcion == "1":
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el teléfono: ")
        agenda[nombre] = telefono
        print("Contacto guardado correctamente")
    # Buscar contacto
    elif opcion == "2":
        nombre = input("Ingrese el nombre a buscar: ")
        if nombre in agenda:
            print("Teléfono:", agenda[nombre])
        else:
            print("Contacto no encontrado")
    # Mostrar contactos
    elif opcion == "3":
        print("\nLista de contactos:")
        if len(agenda) == 0:
            print("La agenda está vacía")
        else:
            for nombre, telefono in agenda.items():

                print(nombre, "->", telefono)
    # Salir
    elif opcion == "4":
        print("Programa finalizado")

        break
    # Opción inválida
    else:
        print("Opción no válida")