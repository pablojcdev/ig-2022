
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

# Ej. 8:

# print("Ingrese tiempo en segundos: ", end="")
# s = int(input())
# d = (s/60/60/24)
# h = (d - int(d))*24
# h_c = (s/60/60)
# m = (h_c - int(h_c))*60
# s= (m - int(m)) * 60
# print(int(d), "dia(s),", int(h), "hora(s),", int(m), "minuto(s),", int(s), "segundo(s).")

# Ej. 9:

# print("Ingrese numero de cantidad impar de cifras (al menos 3 cifras):", end="")
# num=input()
# cifras = len(num)
# f = int(num[0])
# l= int(num[-1])
# c = int(num[cifras//2])

# # Otra solucion posible
# # num = "1234567"
# # cifras = lin(num)
# # num = int(num)
# # f = num%10
# # c = num//10**(cifras-1)%10

# print("El numero ingresado tiene", cifras, "cifras.")
# print("La primera cifra es", f, "la ultima es", l, "y la central es", str(c) + ".")

# Ej.  10:

# print("Ingrese un numero binario: ", end="")
# num = int(input())

# u = (((num//1)%10))*2**0
# d = (((num//10)%10))*2**1
# c = (((num//100)%10))*2**2
# um = (((num//1000)%10))*2**3
# dm = (((num//10000)%10))*2**4

# binario = dm + um + c + d + u

# print("\nNumero en decimal:", binario)

# Ingrese un numero binario: 10101
# Número en decimal: 21
# Ingrese un numero binario: 110
# Número en decimal: 6

# Ej. 11:

print("Ingrese un numero decimal (maximo 5 cifras): ", end="")
num = int(input())

u = num%8
uc = num//8
d = uc%8
dc = uc//8
c = dc%8
cc = dc//8
um = cc%8
umc = cc//8
dm = umc%8

octal = u + d*10 + c*100 + um*1000 + dm*10000

print("\nNumero en octal:", octal)
# print("\nNumero en octal:", str(dm) + str(um) + str(c) + str(d) + str(u))
# print("\nNumero en octal:", "{}{}{}{}{}".format(dm, um, c, d, u))

# # Ingrese un numero decimal (maximo 5 cifras): 1234
# # Numero en octal:2322

# Ej. 12:

# num1 = int(input("Ingrese el 1.er número entero: "))
# num2 = int(input("Ingrese el 2.do número entero: "))
# num3 = int(input("Ingrese el 3.er número entero: "))
# r = num1 + num2 + num3

# print('{:=10d}'.format((num1)))
# print('\n{:=10d}'.format((num2)))
# print('\n{:=10d}'.format((num3)))
# print("")
# print("-" * 10)
# print('\n{:=10d}'.format((r)))

# -        4
#
#        105
#
# -       60
#
# ----------
#
#         41

# Ej. 13:

# num1 = int(input("Ingrese el multiplicando: "))
# num2 = int(input("Ingrese el multiplicador: "))

# u = (num2//1)%10
# d = (num2//10)%10
# c = (num2//100)%10

# r_u = num1 * u
# r_d = num1 * d
# r_c = num1 * c
# r = num1 * num2

# print('{:10d}'.format((num1)))
# print('{}{:9d}'.format("x", (num2)))
# print("-" * 10)
# print('{:10d}'.format((r_u)))
# print('{}{:8d}{}'.format("+", (r_d), "-"))
# print('{:8d}{}'.format((r_c), "--"))
# print("-" * 10)
# print('{:10d}'.format((r)))

# Ingrese el multiplicando: 123
# Ingrese el multiplicador: 456
#        123
# x      456
# ----------
#        738
# +     615-
#      492--
# ----------
#      56088