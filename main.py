#Ejercicio 10: Clasificación de notas
#Escribe un programa que asigne una calificación basada en una nota numérica.
#Enunciado:
#Solicita una nota numérica y clasifícala como A (90-100), B (80-89), C (70-79), D (60-69), o F (<60).

grade = int(input("Type your grade here: "))

if 90 <= grade <= 100:
    print("A")    
elif 80 <= grade <= 89:
    print("B")    
elif 70 <= grade <= 79:
    print("C")    
elif 60 <= grade <= 69:
    print("D")   
elif grade < 60:
    print("F")    
else:
    print("The grade must be between 0 and 100.")