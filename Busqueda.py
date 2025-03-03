matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    # Recorrer la matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                # Si se encuentra el valor, devolver su posición
                return f"El valor {valor} se encontró en la posición ({i}, {j})."
    # Si no se encuentra el valor, devolver un mensaje
    return f"El valor {valor} no se encontró en la matriz."

# Valor a buscar
valor_a_buscar = 5

# Llamar a la función y mostrar el resultado
resultado = buscar_valor(matriz, valor_a_buscar)
print(resultado)