def estaenLista1(n, l):
    res = False
    if n in l:
        res = True
    return res

print(estaenLista1(23, [1,2,3,4]))
print(estaenLista1(23, [1,23,3,4]))
print(estaenLista1(23, []))

def estaenLista2(n, l):
    res = False
    for x in l:
        if x == n:
            res = True
    return res

print(estaenLista2(23, [1,2,3,4]))
print(estaenLista2(23, [1,23,3,4]))
print(estaenLista2(23, []))

def estaenLista3(n, l):
    res = False
    i = 0
    ll = len(l)
    while i < ll:
        p = l[i]
        if p == n:
            res = True
        i += 1
    return res

print(estaenLista3(23, [1,2,3,4]))
print(estaenLista3(23, [1,23,3,4]))
print(estaenLista3(23, []))