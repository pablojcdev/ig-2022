# IG.21.1C.DM.PP3.T1

'''
def consonantes(x):
    res = False
    if x in "bcdfghjklmnopqrstuvwxyz":
        res = True
    return res

def esValido(x, u):
    res = False
    if x == u and consonantes(u):
        res = True
    return res

def maxima(t):
    i = 0
    ls = len(t)
    res = ""
    secMax= ""
    posMax= ""
    while i < ls:
        pal = t[i]
        pos = i
        i += 1
        while i < ls and not esValido(pal[-1], t[i]):
            pal = t[i]
            pos = i
            i += 1
        while i < ls and esValido(pal[-1], t[i]):
            pal += t[i]
            i += 1
        
        if consonantes(pal[-1]) and len(pal)>=len(secMax):
            secMax = pal
            posMax = pos
    if secMax != "":
        res = str(posMax) + "," + secMax
    return res

print(maxima("krppagdciiwwbxb"))
print(maxima(""))# == "") 
print(maxima("a"))# == "") 
print(maxima("bb"))# == "0, bb" ) 
print(maxima("abc"))# == "2,c" ) 
print(maxima("azzc"))# == "1, zz" ) 
print(maxima("wwwfinqqifobdccgernsdd"))# == "0,WWW"), 
print(maxima("krppagdciiwwbxb"))# == "10, WW" ) 
print(maxima("apjutlqkcvrhgK"))# == "13,k") 
print(maxima("aeiiiiua"))# == "") 
print(maxima("qoxfinqqifobdcccgernsddd"))# == "21, ddd" ) 
print(maxima("jpholicwhkhhf"))# == "10, hh" )
print(maxima("aaaavuzfxilwajwycajuwwwwietqrflqdwww1p1")) #== "20,wwww" ) 
'''

# IG.21.1C.GT.PP3.T1

'''
def ordenarlista(ls):
    for x in range(0, len(ls)-1):
        for u in range(x+1, len(ls)):
            if ls[x] > ls[u]:
                aux = ls[x]
                ls[x] = ls[u]
                ls[u] = aux

def listadefinida(ls, n):
    i = 0
    ls2 = [] + ls
    ordenarlista(ls)
    res = str(ls[i])
    i += 1
    while i < len(ls) and i <= n-1:
        res += "-" + str(ls[i])
        i += 1
    print("Para lista: ", ls2, "y N=" + str(n))
    print("Resultado:", res)

listadefinida([12,100,5,23,65,34], 3)
listadefinida([12,100,5,23,65,34], 10)
'''

# IG.21.1C.IT.PP3.T1

'''
def promedio(ls):
    res = 0
    for x in range(len(ls)):
        res += ls[x]
    prom = res / len(ls)
    return prom

def lsmod(ls, prom):
    i = 0
    while i < len(ls):
        while i < len(ls) and ls[i] > prom:
            ls.remove(ls[i])
        i += 1

def main():
    ls = [24,30,2,10,15,6,65,42]
    ls2 = [] + ls
    lsmod(ls, promedio(ls))
    print("Para la lista", str(ls2) + ", el promedio es:", promedio(ls2), "y la lista modificada:", ls)

main()
'''

# IG.21.1C.JT.PP3.T1

'''
def esLetra(x):
    res = False
    if (x>="a" and x<="z") or (x>="A" and x<="Z") or x in "áéíóúÁÉÍÓÚ":
        res = True
    return res

def palabras(t):
    i = 0
    ls = len(t)
    lst = []
    while i < ls:
        while i < ls and not esLetra(t[i]):
            i+=1
        pal=""
        while i < ls and esLetra(t[i]):
            pal += t[i]
            i+=1
        if pal != "":
            if pal not in lst:
                lst.append(pal)
    return lst

print(palabras("hola como estas hola como"))
'''

# IG.21.1C.BM.PP3.T1

def esLetra(x):
    res = False
    if (x>="a" and x<="z") or (x>="A" and x<="Z") or x in "áéíóúÁÉÍÓÚ":
        res = True
    return res

def abierta(x):
    res = False
    if x in "aeoAEEO":
        res = True
    return res

def cerrada(x):
    res = False
    if x in "iuIU":
        res = True
    return res

def palabra(pal):
    x = 0
    a = 0
    c = 0
    res = False
    while x < len(pal):
        if abierta(pal[x]):
            a += 1
        if cerrada(pal[x]):
            c += 1
        x += 1
    #    res = pal + ": " + str(a) + " - " + str(c)
    if a == c:
        res = True
    return res

def maxima(t):
    i = 0
    ls = len(t)
    palm = ""
    while i < ls:
        while i < ls and not esLetra(t[i]):
            i+=1
        pal=""
        while i < ls and esLetra(t[i]):
            pal += t[i]
            i+=1
        if pal != "" and palabra(pal):
            if len(pal) > len(palm):
                palm = pal
    return palm



print( maxima("") =="" ) 
print( maxima("abc") =="" ) 
print( maxima("aie") =="" ) 
print( maxima("t^pucho $ pichichu &") =="pucho" ) 
print( maxima("pucho,-,pucherito-nitoAcarlin") =="pucherito" ) 
print( maxima("? roki +roi nahuelhuapi-huechulafquen $") =="huechulafquen" ) 
print( maxima("$guam - chau &") == "guam" ) 
print( maxima("- nahuel - huapi") == "" ) 
print( maxima("azauwuAai-nahuelhuapi +. doid +") == "nahuelhuapi" ) 
print( maxima("zqui.hui_?raiz.&ravhvrwlil") == "ravhvrwlil" ) 
print( maxima("TaAiUY A TaauAiUY < uIY wwowwwiww") == "wwowwwiww" ) 