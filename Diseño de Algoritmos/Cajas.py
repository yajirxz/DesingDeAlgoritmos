# Definimos la clase Box para representar una caja con altura, ancho y profundidad
class Box:
    def __init__(self, h, w, d):
        self.h = h  # altura de la caja
        self.w = w  # ancho de la caja
        self.d = d  # profundidad de la caja

    # Definimos el operador '<' para comparar el área de la base de dos cajas
    # La comparación se hace multiplicando la profundidad por el ancho
    def __lt__(self, other):
        return self.d * self.w < other.d * other.w

# Función para calcular la altura máxima de una pila de cajas
def maxStackHeight(arr, n):
    # Creamos una lista rot para almacenar todas las rotaciones posibles de las cajas
    rot = [Box(0, 0, 0) for _ in range(3 * n)]
    index = 0  # índice para agregar rotaciones

    # Generamos tres rotaciones para cada caja en arr
    for i in range(n):
        # Primera rotación: la caja mantiene su orientación
        rot[index].h = arr[i].h
        rot[index].d = max(arr[i].d, arr[i].w)
        rot[index].w = min(arr[i].d, arr[i].w)
        index += 1

        # Segunda rotación: rotamos la caja, usando ancho como altura
        rot[index].h = arr[i].w
        rot[index].d = max(arr[i].h, arr[i].d)
        rot[index].w = min(arr[i].h, arr[i].d)
        index += 1

        # Tercera rotación: rotamos la caja, usando profundidad como altura
        rot[index].h = arr[i].d
        rot[index].d = max(arr[i].h, arr[i].w)
        rot[index].w = min(arr[i].h, arr[i].w)
        index += 1

    # Ahora tenemos 3*n cajas (rotaciones) y las ordenamos en orden descendente
    n *= 3
    rot.sort(reverse=True)

    # Inicializamos el arreglo msh para almacenar la máxima altura alcanzable con cada caja
    msh = [0] * n

    # La altura máxima de cada caja es su altura inicial (caso base)
    for i in range(n):
        msh[i] = rot[i].h

    # Calculamos la máxima altura acumulada para cada caja
    for i in range(1, n):
        for j in range(0, i):
            # Verificamos si la caja i puede ir sobre la caja j
            if rot[i].w < rot[j].w and rot[i].d < rot[j].d:
                # Si la altura acumulada al apilar la caja i sobre j es mayor, la actualizamos
                if msh[i] < msh[j] + rot[i].h:
                    msh[i] = msh[j] + rot[i].h

    # Buscamos la máxima altura alcanzada en el arreglo msh
    maxm = -1
    for i in range(n):
        maxm = max(maxm, msh[i])

    return maxm

# Programa principal
if __name__ == "__main__":
    # Definimos un conjunto de cajas con sus dimensiones (altura, ancho, profundidad)
    C = [
        [2, 1, 3],
        [5, 4, 1],
        [3, 3, 4],
        [2, 7, 3],
        [1, 9, 2],
        [5, 1, 4],
        [7, 7, 3],
        [2, 9, 1],
        [4, 8, 7],
        [3, 7, 9]
    ]
    # Creamos una lista de objetos Box a partir de la lista de dimensiones
    arr = [Box(h, w, d) for h, w, d in C]

    # Calculamos la altura máxima posible al apilar las cajas
    n = len(arr)
    print("La altura máxima es:", maxStackHeight(arr, n))
