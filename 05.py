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

def palabra(ext, cad):
    r = "La función ha retornado una palabra vacía"
    if len(ext) == 2 and len(cad)>0:
        r = "La funcion retornó: " + ext[0] + cad + ext[-1:]
    return r

# palabra("<>", "hola")

def main():
    e = input("Ingrese los extremos: ")
    p = input("Ingrese la palabra: ")

    print(palabra(e, p))

main()