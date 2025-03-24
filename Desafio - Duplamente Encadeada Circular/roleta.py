import random

class Guerreiro:
    def __init__(self, nome):
        self.nome = nome
        self.ant = None
        self.prox = None

class RoletaRussaCircular:
    def __init__(self):
        self.inicio = None
    
    def inserir_guerreiro(self, nome):
        novo = Guerreiro(nome)
        
        if self.inicio is None:
            novo.prox = novo
            novo.ant = novo
            self.inicio = novo
        else:
            ultimo = self.inicio.ant
            ultimo.prox = novo
            novo.ant = ultimo
            novo.prox = self.inicio
            self.inicio.ant = novo
    
    def exibir_guerreiros(self):
        if self.inicio is None:
            print("Nenhum guerreiro na lista.")
            return
        
        atual = self.inicio
        guerreiros = []
        while True:
            guerreiros.append(atual.nome)
            atual = atual.prox
            if atual == self.inicio:
                break
        print(" -> ".join(guerreiros) + " -> (volta ao início)")
    
    def remover_guerreiro(self, guerreiro):
        if guerreiro.prox == guerreiro:
            self.inicio = None
            return None
        
        guerreiro.ant.prox = guerreiro.prox
        guerreiro.prox.ant = guerreiro.ant
        
        if guerreiro == self.inicio:
            self.inicio = guerreiro.prox
        
        return self.inicio
    
    def iniciar_jogo(self):
        if self.inicio is None:
            print("Nenhum guerreiro para batalhar.")
            return
        
        print("\n🔥 Início da Roleta Russa Circular 🔥")
        self.exibir_guerreiros()

        atual = self.inicio
        while atual.prox != atual:
            print("\n⚔️ Guerreiros restantes:")
            self.exibir_guerreiros()

            passos = random.randint(1, 5)
            print(f"\n🎲 O revólver girou... Contando {passos} guerreiros!")

            for _ in range(passos):
                atual = atual.prox
            
            eliminado = atual
            print(f"💀 {eliminado.nome} foi eliminado!")
            atual = eliminado.prox 
            self.remover_guerreiro(eliminado)

        print("\n⚔️ Último guerreiro restante:")
        self.exibir_guerreiros()
        print(f"\n🏆 {atual.nome} é o grande vencedor!")

jogo = RoletaRussaCircular()

nomes = ["Cara 1", "Cara 2", "Cara 3", "Cara 4", "Cara 5"]
for nome in nomes:
    jogo.inserir_guerreiro(nome)

jogo.iniciar_jogo()

