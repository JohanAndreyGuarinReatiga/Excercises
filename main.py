#Ejercicio 16: Cálculo del tiempo de viaje
#Escribe un programa que calcule el tiempo que tarda en llegar un automóvil a su destino.
#Enunciado:
#Solicita al usuario la distancia a recorrer (en km) y la velocidad promedio del automóvil (en km/h).
#Calcula el tiempo de viaje en horas y minutos. Si la velocidad es mayor a 120 km/h, muestra un
#mensaje de advertencia.

distance = int(input("Enter the distance in kilometers: "))
avSpeed = int(input("Enter the average speed in kilometers per hour: "))

time = distance / avSpeed

hours = int(time) 
minutes = int((time - hours) * 60) 
if avSpeed > 120:
    print("""
                *********************************
                            WARNING!!!
                    YOURE EXCEEDING 120 km/h 
                *********************************
""")

print(f"The travel time is {hours} hours and {minutes} minutes.")