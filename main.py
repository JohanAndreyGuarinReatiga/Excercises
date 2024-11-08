#Ejercicio 8: Determinación de año bisiesto
#Escribe un programa que determine si un año es bisiesto o no.
#Enunciado:
#Solicita al usuario que ingrese un año y determina si es bisiesto (divisible entre 4, pero no entre
#100, salvo que sea divisible entre 400).

year = int(input("Write a year: "))

if year % 4 == 0 and (year % 100 !=0 or year % 400 == 0):
    print("The year is leap")
else:
    print("The year isnt leap")