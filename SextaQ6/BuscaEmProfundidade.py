def dfs_iterativa(grafo, inicio):
    n = len(grafo)
    visitado = [False] * n
    pilha = [inicio]
    visitado[inicio] = True
    ordem = [inicio]

    while pilha:
        u = pilha[-1]  
        encontrou_vizinho = False      #Complexidade: O(n²)

        for v in range(n):
            if grafo[u][v] == 1 and not visitado[v]:
                visitado[v] = True
                pilha.append(v)
                ordem.append(v)
                encontrou_vizinho = True
                break

        if not encontrou_vizinho:
            pilha.pop()  

    return ordem
   
   # Matriz de adjacência 
grafo = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
]

# Testando os algoritmos
print("DFS Iterativa:", dfs_iterativa(grafo, 0))
