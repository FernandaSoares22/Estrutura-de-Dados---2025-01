# 1. Crie uma pilha com capacidade 10 e empilhe os números de 1 a 5. Depois, desempilhe todos os elementos mostrando na tela um por um.
    
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
    
    # Usando a pilha
    p = Pilha(10)
    p.empilhar(1)
    p.empilhar(2)
    p.empilhar(3)
    p.empilhar(4)
    p.empilhar(5)
    p.empilhar(6)
    
    print("Desempilhando elementos:")
    while not vazia(p):
        print(p.desempilhar())
