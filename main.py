#Ejercicio 14: Adivinanza de letras
#Escribe un programa que permita al usuario adivinar una letra secreta usando match .
#Enunciado:
#El programa contiene una letra secreta (por ejemplo, "A"). El usuario debe adivinar la letra, y el
#programa le indicará si acertó o no.

guessLetter = input("Guess the letter: ")

match guessLetter:
    case "A":
        print("You guessed the secret letter")
    case _:
        print("Thats not the correct letter")