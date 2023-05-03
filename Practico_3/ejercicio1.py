tabla =[
    ["Te","    ","    ","   ","Tt" ," "," "],
    ["   ","+Te","-Te" ,"   ","  " ,"x","x"],
    ["Ft","    ","    "," "  ,"Ft" ," "," "],
    ["   ","x"  ,"x"   ,"%Ft","  " ,"x","x"],
    ["I" ,"   ","    ","    ","(E)"," "," "]]

N=["E","e","T","t","F"]
T=["I","+","-","%","(",")","$"]

def row(pila):
    if pila in N:
        return N.index(pila)
    raise ValueError

def column(entry):
    if entry in T:
        return T.index(entry)
    raise ValueError

def analizar(entrada):
    p=["$","E"]
    if entrada=="" or entrada=="$":
        return "Entrada Vacia"
    for sim in entrada:
        #print(p)
        while p[-1] != sim:
            try:
                accion = tabla[row(p[-1])][column(sim)]
            except IndexError or ValueError:
                print("Valor no reconocido: " + sim)
            p.pop()
            if accion=="x":
                #print(p)
                continue
            for simbolo in accion[::-1]:
                p.append(simbolo)
            #print(p)  
        p.pop()
    return p
        
            
            
        



if __name__ == '__main__':
    analizar("I+I%I$")