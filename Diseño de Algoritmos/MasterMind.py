#La función random se utiliza para generar números aleatorios
import random
#Aquí para cada número, vamos a establecer un límite para que se mantenga en los 
#4 dígitos y que se genere cualquier número de ese rango
numero = random.randrange(1000, 10000)
#Se pide que se ingrese un número de 4 dígitos
num = int(input("Ingresa un número de 4 dígitos:"))
#Aquí si el número se adivino al primer intento, suelta un mensaje 
#El programa termina si el número que se ingreso es igual al que se genero 
if(num == numero):
	print("¡Impresionante! ¡lo lograste con un solo intento!")
else:
	#Aquí se va ha llevar la cuenta de los intentos que se tarde en lograrlo
	#Se va a autoincrementar cuando se repita el ciclo
	contadorIntentos = 0
	while(num != numero):
		contadorIntentos += 1
		#Aquí se leeran que números que se ingresaron son correctos
		cuenta = 0
		num = str(num)
		numero = str(numero)
		#Una cadena vacia para agregar que números son los correctos y ahí se van guardando 
		# hasta que se adivine el número completamente
		correcto = []

		#Se checara cada uno de los cuatro digitos del número que se ingreso 
		#De ellos se checara cuál de esos número estan bien 
		for i in range(0, 4):
			if(num[i] == numero[i]):
				cuenta += 1
				correcto.append(num[i])
			else:
				continue
		
		#Aquí se informa cuantos numeros se acertaron si es que no se adivino el número completo
		if (cuenta < 4) and (cuenta != 0):
			print("No es el número correcto. Pero acertaste ", cuenta, " dígito(s)!") 
			print("Estos números fueron correctos.")

			for k in correcto:
				print(k, end=' ')
			#Se pide que se ingrese otro número
			print('\n')
			num = int(input("Ingresa tú próximo intento: "))
		
		#Cuando ningún numero de la entrada coincide con el número generado, 
		# salta el siguiente mensaje y se pide que se ingrese otro número
		if(cuenta == 0):
			print("Ningún número coincide")
			num = int(input("Ingresa tú próximo intento: "))
	#Si el número ingresado es el mismo que el generado por el programa 
	#se finaliza el juego y se informa en cuantos intentos se logro
	if num == numero:
		print("¡Bien hechoo!")
		print("Solo te tomo: ", contadorIntentos, "intentos")
	
#Complejidad del programa: 0(n)
#Complejidad espacial: 0(1)

