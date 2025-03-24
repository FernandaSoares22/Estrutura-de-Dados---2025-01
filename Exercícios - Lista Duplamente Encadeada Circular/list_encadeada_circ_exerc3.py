# 3. Implemente uma função que remove um elemento específico da lista encadeada circular.

class Lista:
    def __init__(self, info):
        self.info = info
        self.prox = None

def remover_elemento(lista, valor):
    if lista is None:
        return None

    atual = lista
    anterior = None

    if lista.prox == lista and lista.info == valor:
        return None

    while True:
        if atual.info == valor:
            if atual == lista:
                ultimo_elemento = lista
                while ultimo_elemento.prox != lista:
                    ultimo_elemento = ultimo_elemento.prox

                ultimo_elemento.prox = lista.prox
                lista = lista.prox
            else:
                anterior.prox = atual.prox
            return lista

        anterior = atual
        atual = atual.prox

        if atual == lista:
            break

    print("Elemento não encontrado!")
    return lista

def show_elements(lista):
    if lista is None:
        print("Lista vazia!")
        return

    atual = lista
    while True:
        print(atual.info)
        atual = atual.prox
        if atual == lista:
            break

lista = Lista(9)
lista.prox = Lista(7)
lista.prox.prox = Lista(5)
lista.prox.prox.prox = lista

print("Antes da remoção:")
show_elements(lista)

lista = remover_elemento(lista, 7)

print("Após a remoção:")
show_elements(lista)

