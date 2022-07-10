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
'''

###################### UCA.IG.21.FINAL.FEB.A.PRACTICA ######################

'''
alumnos.csv : ID_alumno [int] | Nombre_Apellido [string]

152002,Juan Gonzalez
152001,Ana Martinez
151988,Ricardo Bochini
180372,Vicente Pernia

materias.csv : ID_materia [int] | Nombre [string]

132,Informática Gral
127,Álgebra y Geometría
137,Física I

cursadas.csv . ID_materia [int] | ID_alumno [int] | nota_cierre [float]

137,152001,4.0
127,151988,6.0
137,151988,7.5
132,152002,2.0
132,151988,6.0
127,152001,2.0
127,180372,10.0
'''

def aprobadas(lstAlumnos ,lstMaterias ,lstCursadas,nom):
    ls2 = []
    for linea in lstAlumnos:
        if linea[-1] == "\n":
            linea = linea[:-1]
        ls = linea.split(",")
        if ls[1] == nom:
            ls2.append(ls[0])
            ls2.append(ls[1])

    #print(ls2)

    ls3 = []
    for linea in lstMaterias:
        if linea[-1] == "\n":
            linea = linea[:-1]
        ls = linea.split(",")
        ls3.append(ls)

    # print(ls3)
    # print(ls2)

    d = {}
    mat = ""
    for linea in lstCursadas:
        if linea[-1] == "\n":
            linea = linea[:-1]
        ls = linea.split(",")
        if ls[1] == ls2[0] and float(ls[2]) >= 4:
            d[ls[0]] = ls[2]
    
    #print(d)

    ls4 = []
    for x in ls3:
        if x[0] in d.keys():
            mat = d[x[0]]
        ls4.append((x[1], float(mat)))
    
    for x in range(len(ls4)-1):
        for u in range(x+1, len(ls4)):
            # print(ls4[x][0][0])
            # print(ls4[u][0][0])
            if ls4[x][0][0] > ls4[u][0][0]:
                aux = ls4[x]
                ls4[x] = ls4[u]
                ls4[u] = aux
                #print("asd")

    #print(ls4)
    # if 'Informática Gral' < 'Física I':
    #     print("asd")
    # if 'Informática Gral' < 'Álgebra y Geometría':
    #     print("asd1")

    # Por lo que "Álgebra" tiene acento en la primera letra no toma como que se valor es menor
    # por ende no lo ordena correctamente. Solucion: Sacar el acento, el profe no nos enseño, ya
    # que siempre trabajamos con textos sin acentos asi que no lo hago y simplemente cambio la letra "Á"
    # por una sin acento

    return ls4

# def main():
#     print("Prueba para el EJ01")
#     lstAlumnos = ['152002,Juan Gonzalez\n','152001,Ana Martinez\n','151988,Ricardo Bochini\n','180372,Vicente Pernia\n']
#     lstMaterias = ['132,Informática Gral\n','127,Algebra y Geometría\n','137,Física I\n']
#     lstCursadas = ['137,152001,4.0\n','127,151988,6.0\n','137,151988,7.5\n','132,152002,2.0\n','132,151988,6.0\n','127,152001,2.0\n','127,180372,10.0\n']
#     print(aprobadas(lstAlumnos ,lstMaterias ,lstCursadas,'Ricardo Bochini' ))
#     #aprobadas(lstAlumnos ,lstMaterias ,lstCursadas,'Ricardo Bochini' )

# main()

# EJ 02

def segmentos(lstAlumnos ,lstMaterias ,lstCursadas):
    #d2 = {"M":[], "R":[], "B":[], "E":[]}
    #print(d2.keys())

    # ls2 = []
    # for linea in lstAlumnos:
    #     if linea[-1] == "\n":
    #         linea = linea[:-1]
    #     ls = linea.split(",")
    #     if ls[1] == nom:
    #         ls2.append(ls[0])
    #         ls2.append(ls[1])

    #print(ls2)

    # ls3 = []
    # for linea in lstMaterias:
    #     if linea[-1] == "\n":
    #         linea = linea[:-1]
    #     ls = linea.split(",")
    #     ls3.append(ls)

    # print(ls3)
    # print(ls2)

    d2 = {}
    lsm = []
    lsr = []
    lsb = []
    lse = []
    for linea in lstCursadas:
        if linea[-1] == "\n":
            linea = linea[:-1]
        ls = linea.split(",")
        if float(ls[2]) < 4:
            lsm.append([ls[0], ls[1]])
        elif float(ls[2]) >= 4 and float(ls[2]) < 7:
            lsr.append([ls[0], ls[1]])
        elif float(ls[2]) >= 7 and float(ls[2]) < 8:
            lsb.append([ls[0], ls[1]])
        elif float(ls[2]) >= 8 and float(ls[2]) <= 10:
            lse.append([ls[0], ls[1]])

    #d2["M"] = ls2

    for linea in lstMaterias:
        if linea[-1] == "\n":
            linea = linea[:-1]
        ls = linea.split(",")
        for x in lsm:
            if x[0] == ls[0]:
                x[0] = ls[1]
        for x in lsr:
            if x[0] == ls[0]:
                x[0] = ls[1]
        for x in lsb:
            if x[0] == ls[0]:
                x[0] = ls[1]
        for x in lse:
            if x[0] == ls[0]:
                x[0] = ls[1]

    for linea in lstAlumnos:
        if linea[-1] == "\n":
            linea = linea[:-1]
        ls = linea.split(",")
        for x in lsm:
            if x[1] == ls[0]:
                x[1] = ls[1]
        for x in lsr:
            if x[1] == ls[0]:
                x[1] = ls[1]
        for x in lsb:
            if x[1] == ls[0]:
                x[1] = ls[1]
        for x in lse:
            if x[1] == ls[0]:
                x[1] = ls[1]

    d2["M"] = lsm
    d2["R"] = lsr
    d2["B"] = lsb
    d2["E"] = lse

    return d2


def main():
    print("Prueba para el EJ02")
    lstAlumnos = ['152002,Juan Gonzalez\n','152001,Ana Martinez\n','151988,Ricardo Bochini\n','180372,Vicente Pernia\n']
    lstMaterias = ['132,Informática Gral\n','127,Algebra y Geometría\n','137,Física I\n']
    lstCursadas = ['137,152001,4.0\n','127,151988,6.0\n','137,151988,7.5\n','132,152002,2.0\n','132,151988,6.0\n','127,152001,2.0\n','127,180372,10.0\n']
    print(segmentos(lstAlumnos ,lstMaterias ,lstCursadas))
    #segmentos(lstAlumnos ,lstMaterias ,lstCursadas)

main()