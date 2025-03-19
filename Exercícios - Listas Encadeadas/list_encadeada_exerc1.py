# 1. Considere listas de valores inteiros e implemente uma 
# função que receba como parâmetros uma lista encadeada e 
# um valor inteiro n, retire da lista todas as ocorrências 
# de n e retorne a lista resultante. Esta função deve 
# obedecer ao protótipo: 
# def retira_n(lst, n):


# Classe para representar um nó da lista (isso se repete em todos os exercício)
class Lista:
    def __init__(self, value):
        self.info = value  # Guarda o valor do nó
        self.prox = None  # Aponta para o próximo nó, inicialmente é None

def lista_insert(primeiro_elemento, valor):
    novo_elemento = Lista(valor)  # Cria um novo nó com o valor passado
    novo_elemento.prox = primeiro_elemento  # O novo nó aponta para o nó atual
    return novo_elemento  # Retorna o novo nó como primeiro da lista

def lista_imprime(lista):
    atual = lista
    while atual is not None:  # Enquanto houver elementos na lista
        print(atual.info)  # Imprime o valor do nó
        atual = atual.prox  # Passa para o próximo nó

def retira_n(lst, n):
    atual = lst  # Começa a busca pela cabeça da lista
    anterior = None  # Não há elemento anterior no início

    while atual is not None:  # Enquanto a lista não terminar
        if atual.info == n:  # Se o valor atual for igual a n
            if anterior is None:  # Caso o valor a ser removido seja o primeiro nó
                lst = atual.prox  # Atualiza a cabeça da lista para o próximo nó
            else:
                anterior.prox = atual.prox  # O anterior agora aponta para o próximo do atual
        else:
            anterior = atual  # Atualiza o anterior para o nó atual
        atual = atual.prox  # Avança para o próximo nó
    
    return lst  # Retorna a lista atualizada

# Criando a lista encadeada
lista_encadeada = Lista(12)  # Começamos com o valor 12

lista_encadeada = lista_insert(lista_encadeada, 9)  # Inserir 9
lista_encadeada = lista_insert(lista_encadeada, 7)  # Inserir 7
lista_encadeada = lista_insert(lista_encadeada, 5)  # Inserir 5
lista_encadeada = lista_insert(lista_encadeada, 3)  # Inserir 3

# Imprime a lista original
print("=-=-=-= Lista Original =-=-=-=")
lista_imprime(lista_encadeada)

# Chamando a função para remover o número 7
lista_encadeada = retira_n(lista_encadeada, 7)

# Imprime a lista após remover o número 7
print("=-=-=-= Lista Após Remover 7 =-=-=-=")
lista_imprime(lista_encadeada)

# Chamando a função para remover o número 3
lista_encadeada = retira_n(lista_encadeada, 3)

# Imprime a lista após remover o número 3
print("=-=-=-= Lista Após Remover 3 =-=-=-=")
lista_imprime(lista_encadeada)
