numero= (int(input("Ingrese el numero:")))
resultado=1

#le pedimos que el rango sea de la multiplicación de cada número 
#inferior a 10

numinf=1
#aqui compararemos si a es el numero inferior al número
#que ingresamos es menor 
while numinf<=numero:
    #aqui multiplicamos cada número que componga el numero que ingresamos
    resultado=resultado*numinf
    #cada número inferior debe ser mayor de uno y de otro por 1
    numinf=numinf+1

    print(resultado)

#Complejidad temporal: O(n)
#Complejidad espacial: O(1) 