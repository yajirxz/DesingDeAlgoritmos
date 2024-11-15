#Objetos: Son los objetos que vmaos a poner en las bolsas
#CapMax: Es la capacidad maxima que puede tener cada bolsa
def BolsasUtilizadas(Objetos, CapMax):
    #Se crea una lista vacia para almacenar los objetos en las bolsas
    Bolsas = []
    #La
    CapBolsas = CapMax
    #Si el obbjeto cabe en la bolsa actual
    # resta el peso del elemento a la capacidad restante de la bolsa
    for Peso in Objetos:
        if Peso <= CapBolsas:
            CapBolsas -= Peso
        #Si el elemento no cabe en la bolsa 
        else:
            #Agrega la bolsa en la lista y reinicia la capacidad la bolsa
            #y asigna el nuevo objeto restando su peso de la capacidad total
            Bolsas.append(CapBolsas)
            CapBolsas = CapMax - Peso
    
    #Devuelve la longitud de la lista, que representa el número total de 
    #bolsas utilizadas.
    Bolsas.append(CapBolsas)
    return len(Bolsas)

def main():
    #Es la lista de objetos que vamos a guaradar en las bolsas
    Objetos = [7, 6, 3, 4, 1, 9]
    CapMax = 10
    #Define los objetos y la capacidad de las bolsas,
    # y llama a la función 'Bolsasutilizadas' 
    # para calcular el número de bolsas necesarias.
    CantBolsas = BolsasUtilizadas(Objetos, CapMax)
    print("Bolsas utilizadas: ", CantBolsas)

if __name__ == "__main__":
    main()

#Complejidad Espacial: 0(n)
#Complejidad Temporal: 0(n)