import random

# Juego de adivinanza con un máximo de 7 intentos

def jugar():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 7

    print("He escogido un número entre 1 y 100. Tienes 7 intentos para adivinarlo.")

    while intentos < max_intentos:
        try:
            intento = int(input(f"Intento {intentos + 1}: "))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        intentos += 1
        if intento == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
        elif intento < numero_secreto:
            print("Muy bajo.")
        else:
            print("Muy alto.")

    else:
        print(f"Se acabaron los intentos. El número era {numero_secreto}.")


if __name__ == "__main__":
    jugar()
