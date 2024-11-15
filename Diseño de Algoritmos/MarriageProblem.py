# Número de hombres o mujeres
N = 4

# Esta función devuelve verdadero si
# la mujer 'muj' prefiere al hombre 'homb2' sobre el hombre 'homb'
def MujerPref(prefiere, muj, homb, homb2):
    # Verificar si 'muj' prefiere a 'homb' sobre su compromiso actual 'homb2'
    for i in range(N):
        # Si 'homb2' viene antes que 'homb' en la lista de 'muj',
        # si 'muj' prefiere su compromiso actual, no hacer nada
        if (prefiere[muj][i] == homb2):
            return True

        # Si 'homb' viene antes que 'homb2' en la lista de 'muj',
        # entonces cancela su compromiso actual y se compromete con 'homb'
        if (prefiere[muj][i] == homb):
            return False

def StableMarriage(prefiere):
    # Almacena el compañero de las mujeres. Este es nuestro arreglo de salida
    # que almacena la información de los compromisos.
    ParejaMujer = [-1 for i in range(N)]

    # Un arreglo para almacenar la disponibilidad de los hombres.
    # Si HombreSoltero es False, entonces el hombre está libre,
    # sino, está comprometido.
    HombreSoltero = [False for i in range(N)]

    freeCount = N

    # Si hay hombres libres
    while (freeCount > 0):
        # Escoger el primer hombre libre 
        homb = 0
        while (homb < N):
            if (HombreSoltero[homb] == False):
                break
            homb += 1

        # Uno a uno va a todas las mujeres según
        # las preferencias de 'homb'. Aquí 'homb' es el hombre libre escogido
        i = 0
        while i < N and HombreSoltero[homb] == False:
            muj = prefiere[homb][i]

            # La mujer de preferencia está libre,
            # 'muj' y 'homb' se convierten en pareja
            # Están comprometidos, pero no casados
            if (ParejaMujer[muj - N] == -1):
                ParejaMujer[muj - N] = homb
                HombreSoltero[homb] = True
                freeCount -= 1

            else:
                # Si 'muj' no está soltera
                # Encontrar el compromiso actual de 'muj'
                homb2 = ParejaMujer[muj - N]

                # Si 'muj' prefiere a 'homb' sobre su compromiso actual 'homb2',
                # entonces rompe el compromiso entre 'muj' y 'homb2' y
                # compromete a 'homb' con 'muj'.
                if (MujerPref(prefiere, muj, homb, homb2) == False):
                    ParejaMujer[muj - N] = homb
                    HombreSoltero[homb] = True
                    HombreSoltero[homb2] = False
            i += 1

    print("Mujer ", " Hombre")
    for i in range(N):
        print(i + N, "\t", ParejaMujer[i])
#Se llama a la función 'StableMarriage' para encontrar las parejas estables
prefiere = [
    [7, 5, 6, 4], [5, 4, 6, 7],
    [4, 5, 6, 7], [4, 5, 6, 7],
    [0, 1, 2, 3], [0, 1, 2, 3],
    [0, 1, 2, 3], [0, 1, 2, 3]
]

StableMarriage(prefiere)

#Complejidad temporal: 0(n^2)
#Complejidad espacial: 0(n)

