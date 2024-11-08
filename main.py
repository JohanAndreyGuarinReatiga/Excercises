#Ejercicio 6: Juego de adivinanza de números
#Escribe un programa que implemente un juego de adivinanza de números.
#Enunciado:
#El programa genera un número aleatorio entre 1 y 10. El usuario debe adivinar el número, y el
#programa indica si el número ingresado es mayor, menor o igual al número generado.
import random

number = random.randint(1,10)
while True:
    guessing = int(input("try to guess the number: "))
    if guessing > number:
        print("your guessing is greater than the number")
    if guessing < number:
        print("your guessing is less than the number")
    elif guessing == number:
        print("your guessing is equal to the number, YOU WON!!!")
        break

