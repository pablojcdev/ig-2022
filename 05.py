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