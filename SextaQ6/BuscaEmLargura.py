from collections import deque

def bfs(grafo, inicio):
    n = len(grafo)
    visitado = [False] * n
    fila = deque([inicio])
    visitado[inicio] = True
    ordem = [inicio]                                    
    while fila:                      #Complexidade:  O(n²)

        u = fila.popleft()
        for v in range(n):
            if grafo[u][v] == 1 and not visitado[v]:
                visitado[v] = True
                fila.append(v)
                ordem.append(v)

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
print("BFS:", bfs(grafo, 0))