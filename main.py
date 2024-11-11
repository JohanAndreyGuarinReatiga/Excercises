#Ejercicio 2: Contador de vocales en una cadena
#Enunciado:
#Escribe un programa que solicite al usuario una cadena de texto y cuente cuántas vocales (a, e, i,
#o, u) contiene. Usa un ciclo for para recorrer la cadena y realizar la cuenta.

entrance = input("type something: ")
vowels = "aeiouAEIOU"
count = 0
for char in entrance:
    if char in vowels:
        count += 1
print(f"The text contains {count} vowels")