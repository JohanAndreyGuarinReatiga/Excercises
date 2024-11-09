#Ejercicio 13: Comparación de tres números
#Escribe un programa que determine el mayor de tres números usando if .
#Enunciado:
#Solicita al usuario que ingrese tres números y determina cuál es el mayor.

firstNumber = int(input("Enter a number: "))
secondNumber = int(input("Enter a number: "))
thirdNumber = int(input("Enter a number: "))

if firstNumber >= secondNumber and firstNumber >= thirdNumber:
    print(f"The largest number is: {firstNumber}")
elif secondNumber >= firstNumber and secondNumber >= thirdNumber:
    print(f"The largest number is: {secondNumber}")
else:
    print(f"The largest number is: {thirdNumber}")
