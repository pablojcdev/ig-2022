
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

# print("Ingrese numero: ", end="")
# num = int(input())

# u = ((num//1)%10)**2
# d = ((num//10)%10)**2
# c = ((num//100)%10)**2
# um = ((num//1000)%10)**2
# dm = ((num//10000)%10)**2

# print("\nSeparación en digitos: " + str(dm), um, c, d, u, sep="-")

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

# Ej. 7:

# print("Ingrese el primer numero: ", end="")
# num1 = int(input())
# u1 = ((num1//1)%10)
# print("Ingrese el segundo numero: ", end="")
# num2 = int(input())
# d2 = ((num2//10)%10)*10

# num3 = u1 + d2
# print("El numero resultante es:", num3)

