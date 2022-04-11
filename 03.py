# Ej. 1:

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
op = input ("Ingrese la operación (+, -, *, /): ")

if op == "+":
    r = (num1 + num2)
elif op == "-":
    r = (num1 - num2)
elif op == "/":
    r = (num1 / num2)
elif op == "*":
    r = (num1 * num2)

print("\n", num1, op, num2, "=", r)
