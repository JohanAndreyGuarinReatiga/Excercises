#Ejercicio 21: Sistema de estacionamiento con tarifas progresivas
#Escribe un programa que calcule el costo de estacionamiento basado en el número de horas, con tarifas progresivas.
#Enunciado:
#El costo de estacionamiento se calcula de la siguiente manera:
#Primera hora: $5
#Segunda a cuarta hora: $4 por hora
#Más de cuatro horas: $3 por cada hora adicional
#Solicita al usuario el número de horas de estacionamiento y calcula el costo total.

hours = int(input("Enter the parking lot hours: "))
totalCost = 0
additionalHours = hours - 4 

if hours == 1:
    totalCost += 5
elif 2 <= hours <= 4:
    totalCost += 5 + ((hours - 1) * 4)
elif hours > 4:
    totalCost += 17 + (additionalHours * 3)
        
print(f"The total parking lot cost will be: ${totalCost}")

