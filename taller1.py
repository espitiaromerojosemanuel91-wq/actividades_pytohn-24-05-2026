## Función para analizar calificaciones
def analizar_calificaciones(calificaciones):
    # Validar que la lista no esté vacía para evitar errores de división por cero
    if not calificaciones:
        return (0, 0, 0)
        
    promedio = sum(calificaciones) / len(calificaciones)
    nota_alta = max(calificaciones)
    nota_baja = min(calificaciones)
    return (promedio, nota_alta, nota_baja)


# Lista vacía para almacenar las entradas del usuario
notas = []

print("--- Ingreso de Calificaciones ---")
print("Escribe una nota y presiona Enter. Cuando termines, escribe 'fin'.")

# Bucle para capturar los datos del usuario
while True:
    entrada = input("Ingresa una nota (o 'fin' para terminar): ").strip().lower()
    
    # Condición de salida
    if entrada == 'fin':
        break
        
    try:
        # Convertir la entrada a número decimal
        nota = float(entrada)
        notas.append(nota)
    except ValueError:
        # Manejo de error si el usuario no ingresa un número válido
        print("¡Error! Por favor ingresa un número válido o la palabra 'fin'.")


# Validar si el usuario ingresó al menos una nota antes de calcular
if len(notas) > 0:
    # Llamar función
    resultado = analizar_calificaciones(notas)

    # Mostrar resultados
    print("\n--- Resultados del Análisis ---")
    print("Promedio:", round(resultado[0], 2))
    print("Nota más alta:", resultado[1])
    print("Nota más baja:", resultado[2])
else:
    print("\nNo se ingresaron calificaciones para analizar.")
