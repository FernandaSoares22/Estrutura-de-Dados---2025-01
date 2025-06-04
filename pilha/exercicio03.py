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

p = Pilha(10)

# Solicitando os números ao usuário
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    p.empilhar(numero)

# Desempilhando os números na ordem inversa
print("Números na ordem inversa:")
while not vazia(p):
    print(p.desempilhar())
