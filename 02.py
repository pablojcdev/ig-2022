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

'''

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

# Ingrese un numero de binario de hasta 8 bits: 10111
# Bit de paridad generado: 0

'''

# Ej. 4:

'''
from math import pi
from math import pow

def areacirc (r_cc):
	a_cc = pi * (pow(r_cc, 2)) # 12.56
	return a_cc

def areacuad (lado):
	a_cuadrado = pow(lado, 2)
	return a_cuadrado

def areanegra (a_cuadrado, a_circulos):
	a_negra = a_cuadrado - a_circulos
	return a_negra

def main():
	lado = int(input("Ingrese el lado: "))
	areacuad(lado)
	
	r_cc = ((1/3*lado)/2) #2
	areacirc(r_cc)
	
	# a_cg = 4(a_cc)
	a_circulos = (2*areacirc(r_cc))+(4*areacirc(r_cc)) # 68.60 # 75.36

	p_a_negra = (((areanegra(areacuad(lado), a_circulos))) * 100)/areacuad(lado) # 47.64
    # p_a_negra = round(((a_negra * 100%)/a_cuadrado), 2)
	print("El area negra es", round(areanegra(areacuad(lado), a_circulos), 2), "y es un", str(round(p_a_negra, 2)) + "%", "del area total del cuadrado")	

main()

'''

# Ej. 5:

import random

def r(li, Is):
    r_random = random.randint(li, Is) 
    return r_random

def main():
    li = int("14") 
    Is= int("31")
    
    print(r(li, Is)) 
    li = r(li, Is)

    print(r(li, Is)) 
    Is = r(li, Is)

    print(r(li, Is))

main()