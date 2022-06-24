'''
def indiceCad(cad, frase ):
    res = None                                  # inicializa var de respuesta
    i = 0                                       # inicializa var indice
    if cad!="":
        while i<(len(frase)-len(cad)+1):
            if frase[i:i+len(cad)]==cad:
                #SI encontre cad en frase               
                res = str(i)
                # if (res==None):                 # Armado cadena de respuesta
                #     res = str(i)                # primera vez
                # else:
                #     res = res + "," + str(i)    # el resto de las veces                   
                i = i + len(cad)                # incremento saltando la 
                                                #    cadena encontrada
            else:
                #NO encontre cad en frase
                i = i + 1                       # incremento de a uno              
    return res

print(indiceCad("h", "kk h como estas h como h"))
'''
