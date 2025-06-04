# 1. Você deve implementar o clássico jogo da Batata Quente utilizando uma lista simplesmente encadeada circular.

# Regras do Jogo:
# - Cada jogador é um nó na lista circular.
# - Um número aleatório k é gerado a cada rodada.
# - A batata é passada de jogador para jogador até o k-ésimo jogador, que é eliminado.
# - O jogo termina quando restar apenas um jogador (o vencedor).

import random

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaCircular:
    def __init__(self):
        self.inicio = None

    def inserir(self, valor):
        novo = Node(valor)
        if not self.inicio:
            self.inicio = novo
            novo.proximo = novo
        else:
            atual = self.inicio
            while atual.proximo != self.inicio:
                atual = atual.proximo
            atual.proximo = novo
            novo.proximo = self.inicio

    def remover(self, valor):
        if not self.inicio:
            return False

        atual = self.inicio
        anterior = None

        while True:
            if atual.valor == valor:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    # Remover o primeiro nó
                    if atual.proximo == self.inicio:
                        self.inicio = None
                    else:
                        ultimo = self.inicio
                        while ultimo.proximo != self.inicio:
                            ultimo = ultimo.proximo
                        self.inicio = atual.proximo
                        ultimo.proximo = self.inicio
                return True

            anterior = atual
            atual = atual.proximo
            if atual == self.inicio:
                break
        return False

    def contar(self):
        if not self.inicio:
            return 0
        contador = 1
        atual = self.inicio
        while atual.proximo != self.inicio:
            contador += 1
            atual = atual.proximo
        return contador

def batata_quente(nomes):
    lista = ListaCircular()
    for nome in nomes:
        lista.inserir(nome)

    atual = lista.inicio

    while lista.contar() > 1:
        k = random.randint(1, 5)
        print(f"\nNúmero sorteado: {k}")
        for _ in range(k - 1):
            atual = atual.proximo
        print(f"{atual.valor} foi eliminado!")
        lista.remover(atual.valor)
        atual = atual.proximo

    print(f"\n🏆 Vencedor: {lista.inicio.valor}")

# Exemplo de uso
jogadores = ["Ana", "Beto", "Carla", "Diego", "Eduarda"]
batata_quente(jogadores)
