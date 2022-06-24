import random

def imprimirMatriz(ls):
    res=""
    for f in range(0,len(ls)): 
        for c in range(0,len(ls[0])):
            res = res +  "{:6}".format(ls[f][c])
        res=res+"\n"
    print(res)
    
    
def cargarMatrizAle(nFil,nCol):
    #retorna una lista  de lista 'ls' con la matriz cargada con aleatorios
    ls=[]                        # lista a retornar       
    for f in range(0,nFil):
        auxF=[]                  # lista auxiliar Para cargar la Fila  
        for c in range(0,nCol):
            val= random.randint(0,200)
            auxF.append(val)
        ls.append(auxF)          # cargo la fila en la lista matriz
            
    return ls

def main_02():
    ls = cargarMatrizAle(5,4)
    print(ls)
    #imprimirMatriz(ls)

main_02()