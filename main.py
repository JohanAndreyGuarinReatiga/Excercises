#jercicio 9: Clasificación de edades
#Escribe un programa que clasifique a una persona en función de su edad.
#Enunciado:
#Solicita la edad de la persona e indica si es niño (0-12 años), adolescente (13-17 años), adulto (18-
#64 años) o anciano (65 años o más).

age = int(input("Write your age: "))

if age <= 12:
    print("Youre a child")
if age >= 13 and age <= 17 :
    print("Youre a teenager")
if age >= 18 and age <= 64:
    print("Youre an adult")
if age >= 65:
    print("youre an elder")