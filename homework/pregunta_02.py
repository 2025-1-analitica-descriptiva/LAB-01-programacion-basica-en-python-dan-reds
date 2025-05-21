"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    registros = {}  # Inicializa un diccionario para contar registros por letra
    with open("./files/input/data.csv", "r") as file:
        for line in file:
            columnas = line.strip().split("\t")  # Separa la línea en columnas
            letra = columnas[0]  # Toma la primera columna como letra
            if letra in registros:
                registros[letra] += 1  # Incrementa el contador si la letra ya existe
            else:
                registros[letra] = 1  # Inicializa el contador si es una nueva letra
    registros_ordenados = sorted(registros.items())
    return registros_ordenados  # Retorna la lista de tuplas ordenadas alfabéticamente

print(pregunta_02())
    

