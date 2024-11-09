def MergeSort(lista):
    #se revisa si el tamaño de la lista es mayor a 1, sino la lista ya está ordenada
    if len (lista) > 1:
        #vamos a dividir la lista en dos sublistas
        #izquierda y derecha
        izquierda = lista[:len(lista)//2]
        derecha = lista[len(lista)//2:]
        #La recursion para llamarlos de nuevo 
        MergeSort(izquierda)
        MergeSort(derecha)
        #Aqui las listas reciben un valor de cero por defecto
        i = 0 # indice sublista izquierda
        j = 0 # indice sublista derecha 
        k = 0 # indice de la lista entera 

        #Aquí compara las sublistas izquierda y derecha 
        #y los ordena en la lista en orden
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        #Aquí checa si cada elemento de lista izquierda que elemento es mayor o menor del otro
        while i < len (izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        #Aquí checa si cada elemento de lista derecha que elemento es mayor o menor del otro
        while j < len (derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
#Aquí se recibe la lista desordenada
listaOrdenada = [5,9,3,1,7,4,2,6,8,10]
MergeSort(listaOrdenada)
print(listaOrdenada)

#Complejidad temporal: 0(n log n)
#Complejidad espacial: 0(n)