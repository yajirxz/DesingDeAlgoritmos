def quickSort(lista):
	#Si la lista está vacía entonces solo regresa un 0
	if lista is None:
		return 0
	if len(lista) <= 1:
		return lista
	#se crean dos listas vacias de izquierda a derecha 
	#para almacenar los números que sean menor o mayor al pivote 
	else:
		piv = lista[-1]
		izquierda = []
		derecha = []
		for x in lista[:-1]:
			#aqui se comparan si los numeros son mayores al pivote y se manda a la derecha
			if x > piv:
				derecha.append(x)
			#si el número no es mayor al pivote se manda a la izquierda del pivote 
			else:
				izquierda.append(x)
		#Esto muestra la lista ya ordenada
		#primero los numeros menores al pivote, el pivote y los números mayores al pivote
		resultado = quickSort(izquierda) + [piv] + quickSort(derecha)
		return resultado
#Aquí se muestra la lista desordenada 
lista = [10,1,12,5,8,4,3,11,2,6,9]
quickSort(print(quickSort(lista)))

#Complejidad temporal: 0(nlogn)
#Complejidad temporal: 0(n)