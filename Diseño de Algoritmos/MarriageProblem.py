# Función para realizar el matrimonio
def emparejamiento_estable(preferencias_a, preferencias_b):
    # Lista  (sin matrimonio)
    libres_a = list(preferencias_a.keys())
    
    # Diccionario para almacenar las propuestas que hacen
    propuestas = {a: [] for a in preferencias_a}
    
    # Diccionario para almacenar las parejas 
    parejas = {}

    # Mientras haya personas libres
    while libres_a:
        # Selecciona el primer persona libre
        a = libres_a[0]
        
        # Obtiene la lista de preferencias de la persona
        lista_preferencias = preferencias_a[a]

        # Itera sobre la lista de preferencias de a
        for b in lista_preferencias:
            # Si a no ha propuesto a b antes
            if b not in propuestas[a]:
                # Registra la propuesta de a hacia b
                propuestas[a].append(b)

                # Si b está libre, empareja a con b
                if b not in parejas:
                    parejas[b] = a
                    libres_a.pop(0)  # a ya no está libre
                    break
                else:
                    # Si b ya tiene pareja, obtenemos la pareja actual de b
                    otro_a = parejas[b]