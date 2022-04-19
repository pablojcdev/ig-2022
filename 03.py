# Ej. 1:

'''

def calculadora(num1, num2, op):
    if op == "+":
        r = (num1 + num2)
    elif op == "-":
        r = (num1 - num2)
    elif op == "/":
        r = (num1 / num2)
    elif op == "*":
        r = (num1 * num2)
    
    print("\n", num1, op, num2, "=", r)

def main():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    op = input ("Ingrese la operación (+, -, *, /): ")

    calculadora(num1, num2, op)

main()

'''

# Ej. 2:

'''

def orden(num1, num2, num3):
    if num1 > num2 and num2 > num3:
        print(num3, num2, num1)
    elif num1 > num3 and num3 > num2:
        print(num2, num3, num1)
    elif num2 > num1 and num1 > num3:
        print(num3, num1, num2)
    elif num2 > num3 and num3 > num1:
        print(num1, num3, num2)
    elif num3 > num1 and num1 > num2:
        print(num2, num1, num3)
    elif num3 > num2 and num2 > num1:
        print(num1, num2, num3)

def main():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))

    print("\nLos números ordenados en forma ascendente son:")
    orden(num1, num2, num3)

main()

'''

# Ej. 3:

'''

def signo(num):
    s = "positivo"
    if num == 0:
        s = "cero"
    elif num < 0:
        s = "negatvo"
    return s

def tipo(num):
    t = "real"
    if num > 0 and num % 1 == 0 :
        t = "entero natural"
    elif num <= 0 and num % 1 == 0:
        t = "entero"
    return t

def main():
    num = int(input("Ingrese un número: "))

    print("El número es", signo(num), "y", tipo(num))

main()

'''

# Ej. 4:

def mayor(num1, num2):
    m = num1
    if num2 > num1:
        m = num2
    return m

def menor(num1, num2):
    min = num1
    if num2 < num1:
        min = num2
    return min

def valid(highest, lowest, num):
    r = "NO"
    if num >= lowest and num <= highest:
        r = "SI"
    return r

def main():
    num1 = int(input("Ingrese un número A: "))
    num2 = int(input("Ingrese un número B: "))

    highest = mayor(num1, num2)
    lowest = menor(num1, num2)

    num = highest - lowest

    print(valid(highest, lowest, num), "cumple la condicion.")

main()