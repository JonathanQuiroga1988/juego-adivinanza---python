print("Bienvenidos al piedra, papel o tijeras")

nombre1 = input("Nick jugador 1: ")
nombre2 = input("Nick jugador 2: ")

puntos1 = 0
puntos2 = 0

while puntos1 < 3 and puntos2 < 3:
    jugador1 = input(f"{nombre1}, ¿Qué eliges? ¿Piedra, papel o tijeras?: ").strip().lower()
    jugador2 = input(f"{nombre2}, ¿Qué eliges? ¿Piedra, papel o tijeras?: ").strip().lower()

    print(f"DEBUG --> jugador1: {jugador1}, jugador2: {jugador2}")  # trazas para verificar

    if jugador1 == jugador2:
        print("Empate")
    elif (jugador1 == "piedra" and jugador2 == "tijeras") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijeras" and jugador2 == "papel"):
        print("Ganador de la ronda:", nombre1)
        puntos1 += 1
    elif (jugador2 == "piedra" and jugador1 == "tijeras") or \
         (jugador2 == "papel" and jugador1 == "piedra") or \
         (jugador2 == "tijeras" and jugador1 == "papel"):
        print("Ganador de la ronda:", nombre2)
        puntos2 += 1
    else:
        print("Entrada no válida. Intenta nuevamente.")

    print(f"Puntaje: {nombre1} {puntos1} - {puntos2} {nombre2}")
    print("-" * 30)

# Mostrar el ganador final
if puntos1 == 3:
    print(f"🏆 ¡{nombre1} gana la partida!")
else:
    print(f"🏆 ¡{nombre2} gana la partida!")