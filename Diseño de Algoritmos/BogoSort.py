#Es para poder generar números aleatorios
import random

def orden(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

#Mezcla los números de la lista de manera akeatoria 
#hasta que este ordenada
def BogoSort(lista):
    intentos = 0  # Números de intentos
    while not orden(lista):
        intentos += 1
        #Mezcla los números de la lista de manera akeatoria 
        #hasta que este ordenada
        random.shuffle(lista)
        print(f"Intento {intentos}: {lista}")
    return lista

# Lista desordenada
lista = [3, 5, 1, 4, 2]

# Llamada a la función para ordenar la lista
print("Lista original:", lista)
ListaOrdenada = BogoSort(lista)
print("Lista ordenada:", ListaOrdenada)

#Complejidad = 0 ((n + 1)!) 
