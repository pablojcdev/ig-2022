# Ej. 1:

'''

from math import sqrt

def area(l1, l2, l3):
    p = (l1 + l2 + l3)/2
    a = sqrt(p*(p-1)*(p-l2)*(p-l3))
    return a

def main():
    l1 = int(input("Ingrese el 1.er lado: "))
    l2 = int(input("Ingrese el 2.do lado: "))
    l3 = int(input("Ingrese el 3.er lado: "))

    miarea = round(area(l1, l2, l3), 2)
    print(miarea)

main()

# Ingrese lado 1: 2
# Ingrese lado 2: 6
# Ingrese lado 3: 7
# El area del triangulo es = 5.56

'''

# Ej. 2:

'''

from math import pow

def sqrt(x, n):
    r = pow(x, 1/n)
    return r

def main():
    x = int(input("Ingrese el radicando (numero real): "))
    n = int(input("Ingrese el índice (numero natural): "))

    miraiz = round(sqrt(x, n), 2)
    print("La raiz", n, "de", x, "es =", miraiz)

main()

# Ingrese el radicando (numero real): 14
# Ingrese el índice (numero natural): 3
# La raiz 3 de 14 es = 2.410142

'''

# Ej. 3:

def paridad(binario):
    bit = binario % 2 
    return bit

def main():
    num = int(input("Ingrese un numero de binario de hasta 8 bits: "))

    n8 = (((num//1)%10))
    n7 = (((num//10)%10))
    n6 = (((num//100)%10))
    n5 = (((num//1000)%10))
    n4 = (((num//10000)%10))
    n3 = (((num//100000)%10))
    n2 = (((num//1000000)%10))
    n1 = (((num//10000000)%10))

    binario = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8

    miparidad = paridad(binario)
    print("Bit de paridad generado:", miparidad)

main()

#Ingrese un numero binario: 10101