# print('{:6.2f}'.format(3.141592653589793))

'''def subnumero(num, ls, li):
    return (num//10(10**(li-1)))%(10**(ls-li+1))

def main():
    print(subnumero(12345, 3, 1))

main()'''

from math import pi

def areaCuad(l):
    ac = l * l
    return ac
	
def areaCirc(r):
    acirc = pi*(r**2)
    return acirc

def areaTria(b, h):
    atria = (b * h)/2
    return atria
	
def areaNegra(x):
    aniz = ((areaCuad(x))/2) - (areaCirc(x/2)/2) + areaTria(x, x/2)
    ande = ((areaCuad(x))/2) - (areaCirc(x/2)/2) + areaCirc(x/4)
    an = aniz + ande
    return an

def areaBlanca(x):
	# circ chiquito x/4
    abiz = (areaCirc(x/2)/2)-(areaTria(x, x/2))
    abde = (areaCirc(x/2)/2)-areaCirc(x/4)
    ablanca = abiz + abde
    return ablanca
	
def main():
    x = int(input("Ingrese X: "))
    print(areaNegra(x))
	
main()

# x = int(input("Ingrese X: "))
# ac = x * x
# print(ac)