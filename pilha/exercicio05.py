# 5. Crie um método para remover um item do meio de uma pilha. Ele deve manter a ordem original apenas removendo o item especificado.

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

def remover_item(pilha, item_remover):
    pilha_aux = Pilha(pilha.capacidade)
    
    # Desempilha todos os elementos, exceto o que queremos remover,
    # e coloca na pilha auxiliar para guardar a ordem invertida.
    while not vazia(pilha):
        topo = desempilhar(pilha)
        if topo != item_remover:
            empilhar(pilha_aux, topo)
        # se for o item_remover, não empilha na pilha_aux (remove)
    
    # Agora, desempilha da pilha auxiliar de volta para a pilha original,
    # para restaurar a ordem original (menos o item removido)
    while not vazia(pilha_aux):
        empilhar(pilha, desempilhar(pilha_aux))


# Exemplo de uso

p = Pilha(10)

empilhar(p, 1)
empilhar(p, 2)
empilhar(p, 3)
empilhar(p, 4)
empilhar(p, 5)

print("Pilha antes de remover o 3:")
i = 0
while i < len(p.itens):
    print(p.itens[i], end=" ")
    i += 1
print()

remover_item(p, 3)

print("Pilha depois de remover o 3:")
i = 0
while i < len(p.itens):
    print(p.itens[i], end=" ")
    i += 1
print()
