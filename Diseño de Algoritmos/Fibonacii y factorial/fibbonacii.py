def fibbonaci(n):
	#Esta condición verifica si n es igual a 0 o 1. 
    #En el caso de que sea cierto, la función devuelve 1
	if n == 0 or n == 1:
		return 1
	#Si n no es 0 o 1, la función llama a sí misma recursivamente
    # para calcular la suma de los dos números anteriores en la secuencia de Fibonacci
	else:
		return fibbonaci(n -1) + fibbonaci(n-2)
	
#Se pide que se ingrese un rango que queremos que calcule  
funcion = int(input("introduce un rango: "))
x = 0
while x <= funcion:
	print(fibbonaci(x))
	x += 1
	
#Complejidad temporal: O(2^n)
#Complejidad espacial: O(n)