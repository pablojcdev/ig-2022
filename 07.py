# Ej: 1

'''
def informe():
    max = 0
    min = None
    c = 0
    sp = 0
    prom = 0

    arch = open("07-1.txt", "r")
    lsarch = arch.readlines()

    for x in range(len(lsarch)):
        c += 1
        linea = int(lsarch[x])
        if linea >= max:
            max = linea
        if min == None:
            min = linea
        elif linea <= min:
            min = linea
        sp += linea
    if c != 0:
        prom = sp / c
    print(max, min, prom, c)
    arch.close()

informe()

# def informe():
#     max = 0
#     min = None
#     c = 0
#     sp = 0

#     arch = open("07-1.txt", "r")
#     linea = arch.readline()

#     while linea != '':
#         c += 1
#         linea = linea[:-1]
#         linea = int(linea)
#         if linea >= max:
#             max = linea
#         if min == None:
#             min = linea
#         elif linea <= min:
#             min = linea
#         sp += linea
#         linea = arch.readline()
#     prom = sp / c
#     print(max, min, prom, c)
#     arch.close()

# def informe():
#     max = 0
#     min = None
#     c = 0
#     sp = 0

#     arch = open("07-1.txt", "r")

#     for linea in arch:
#         c += 1
#         linea = int(linea[:-1])
#         if linea >= max:
#             max = linea
#         if min == None:
#             min = linea
#         elif linea <= min:
#             min = linea
#         sp += linea
#     prom = sp / c
#     print(max, min, prom, c)
#     arch.close()ñ
'''

# Ej. 2:

'''
open r
tomar toda los valores
	recorer todas las lineas mientras haces split(,)
	recorrer esa lista y sacar el promedio
	ir creando una nueva lista de lista 	donde 0 es la misma iista de la linea y 	1 sera el promedio obtenido
pasar al valor siguiente saltando de 2 en dos hasta recorrer todo el archivo
close

open w
	reescribir el archivo con todo lo que hay en la lista que stackeaba
'''

'''
def promedio(ls):
    s = 0
    c = 0
    for x in ls:
        x = int(x)
        s += x
        c += 1
    prom = s / c
    prom = "Promedio: " + str(prom) + "\n"
    return prom

# print(promedio(['10', ' 5', ' 6', ' 8'])) #7,25

def agegarMedia(narch):
    lsn = []
    arch = open(narch, "r")
    for linea in arch:
        linea = linea[:-1]
        aux = linea + "\n"
        lsl = linea.split(",")
        lsn.append(aux)
        lsn.append(promedio(lsl))
    #lsn = str(lsn)
    #print(lsn)
    arch.close()

    arch = open("07-2 promediado", "w")
    for x in lsn:
        arch.write(x)
    arch.close()

agegarMedia("07-2.txt")
'''

# Ej. 3:

# Utiliza el EJ 11 de la anterior practica

'''
open r
extraer las palabras de cada linea con espalabra()
if palabra not in d.keys()
	cada una de esas palabras se 	va agregar como una nueva key 	en un nuevo diccionario d	["palabra"] = 1
elif palabra in d.keys()
	d["palabra"] += 1
	(tomar el valor de lo que esta en tal key y hacer += 1, despues reescribir el dic en tal key con ese nuevo valor aux)

al final recorrer el dic y a cada key agregarla a una lista frecuencias.csv donde cada [] será ["key", "valor en la key"]

close

despues print frecuencias.csv
'''

'''def esletra(x):
    res = False
    if (x>="a" and x<="z") or (x>="A" and x<="Z") or (x in "áéíóúÁÉÍÓÚñÑ/"):
        res = True
    return res

# espalabra("no se porque pienso que escribir de esta manera probara que mi capacidad para escribir mucho mas rapido y sin acentos sea mi unica forma de escribir mas rapido en esta pagina pero aun asi tengo que seguir comprobando esto y hago este texto para comprobar de nuevo mis habilidades y mi velocidad asi que solo estoy poniendo palabras o frases aleatorias para llenar suficientes palabras o lineas para darme cuenta mi velocidad al escribir este texto y que asi de alguna manera ponga una barra y tratar de superarla haciendo el mismo test varias veces hasta que pueda escribirlo todo aunque no se si llegara el dia en que pueda escribir todo esto en menos de un minuto")
# 119

def frecuenciaPalabra(narch):
    arch = open(narch, "r")
    d = {}
    for linea in arch:
        if (linea[-1]) == "\n":
            linea = linea[:-1]
        #print(linea)

        i = 0
        lt = len(linea)
        while i < lt:
            while i < lt and not esletra(linea[i]):
                i += 1
            pal = ""
            v = 0
            while i < lt and esletra(linea[i]):
                pal += linea[i]
                i += 1
            if pal != "" and pal not in d.keys():
                d[pal] = 1
            elif pal != "" and pal in d.keys():
                v = d[pal]
                d[pal] = v + 1
                #print(pal)
    #print(d)
    arch.close()

    ls = []
    k = d.keys()
    #print(k) 
    for x in k:
        cont = x + ", " + str(d[x]) + "\n"
        #ls.append([x, str(d[x])])
        ls.append(cont)
    print(ls)

    arch = open("07-3-frecuencias.csv", "w")
    for x in ls:
        arch.write(x)
    arch.close

    # ls2 = []
    # for x in ls:
    #     cont = x[0] + ", " + x[1] + "\n"
    #     ls2.append(cont)

frecuenciaPalabra("07-3, 4, 5.txt")

# def espalabra(txt):
#     i = 0
#     lt = len(txt)
#     c = 0
#     while i < lt:
#         while i < lt and not esletra(txt[i]):
#             i += 1
#         pal = ""
#         while i < lt and esletra(txt[i]):
#             pal += txt[i]
#             i += 1
#         if pal != "":
#             c += 1
#             print(pal)
#     print(c)
'''

# Ej. 4:

# Posible

'''
def esletra(x):
    res = False
    if (x<="z" and x>="a") or (x<="Z" and x>="A") or x in "áéíóúÁÉÍÓÚñÑ":
        res = True
    return res

def cabecera(narch, cant, pmin, pmax):

    c = 0
    arch = open(narch, "r")
    for linea in arch:
        linea = linea[:-1]

        i = 0
        lt = len(linea)
        while i < lt and c < cant:
            while i < lt and not esletra(linea[i]):
                i += 1
            pal = ""
            while i < lt and esletra(linea[i]):
                pal += linea[i]
                i += 1

            lpal = len(pal)
            if pal != "" and lpal >= pmin and lpal <= pmax:
                c += 1
                print(pal)

cabecera("07-3, 4, 5.txt", 3, 4, 9)
'''

# Ej. 5:

# Utiliza el no repetir palabras del EJ 11

'''
def esletra(x):
    res = False
    if (x<="z" and x>="a") or (x<="Z" and x>="A") or x in "áéíóúÁÉÍÓÚñÑ":
        res = True
    return res

def cabecera2(narch, cant, pmin, pmax):

    c = 0
    d = {}
    arch = open(narch, "r")
    for linea in arch:
        linea = linea[:-1]

        i = 0
        ll = len(linea)
        while i < ll and c < cant:
            while i < ll and not esletra(linea[i]):
                i += 1
            pal = ""
            while i < ll and esletra(linea[i]):
                pal += linea[i]
                i += 1
            
            lpal = len(pal)
            if pal != "" and lpal <= pmax and lpal >= pmin and pal not in d.keys():
                pal = pal + "\n"
                d[pal] = 1
                c += 1
    arch.close()

    arch = open("07-5-resultado.csv", "w")
    for x in d.keys():
        arch.write(x)
    arch.close()

    arch = open("07-5-resultado.csv", "r")
    for linea in arch:
        linea = linea[:-1]
        print(linea)
    arch.close()

cabecera2("07-3, 4, 5.txt", 3, 4, 9)
'''

# Ej. 6:

# Utiliza el no repetir palabras del EJ 11

'''
va a tomar cada palabra del texto y las va ir ingresando en un diccionario 

dic = {"asd":1, "asd2":1, "asd3":1}
k = dic.keys()
print(k[0])

lo que se tiene que hacer es un randint para buscar sacar una key aleatoria desde la posicion aleatoria en la lista (randint(0,len(dic.keys())))
'''

from random import randint

def generadora(ori, dest, cant):
    arch = open(ori, "r")

    d = {}
    for linea in arch:
        if linea[:-1] == "\n":
            linea = linea[:-1]
        if linea not in d.keys():
            d[linea] = 1
    arch.close()

    ls = []
    for x in d.keys():
        ls.append(x)
    
    #print(ls)
    arch = open(dest, "w")
    i = 0
    while i < len(ls) and i < cant:
        arch.write(ls[randint(0, len(ls))])
        i += 1

generadora("07-6-origen.txt", "07-6-destino.txt", 3)

# Ej. 7 y 8 menu
