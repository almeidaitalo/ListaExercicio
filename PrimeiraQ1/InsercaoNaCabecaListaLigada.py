
# a)Inserção na cabeça de uma lista ligada

class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.cabeca = None

    def inserir_na_cabeca(self, dado):
        novo_no = No(dado)                        #Complexidade: O(1)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def imprimir_lista(self):
        atual = self.cabeca
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("None")


lista = ListaLigada()
lista.inserir_na_cabeca(10)
lista.inserir_na_cabeca(20)
lista.inserir_na_cabeca(30)
lista.imprimir_lista()