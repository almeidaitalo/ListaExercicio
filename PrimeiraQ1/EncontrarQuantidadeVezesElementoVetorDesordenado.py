
# e) Encontrar a quantidade de vezes que um elemento ocorre em um vetor
# desordenado, adaptando o algoritmo de busca sequencial


def contar_ocorrencias(vetor, elemento_buscado):
    contador = 0
    for elemento in vetor:
        if elemento == elemento_buscado:                   #Complexidade: O(n)
            contador += 1
    return contador


vetor_desordenado = [5, 2, 8, 2, 9, 1, 2, 5]
elemento = 2
print(f"O elemento {elemento} ocorre {contar_ocorrencias(vetor_desordenado, elemento)} vezes.")

elemento = 9
print(f"O elemento {elemento} ocorre {contar_ocorrencias(vetor_desordenado, elemento)} vezes.")