import random


numero_secreto = random.randint (1,100)
adivinado=False
cantidad_intentos= 0
cantidad_max_intentos = 3
print ("---Bienvenido al juego de adivinar el numero secreto---")

while not adivinado and cantidad_intentos < cantidad_max_intentos:
    print ("Cantidad de intentos : ", cantidad_max_intentos-cantidad_intentos)
    entrada = input ("Introduce un numero del 1 al 99: ")
    numero = int(entrada)


    if numero == numero_secreto:
        print("Felicitaciones, adivinaste")
        adivinado=True
    elif numero < numero_secreto:
        print("El numero es mayor que el ingresado")
    else:
        print("el numero es menor al ingresado")

    cantidad_intentos +=1


if not cantidad_intentos < cantidad_max_intentos:
    print("GAME OVER")
