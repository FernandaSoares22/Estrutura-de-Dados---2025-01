class Lista:
    def __init__(self, value):
        self.info = value
        self.ant = None
        self.prox = None

# LISTA DUPLAMENTE ENCADEADA

def insert_list(lista, value):
    novo_elemento = Lista(value)
    novo_elemento.prox = lista
    if lista:
        lista.ant = novo_elemento
    return novo_elemento

def print_lista(lista):
    atual = lista
    while atual:
        print(atual.info)
        atual = atual.prox

def search_list(lista, value):
    atual = lista
    while atual:
        if atual.info == value:
            return atual
        atual = atual.prox
    return None

def remove_list(lista, value):
    atual = lista
    while atual:
        if atual.info == value:
            if atual.ant:
                atual.ant.prox = atual.prox
            if atual.prox:
                atual.prox.ant = atual.ant
            return lista if atual != lista else atual.prox
        atual = atual.prox
    return lista

def insert_end(lista, value):
    if not lista:
        return Lista(value)
    atual = lista
    while atual.prox:
        atual = atual.prox
    novo_elemento = Lista(value)
    atual.prox = novo_elemento
    novo_elemento.ant = atual
    return lista

def insert_sorted(lista, value):
    if not lista or value < lista.info:
        return insert_list(lista, value)
    atual = lista
    while atual.prox and atual.prox.info < value:
        atual = atual.prox
    novo_elemento = Lista(value)
    novo_elemento.prox = atual.prox
    if atual.prox:
        atual.prox.ant = novo_elemento
    novo_elemento.ant = atual
    atual.prox = novo_elemento
    return lista

# LISTA DUPLAMENTE ENCADEADA CIRCULAR

def insert_circular(lista, value):
    novo_elemento = Lista(value)
    if not lista:
        novo_elemento.prox = novo_elemento
        novo_elemento.ant = novo_elemento
        return novo_elemento
    ultimo = lista.ant
    novo_elemento.prox = lista
    novo_elemento.ant = ultimo
    lista.ant = novo_elemento
    ultimo.prox = novo_elemento
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
    while True:
        if atual.info == value:
            if atual.prox == atual:
                return None
            atual.ant.prox = atual.prox
            atual.prox.ant = atual.ant
            return atual.prox if atual == lista else lista
        atual = atual.prox
        if atual == lista:
            break
    return lista

def insert_end_circular(lista, value):
    return insert_circular(lista.prox if lista else None, value)

def insert_sorted_circular(lista, value):
    if not lista or value < lista.info:
        novo_elemento = insert_circular(lista, value)
        return novo_elemento if value < lista.info else lista
    atual = lista
    while atual.prox != lista and atual.prox.info < value:
        atual = atual.prox
    novo_elemento = Lista(value)
    novo_elemento.prox = atual.prox
    novo_elemento.ant = atual
    atual.prox.ant = novo_elemento
    atual.prox = novo_elemento
    return lista

def print_inverse_circular(lista):
    if not lista:
        return
    atual = lista.ant
    while True:
        print(atual.info)
        atual = atual.ant
        if atual == lista.ant:
            break

# Testes
minha_lista = None
minha_lista = insert_list(minha_lista, 10)
minha_lista = insert_list(minha_lista, 5)
minha_lista = insert_list(minha_lista, 20)
print("Lista duplamente encadeada:")
print_lista(minha_lista)

minha_lista = remove_list(minha_lista, 5)
print("Após remover 5:")
print_lista(minha_lista)

minha_lista = insert_end(minha_lista, 30)
print("Após inserir 30 no fim:")
print_lista(minha_lista)

minha_lista = insert_sorted(minha_lista, 15)
print("Após inserção ordenada de 15:")
print_lista(minha_lista)

# Lista Circular
dupla_circular = None
dupla_circular = insert_circular(dupla_circular, 50)
dupla_circular = insert_circular(dupla_circular, 25)
dupla_circular = insert_circular(dupla_circular, 75)
print("\nLista duplamente encadeada circular:")
print_circular(dupla_circular)

dupla_circular = remove_circular(dupla_circular, 25)
print("Após remover 25:")
print_circular(dupla_circular)

print("Impressão inversa:")
print_inverse_circular(dupla_circular)
