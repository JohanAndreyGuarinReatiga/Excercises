#Ejercicio 15: Cálculo del salario neto
#Escribe un programa que calcule el salario neto de un empleado después de aplicar impuestos.
#Enunciado:
#Solicita al usuario su salario bruto y su país de residencia. Calcula el salario neto aplicando
#impuestos: el 20% para residentes de "País A", el 15% para "País B" y el 10% para "País C". Si el
#país no está en la lista, aplica un 25% de impuestos.

grossSalary = int(input("Type your gross salary: "))
country = input("Type the country were you live (A, B, C): ")

if country == "A":
    taxRate = 0.20
elif country == "B":
    taxRate = 0.15
elif country == "C":
    taxRate = 0.10
else:
    taxRate = 0.25
    
netSalary = (grossSalary * (1 - taxRate))
print(f"your net salary after taxaes is: ${netSalary}")