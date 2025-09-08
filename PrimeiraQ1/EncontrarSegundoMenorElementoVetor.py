#C) Encontrar o segundo menor elemento de um vetor

def encontrar_segundo_menor(vetor):
    if len(vetor) < 2:
        return None  # Não há segundo menor se o vetor tiver menos de 2 elementos

    menor = float('inf')
    segundo_menor = float('inf')

    for numero in vetor:
        if numero < menor:
            segundo_menor = menor
            menor = numero
        elif numero < segundo_menor and numero != menor:
            segundo_menor = numero

    return segundo_menor if segundo_menor != float('inf') else None


vetor1 = [10, 5, 8, 2, 9, 1]
print(f"O segundo menor elemento do vetor {vetor1} é: {encontrar_segundo_menor(vetor1)}")

vetor2 = [5, 1, 3, 2, 4]
print(f"O segundo menor elemento do vetor {vetor2} é: {encontrar_segundo_menor(vetor2)}")