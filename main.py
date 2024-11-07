#Ejercicio 1: Verificación de números pares e impares
#Escribe un programa que verifique si un número es par o impar utilizando if .
#Enunciado: Solicita al usuario que ingrese un número y verifica si es par o impar

number = int(input("Enter a digit: "))
if (number % 2) == 0:
    print("The number is even")
else:
    print("The number is odd")
