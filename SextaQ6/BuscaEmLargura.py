from collections import deque

def bfs(grafo, inicio):
    n = len(grafo)
    visitado = [False] * n
    fila = deque([inicio])
    visitado[inicio] = True
                                         
    while fila:                      #Complexidade:  O(n²)

        u = fila.popleft()
        for v in range(n):
            if grafo[u][v] == 1 and not visitado[v]:
                visitado[v] = True
                fila.append(v)

    return visitado
