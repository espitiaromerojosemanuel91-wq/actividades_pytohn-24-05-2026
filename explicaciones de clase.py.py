# SENTENCIA MATCH (PYTHON 3.10+) => SWITCH

dia = int(input("Ingrese el número del día: "))

# SENTENCIA MATCH

match dia:

    case 1:
        print("Lunes")

    case 2:
        print("Martes")

    case 3:
        print("Miércoles")

    case 4:
        print("Jueves")

    case 5:
        print("Viernes")

    case 6:
        print("Sábado")

    case 7:
        print("Domingo")

    case _:
        print("Día incorrecto")