class NodoNario:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []
    def __str__(self):
        return str(self.valor)
    def agregarHijo(self,hijo):
        self.hijos.append(hijo)
        
def arbolPrincipal(lista,arbol):
    if (arbol==None):
        return arbolPrincipal(lista[1:],NodoNario(lista[0]))
    if(len(lista)==0):
        return arbol
    else:
        ancestro(arbol,lista[0]).agregarHijo(NodoNario(lista[0]))
        return arbolPrincipal(lista[1:],arbol)

def impresion(arbol):
    print arbol.valor
    for hijo in arbol.hijos:
        impresion(hijo)

def subArbol(arbol, valor):
    if arbol.valor == valor:
        return arbol
    for sub in arbol.hijos:
        if (subArbol(sub, valor) != None):
            return subArbol(sub, valor)
    return None   

def ancestro(arbol,dato):
    if(len(dato)==1):
        return arbol
    else:
        if(subArbol(arbol,dato)!=None):
            return subArbol(arbol,dato)
        else:
            return ancestro(arbol,dato[0:(len(dato)-1)])
            
def ordenamiento(lista):
    if(len(lista)<2):
        return [lista[0]]
    else:
        if lista[0]>lista[1]:
            return [lista[1]]+ordenamiento([lista[0]]+lista[2:])
        else:
            return [lista[0]]+ordenamiento(lista[1:])
        
def burbuja(lista):
    if(len(lista)==0):
        return []
    else:
        return burbuja(ordenamiento(lista)[0:len(lista)-1])+[ordenamiento(lista)[len(lista)-1]]



print(burbuja(['e','em','emo','emigrar','empalar','es','estrenar','estirar','esconder','eco','ecologico']))

a=arbolPrincipal(burbuja(['e','em','emo','emigrar','empalar','es','estrenar','estirar','esconder','eco','ecologico']),None)


impresion(arbolPrincipal(burbuja(['e','em','emo','emigrar','empalar','es','estrenar','estirar','esconder','eco','ecologico']),None))

print(a.hijos[1].hijos[0].valor)
