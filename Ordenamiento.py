matriz2 = [
    [9, 3, 5, 1],
    [4, 8, 2, 7],
    [6, 0, 11, 10],
    [15, 12, 13, 14]
]

# Función para ordenar una fila específica usando Bubble Sort
def ordenar_fila(matriz2, fila):
    n = len(matriz2[fila])
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if matriz2[fila][j] > matriz2[fila][j + 1]:
                # Intercambiar elementos si están en el orden incorrecto
                matriz2[fila][j], matriz2[fila][j + 1] = matriz2[fila][j + 1], matriz2[fila][j]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz2:
    print(fila)

# Ordenar una fila específica (por ejemplo, la fila 1)
fila_a_ordenar = 1  # Puedes cambiar este valor para ordenar otra fila
ordenar_fila(matriz2, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz2:
    print(fila)