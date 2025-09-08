def calcular_intervalo_vetor_ordenado(vetor_ordenado):
    """
    Calcula o intervalo de um conjunto de números representado por um vetor ordenado.
    O intervalo é a diferença entre o maior e o menor elemento.
    """
    # Verifica se o vetor tem elementos suficientes para ter um intervalo.
    # Conforme a definição, o conjunto é não vazio. Se tiver só 1 elemento, o intervalo é 0.
    if len(vetor_ordenado) < 2:
        return 0

    # O menor elemento está na primeira posição (índice 0)
    menor = vetor_ordenado[0]
    
    # O maior elemento está na última posição (índice -1 em Python)
    maior = vetor_ordenado[-1]
    
    return maior - menor

# Exemplo de uso:
vetor_s_ordenado = [3, 8, 15, 22, 31, 40]
intervalo = calcular_intervalo_vetor_ordenado(vetor_s_ordenado)
print(f"Vetor: {vetor_s_ordenado}")
print(f"Intervalo: {intervalo}")  # Saída: 37 (pois 40 - 3 = 37)