# Definimos la clase Arbol para representar el árbol de búsqueda de soluciones
class Arbol:
    def __init__(self, r):
        # La raíz del árbol es un nodo que contiene el estado inicial del tablero
        self.raiz = r
        # Bandera para detener la búsqueda cuando se encuentra una solución
        self.detenerBusqueda = False

# Definimos la clase Nodo para representar cada nodo del árbol de soluciones
class Nodo:
    def __init__(self, cont):
        # contenido representa el estado actual del tablero de ajedrez
        self.contenido = cont
        # hijos es una lista de nodos hijos
        self.hijos = []

    # Método para hacer una copia del tablero actual
    def copia(self, cont):
        return [list(fila) for fila in cont]

    # Método para verificar si es válido colocar una reina en (fila, col)
    def es_valido(self, fila, col):
        # Recorremos todas las filas y columnas para verificar que no haya conflicto
        for i in range(8):
            # Verifica si hay una reina en la misma fila o columna
            if self.contenido[fila][i] == 1:
                return False
            if self.contenido[i][col] == 1:  
                return False
            # Verifica si hay una reina en las diagonales principales
            if fila + i < 8 and col + i < 8 and self.contenido[fila + i][col + i] == 1:
                return False
            if fila - i >= 0 and col - i >= 0 and self.contenido[fila - i][col - i] == 1:
                return False
            # Verifica si hay una reina en las diagonales secundarias
            if fila + i < 8 and col - i >= 0 and self.contenido[fila + i][col - i] == 1:
                return False
            if fila - i >= 0 and col + i < 8 and self.contenido[fila - i][col + i] == 1:
                return False
        return True

    # Método recursivo para crear los hijos del nodo actual en la fila n
    def creaHijos(self, n, arbol):
        # Si hemos ubicado 8 reinas, se imprime una solución y se detiene la búsqueda
        if n == 8:
            print("Resultado encontrado:")
            for fila in self.contenido:
                print(fila)
            print("\n")
            arbol.detenerBusqueda = True
            return

        # Intentamos colocar una reina en cada columna de la fila n
        for i in range(8):
            # Si es válido colocar una reina en (n, i)
            if self.es_valido(n, i):
                # Copiamos el tablero actual y colocamos una reina en (n, i)
                contHijo = self.copia(self.contenido)
                contHijo[n][i] = 1
                # Creamos un nuevo nodo hijo con esta configuración
                H = Nodo(contHijo)
                # Llamada recursiva para intentar ubicar la siguiente reina en la siguiente fila
                H.creaHijos(n + 1, arbol)
                # Añadimos el hijo a la lista de hijos del nodo actual
                self.hijos.append(H)
                # Si se encontró una solución y se activó detenerBusqueda, salimos del bucle
                if arbol.detenerBusqueda:
                    return

# Configuramos el tablero inicial sin reinas (0 indica espacio vacío)
R = Nodo([[0] * 8 for _ in range(8)])
# Creamos el árbol de soluciones con el nodo raíz R
arbol = Arbol(R)
# Ejecutamos el proceso de creación de hijos, comenzando desde la fila 0
R.creaHijos(0, arbol=arbol)
