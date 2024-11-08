#jercicio 7: Número positivo, negativo o cero
#Escribe un programa que determine si un número es positivo, negativo o cero usando if .
#Enunciado:
#Solicita al usuario que ingrese un número y determina si es positivo, negativo o cero

while True: 
    number = int(input("Enter a number: "))
    if number > 0:
        print("The number is positive")
    if number == 0:
        print("The number is 0")
    if number < 0:
        print("The number is negative")
    cont = input("if you want to write another number type 'continue' or 'leave' to exit: ")
    if cont == "leave": 
        break