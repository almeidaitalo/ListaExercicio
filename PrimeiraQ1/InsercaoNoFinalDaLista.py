
#b) Inserção no final de uma lista ligada, sem apontador de final de lista;


class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.cabeca = None

    def inserir_no_final(self, dado):
        novo_no = No(dado)
        if not self.cabeca:
            self.cabeca = novo_no
            return                          #Complexidade: O(n)

        ultimo = self.cabeca
        while ultimo.proximo:
            ultimo = ultimo.proximo
        ultimo.proximo = novo_no

    def imprimir_lista(self):
        atual = self.cabeca
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("None")


lista = ListaLigada()
lista.inserir_no_final(10)
lista.inserir_no_final(20)
lista.inserir_no_final(30)
lista.imprimir_lista()