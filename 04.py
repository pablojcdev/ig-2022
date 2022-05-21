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

    # for i in range(2, num):
    #     if num % i == 0:
    #         break
    # else:
    #     print(num)

    es_primo = True
    i = 2
    while i < n and es_primo:
        if n%i == 0:
            es_primo = False
        i = i+1
    return es_primo and n!1

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

'''
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
'''

# Ej. 8:

'''

def valid():
    n = int(input("Ingrese un número entero: "))
    while n < 0:
        print("No se cpuede calcular el factorial de un numero negativo", end="")
        n = int(input("aasd: "))
    return n

def factorial(n):
    r = 1
    while n > 1:
        r = r * n
        n -= 1
    return r
    
def main():
    n = valid()
    print(factorial(n))    

main()

'''

# Ej. 9:

'''
def capicua(n):
    r = "No es"
    st = ""
    l = (len(str(n)))
    for i in range (0, l):
        cifras = (n//10**i)%10
        st += str(cifras)
    if int(st) == n:
        r = "Es capicua"
    return r

def main():
    n = int(input("Número entero positivo(de hasta nueve cifras): "))
    print(capicua(n))

main()

'''

# Ej. 10:

'''
def valid(msg):
    ent = int(input("Ingrese " + msg + ": "))
    while ent < 2:
        print("Error, debee ser mayor o igual a 2. ", end="")
        ent = int(input("Ingrese " + msg + ": "))
    return ent

def figura(b, h):
    for f in range (0, h):
        for c in range (0, b):
            print("* ", end="")
        print()

figura()

def main():
    b = valid("base")
    h = valid("altura")
    figura(b, h)

main()
'''

# Ej. 11:

'''
def valid(msg):
    ent = int(input("Ingrese " + msg + ": "))
    while ent < 2:
        print("Error, debee ser mayor o igual a 2. ", end="")
        ent = int(input("Ingrese " + msg + ": "))
    return ent

def figura(b, h):
    for f in range (0, h):
        for c in range (0, b):
            if f == 0 or c == 0 or c == b-1 or f == h-1:
                print("* ", end="")
            else:
                print("  ", end="")
        print()

def main():
    b = valid("base")
    h = valid("altura")
    figura(b, h)

'''

# Ej. 12:

'''
def figura(b):
    for f in range (0, b):
        for c in range (0, b):
            if f > c or f == c:
                print("* ", end="")
                # print("(", f, ":", c, ")", end="")
            else:
                # print(" "*9, end="")
                print("  ", end="")
        print()

figura(5)
'''

# Ej. 13:

'''
Ingrese base: 8
Número no válido. Ingrese base: 11
     *
    ***
   *****
  *******
 *********
***********
Observar en la figura que su base tiene 11 y la altura tiene 6 .
'''

'''
def figura(b):
    for f in range (0, b):
        for c in range (0, b):
            if f < c or f+c<b-1:
                print("  ", end="")
            else:
                print("* ", end="")
        print()

figura(11)
'''

# Ej. 14

'''
Ingrese altura: 7
*
***
*****
*******
*****
***
*
'''

'''
def figura(b):
    for f in range (0, b):
        for c in range (0, b):
            if f < c or f+c>b-1:
                print("  ", end="")
            else:
                print("* ", end="")
        print()
        
figura(11)
'''

# Ej. 15:

'''
Ingrese diagonal: 8
Valor incorrecto. Ingrese diagonal: 7
   *
  ***
 *****
*******
 *****
  ***
   *
'''

'''
def figura(b):
    for f in range (0, b):
        for c in range (0, b):
            # if f+4 <= c or f+c-4>=b-1 or f-4 >= c or f+c+4<=b-1:
            if f+(b//2+1) <= c or f+c-(b//2+1)>=b-1 or f-(b//2+1) >= c or f+c+(b//2+1)<=b-1:
                print("  ", end="")
            else:
                print("* ", end="")
        print()
        
figura(5)
'''

# Ej. 16:

'''
Ingrese ancho: 13
*************
* ********* *
*  *******  *
*   *****   *
*    ***    *
*     *     *
*************
'''

def figura(b):
    for f in range (0, b):
        for c in range (0, b):
            # if f+4 <= c or f+c-4>=b-1 or f-4 >= c or f+c+4<=b-1:
            if f-(b//2+1) >= c or f+c-(b//2+1)>=b-1: #or f+c-(b//2+1)>=b-1 or f-(b//2+1) >= c or f+c+(b//2+1)<=b-1:
                print("  ", end="")
            else:
                print("* ", end="")
        print()
        
figura(13)