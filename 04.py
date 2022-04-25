# #Ej. 1:

def numeroentero():
    r = None
    i = 0
    while (i < 5):
        num = int(input("Ingrese num: "))
        if(num % 2 == 0):
            i += 1
            r = print("Numero Par. Total de numeros pares ingresados:", i)
            if(num % 4 == 0):
                r = print("Numero Par. Tambien es multiplo de 4. Total de numeros pares ingresados:", i)
    return r

def main():
    numeroentero()

main()