# Función que agrupa las respuestas en parejas
def agrupar_parejas(respuestas):
    parejas = []  # Lista que almacenará las parejas formadas
    i = 0  # Índice para recorrer las respuestas
    while i < len(respuestas) - 1:  # Se agrupan en pares mientras haya al menos dos elementos
        parejas.append((respuestas[i], respuestas[i+1]))  # Agrega la pareja a la lista
        i += 2  # Avanza al siguiente par
    # Si hay un número impar de respuestas, se agrega el último elemento sin pareja
    if len(respuestas) % 2 != 0:
        parejas.append((respuestas[-1],))  # Agrega el último elemento solo
    return parejas

# Función que filtra las parejas según el tipo de respuestas
def filtrar_parejas(parejas):
    nuevo_grupo = []  # Lista que almacenará las respuestas filtradas
    for pareja in parejas:
        if len(pareja) == 2:  # Solo procesamos las parejas que tienen dos elementos
            if pareja[0] == 'v' and pareja[1] == 'v':  # Si ambas respuestas son 'v', se agrega 'v'
                nuevo_grupo.append('v')
            elif pareja[0] == 'f' and pareja[1] == 'f':  # Si ambas respuestas son 'f', se agrega 'f'
                nuevo_grupo.append('f')
        elif len(pareja) == 1:  # Si la pareja tiene un solo elemento (en caso de número impar de respuestas)
            if pareja[0] == 'v':  # Si el único elemento es 'v', se agrega 'v'
                nuevo_grupo.append('v')
    return nuevo_grupo

# Función principal para determinar si los mentirosos son 'v' o 'f'
def los_mentirosos(respuestas):
    while len(respuestas) > 1:  # Mientras haya más de una respuesta
        parejas = agrupar_parejas(respuestas)  # Agrupa las respuestas en parejas
        respuestas = filtrar_parejas(parejas)  # Filtra las parejas según las reglas
        if not respuestas:  # Si no quedan respuestas, significa que no se puede determinar
            return False
    return respuestas[0] if respuestas else False  # Si queda una respuesta, se devuelve, sino False

# Ejemplo de uso
respuestas_iniciales = ['v', 'v', 'v', 'f', 'f', 'f', 'v', 'f', 'v']
resultado_final = los_mentirosos(respuestas_iniciales)
print(resultado_final)
