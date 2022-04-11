# Ej. 1:

'''

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

'''

num1 = 8
num2 = 2
num3 = 7

if num1 > num2 and num2 > num3:
    print(num1, num2, num3)
elif num1 > num2 and num2 > num3:
    print(num1, num2, num3)
# Ingrese el primer número: 8
# Ingrese el segundo número: 2
# Ingrese el tercer número: 7
# Los números ordenados en forma ascendente son:
# 2
# 7
# 8