```python
# ==========================================
# 1. BUCLES FOR BÁSICOS
# ==========================================

# Recorrer una cadena

lenguaje = "Python"

for letra in lenguaje:
    print(letra)


# Recorrer una lista

frutas = ["manzana", "banana", "pera"]

for fruta in frutas:

    if fruta == "banana":
        continue  # Salta esta iteración

    print(fruta)

else:
    print("Se han recorrido todas las frutas")


# ==========================================
# 2. RECORRER RANGOS DE NÚMEROS
# ==========================================

for i in range(5):
    print(i)

for i in range(1, 6):
    pass


# ==========================================
# 3. RECORRER TUPLAS Y DICCIONARIOS
# ==========================================

# Tupla

colores = ("rojo", "verde", "azul")

for color in colores:
    print(color)


# Diccionario

diccionario_aprendices = {
    "nombre": "Felipe",
    "edad": 32,
    "ciudad": "Duitama"
}

for clave, valor in diccionario_aprendices.items():
    print(f"{clave}: {valor}")


# ==========================================
# 4. BUCLE WHILE
# ==========================================

contador = 1

while contador <= 5:

    print(f"El contador vale: {contador}")

    contador += 1


# Ejemplo WHILE simple

i = 1

while i < 6:

    print("Hola, soy un bucle WHILE")

    i += 1


# Ejemplo con BREAK

i = 0

while i < 6:

    print("Hola, soy un bucle WHILE")

    if i == 3:
        break

    i += 1


# Ejemplo con CONTINUE

i = 0

while i < 6:

    i += 1

    if i == 3:
        continue

    print(i)


# ==========================================
# 5. JUEGO SIMPLE DE POKEMON
# ==========================================

puntos_vida = 100

pokemon = input("Elige tu pokemon: ")

while puntos_vida > 0:

    print(f"Tu {pokemon} tiene {puntos_vida} puntos de vida")

    ataque = int(input("Ingresa el daño del ataque: "))

    puntos_vida -= ataque

print(f"Tu {pokemon} ha sido derrotado")


# ==========================================
# 6. JUEGO POKEMON MEJORADO
# ==========================================

import random

tu_pokemon = input(
    "Elige tu pokemon (Pikachu, Charmander o Bulbasaur): "
)

enemigo = "Mewtwo"

tus_hp = 100
enemigo_hp = 100

print(f"\n¡Un {enemigo} salvaje ha aparecido!")

while tus_hp > 0 and enemigo_hp > 0:

    print("-" * 40)

    print(
        f"{tu_pokemon}: {tus_hp} HP | "
        f"{enemigo}: {enemigo_hp} HP"
    )

    print("-" * 40)

    print("1. Atacar")
    print("2. Curarse")

    opcion = input("Elige una opción: ")

    # Turno jugador

    if opcion == "1":

        dano_jugador = random.randint(15, 25)

        enemigo_hp -= dano_jugador

        print(
            f"{tu_pokemon} causó "
            f"{dano_jugador} de daño"
        )

    elif opcion == "2":

        tus_hp += 20

        if tus_hp > 100:
            tus_hp = 100

        print(f"{tu_pokemon} recuperó vida")

    else:

        print("Opción inválida")

    # Verificar derrota enemigo

    if enemigo_hp <= 0:
        break

    # Turno enemigo

    dano_enemigo = random.randint(10, 22)

    tus_hp -= dano_enemigo

    print(
        f"{enemigo} causó "
        f"{dano_enemigo} de daño"
    )


# Resultado final

print("\n===== RESULTADO =====")

if tus_hp > 0:

    print(f"¡Victoria! {enemigo} fue derrotado")

else:

    print(f"{tu_pokemon} fue derrotado")


# ==========================================
# 7. FUNCIONES
# ==========================================

# Función simple

def nombre_funcion():

    print("Hola, soy una función")


nombre_funcion()


# Función con parámetros

def saludar(nombre):

    return (
        f"Hola, {nombre}, "
        "Bienvenido a programación"
    )


print(saludar("Felipe"))
print(saludar("Andres"))
print(saludar("Maria"))


# ==========================================
# 8. FUNCIONES CON LISTAS
# ==========================================

# Listas de aprendices

aprendices_ficha_3321349 = [
    "Juan",
    "Carlos",
    "Maria"
]

aprendices_ficha_2993648 = [
    "Pedro",
    "Luisa"
]


# Agregar aprendiz

def agregar_aprendiz(ficha, aprendiz):

    ficha.append(aprendiz)

    print(
        f"El aprendiz {aprendiz} "
        "ha sido agregado"
    )


nuevo_aprendiz = input(
    "Ingrese el nombre del nuevo aprendiz: "
)

agregar_aprendiz(
    aprendices_ficha_3321349,
    nuevo_aprendiz
)

agregar_aprendiz(
    aprendices_ficha_2993648,
    "Marcelino"
)

print(aprendices_ficha_3321349)


# Modificar aprendiz

def modificar_aprendiz(
    ficha,
    aprendiz_viejo,
    aprendiz_nuevo
):

    if aprendiz_viejo in ficha:

        indice = ficha.index(aprendiz_viejo)

        ficha[indice] = aprendiz_nuevo

        print(
            "El nombre del aprendiz "
            "ha sido modificado"
        )

    else:

        print("Aprendiz no encontrado")


modificar_aprendiz(
    aprendices_ficha_3321349,
    "Juan",
    "Juan David"
)

print(aprendices_ficha_3321349)

