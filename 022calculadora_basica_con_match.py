'''
Pide dos números y una operación al usuario (+, -, *, /). Usa match para realizar la operación. Recuerda, para poder dividir, el primer número (dividendo) debe ser mayor que el segundo (divisor) si no, no hará la operación y mostrará un mensaje de error.
'''
num1 = float(input("Dime el primer numero que quieras calcular: "))
num2 = float(input("Dime el segundo numero que calcular: "))

operacion = input("Elige una operacion: +, -, *, /")

match operacion:
    case "+":
        print(f"La suma del los numeros {num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"La resta del los numeros {num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"La multiplicacion del los numeros {num1} * {num2} = {num1 * num2}")
    case "/":
        print(f"La division del los numeros {num1} / {num2} = {num1 / num2}")    