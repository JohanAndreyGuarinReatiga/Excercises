#Ejercicio 6: Adivina el número (con while )
#Enunciado: (random.randint(1, 100))
#Escribe un programa que genere un número aleatorio entre 1 y 100 y permita al usuario
#adivinarlo. El programa debe dar pistas si el número ingresado es mayor o menor que el número
#secreto. Usa un ciclo while para permitir al usuario seguir intentando hasta que adivine el
#número

import random

number = random.randint(1,100)
while True:
    guessing = int(input("try to guess the number: "))
    if guessing > number:
        print("your guessing is greater than the number")
    if guessing < number:
        print("your guessing is less than the number")
    elif guessing == number:
        print("\nYOU'VE GUESSED THE NUMBER!!!\n")
        break