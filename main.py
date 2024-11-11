#Ejercicio 20: Conversión de calificaciones numéricas a letras
#Escribe un programa que convierta una calificación numérica en una letra de acuerdo a un
#sistema de calificación específico, usando match .
#Enunciado:
#Solicita una calificación numérica (0-100) y convierte esa calificación a una letra usando el
#siguiente esquema:
#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: 0-59

grade = int(input("Write your grade: "))

match grade:
    case A:
        if 90 <= grade <= 100:
            print("A")
        elif 80 <= grade <= 89:
            print("B")
        elif 70 <= grade <= 79:
            print("C")
        elif 60 <= grade <= 69:
            print("D")
        else:
            print("F")
        