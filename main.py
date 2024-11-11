#Ejercicio 18: Sistema de evaluación de créditos universitarios
#Escribe un programa que calcule el número de créditos totales de un estudiante en base a las
#materias cursadas y el puntaje obtenido en cada una. El puntaje debe ser evaluado como
#aprobado o no aprobado.
#Enunciado:
#Solicita al usuario ingresar el número de materias que ha cursado. Para cada materia, solicita el
#puntaje y determina si ha aprobado o no (>= 60). Luego, calcula el número total de créditos del
#estudiante (cada materia aprobada otorga 3 créditos)

numSubjects = int(input("How many subjects have you completed? write it here: "))
credits = 0

for i in range(numSubjects):
    grade = float(input(f"what have you scored in the {i+1} subject?: "))
    if grade >= 60:
        credits += 3
    
print(f"Your total on credits is {credits}")