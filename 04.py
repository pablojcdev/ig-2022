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

# Ej. 3:

'''

def EsPrimo(num):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)

def Range(num):
    for num in range(1, num + 1):
        EsPrimo(num)

def main():
    num = int(input("Num: "))
    Range(num)

main()

'''

# Ej. 4:

'''

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

'''

# Ej. 5:

'''

def cond(n):
    n1 = (n // 1) % 10
    n2 = (n // 10) % 10
    n3 = (n // 100) % 10
    n4 = (n // 1000) % 10

    n = n1 + n2*10 + n3*100 + n4*1000

    if n1+n3 == n2+n4:
        print(n)

def true():
    for num in range(1000, 10000):
        cond(num)

def main():
    n = int(input("Ingrese un numero entero positivo; "))
    cond(n)
    true()

main()

'''

# Ej. 6:

'''

def aBinario(i):
    binario = ""
    c = ""
    while i != 0:
        c = i%2
        i = i//2
        # print(c, end="")
        binario = str(c) + binario
    return binario

def main():
    n = int(input("Ingrese un numero decimal: "))
    print(aBinario(n))

main()

'''

# Ej. 7:

def notas():
    n = ""
    c = 0
    a = 0
    apr = 0
    prom = 0
    st = 0
    while n != 0:
        n = int(input("Ingrese nota: "))
        if n > 0 and n <=10:
            c += 1
            st = st + n
            if n > 0 and n <= 3:
                a += 1
            elif n >= 4 and n <= 7:
                apr += 1
            elif n > 7 and n <= 10:
                prom += 1

    p_a = (a*100)/c
    p_apr = (apr*100)/c
    p_prom = (prom*100)/c

    promg = st / c

    print("\nCantidad de aplazos: {} ({:.2f}%)".format(a, p_a))
    print("Cantidad de aprobados: {} ({:.2f}%)".format(apr, p_apr))
    print("Cantidad de promocionados: {} ({:.2f}%)".format(prom, p_prom))
    print("Promedio general: {:.2f}".format(promg))

def main():
    notas()

main()
