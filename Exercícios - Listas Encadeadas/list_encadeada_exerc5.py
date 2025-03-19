# 5. Considere listas que armazenam cadeias de caracteres e implemente uma função para testar se duas listas 
# passadas como parâmetros são iguais. Essa função deve obedecer ao protótipo: def igual(l1, l2): 

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

# Função para testar se duas listas são iguais
def igual(l1, l2):
    # Enquanto ambas as listas não forem vazias
    while l1 is not None and l2 is not None:
        # Se os valores dos nós forem diferentes, as listas não são iguais
        if l1.info != l2.info:
            return False
        # Avançamos para o próximo nó em ambas as listas
        l1 = l1.prox
        l2 = l2.prox
    
    # Se as duas listas chegaram ao final ao mesmo tempo, elas são iguais
    # Caso contrário, uma lista é mais longa que a outra
    if l1 is None and l2 is None:
        return True
    return False


l1 = Lista("A")
l1 = lista_insert(l1, "B")
l1 = lista_insert(l1, "C")

l2 = Lista("A")
l2 = lista_insert(l2, "B")
l2 = lista_insert(l2, "C")

l3 = Lista("A")
l3 = lista_insert(l3, "B")
l3 = lista_insert(l3, "D")

print("l1 e l2 são iguais?", igual(l1, l2)) 
print("l1 e l3 são iguais?", igual(l1, l3))  
print("l2 e l3 são iguais?", igual(l2, l3)) 
