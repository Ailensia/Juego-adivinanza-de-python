import random


numero_secreto = random.randint(1,101)
cantidad_intentos = 0
cantidad_max_intentos = 10
adivinado = False 

print("Bienvenido al juego! Tienes 5 intentos")

while not adivinado:
    if not cantidad_intentos < cantidad_max_intentos:
        print("Game Over! No has podido adivinar dentro de los 10 intentos")
        break

    entrada = input("Introduce un número del 1 al 100: ") 
    numero = int(entrada)

    if numero == numero_secreto:
        print("Felicidades has adivinado el número secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("El número es mayor al ingresado")
    else:
        print("El número es menor al ingresado")
    
    cantidad_intentos += 1











































