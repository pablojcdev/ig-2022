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
'''

# Ej. 7: 

'''
def agregar():
    arch = open("07-7-persona.csv", "r")

    d = {}
    for linea in arch:
        if linea[-1] == "\n":
            linea = linea[:-1]
        #print(linea)
        aux = linea
        ls = aux.split(",")
        #print(ls[2], end="")
        d[ls[2]] = [ls[0], ls[1]]
    arch.close()

    dni = input("DNI: ")
    while dni in d.keys():
        print("ERROR, este campo no puede estar repetido")
        dni = input("DNI: ")
    nombre = input("NOMBRE: ")
    apellido = input("APELLIDO: ")

    arch = open("07-7-persona.csv", "a")
    cont = nombre + "," + apellido + "," + dni + "\n"
    arch.write(cont)
    arch.close()

#agregar()


# Tengo todas las keys por DNI
# Pide el input del DNI
# Si existe, buscar en ls2[x][2] == DNI
# hacer un remove() a esa posicion de la lista
# reescribir la lista de lista cada los 3 valores agregando el \n al final 
# reescribir el archivo usando la nueva lista


def eliminar():
    arch = open("07-7-persona.csv", "r")

    d = {}
    ls2 = []
    for linea in arch:
        # aux2 = linea
        # ls2.append(aux2)

        if linea[-1] == "\n":
            linea = linea[:-1]
        #print(linea)
        aux = linea
        ls = aux.split(",")
        ls2.append(ls)
        #print(ls[2], end="")
        d[ls[2]] = [ls[0], ls[1]]
    arch.close()

    #print(ls2)

    dni = input("DNI: ")
    while dni not in d.keys():
        print("ERROR, no se encontró tal DNI")
        dni = input("DNI: ")
    #dni = "89236547"

    for x in ls2:
        if x[2] == dni:
            ls2.remove(x)

    #print(ls2)

    ls3 = []
    for x in ls2:
        cont = x[0] + "," + x[1] + "," + x[2] + "\n"
        ls3.append(cont)
    
    #print(ls3)

    arch = open("07-7-persona.csv", "w")
    for x in ls3:
        arch.write(x)
    arch.close()

# eliminar()

# El user puede ingresar tanto DNI como apellido
#     Si es DNI
#         Tiene 8 caracteres y esta compuesto unicamente por numeros
#             Para saber si esta compuesto unicamente por nuemros va a ser un "x in "1234567890"
#     Apelliodo (else)

# Recorrer el registro
#     ls = []
#     open arch en "r"
#     for linea in arch
#         linea[-1] == "\n"
#             remoueve el n
#         aux = linea
#         ls = linea.split(",")
#         comparar la ls
#             Hasta que x[2] o x[0] sea igual a INPUT
#             print(aux)

def buscar():

    entrada = input("Ingrese DNI o Apellido: ")
    #input = "89236547"

    arch = open("07-7-persona.csv", "r")
    for linea in arch:
        if linea[-1] == "\n":
            linea = linea[:-1]
        aux = linea
        ls = linea.split(",")
        if ls[1] == entrada or ls[2] == entrada:
            print(aux)
    arch.close()

# buscar()

# ORDENAR

# ordenar es una reescritura del archivo en base a tal campo

# input de por que campo lo queres ordenar
#     1 = 0
#     2 = 1
#     3 = 2

# ls = []
# ls2 = []
# arch open en r
#     if linea...
#     ls = linea.split
#     ls2.append(ls)
# arch.close()

# if input == 1 # (0)
#     for x in range(len(ls2)-1)
#         for u in range(x+1, len(ls2)):
#             if ls[x][1] > ls[u][1]
#                 aux = ls[x][1]
#                 ls[x][1] = ls[u][1]
#                 ls[u][1] = aux


def ordenar():
    entrada = int(input("Ingrese un numero para ordenarlo segun ese campo. Las opciones serán 1 Nombre; 2 Apellido; 3 DNI: "))
    nums = [1,2,3]
    while entrada not in nums:
        entrada = int(input("ERROR. Las opciones son 1 Nombre; 2 Apellido; 3 DNI: "))

    #entrada = 3

    arch = open("07-7-persona.csv", "r")
    ls = []
    ls2 = []
    for linea in arch:
        if linea[-1] == "\n":
            linea = linea[:-1]
        ls = linea.split(",")
        ls2.append(ls)
    arch.close()

    print(ls2)

    if entrada == 1:
        entrada = 0
    elif entrada == 2:
        entrada = 1
    elif entrada == 3:
        entrada = 2

    for x in range(len(ls2)-1):
        for u in range(x+1, len(ls2)):
            if ls2[x][entrada] > ls2[u][entrada]:
                aux = ls2[x]
                ls2[x] = ls2[u]
                ls2[u] = aux

    print(ls2)

    ls3 = []
    for x in ls2:
        cont = x[0] + "," + x[1] + "," + x[2] + "\n"
        ls3.append(cont)
    print(ls3)

    arch = open("07-7-persona.csv", "w")
    for x in ls3:
        arch.write(x)
    arch.close()

# ordenar()

def mostrar():
    arch = open("07-7-persona.csv", "r")
    for linea in arch:
        if linea[-1] == "\n":
            linea = linea[:-1]
        print(linea)
    arch.close()

#mostrar()

def selector(x):
    if x == 1:
        agregar()
    elif x == 2:
        eliminar()
    elif x == 3:
        buscar()
    elif x == 4:
        ordenar()
    elif x == 5:
        mostrar()


def main():
    x = int(input("1. AGREGAR REGISTRO\n2. ELIMINAR REGISTRO\n3. BUSCAR REGISTRO\n4. ORDENAR ARCHIVO POR\n5. MOSTRAR ARCHIVO\n6. SALIR\nIngrese el valor de la opción: "))
    nums = [1,2,3,4,5,6]
    while x not in nums:
        x = int(input("ERROR, ingrese una de las siguientes opciones:\n1. AGREGAR REGISTRO\n2. ELIMINAR REGISTRO\n3. BUSCAR REGISTRO\n4. ORDENAR ARCHIVO POR\n5. MOSTRAR ARCHIVO\n6. SALIR\nIngrese el valor de la opción: "))
    
    while x != 6:
        selector(x)
        x = int(input("1. AGREGAR REGISTRO\n2. ELIMINAR REGISTRO\n3. BUSCAR REGISTRO\n4. ORDENAR ARCHIVO POR\n5. MOSTRAR ARCHIVO\n6. SALIR\nIngrese el valor de la opción: "))
main()

# 233 LINEAS DE CODIGO PARA EL EJ 7 MDS

'''

# Ej. 8: menu

# provincias.txt
# (archivo CSV)

#   ID_provincia(entero) | nombre(cadena de caracteres) | ID_pais

# localidades.txt
# (archivo CSV)

#   ID_localidad (entero) | nombre (cadena de caracteres) | ID_provincia (entero) | superficie (entero) | poblacion (entero)

# paises.txt
# (archivo CSV)

#   ID_pais (entero) | nombre (cadena de caracteres) | ID_idioma (entero)

def poblacion(id):
    ls = []
    arch = open("07-8-provincias.txt", "r")
    for linea in arch:
        if linea[-1] == "\n":
            linea = linea[:-1]
        ls = linea.split(",")
        if int(ls[0]) == id:
            nom = ls[1]
    arch.close()

    pobl = 0
    arch = open("07-8-localidades.txt", "r")
    for linea in arch:
        if linea[-1] == "\n":
            linea = linea[:-1]
        ls = linea.split(",")
        if int(ls[2]) == id:
            pobl += int(ls[4])
    arch.close()

    print(nom, pobl)

#poblacion(1)

'''
max = 0
d = {}
Recorrer el localidades.txt
    hacer linea...
    ahcer split
    if max == 0:
        max = int(ls[4])
    elif max != 0 and int(ls[4]) >= max:
        max = int(ls[4])
    d[max] = ls[1]
'''

def localidadMaxima():
    ls = []
    ls2 = []
    max = 0

    arch = open("07-8-localidades.txt", "r")
    for linea in arch:
        if linea[-1] == "\n":
            linea = linea[:-1]
        ls = linea.split(",")
        if max == 0:
            max = int(ls[4])
            ls2 = [str(max), ls[1], ls[2]]
        elif max != 0 and int(ls[4]) >= max:
            max = int(ls[4])
            ls2 = [str(max), ls[1], ls[2]]
    arch.close()
    # print(ls2)

    arch = open("07-8-provincias.txt", "r")
    for linea in arch:
        if linea[-1] == "\n":
            linea = linea[:-1]
        ls = linea.split(",")
        
        if ls[0] == ls2[2]:
            ls2.append(ls[1])
            ls2.append(ls[2])
    arch.close()
    # print(ls2)

    arch = open("07-8-paises.txt", "r")
    for linea in arch:
        if linea[-1] == "\n":
            linea = linea[:-1]
        ls = linea.split(",")

        if ls[0] == ls2[4]:
            ls2.append(ls[1])
        
    # print(ls2)

    #print("Poblacion: " + ls2[0] + "\nLocalidad: " + ls2[1] + "\nProvincia: " + ls2[3] + "\nPais: " + ls2[5])
    print("{:12}{:>10}\n{:12}{:>10}\n{:12}{:>10}\n{:12}{:>10}".format("Poblacion:", ls2[0], "Localidad:", ls2[1], "Provincia:", ls2[3], "Pais:", ls2[5]))

localidadMaxima()