

#a) um vetor ordenado

def calcular_intervalo_vetor_ordenado(vetor_ordenado):
    
    # Verifica se o vetor tem elementos suficientes para ter um intervalo.
    # Conforme a definição, o conjunto é não vazio. Se tiver só 1 elemento, o intervalo é 0.
    if len(vetor_ordenado) < 2:
        return 0

   
    menor = vetor_ordenado[0]
    
   
    maior = vetor_ordenado[-1]
    
    return maior - menor


vetor_s_ordenado = [3, 8, 15, 22, 31, 40]
intervalo = calcular_intervalo_vetor_ordenado(vetor_s_ordenado)
print(f"Vetor: {vetor_s_ordenado}")
print(f"Intervalo: {intervalo}")  