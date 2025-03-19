# Implemente uma função que construa uma nova lista com a 
# intercalação dos nós de outras duas listas passadas como 
# parâmetros. Esta função deve retornar a lista resultante, 
# conforme ilustrado a seguir: 

# l1                      |    l2
# 2.1 -> 4.5 -> 1.0       |    7.2 -> 3.1 -> 9.8
#                 merge(l1, l2)
#     2.1 -> 7.2 -> 4.5 -> 3.1 -> 1.0 -> 9.8

# Esta função deve obedecer ao protótipo: def merge(l1, l2):

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

# Função que intercala duas listas
def merge(l1, l2):
    # Criar um nó inicial para a lista resultante
    mesclada = None
    # Ponteiro para adicionar os elementos à nova lista
    atual = None

    # Enquanto houver nós nas duas listas
    while l1 is not None and l2 is not None:
        # Adiciona o nó de l1
        if mesclada is None:
            mesclada = l1  # O primeiro nó de l1 será o início da nova lista
            atual = mesclada  # O ponteiro para a nova lista é o início de l1
        else:
            atual.prox = l1
            atual = atual.prox  # Avança o ponteiro

        # Avançar em l1
        l1 = l1.prox

        # Adiciona o nó de l2
        if l1 is not None or l2 is not None:
            atual.prox = l2
            atual = atual.prox  # Avança o ponteiro

        # Avança em l2
        l2 = l2.prox

    # Adiciona o restante de l1 ou l2 se houver algum
    if l1 is not None:
        atual.prox = l1
    elif l2 is not None:
        atual.prox = l2

    return mesclada


l1 = Lista(1.0)
l1 = lista_insert(l1, 4.5)
l1 = lista_insert(l1, 2.1)

print("=-=-=-= Lista l1 =-=-=-=")
lista_imprime(l1)

l2 = Lista(9.8)
l2 = lista_insert(l2, 3.1)
l2 = lista_insert(l2, 7.2)

print("=-=-=-= Lista l2 =-=-=-=")
lista_imprime(l2)

lista_resultante = merge(l1, l2)

print("=-=-=-= Lista Resultante =-=-=-=")
lista_imprime(lista_resultante)