
#b)um vetor desordenado

def calcular_intervalo_vetor_desordenado(vetor_desordenado):
    
    if len(vetor_desordenado) < 2:
        return 0
    
    menor = vetor_desordenado[0]
    maior = vetor_desordenado[0]                                                                       
   
    for i in range(1, len(vetor_desordenado)):
       
        if vetor_desordenado[i] < menor:                                  #complexidade: O(n)
            menor = vetor_desordenado[i]
        
        if vetor_desordenado[i] > maior:
            maior = vetor_desordenado[i]
            
    return maior - menor


vetor_s_desordenado = [15, 8, 40, 3, 31, 22]
intervalo = calcular_intervalo_vetor_desordenado(vetor_s_desordenado)
print(f"Vetor: {vetor_s_desordenado}")
print(f"Intervalo: {intervalo}") 