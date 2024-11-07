#Ejercicio 4: Determinación del tipo de triángulo
#Escribe un programa que determine el tipo de triángulo en función de sus lados usando if .
#Enunciado:
#Solicita al usuario que ingrese las longitudes de los tres lados de un triángulo. Determina si el
#triángulo es equilátero, isósceles o escaleno.

a = int (input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

if a == b == c:
    print("The triangle is equilateral") 
if (a == b and b != c) or (a == c and b != c) or (c == b and a != c):
    print("The triangle is isosceles")
if a != b and b != c and c != a: 
    print("The triangle is scalene")
