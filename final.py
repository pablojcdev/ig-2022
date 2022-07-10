# import random
# def fun(a,b):
#     x = not(a and b)
#     y = not a and not b
#     if x != y:
#         res = 50
#     else:
#         res = 20
#     return res

# def main():
#     a = random.randint(0,1)
#     b = random.randint(0,1)
#     #print("{1:d} {0:d}".format(fun(a,b),fun(b,a)))

#     print(fun(1,1))
#     print(fun(1,0))
#     print(fun(0,1))
#     print(fun(0,0))
# main()

'''
A. Imprime SIEMPRE los valores -> 20 20
B. Imprime SIEMPRE el valor -> 20
C. Imprime SIEMPRE los valores -> 50 50
D. Imprime SIEMPRE el valor -> 50
E. Lo que imprime DEPENDE EXCLUSIVAMENTE de los valores pasados a la función 'fun'
F. No imprime. Hay un ERROR cuando se ejecuta el código.
G. NINGUNA de las respuestas son correctas.
'''

'''
def fun(lst):
    lst+=[4,5,6]
    lst.pop(6)
    return lst

def main():
    lst=[1,2,3]
    fun(lst)
    print(lst)

main()
'''

###################### UCA.IG.21.FINAL.FEB.B.PRACTICA[20210223] ######################

'''
energia.csv

    AMD [string] | ID_parque [int] | cantidad [float]

parque.csv

    ID_parque [int] | nombre [string] | cantidadMolinos [int]

Formato: AMD (Año Mes Día). Dentro de un string de seis caracteres numéricos hay
una fecha representada según se indica: AAMMDD. Ejemplo: 120318. El año (AA) es
12, el mes (MM) es 03, el día (DD) es 18.

{ AMD y ID_parque }

lstEnergia = ['101205, 1, 24.2\n', '110607, 8, 54.4\n', '120318, 3, 18.1\n', '090501, 9,
88.4\n', '101209, 1, 26.8\n', '101217, 3, 22.4\n', '190101, 8, 44.0\n'

101205, 1, 24.2
110607, 8, 54.4
120318, 3, 18.1
090501, 9, 88.4
101209, 1, 26.8
101217, 3, 22.4
190101, 8, 44.0

lstParque = ['1,Rosario, 8\n', '6,San Martin, 4\n', '8,Lavalle, 10\n', '3,Esperanza,
3\n', '7,General Pico, 9\n', '9,P.Madryn, 4\n']

1,Rosario, 8
6,San Martin, 4
8,Lavalle, 10
3,Esperanza, 3
7,General Pico, 9
9,P.Madryn, 4
'''


lstEnergia = ['101205, 1, 24.2\n', '110607, 8, 54.4\n', '120318, 3, 18.1\n', '090501, 9, 88.4\n', '101209, 1, 26.8\n', '101217, 3, 22.4\n', '190101, 8, 44.0\n']

def separador(ls):
    i = 0
    ls2 = []
    while i < len(ls):
        while i < len(ls) and ls[i] in ", ":
            i += 1
        pal = ""
        while i < len(ls) and ls[i] not in ", ":
            pal += ls[i]
            i += 1
        if pal != "":
            ls2.append(pal)
    return ls2

#print(separador("101205, 1, 24.2"))

def minimos(lstEnergia):
    d = {}
    arch = lstEnergia
    for linea in arch:
        if linea[-1] == "\n":
            linea = linea[:-1]
        ls = separador(linea) # CORRECTO USO: split(",")
        d[ls[0][:2]] = ls[2]
    

    cEnergiaA = 0
    for x in d.keys():
        if cEnergiaA == 0:
            cEnergiaA = d[x]
        elif cEnergiaA != 0 and d[x] < cEnergiaA:
            cEnergiaA = d[x]
    #print(menor)

    for x in d.keys():
        if d[x] == cEnergiaA:
            AA = x
    #print(año)

    añomenor = AA, float(cEnergiaA)
    
    #print(añomenor)

    d = {}
    for linea in arch:
            if linea[-1] == "\n":
                linea = linea[:-1]
            ls = separador(linea) #CORRECTO USO: split(",")
            d[ls[0][:4]] = ls[2]
    #print(d)

    cEnergiaM = 0
    for x in d.keys():
        if cEnergiaM == 0:
            cEnergiaM = d[x]
        elif cEnergiaM != 0 and d[x] < cEnergiaM:
            cEnergiaM = d[x]
    #print(menor)

    for x in d.keys():
        if d[x] == cEnergiaM:
            AAMM = x
    #print(año)

    añoymesmenor = AAMM, float(cEnergiaM)

    #print(añoymesmenor)

    cont = [añomenor, añoymesmenor]
    return cont

#minimos(lstEnergia)

# def main():
#     print("Prueba para el EJ01")
#     lstEnergia = ['101205,1,24.2\n', '110607,8,54.4\n', '120318,3,18.1\n', '090501,9,88.4\n', '101209,1,26.8\n', '101217,3,22.4\n', '190101,8,44.0\n']
#     print(minimos(lstEnergia))

# main()

# FUNCIONA

def energiaTotal(n, lstEnergia, lstParque):
    d = {}
    arch = lstEnergia
    for linea in arch:
        if linea[-1] == "\n":
            linea = linea[:-1]
        ls = separador(linea) # podria hacerse lo mismo con split solo que antes cuando dieron las lst que retornaria el readlines() las pusieron con " " es por eso que creé esta funcion

        ls[1] = int(ls[1])
        ls[2] = float(ls[2])

        if ls[1] not in d.keys():
            d[ls[1]] = ls[2]
        elif ls[1] in d.keys():
            valor = d[ls[1]]
            d[ls[1]] = valor + ls[2]
    #print(d)

    for x in d.keys():
        d[x] = [d[x]]

    #print(d)

    arch = lstParque
    for linea in arch:
        if linea[-1] == "\n":
            linea = linea[:-1]
        ls = linea.split(",")
        #print(ls)
        ls[0] = int(ls[0])
        ls[2] = int(ls[2])

        #print(ls)

        if ls[0] in d.keys():
            d[ls[0]].append(ls[2])
            d[ls[0]].append(ls[1])

    # print(d)
    # print(ls[0])
    
    for x in d.keys():
        cem = d[x][0] / d[x][1]
        #print(d[x][0])
        d[x].append(cem)
        #d[ls[0]].append(cem)

    #print(d)
    #print(lscem)
    ls2 = []
    for x in d.keys():
        ls2.append(d[x])

    #print(ls2)

    for x in range(len(ls2)-1):
        for u in range(x+1, len(ls2)):
            if ls2[x][0] < ls2[u][0]:
                aux = ls2[x]
                ls2[x] = ls2[u]
                ls2[u] = aux

    #print(ls2)

    ls3 = []
    i = 0
    while i < n:
        cont = [ls2[i][2], ls2[i][0], ls2[i][3]]
        ls3.append(cont)
        i += 1

    return ls3


def main():
    print("Prueba para el EJ02")
    lstEnergia = ['101205,1,24.2\n', '110607,8,54.4\n', '120318,3,18.1\n', '090501,9,88.4\n', '101209,1,26.8\n', '101217,3,22.4\n', '190101,8,44.0\n']
    lstParque = ['1,Rosario,8\n', '6,San Martin,4\n', '8,Lavalle,10\n', '3,Esperanza,3\n', '7,General Pico,9\n', '9,P.Madryn,4\n']
    print(energiaTotal(3, lstEnergia, lstParque))
    #energiaTotal(3, lstEnergia, lstParque)

main()

