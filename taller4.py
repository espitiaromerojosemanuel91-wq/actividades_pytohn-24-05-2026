# Diccionario con factores de conversion
conversiones = {
    "metros_pies": 3.28084,
    "pies_metros": 0.3048,
    "cm_mm": 10,
    "mm_cm": 0.1,
    "kg_lb": 2.20462,
    "lb_kg": 0.453592
}

# Funcion para convertir unidades
def convertir(cantidad, origen, destino):
    # .lower() convierte el texto a minusculas para evitar errores
    clave = origen.lower() + "_" + destino.lower()

    if clave in conversiones:
        return cantidad * conversiones[clave]
    else:
        return "Conversion no disponible."

# Programa principal
try:
    cantidad = float(input("Ingrese la cantidad: "))
    unidad_origen = input("Unidad de origen (ej: metros, cm, kg): ")
    unidad_destino = input("Unidad de destino (ej: pies, mm, lb): ")

    resultado = convertir(cantidad, unidad_origen, unidad_destino)
    print("Resultado:", resultado)

except ValueError:
    print("Error: Por favor, ingrese un numero valido para la cantidad.")

