

#a) um vetor ordenado

def calcular_intervalo_vetor_ordenado(vetor_ordenado):
    
    # Verifica se o vetor tem elementos suficientes para ter um intervalo.
    
    if len(vetor_ordenado) < 2:
        return 0

    # O menor elemento é o primeiro do vetor ordenado
    menor = vetor_ordenado[0]
                                                                             #Complexidade: O(1)
    # O maior elemento é o último do vetor ordenado
    maior = vetor_ordenado[-1]
    
    return maior - menor


vetor_s_ordenado = [3, 8, 15, 22, 31, 40]
intervalo = calcular_intervalo_vetor_ordenado(vetor_s_ordenado)
print(f"Vetor: {vetor_s_ordenado}")
print(f"Intervalo: {intervalo}")  