# 6. Considere listas que armazenam cadeias de caracteres e implemente uma função para criar 
# uma cópia de uma lista encadeada. Essa função deve obedecer ao protótipo: def copia(lst):

class Lista:
    def __init__(self, value):
        self.info = value
        self.prox = None

def lista_insert(primeiro_elemento, valor):
    novo_elemento = Lista(valor)
    novo_elemento.prox = primeiro_elemento
    return novo_elemento

def lista_imprime(lista):
    atual = lista
    while atual is not None:
        print(atual.info, end=" -> ")
        atual = atual.prox
    print("None")

# Função para criar uma cópia da lista
def copia(lst):
    if lst is None:
        return None  # Se a lista estiver vazia, retornamos None
    
    # Criando o primeiro nó da cópia
    copia_lista = Lista(lst.info)
    atual_original = lst.prox
    atual_copia = copia_lista

    # Percorrendo a lista original e copiando os nós
    while atual_original is not None:
        novo_nó = Lista(atual_original.info)  # Criando novo nó
        atual_copia.prox = novo_nó  # Ligando o novo nó à cópia
        atual_copia = novo_nó  # Avançando para o próximo nó na cópia
        atual_original = atual_original.prox  # Avançando na lista original
    
    return copia_lista  # Retornando a cabeça da lista copiada

l1 = Lista("C")
l1 = lista_insert(l1, "B")
l1 = lista_insert(l1, "A")

l2 = copia(l1)

print("Lista original:")
lista_imprime(l1)  

print("Lista copiada:")
lista_imprime(l2)