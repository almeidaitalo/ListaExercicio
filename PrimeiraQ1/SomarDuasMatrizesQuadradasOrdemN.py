#c)Somar duas matrizes quadradas de ordem n

def somar_matrizes(matriz1, matriz2):
    n = len(matriz1)
    matriz_soma = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            matriz_soma[i][j] = matriz1[i][j] + matriz2[i][j]

    return matriz_soma

matriz_a = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]                        #Complexidade: O(n^2)

matriz_b = [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]

resultado = somar_matrizes(matriz_a, matriz_b)


for linha in resultado:
    print(linha)