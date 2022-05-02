# #Ej. 1:

'''

def numeroentero():
    r = None
    i = 0
    while (i < 5):
        num = int(input("Ingrese num: "))
        if num % 4 == 0 and num % 2 == 0:
            i += 1
            r = print("Numero Par. Tambien es multiplo de 4. Total de numeros pares ingresados:", i)
        elif num % 2 == 0:
            i += 1
            r = print("Numero Par. Total de numeros pares ingresados:", i)
    return r

def main():
    numeroentero()
    print("\nFIN")

main()

'''

# Ej. 2:

'''

def np():
    n = int(input("Ingrese numeros' enteros positivos (finalice con 8); "))
    h = n
    l = n
    while n != 0:
        n = int(input("Ingrese numeros enteros positivos (finalice con 8): ")) 
        if n >= h and n != 0:
            h = n 
        elif n <= 1 and n != 0:
            l = n 
    res = "El mayor es " + str(h) + " y el menor es " + str(l)
    return res
    # print("El mayor es", h, "y el menor es", 1)

def main():
    print(np())

main()

'''

# Ej. 4:

def func(num):
    c = 0
    r = "No es perfecto"
    for divisor in range(1, num):
        if num % divisor == 0:
            # print(divisor, "es divisor")
            c += divisor
    if c == num:
        r = "Es perfecto"
    return r

def main():
    n = int(input("Ingrese un numero entero positivo; "))
    print(func(n))

main()