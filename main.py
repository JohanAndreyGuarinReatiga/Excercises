#Ejercicio 22: Clasificación de triángulos por sus ángulos
#Escribe un programa que clasifique un triángulo en agudo, obtuso o rectángulo según sus ángulos
#internos usando if .
#Enunciado:
#Solicita al usuario los tres ángulos de un triángulo y clasifícalo en:
#Agudo: Todos los ángulos son menores a 90°.
#Rectángulo: Un ángulo es exactamente 90°.
#Obtuso: Un ángulo es mayor a 90°.


while True:
    firstAngle = float(input("Enter the first angle: "))
    secondAngle = float(input("Enter the second angle: "))
    thirdAngle = float(input("Enter the third angle: "))
    
    if (firstAngle + secondAngle + thirdAngle) != 180:
        print("Thats not a triangle, try again")
    elif firstAngle < 90 and secondAngle < 90 and thirdAngle < 90:
        print("The triangle is Acute")
        break
    elif firstAngle == 90 or secondAngle == 90 or thirdAngle == 90:
        print("The triangle is Right")
        break
    else:
        print("The triangle is Obtuse")
        break