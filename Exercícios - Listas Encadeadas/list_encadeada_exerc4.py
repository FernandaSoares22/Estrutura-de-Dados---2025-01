# 4. Implemente uma função que receba como parâmetro uma lista encadeada e inverta o encadeamento 
# de seus nós, retornando a lista resultante. Após a execução desta função, cada nó da lista vai 
# estar referenciando (prox) o nó que originalmente era seu antecessor, e o último nó da lista 
# passará a ser o primeiro nó da lista invertida, conforme ilustrado a seguir: 

# 2.1 -> 4.5 -> 1.0 -> 7.2 -> 9.8
# Inverte
# 9.8 -> 7.2 -> 1.0 -> 4.5 -> 2.1

# Esta função deve obedecer ao protótipo: def inverte(lst): 

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

# Função que inverte a lista
def inverte(lst):
    anterior = None
    atual = lst
    while atual is not None:
        # Salva o próximo nó
        proximo = atual.prox
        # Inverte o ponteiro do nó atual
        atual.prox = anterior
        # Move os ponteiros para o próximo nó
        anterior = atual
        atual = proximo
    # O anterior agora é o novo primeiro nó da lista
    return anterior

l = Lista(2.1)
l = lista_insert(l, 4.5)
l = lista_insert(l, 1.0)
l = lista_insert(l, 7.2)
l = lista_insert(l, 9.8)

print("Lista Original:")
lista_imprime(l)

l_invertida = inverte(l)

print("Lista Invertida:")
lista_imprime(l_invertida)