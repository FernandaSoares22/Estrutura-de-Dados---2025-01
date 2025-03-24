# 2. Implemente uma função que busca um valor específico na lista encadeada circular e retorne True se encontrado ou False caso contrário.

class Lista:
    def __init__(self, info):
        self.info = info
        self.prox = None

def buscar_elemento(lista, valor):
    if lista is None:
        return False

    atual = lista
    while True:
        if atual.info == valor:
            return True
        atual = atual.prox
        if atual == lista:
            break

    return False

lista = Lista(9)
lista.prox = Lista(7)
lista.prox.prox = Lista(5)
lista.prox.prox.prox = lista 

print(buscar_elemento(lista, 7))  
print(buscar_elemento(lista, 3)) 
