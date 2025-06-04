# 2. Em uma arena circular, cavaleiros se enfrentam em uma batalha épica. Cada cavaleiro é representado por um nó na lista simplesmente encadeada circular.

# Regras do Jogo
# - Cada cavaleiro começa com uma quantidade de HP (vida) gerada aleatoriamente entre 50 e 100.
# - Cada cavaleiro ataca o próximo jogador da lista, causando uma quantidade de dano gerada aleatoriamente entre 5 e 10.
# - Quando o HP de um cavaleiro chega a zero ou menos, ele é eliminado da lista.
# - O jogo termina quando restar apenas um cavaleiro na arena, que será declarado o campeão.

import random

class Node:
    def __init__(self, nome):
        self.nome = nome
        self.hp = random.randint(50, 100)
        self.proximo = None

class ListaCircular:
    def __init__(self):
        self.inicio = None

    def inserir(self, nome):
        novo = Node(nome)
        if not self.inicio:
            self.inicio = novo
            novo.proximo = novo
        else:
            atual = self.inicio
            while atual.proximo != self.inicio:
                atual = atual.proximo
            atual.proximo = novo
            novo.proximo = self.inicio

    def remover(self, nome):
        if not self.inicio:
            return False

        atual = self.inicio
        anterior = None

        while True:
            if atual.nome == nome:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
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

    def mostrar_hp(self):
        if not self.inicio:
            return
        atual = self.inicio
        print("HP dos Cavaleiros:")
        while True:
            print(f"- {atual.nome}: {atual.hp} HP")
            atual = atual.proximo
            if atual == self.inicio:
                break

def batalha_cavaleiros(nomes):
    arena = ListaCircular()
    for nome in nomes:
        arena.inserir(nome)

    atual = arena.inicio

    print("🏰 Início da Batalha dos Cavaleiros 🗡️")
    arena.mostrar_hp()

    while arena.contar() > 1:
        atacante = atual
        defensor = atual.proximo
        dano = random.randint(5, 10)
        defensor.hp -= dano
        print(f"\n⚔️ {atacante.nome} ataca {defensor.nome} causando {dano} de dano!")

        if defensor.hp <= 0:
            print(f"💀 {defensor.nome} foi eliminado!")
            arena.remover(defensor.nome)
            if defensor == arena.inicio:
                atual = arena.inicio
            else:
                atual = atacante
        else:
            atual = atual.proximo

    print(f"\n🏆 O grande campeão é {arena.inicio.nome} com {arena.inicio.hp} de HP!")

# Exemplo de uso
nomes_cavaleiros = ["Arthur", "Lancelot", "Gawain", "Percival", "Galahad"]
batalha_cavaleiros(nomes_cavaleiros)
