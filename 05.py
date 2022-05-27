# Ej. 1:

'''
def palabra(cad):
    if len(cad) >= 2:
        r = cad[-2:]*3
        # print(cad[len(cad)-2:len(cad)], end="")
    else:
        r = "La función ha retornado una palabra vacía"
    return r

def main():
    p = input("Ingrese la palabra: ")
    print(palabra(p))

main()
'''

# Ej. 2:

'''
def palabra(ext, cad):
    r = "La función ha retornado una palabra vacía"
    if len(ext) == 2 and len(cad)>0:
        r = "La funcion retornó: " + ext[0] + cad + ext[-1:]
    return r

def main():
    e = input("Ingrese los extremos: ")
    p = input("Ingrese la palabra: ")

    print(palabra(e, p))

main()
'''

# Ej. 3:

'''
def esLetra2(car):
    res = False
    acentos = car in "áéíóúüñÁÉÍÓÚÜÑ"
    if ((car>='a'and car<='z') or (car>='A' and car<='Z') or acentos  ):
        res = True
    return res

def esPalabra(pal):
    res = True
    i=0
    while i<len(pal):
        if not esLetra2(pal[i]):
            res=False
        i=i+1
    return res

def pal(p):
    while len(p)%2 != 0 or not esPalabra(p):
        p = input("Ingrese una palabra de longitud par: ")
    r = "La función ha retornado: " + p[0: len(p)//2]
    return r

def main():
    p = input("Ingrese una palabra de longitud par: ")
    print(pal(p))

main()
'''

# Ej. 4:

'''
def esLetra2(car):
    res = False
    acentos = car in "áéíóúüñÁÉÍÓÚÜÑ"
    if ((car>='a'and car<='z') or (car>='A' and car<='Z') or acentos  ):
        res = True
    return res

def verPal(frase):
    res = ""
    i=0                                             
    largoFrase = len(frase)                         
    s = ""
    c = 0
    ult = ""
    while i<largoFrase :
        pal=""                              
        while i<largoFrase and not esLetra2(frase[i]): 
            i+=1                                      
        while i<largoFrase and esLetra2(frase[i]):    
            pal = pal + frase[i]                      
            i+=1
        if pal != "":
            c += 1
            if c == 1:
                s = s + pal
            if i == largoFrase-1:
                ult = pal
        if pal!="": 
            print(pal)
            # res = res + pal + "\n"         
    # return res
    print("primera:" + s)
    print("ultima:" + ult)

# me ayudo manuel con la variable ult

verPal("Hombre de poca fe, he dicho! Vamos, vamos hombre!")

# Usar el ultimo algoritmo y guardar la primer palabra que se encuentra y compararla con la ultima
# Encontrar la primera palabra con un contador que sea = 1 y 
'''

# Ej. 5:

'''
def valid(x):
    lx = len(x)
    while (lx % 2) != 0 or lx < 2:
        print("Error. ", end="")
        x = input("Ingrese un texto: ")
        lx = len(x)
    return x

def rotacion(x):
    x = valid(x)
    res = x[len(x)//2:] + x[:len(x)//2]
    print(res)

def main():
    x = input("Ingrese un texto: ")
    rotacion(x)

main()
'''

# Ej. 6:

'''
def esLetra2(car):
    res = False
    acentos = car in "áéíóúüñÁÉÍÓÚÜÑ"
    if ((car>='a'and car<='z') or (car>='A' and car<='Z') or acentos  ):
        res = True
    return res

def carAMayu(car):
    if car>='a' and car<='z':
        car = chr(ord (car)-32)    
    return car

def palAMayu (pal):
    i=0
    palMay = ""
    while i<len(pal):
        palMay = palMay + carAMayu(pal[i])
        i=i+1    
    return palMay

def palindroma(frase):
    res = ""
    i=0                                             
    largoFrase = len(frase)                        
    while i<largoFrase :
        pal=""                              
        while i<largoFrase and not esLetra2(frase[i]): 
            i+=1                                      
        while i<largoFrase and esLetra2(frase[i]):    
            pal = pal + frase[i]                      
            i+=1
        if pal!="": 
            res = res + pal
    return res

def main():
    r = palAMayu(palindroma("Así Ramona va, no Marisa"))
    rr = palAMayu(palindroma("Así Ramona va, no Marisa"))[::-1]
    print(r)
    print(rr)

main()

# Sacar el acento de la palabra a convertir
'''

# Ej. 7:

'''
def contarCad(cad, frase):       
    i = 0
    lc = len(cad)
    lf = len(frase)
    c = 0
    while i<lf:
        r = frase[i:lc+i]
        if r == cad:
            c += 1
        i += 1
    print(c)

print(contarCad("o sea","Bueno, yo o sea, este … o sea, o sea"))
'''

# Ej. 8:

'''
def esletra(x):
    res = False
    acentos = x in "áéíóúÁÉÍÓÚ"
    if (x >= "a" and x <= "z") or (x >= "A" and x <= "Z") or acentos:
        res = True
    return res

def texto(frase):
    i = 0
    lf = len(frase)
    res = ""
    palm = ""
    mayusculas = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    while i<lf:
        pal = ""
        palm = ""
        while i<lf and not esletra(frase[i]):
            i += 1
        while i<lf and esletra(frase[i]):
            pal = pal + frase[i]
            i += 1
        if pal != "":
            if pal[0] not in mayusculas:
                palm = palm + (chr(ord(pal[0]) - 32))
            elif pal[0] in mayusculas:
                palm = palm + pal[0]
            res = res + palm + pal[1:] + " "
    return res

print(texto("Soy el hombre más sabio de la tierra"))
'''
# Ej. 9:

'''

def esletra(x):
    res = False
    acentos = x in "áéíóúÁÉÍÓÚ"
    if (x >= "a" and x <= "z") or (x >= "A" and x <= "Z") or acentos:
        res = True
    return res

def texto(frase):
    i = 0
    lf = len(frase)
    c = 0
    res = ""
    pml = ""
    pmc = ""
    lpml = 0
    lpmc = 0
    lp = 0
    while i<lf:
        pal = ""
        while i<lf and not esletra(frase[i]):
            i += 1
        while i<lf and esletra(frase[i]):
            pal = pal + frase[i]
            i += 1
        if pal != "":
            c += 1
            lp = len(pal)
            res = res + pal + " "
            if lp >= lpml:
                pml = pal
                lpml = len(pml)
            if c == 1:
                if lp <= lp:
                    pmc = pal
                    lpmc = len(pmc)
            else: 
                if lp <= lpmc:
                    pmc = pal
                    lpmc = len(pmc)
            print(c, lp)
    print(c)
    print(pml, pmc)
    return res

print(texto("Si hay problema serio, la nave vuelve a la base"))

'''

# Ej. 10:

def esletra(x):
    res = False
    acentos = x in "áéíóúÁÉÍÓÚ"
    if (x>="a" and x<="z") or (x>="A" and x<="Z") or acentos:
        res = True
    return res

def algoritmo(p, t):
    i = 0
    lt = len(t)
    res = False
    while i < lt:
        pal = ""
        resps = 0
        while i < lt and not esletra(t[i]):
            i+=1
        while i < lt and esletra(t[i]):
            pal = pal + t[i]
            i+=1
        if pal != "":
            resp = False
            for x in p:
                if x in pal:
                    resp = True
                resps = resps + resp
            if resps == len(pal):
                res = True
    return res

def main():
    t = input("Texto: ")
    p = input("Palabra: ")
    print(algoritmo(p, t))

main()

# print(algoritmo("casa", "casa bella"))
# print(algoritmo("casa", "el lo saca"))
# print(algoritmo("casa", "casada la bella"))

