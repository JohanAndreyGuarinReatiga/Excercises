#Ejercicio 7: Suma de números pares hasta que se introduce un impar
#Enunciado:
#Escribe un programa que solicite al usuario ingresar números enteros indefinidamente. El
#programa debe sumar los números siempre que sean pares, pero debe detenerse si el usuario
#ingresa un número impar. Usa un ciclo while para lograr esto.

sum = 0
while True:
    n = int(input("Enter a number: "))
    if n %2 != 0:
        break
    else:
        sum += n
        print(sum)
        pass