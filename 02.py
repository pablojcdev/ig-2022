from math import sqrt

def area(l1, l2, l3):
    p = (l1 + l2 + l3)/2
    a = sqrt(p*(p-1)*(p-l2)*(p-l3))
    return a

def main():
    l1 = int(input("Ingrese el 1.er lado: "))
    l2 = int(input("Ingrese el 2.do lado: "))
    l3 = int(input("Ingrese el 3.er lado: "))

    miarea = round(area(l1, l2, l3), 2)
    print(miarea)

main()

# Ingrese lado 1: 2
# Ingrese lado 2: 6
# Ingrese lado 3: 7
# El area del triangulo es = 5.56

# El área de un triángulo se puede calcular como √ p(p − a)(p − b)(p − c) siendo p =(a
# +b +c) / 2 y donde a, b, c son los lados del triángulo.