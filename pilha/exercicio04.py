class Pilha:
    def __init__(self, capacidade):
        self.itens = []
        self.capacidade = capacidade

def empilhar(pilha, item):
    if len(pilha.itens) < pilha.capacidade:
        pilha.itens.append(item)
    else:
        print("Pilha cheia!")

def desempilhar(pilha):
    if not vazia(pilha):
        return pilha.itens.pop()
    else:
        print("Pilha vazia!")

def vazia(pilha):
    return len(pilha.itens) == 0

# Criando a pilha
p = Pilha(100)


texto = input("Digite o texto (use # para apagar o último caractere): ")

# Processando caractere por caractere
indice = 0
while indice < len(texto):
    letra = texto[indice]
    if letra == "#":
        desempilhar(p)
    else:
        empilhar(p, letra)
    indice = indice + 1

# Mostrando o texto final, um por um
print("Texto final:")
i = 0
while i < len(p.itens):
    print(p.itens[i], end="")  # sem usar join
    i = i + 1
print()  # quebra de linha final
