#CRUD
# Crear una tupla
mi_tupla = (1, 2, 3, "Hola", True)

# Acceder a elementos de la tupla
print(mi_tupla[0])  # Salida: 1
print(mi_tupla[3])  # Salida: Hola

# Intentar modificar un elemento (esto dará un error)
#mi_tupla[0] = 5  # Esto generará un error porque las tuplas son inmutables

# Iterar sobre una tupla
for elemento in mi_tupla:
    print((elemento))

# Obtener la longitud de una tupla
print(len(mi_tupla))  # Salida: 5
