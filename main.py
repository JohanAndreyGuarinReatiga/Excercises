#Ejercicio 17: Sistema de calificaciones con bonificaciones
#Escribe un programa que calcule la calificación final de un estudiante basándose en su calificación
#y si ha hecho tareas adicionales. Las tareas adicionales pueden darle un extra de puntos, pero el
#máximo de puntos no puede exceder 100.
#Enunciado:
#Solicita la calificación del estudiante y pregunta si hizo tareas adicionales. Si la respuesta es "sí",
#añade un 5% extra a la calificación, pero si la calificación supera 100, ajústala a 100. Si la respuesta
#es "no", simplemente muestra la calificación original

grade = int(input("Write your grade: "))
extraAssignments = input("have you done extra assignments?(yes or no): ")
extraScore = grade + (grade * 0.05)

match extraAssignments: 
    case "yes":
        if extraScore < 100:
            print(f"Your final score is {extraScore}")
        elif extraScore > 100:    
            print("Your final score is 100")
    case _:
        print(f"Your grade is {grade}")