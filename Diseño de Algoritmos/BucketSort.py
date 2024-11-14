def BucketSort(Lista):
    #Crea las cubetas vacias para poner los números a ordenar
    Cubetas = [[] for i in range(10)]
    for numero in Lista:
        #Dependiendo el indice de cada número se va a acomodar en cada una de las cubetas
        #esperando a ser llamadas para el ordenamiento
        index = numero // 10
        Cubetas[index].append(numero)
    #Se da una lista vacia para acomodar los números 
    ListaOrdenada = []
    #Se vaq checando cada cubeta  
    for cubeta in Cubetas:
        #Se van ordenando los números de cada cubeta y se van agregando en la lista vacía
        ListaOrdenada.extend(sorted(cubeta))
    return ListaOrdenada
 
#Lista a ordenar 
Lista = [6, 9, 1, 7, 3, 4, 2, 0, 5]
print("Lista Original:", Lista)
print("Lista Ordenada:", BucketSort(Lista))

#Complejidad temporal: 0(n)