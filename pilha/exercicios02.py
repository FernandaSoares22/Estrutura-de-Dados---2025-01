# 2. Crie uma função esvaziar_pilha(p) que desempilha todos os elementos até que a pilha esteja vazia. Ao final, imprima “Pilha esvaziada”.

class Pilha:
    def __init__(self, capacidade):
        self.itens = []
        self.capacidade = capacidade

    def empilhar(self, item):
        if len(self.itens) < self.capacidade:
            self.itens.append(item)
        else:
            print("Pilha cheia!")

    def desempilhar(self):
        if not vazia(self):
            return self.itens.pop()
        else:
            print("Pilha vazia!")

def vazia(pilha):
    return len(pilha.itens) == 0

def esvaziar_pilha(p):
    while not vazia(p):
        p.desempilhar()
    print("Pilha esvaziada")

# Testando a função
p = Pilha(10)
p.empilhar(1)
p.empilhar(2)
p.empilhar(3)

esvaziar_pilha(p)
