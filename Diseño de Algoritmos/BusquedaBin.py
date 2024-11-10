# Aplicamos el algoritmo  de busqueda binaria para encontrar un elemento de una lista

#definimos la función y dos parametros
#'lista' para definir la lista de números
#'valor' para encontrar eñ número que queremos encontrar en la lista
def buscar(lista,valor):
    #Si el tamaño de la lista es mayor a dos se divide para hacer la busqueda binaria
    if len(lista) > 2:
        #Indice del centro de la lista
        centro = len(lista) // 2 #T(n) = 1
        #Si valor es igual al valor del centro, se devuelve el mismo centro
        if valor == lista[centro]: #T(n) = 1
            return lista[centro]
        else:
            #Si valor es mayor que el número del centro, busca en la sublista izquierda
            if valor > lista[centro]: # T(n) = log n 
                izquierda = lista[centro +1:]
                return buscar(izquierda, valor)
            #Si valor es menor o igual al número del centro, busca en la sublista derecha
            else:#T(n) = log n 
                derecha = lista[:centro +1]
                return buscar(derecha,valor)
    if len(lista) == 2: # T(n) = 2
        if valor == lista[0]:
            return lista[0]#T(n) = 1 
        if valor == lista[1]:
            return lista[1] # T(n) = 1
    if len(lista) == 1: # T(n) = 1
        if lista[0] == valor:
           return lista[0] 

# T(n) => 1 + 1 + log n + log n + 2 => log n + 4
# O(?) => log n + 4 => O(n) = log n => Es la complejidad del algoritmo

def  listaPrincipal():
    #Aquí ponemos la lista donde queramos buscar
    datos = [-8,4,5,9,12,18,25,40,60,100,220]
    #Aquí ponemos el número que queramos buscar
    #Si el dato que queremos buscar no está en la lista, se dara un mensaje de 'none'
    #significa que no está en la lista
    print(buscar(datos, 56))

if __name__ == '__main__':
    listaPrincipal()