# Crear un set
mi_set = {1, 2, 3, 4, 5}

# Agregar un elemento al set
mi_set.add(6)
print(mi_set)  # Salida: {1, 2, 3, 4, 5, 6}

# Intentar agregar un elemento existente (esto no tiene efecto en el set)
mi_set.add(3)
print(mi_set)  # Salida: {1, 2, 3, 4, 5, 6}

# Remover un elemento del set
mi_set.remove(2)
print(mi_set)  # Salida: {1, 3, 4, 5, 6}

# Verificar la pertenencia de un elemento en el set
print(3 in mi_set)  # Salida: True
print(7 in mi_set)  # Salida: False

# Iterar sobre un set
for elemento in mi_set:
    print(elemento)
