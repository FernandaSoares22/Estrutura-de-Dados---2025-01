class Lista:
    def __init__(self, info):
        self.info = info
        self.prox = None

def insert_node_fim(lista, info):
    novo_elemento = Lista(info)

    if lista is None:
        novo_elemento.prox = novo_elemento  
        return novo_elemento

    atual = lista
    while atual.prox != lista:
        atual = atual.prox

    atual.prox = novo_elemento
    novo_elemento.prox = lista

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

lista = None
lista = insert_node_fim(lista, 9)
lista = insert_node_fim(lista, 7)
lista = insert_node_fim(lista, 5)
lista = insert_node_fim(lista, 3)

print("################ Lista ################")
show_elements(lista)
