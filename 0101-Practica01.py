
# Ej. 1:

# print(".............................")
# print(".         ppppppppp         .")
# print(".      pp           pp      .")
# print(".     pp             pp     .")
# print(".    pp    PP   PP    pp    .")
# print(".   pp     PP   PP     pp   .")
# print(".   pp                 pp   .")
# print(".   pp   PP       PP   pp   .")
# print(".    pp   PP     PP   pp    .")
# print(".     pp    PPPPP    pp     .")
# print(".      pp           pp      .")
# print(".         ppppppppp         .")
# print(".............................")

# Ej. 2:

# print("Ingrese su nombre: ", end="")
# nombre = input()
# print("Ingrese su apellido: ", end="")
# apellido = input()
# print("Hola", nombre.capitalize(), apellido.capitalize() + "!")

# Ej. 3:

# print("Ingrese lado 1: ", end="")
# lado1 = int(input())
# print("Ingrese lado 2: ", end="")
# lado2 = int(input())
# perimetro = lado1*2 + lado2*2
# print("\nPerímetro:", perimetro)
# area = lado1 * lado2
# print("Área:", area)

# Ej. 4:

# print("Ingrese numero: ", end="")
# numc = float(input())
# ent = int(numc)
# print("\nParte entera:", ent)
# frac = numc - ent
# print("Parte fraccionaria:", round(frac, 3))

# Ej. 5:

def print_n(n):
    while n > 0:
        print (n % 10),
        n = n / 10

print("Ingrese numero: ", end="")

n = input()
print_n(n)
#print("\nSeparación en digitos:", print_n(n), sep="-")


# Ej. 6:

# import math

# print("Ingrese base: ", end="")
# base = float(input())
# print("Ingrese altura: ", end="")
# altura = float(input())
# area = (base*altura)/2
# diametro = math.sqrt(((altura)**2 + (base/2)**2))
# perimetro = round(diametro*2+base, 2)
# print("Cálculos para un triangulo de base", int(base), "y altura", str(int((altura))) + ":")
# print("<<< Área=" + str(area), ">>>   <<< Perímetro=" + str(perimetro), ">>>")