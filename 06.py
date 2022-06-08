# Ej. 1:

'''
def estaenLista1(n, l):
    res = False
    if n in l:
        res = True
    return res

print(estaenLista1(23, [1,2,3,4]))
print(estaenLista1(23, [1,23,3,4]))
print(estaenLista1(23, []))

def estaenLista2(n, l):
    res = False
    for x in l:
        if x == n:
            res = True
    return res

print(estaenLista2(23, [1,2,3,4]))
print(estaenLista2(23, [1,23,3,4]))
print(estaenLista2(23, []))

def estaenLista3(n, l):
    res = False
    i = 0
    ll = len(l)
    while i < ll:
        p = l[i]
        if p == n:
            res = True
        i += 1
    return res

print(estaenLista3(23, [1,2,3,4]))
print(estaenLista3(23, [1,23,3,4]))
print(estaenLista3(23, []))
'''

# Ej. 2:

'''
def estaenLista1(n, l):
    res = False
    if n in l:
        res = True
    return res  

def cargarlista():
    l = []
    n = int(input("Numero: "))
    while n != 0:
        if estaenLista1(n, l):
            print("Error ya esta en lista")
            n = int(input("Numero: "))
        if n < 0:
            print("Error el numero debe ser positivo")
            n = int(input("Numero: "))
        if not estaenLista1(n, l) and n >= 1:
            l.append(n)
            n = int(input("Numero: "))
    print(l)

cargarlista()
'''

# Ej. 3:

'''
def estanEnLista(n, l):
    res = False
    if n in l:
        res = True
    return res

def cargarLista():
    l = []
    n = int(input("Ingrese un numero: "))
    while n != 0:
        n = int(input("Ingrese un numero: "))
        if estanEnLista(n, l):
            print("Ya esta en lista. ", end = "")
        if n < 0: 
            print("Debe ser positivo. ", end = "")
        if n > 0 and not estanEnLista(n, l):
            l.append(n)

def ordenarLista(l):
    ll = len(l)
    for x in range(0, ll-1):
        for u in range(x+1, ll):
            if l[x]>l[u]: 
                aux = l[x]
                l[x] = l[u]
                l[u] = aux
    return l

# PREGUNTAR porque la unica forma de hacer que
# funcione es que retorne dos valores (a, b)
''' 
from random import randint


def cargarConjuntos():
    a = cargarLista()
    b = cargarLista()
'''

def union(a, b):
    for x in range(0, len(a)):
        if a[x] not in b:
            b.append(a[x])
    print(ordenarLista(b))

def interseccion(a, b):
    nv = []
    for x in range(0, len(a)):
        if a[x] in b:
            nv.append(a[x])
    print(ordenarLista(nv))

def diferencia(a, b):
    for x in range(0, len(b)):
        if b[x] in a:
            a.remove(b[x])
    print(a)

def diferenciaSimetrica(a, b):
    c = [] + b
    for x in range(0, len(a)):
        if a[x] not in b:
            c.append(a[x])
    ordenarLista(c)    
    i = 0
    while i < len(c):
        if c[i] in a and c[i] in b:
            c.remove(c[i])
        else:
            i += 1
    print(c)

def menu():
    print("1. CARGAR CONJUNTOS \n2. SALIR")
    x = int(input("Ingrese el valor de la opción: "))
    if x == 1:
        a = cargarLista()
        b = cargarLista()
        print("1. UNION\n2. INTERSECCION\n3. DIFERENCIA (A-B)\n4. DIFERENCIA SIMETRICA")
        u = int(input("Ingrese el valor de la opción: "))
        if u == 1:
            union(a, b)
        elif u == 2:
            interseccion(a, b)
        elif u == 3:
            diferencia(a, b)
        else:
            diferenciaSimetrica(a, b)
    else:
        print("Adeus")

def main():
    menu()

main()
'''

# Ej. 4:

'''
from random import randint

def maxv(ls):
    max = 0
    for x in range(0, len(ls)):
        if ls[x] >= max:
            max = ls[x]
    return max

# def minv(ls):
#     i = 0
#     min = ls[i]
#     while i < len(ls):
#         if ls[i] <= min:
#             min = ls[i]
#         i += 1
#     return min

def minv(ls):
    min = ls[0]
    for x in range(0, len(ls)):
        if ls[x] <= min:
            min = ls[x]
    return min

def cargarListaAleat(a, b, x):
    ls = []
    for x in range(0, x):
        v = randint(a, b)
        ls.append(v)
    print(ls)
    print(maxv(ls))
    print(minv(ls))

def main():    
    a = int(input("Rango inferior: "))
    b = int(input("Rango superior: "))
    x = int(input("Cantidad de numeros aleatorios a generar: "))
    cargarListaAleat(a, b, x)

main()
'''

# Ej. 5:

'''
from random import randint

def enLista(x, ls):
    res = False
    if x in ls:
        res = True
    return res

def cargarLista():
    ls = []
    i = int(input("Ingrese un numero: "))
    while i != 0:
        if enLista(i, ls):
            print("Ya esta en lista. ", end="")
            i = int(input("Ingrese un numero: "))
        elif i < 0:
            print("Debe ser un numero positivo. ", end="")
            i = int(input("Ingrese un numero: "))
        elif i > 0 and not enLista(i, ls):
            ls.append(i)
            i = int(input("Ingrese un numero: "))

def cambiaLista(ls, a, b):
    for x in range(0, len(ls)):
        if ls[x] < a or ls[x] > b:
            ls[x] = randint(a, b)

def main():
    ls = cargarLista()
    a = int(input("Valor minimo"))
    b = int(input("Valor maximo"))

    cambiaLista(ls, a, b)
    # cambiaLista([2,12,5,31,7], 5, 7)

main()
'''

# Ej. 6:

'''
def enLista(x, ls):
    res = False
    if x in ls:
        res = True
    return res

def cargarValores():
    ls = []
    x = int(input("Ingrese numero: "))
    while x != 0:
        if enLista(x, ls):
            print("Ya esta en lista. ", end="")
            x = int(input("Ingrese numero: "))
        if x < 0:
            print("Debe ser positivo. ", end="")
            x = int(input("Ingrese numero: "))
        if x > 0 and not enLista(x, ls):
            ls.append(x)
            x = int(input("Ingrese numero: "))
    return ls

def ordenar(ls):
    for x in range(0, len(ls)-1):
        for u in range(x+1, len(ls)):
            if ls[x] > ls[u]:
                aux = ls[x]
                ls[x] = ls[u]
                ls[u] = aux
    return ls

# print(ordenar([2,12,5,31,7]))

def main():
    ls = cargarValores()
    print(ordenar(ls))

main()
'''

# Ej. 7: 

'''
def insertOrd(ls, num):
    for x in range(0, len(ls)-1):
        if ls[x] < num and ls[x+1] > num:
            ls.insert(x+1, num)
    return ls

# print(insertOrd([2,5,12,31,70], 6))

def main():
    ls = [2,5,12,31,70]
    num = int(input("Numero: "))
    print(insertOrd(ls, num))

main()
'''

# Ej. 8: 

'''
def insertOrd(ls, num):
    for x in range(0, len(ls)-1):
        if ls[x] < num and ls[x+1] > num:
            ls.insert(x+1, num)
    return ls

print(insertOrd([2,7], 6))
'''

def enLista(x, ls):
    res = None
    if x in ls:
        res = "Esta"
    return res

print(enLista(5, [1,2,3,4]))