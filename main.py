#Ejercicio 1: Suma de los primeros N números enteros
#Enunciado:
#Escribe un programa que solicite al usuario un número entero positivo n y calcule la suma de los
#primeros n números enteros. Utiliza un ciclo for para realizar la suma.

sum = 0

n = int(input("Enter an integer positive number: "))
for i in range(1, n+1):
    sum += i

print(sum)