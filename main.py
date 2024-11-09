#Ejercicio 12: Calculadora de IMC (Índice de Masa Corporal)  BODY MASS INDEX (BMI)
#Escribe un programa que calcule el IMC y determine el estado de peso.
#Enunciado:
#Solicita al usuario su peso (en kg) y su altura (en metros). Calcula el IMC y clasifícalo en bajo peso
#(<18.5), peso normal (18.5-24.9), sobrepeso (25-29.9), o obesidad (>=30).
import math
height = float(input("Enter you height in meters: "))
weight = float(input("Enter you weight in kilos: "))

imc = weight / (math.pow(height,2))  

if imc <= 18.5:
    print("Underweight")
elif 18.5 <= imc <= 24.9:
    print("Normal weight")
elif 25 <= imc <= 29.9:
    print("Overweight")
elif imc >= 30: 
    print("YOURE OBESE")