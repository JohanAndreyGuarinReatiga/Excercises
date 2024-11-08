#Ejercicio 3: Calculadora básica
#Utiliza match para implementar una calculadora simple.
#Enunciado:
#Crea una calculadora que solicite dos números y una operación matemática (+, -, *, /). Usa match
#para realizar la operación correspondiente.

while True:
    firstNumber = int(input("Enter the first number: "))
    secondNumber = int(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /):")
    match operator:
        case "+":
            print(firstNumber + secondNumber)
        case "-":
            print(firstNumber - secondNumber)
        case "*":
            print(firstNumber * secondNumber)
        case "/":
            print(firstNumber / secondNumber)
        case _:
            print("Thats not an operator")
    quest = input("do you want to continue? type yes or no: ")
    if quest == "yes":
        continue
    else: 
        break
