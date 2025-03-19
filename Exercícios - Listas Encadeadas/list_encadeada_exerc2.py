# 2. Considere listas de valores inteiros e implemente uma função 
# que receba como parâmetro uma lista encadeada e um valor inteiro 
# n e divida a lista em duas, de forma a segunda lista começar no 
# primeiro nó logo após a ocorrência de n na lista original. 
# A figura a seguir ilustra esta separação: 

# 3 -> 17 -> 5 -> 12 -> 1 
# 3 -> 17 -> 5
# 12 -> 1

# A função deve retornar a referência para a segunda subdivisão 
# da lista original, enquanto lst deve continuar apontando para o 
# primeiro elemento da primeira subdivisão da lista. 
# Essa função deve obedecer ao protótipo: def separa(lst, n): 

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

# Função que separa a lista a partir do valor n
def separa(lst, n):
    atual = lst  # Começa a busca a partir do primeiro nó
    anterior = None  # Não há elemento anterior no início
    
    # Percorre a lista até encontrar o valor n
    while atual is not None:
        if atual.info == n:  # Quando encontramos o valor n
            if atual.prox is not None:  # Verifica se há um próximo nó
                nova_lista = atual.prox  # Nova lista começa logo após o valor n
                atual.prox = None  # Termina a primeira lista antes do valor n
                return nova_lista  # Retorna a nova lista
        # Avança na lista
        anterior = atual
        atual = atual.prox
    
    return None  # Retorna None se o valor n não for encontrado

lista_encadeada = Lista(1)  
lista_encadeada = lista_insert(lista_encadeada, 12)
lista_encadeada = lista_insert(lista_encadeada, 5)
lista_encadeada = lista_insert(lista_encadeada, 17)
lista_encadeada = lista_insert(lista_encadeada, 3)

print("=-=-=-= Lista Original =-=-=-=")
lista_imprime(lista_encadeada)

segunda_lista = separa(lista_encadeada, 5)

print("=-=-=-= Primeira Lista Após Separação =-=-=-=")
lista_imprime(lista_encadeada)

print("=-=-=-= Segunda Lista Após Separação =-=-=-=")
lista_imprime(segunda_lista)
