# Función para analizar calificaciones

def analizar_calificaciones(calificaciones):

    promedio = sum(calificaciones) / len(calificaciones)

    nota_alta = max(calificaciones)

    nota_baja = min(calificaciones)

    return (promedio, nota_alta, nota_baja)


# Lista 

notas = [4.5, 3.8, 5.0, 2.9, 4.2]


# Llamar función

resultado = analizar_calificaciones(notas)


# Mostrar resultados

print("Promedio:", round(resultado[0], 2))
print("Nota más alta:", resultado[1])
print("Nota más baja:", resultado[2])