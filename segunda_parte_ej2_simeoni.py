# Definir el conjunto A
A = {1, 2, 3}

# Definir la relación binaria sobre A como un conjunto de pares ordenados
relacion = {(1, 1), (1, 2), (2, 1), (2, 2), (3, 3)}

# Verificar si la relación es reflexiva
reflexiva = True
for elemento in A:
    if (elemento, elemento) not in relacion:
        reflexiva = False
        break
if reflexiva:
    print("La relación es reflexiva.")
else:
    print("La relación no es reflexiva.")

# Verificar si la relación es simétrica
simetrica = True
for par in relacion:
    if (par[1], par[0]) not in relacion:
        simetrica = False
        break
if simetrica:
    print("La relación es simétrica.")
else:
    print("La relación no es simétrica.")

