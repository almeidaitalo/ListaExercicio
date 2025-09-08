def calcular_intervalo_vetor_desordenado(vetor_desordenado):
    """
    Calcula o intervalo de um conjunto de números representado por um vetor desordenado.
    """
    if len(vetor_desordenado) < 2:
        return 0
    
    # Inicializa o menor e o maior com o primeiro elemento do vetor
    menor = vetor_desordenado[0]
    maior = vetor_desordenado[0]
    
    # Percorre o restante do vetor a partir do segundo elemento
    for i in range(1, len(vetor_desordenado)):
        # Atualiza o menor valor se encontrar um elemento menor
        if vetor_desordenado[i] < menor:
            menor = vetor_desordenado[i]
        
        # Atualiza o maior valor se encontrar um elemento maior
        if vetor_desordenado[i] > maior:
            maior = vetor_desordenado[i]
            
    return maior - menor


vetor_s_desordenado = [15, 8, 40, 3, 31, 22]
intervalo = calcular_intervalo_vetor_desordenado(vetor_s_desordenado)
print(f"Vetor: {vetor_s_desordenado}")
print(f"Intervalo: {intervalo}") # Saída: 37 (pois 40 - 3 = 37)