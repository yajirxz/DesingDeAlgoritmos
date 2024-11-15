#PesoMax: el peso maximo que puede cargar la mochila
#Objetos: son los objetos dentro de la mochila con su peso cada uno 
#TotalObj: Es el total de los objetos que estan en la mochila
def mochila(PesoMax, objetos, TotalObj):
    #La matriz se utiliza para poder guardar los objetos en la  mochila
    Matriz = [[0 for x in range(PesoMax + 1)] for y in range(TotalObj + 1)]


    for i in range(1, TotalObj + 1):
        #PesoObj: Es el peso del objeto actual
        PesoObj = objetos[i - 1][0]
        #Valor: Es el valor del elemento actual
        valor = objetos[i - 1][1]
        #Itera sobre cada posible capacidad de la mochila desde 0 hasta la maxima
        for capActual in range(PesoMax + 1):
            if PesoObj <= capActual:
                #Suma el valor del elemento actual y el valor máximo obtenido con el resto de la capacidad
                #Toma el valor máximo obtenido sin incluir el elemento actual.  
                Matriz[i][capActual] = max(valor + Matriz[i - 1][capActual - PesoObj], Matriz[i - 1][capActual])
            #Si el peso del elemento actual es mayor que la capacidad actual, copia el valor de la fila anterior
            else:
                Matriz[i][capActual] = Matriz[i - 1][capActual]
    #Devuelve el valor máximo obtenible con los n elementos y la capacidad de la mochila.
    return Matriz[TotalObj][PesoMax]
#Es la capacidad maxima que puede soportar la mochila
CapMax = 12 
#Es una lista de objetos donde cada objeto tiene su peso
objetos = [[1, 2],[2, 3],[3, 4],[4, 5], [5, 6]]

TotalObj = len(objetos)
PesoTotal = mochila(CapMax, objetos, TotalObj)
print(f"El peso total de la mochila es: {PesoTotal}")


#Complejidad espacial: 0(n*CapMax)
#Complejidad temporal: 0(n*CapMax)
