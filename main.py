#Ejercicio 4: Números pares en un rango
#Enunciado:
#Escribe un programa que solicite al usuario dos números enteros, un valor de inicio y un valor de
#fin. El programa debe imprimir todos los números pares en ese rango, incluyendo los límites. Usa
#un ciclo for para recorrer el rango

numOne = int(input("Enter a number: "))
numTwo = int(input("Enter a number: "))

if numOne % 2 != 0:
    numOne += 1  

for i in range(numOne, numTwo + 1, 2):
    print(i)
