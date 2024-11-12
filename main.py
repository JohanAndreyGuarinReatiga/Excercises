#Ejercicio 5: Días de la semana
#Escribe un programa que, dado un número del 1 al 7, imprima el día correspondiente de la
#semana usando match .
#Enunciado:
#Solicita al usuario un número del 1 al 7 y muestra el día de la semana correspondiente (1 = Lunes,
#7 = Domingo).

while True:
    number = int(input("Enter a number to tell you what day is: "))
    match number: 
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wednesday")
        case 5:
            print("Thursday")
        case 6:
            print("Friday")
        case 7:
            print("Saturday")
        case _:
            print("Thats not a day in the week")