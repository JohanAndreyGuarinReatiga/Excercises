#Ejercicio 2: Calificación de una nota
#Escribe un programa que determine si una nota numérica es "Aprobado" o "Reprobado" usando
#if .
#Enunciado:
#Solicita al usuario una calificación y determina si la nota es aprobatoria (>= 60) o reprobatoria (<
#60).

grade = int(input("Type your grade to define if youre approved or not: "))

if grade >= 60:
    print("Your grade is passing")
if grade: 
    print("Your grade is failing")