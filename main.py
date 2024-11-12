#Ejercicio 3: Factorial de un número
#Enunciado:
#Escribe un programa que solicite al usuario un número entero positivo n y calcule el factorial de
#dicho número ( n! = 1 * 2 * 3 * ... * n ). Usa un ciclo for para realizar el cálculo.

n = int(input("Enter a number: "))

factor = 1
for i in range(1, n + 1):
    factor *= i

print(f"The factorial of {n} is: {factor}")