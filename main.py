#Ejercicio 11: Conversión de temperaturas
#Escribe un programa que convierta grados Celsius a Fahrenheit o Fahrenheit a Celsius usando match .
#Enunciado:
#Solicita al usuario que ingrese una temperatura y una escala (C o F). Convierte la temperatura a la
#escala opuesta usando match .

temp = int(input("Enter a temperature: "))
scale = input("if your temperature is in Celsius type 'C' or if its in Fahrenheit type 'F': ").upper()

match scale:
    case "C":
        print((temp * 9 / 5) + 32)
    case "F":
        print((temp - 32) * 5 / 9 )