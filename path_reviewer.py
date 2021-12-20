import os

"""
Ordene los nombres de archivo en un directorio y modifique el nombre de cada archivo al número de índice
"""

# Obtener la ruta del directorio
path = input("Introduzca la ruta del directorio: /n")

# Determina si la ruta existe
if os.path.exists(path):
    file_list = os.listdir(path)
    # Recorre la lista
    for index, item in enumerate(file_list):
        suffix = item.split('.')[-1]
        old_name = path + '\\' + item
        new_name = path + '\\' + str(index) + '.' + suffix
        os.rename(old_name, new_name)
else:
    print("¡¡¡El camino no existe !!!")
