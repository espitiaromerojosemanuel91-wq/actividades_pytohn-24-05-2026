# Agenda de Contactos con Diccionario
agenda = {}

while True:
    print("\nAGENDA DE CONTACTOS")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Mostrar contactos")
    print("4. Salir")
    
    opcion = input("Seleccione una opcion: ")
    
    # Añadir contacto
    if opcion == "1":
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el telefono: ")
        agenda[nombre] = telefono
        print("Contacto guardado correctamente")
        
    # Buscar contacto
    elif opcion == "2":
        nombre = input("Ingrese el nombre a buscar: ")
        if nombre in agenda:
            print("Telefono:", agenda[nombre])
        else:
            print("Contacto no encontrado")
            
    # Mostrar contactos
    elif opcion == "3":
        print("\nLista de contactos:")
        if len(agenda) == 0:
            print("La agenda esta vacia")
        else:
            for nombre, telefono in agenda.items():
                print(nombre, "->", telefono)
                
    # Salir
    elif opcion == "4":
        print("Programa finalizado")
        break
        
    # Opcion invalida
    else:
        print("Opcion no valida")
