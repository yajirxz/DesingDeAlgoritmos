#tamaño del tablero de ajedrez 8x8, en total 64 casillas
N = 8
#Son los movimientos que puede hacer el caballo al moverse de arriba - abajo e izquierda - derecha
EjeX = [2, 1, -1, -2, -2, -1, 1, 2]
EjeY = [1, 2, 2, 1, -1, -2, -2, -1]
#Aquí se checa que el caballo pueda hacer el movimiento para que pueda avanzar
def Avanzar(x, y, casillas):
    #tambien checa que al hacer el movimiento no se salga del tablero
    return 0 <= x < N and 0 <= y < N and casillas[x][y] == -1
#Se checa que el caballo pueda moverse de manera seguida
def Tour(x, y, movimiento, casillas):
    #Si el caballo realizo 64 movimientos entonces fue un exito
    if movimiento == N * N:
        return True  
    #Si el movimiento del caballo es realizado deja un número en esa casilla que indica que paso por ahí
    for i in range(8):
        AvanzarX = x + EjeX[i]
        AvanzarY = y + EjeY[i]
        if Avanzar(AvanzarX, AvanzarY, casillas):
            casillas[AvanzarX][AvanzarY] = movimiento
            #Autoincrementa el número de movimientos  
            if Tour(AvanzarX, AvanzarY, movimiento + 1, casillas):
                return True  
            #Si el caballo no pudo realizar el movimiento, entonces se regrea 1 a la cuenta 
            #hasta que avanace en una casilla que no ha estado 
            casillas[AvanzarX][AvanzarY] = -1  
    return False
#Aqui se crea el tablero, con todas sus casillas 
def TourCaballo():
    casillas = [[-1 for _ in range(N)] for _ in range(N)]
    #El caballo inicia desde la casilla con ejeX 0 y ejeY 0
    #El movimiento seria marcado como el movimiento cero
    casillas[0][0] = 0
    #Se resuleve el tour desde la posicion inicial y se imprime el tablero con los numeros de movimiento
    if Tour(0, 0, 1, casillas):
        for avance in casillas:
            print(avance)
TourCaballo()

#Complejidad espacial: 0(n^2)
#Complejidad temporal: 0(8^(n^2)) en el peor caso 