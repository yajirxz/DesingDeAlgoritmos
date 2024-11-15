#Aquí se presentan las dos cadenas para analizarlas
Cadena1 = "abcabccabaccabbcacabcaccbacc"
Cadena2 = "cabbccabccabbcacbcaacbcaccab"
#Aquí se guarda la subcadena comun mas larga que encontremos
#Por eso se inicializa en cero y esta vacia
resultado = 0
CadenaComun = ""
#Aquí recorre cada carácter en Cadena1, utilizando 'i' como índice
for i in range(len(Cadena1)):
    #Aquí recorre cada carácter en Cadena2, utilizando 'j' como índice
    for j in range(len(Cadena2)):
        #Se utiliza la variable 'k' para encontrar la subcadena mas larga encontrada hasta el momernto
        k = 0

        #Aquí Este bucle compara los caracteres en ambas cadenas desde las
        # posiciones i y j mientras sean iguales y no se excedan los límites de las cadenas
        while (i + k) < len(Cadena1) and (j + k) < len(Cadena2) and Cadena1[i + k] == Cadena2[j + k]:
            #Se incrementa cada iteración de la subcadena mas larga
            k += 1
        #Si una nueva subcadena es mas grande que la subcadena actual se reemplza como la más larga
        if k > resultado:
            resultado = k
            CadenaComun = Cadena1[i:i + k]

print("La subcadena común más larga es: ", CadenaComun)

#Complejidad temporal: 0(n*m*min(n,m))
#Complejidad  espacial: 0(n+m) 