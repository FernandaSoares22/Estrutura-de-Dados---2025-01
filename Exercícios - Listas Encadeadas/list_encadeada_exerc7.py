# 7. Implemente funções para inserir e retirar um elemento de uma lista circular simplesmente 
# encadeada (obtenha informações adicionais sobre listas circulares na bibliografia básica da disciplina).
# inf (info1) -> (info2) -> (info3) retorna

class Lista:
    def __init__(self, value):
        self.info = value
        self.prox = None

def insert_circular(lista, value):
    novo_elemento = Lista(value)
    if not lista:
        novo_elemento.prox = novo_elemento
        return novo_elemento
    atual = lista
    while atual.prox != lista:
        atual = atual.prox
    atual.prox = novo_elemento
    novo_elemento.prox = lista
    return novo_elemento

def print_circular(lista):
    if not lista:
        return
    atual = lista
    while True:
        print(atual.info)
        atual = atual.prox
        if atual == lista:
            break

def search_circular(lista, value):
    if not lista:
        return None
    atual = lista
    while True:
        if atual.info == value:
            return atual
        atual = atual.prox
        if atual == lista:
            break
    return None

def remove_circular(lista, value):
    if not lista:
        return None
    atual = lista
    anterior = None
    while True:
        if atual.info == value:
            if anterior:
                anterior.prox = atual.prox
                if atual == lista:
                    lista = atual.prox
            else:
                if atual.prox == lista:
                    return None
                temp = lista
                while temp.prox != lista:
                    temp = temp.prox
                lista = atual.prox
                temp.prox = lista
            return lista
        anterior = atual
        atual = atual.prox
        if atual == lista:
            break
    return lista

minha_lista = None
minha_lista = insert_circular(minha_lista, 10)
minha_lista = insert_circular(minha_lista, 5)
minha_lista = insert_circular(minha_lista, 20)
print("Lista circular:")
print_circular(minha_lista)

minha_lista = remove_circular(minha_lista, 5)
print("Após remover 5:")
print_circular(minha_lista)
