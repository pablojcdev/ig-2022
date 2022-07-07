# import random
# def fun(a,b):
#     x = not(a and b)
#     y = not a and not b
#     if x != y:
#         res = 50
#     else:
#         res = 20
#     return res

# def main():
#     a = random.randint(0,1)
#     b = random.randint(0,1)
#     #print("{1:d} {0:d}".format(fun(a,b),fun(b,a)))

#     print(fun(1,1))
#     print(fun(1,0))
#     print(fun(0,1))
#     print(fun(0,0))
# main()

'''
A. Imprime SIEMPRE los valores -> 20 20
B. Imprime SIEMPRE el valor -> 20
C. Imprime SIEMPRE los valores -> 50 50
D. Imprime SIEMPRE el valor -> 50
E. Lo que imprime DEPENDE EXCLUSIVAMENTE de los valores pasados a la función 'fun'
F. No imprime. Hay un ERROR cuando se ejecuta el código.
G. NINGUNA de las respuestas son correctas.
'''

def fun(lst):
    lst+=[4,5,6]
    lst.pop(6)
    return lst

def main():
    lst=[1,2,3]
    fun(lst)
    print(lst)

main()