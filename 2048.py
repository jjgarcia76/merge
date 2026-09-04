import random

# Crear el tablero 4x4 lleno de ceros
def crear():
    tablero = []
    for numero_fila in range(4):
        fila = [0, 0, 0, 0]
        tablero.append(fila)
    return tablero

# Mostrar el tablero en consola
def mostrar(tablero):
    print("\nTABLERO:")
    for fila in tablero:
        print(fila)

# Insertar un nuevo número (2 o 4) en una posición vacía aleatoria
def insertar(tablero):
    vacias = []

    for fila in range(4):
        for columna in range(4):
            if tablero[fila][columna] == 0:
                vacias.append((fila, columna))

    if vacias:
        fila, columna = random.choice(vacias)
        tablero[fila][columna] = random.choice([2, 4])

# Mover una fila a la izquierda con suma de casillas iguales
def mover_fila(fila):
    nueva_fila = []

    for numero in fila:
        if numero != 0:
            nueva_fila.append(numero)

    columna_actual = 0
    while columna_actual < len(nueva_fila) - 1:
        if nueva_fila[columna_actual] == nueva_fila[columna_actual + 1]:
            nueva_fila[columna_actual] *= 2
            nueva_fila[columna_actual + 1] = 0
            columna_actual += 2
        else:
            columna_actual += 1

        fila_final = []   # Fila final se refiere a la fila nueva sin ceros
    for numero in nueva_fila:
        if numero != 0:
            fila_final.append(numero)

    while len(fila_final) < 4:
        fila_final.append(0)

    return fila_final

# Rotaciones para usar movimientos en todas direcciones
def rotar_derecha(tablero):
    nuevo_tablero = []

    for fila_actual in range(4):
        fila_nueva = []
        for columna_actual in range(4):
            fila_nueva.append(0)
        nuevo_tablero.append(fila_nueva)

    for fila in range(4):
        for columna in range(4):
            nuevo_tablero[columna][3 - fila] = tablero[fila][columna]

    return nuevo_tablero


def rotar_izquierda(tablero):
    nuevo_tablero = []

    for fila_actual in range(4):
        fila_nueva = []
        for columna_actual in range(4):
            fila_nueva.append(0)
        nuevo_tablero.append(fila_nueva)

    for fila in range(4):
        for columna in range(4):
            nuevo_tablero[3 - columna][fila] = tablero[fila][columna]

    return nuevo_tablero


def rotar180(tablero):
    return rotarderecha(rotarderecha(tablero))

# Movimiento del tablero según dirección
def mover(tablero, direccion):
    if direccion == "a":  # izquierda
        nuevo = []
        for fila in tablero:
            nueva = moverfila(fila)
            nuevo.append(nueva)
        return nuevo

    elif direccion == "d":  # derecha
        rotado = rotar180(tablero)
        movido = mover(rotado, "a")
        return rotar180(movido)

    elif direccion == "w":  # arriba
        rotado = rotarizquierda(tablero)
        movido = mover(rotado, "a")
        return rotarderecha(movido)

    elif direccion == "s":  # abajo
        rotado = rotarderecha(tablero)
        movido = mover(rotado, "a")
        return rotarizquierda(movido)

    else:
        print("Movimiento invalido, Usa W, A, S o D para poder moverte")
        return tablero

# Juego principal
def jugar():
    tablero = crear()
    insertar(tablero)
    insertar(tablero)
    movimientos = 0

    while True:
        mostrar(tablero)

        print("Movimiento número:", movimientos)
        mayor = max(max(fila) for fila in tablero)
        print("Número mayor en el tablero:", mayor)
        vacias = sum(fila.count(0) for fila in tablero)
        print("Casillas vacías:", vacias)

        movimiento = input("Mover (W/A/S/D), o X para salir: ").lower()
        if movimiento == "x":
            print("Gracias por jugar")
            break

        nuevo_tablero = mover(tablero, movimiento)
        if nuevo_tablero != tablero:
            tablero = nuevo_tablero
            insertar(tablero)
            movimientos += 1
        else:
            print("No se movio nada, intenta con otra dirección :p")

# Iniciar el juego
jugar()

# ==============================
# A partir de aquí, continúan el 2do y 3er integrante del grupo:
# ==============================

# Segunda persona:
# - Agregar condición de GANAR (si hay 2048 en el tablero, terminar juego).
# - Agregar condición de PERDER (si está lleno y no se pueden hacer más movimientos).
# - Puedes hacerlo dentro del ciclo while en la función jugar().

# Tercera persona:
# - Crear función dos_jugadores() para modo de 2 jugadores.
# - Guardar tablero inicial, dejar que juegue el segundo jugador.
# - Comparar resultados: movimientos y número mayor.
# - Mostrar quién ganó o si hubo empate.

# Extra (opcional):
# - Crear modo jugador vs máquina (IA simple no IA como tal, mas bien un bot para que pueda jugar con el usuario).
# - Agregar opción "replay" para mostrar las jugadas anteriores.
# - Agregar menú de ayuda que muestre cómo jugar.
