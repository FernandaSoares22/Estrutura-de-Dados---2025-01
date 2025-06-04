# 1. Para a árvore a seguir:

# Implemente as funções de percurso pré-ordem, pós-ordem e ordem simétrica. Exiba o resultado esperado
# ao executar cada uma das funções. Ordem de inserção: [5, 6, 7, 4, 2, 1, 3, 9, 8, 10]

class No:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (
            self.esquerda and self.esquerda.chave,
            self.chave,
            self.direita and self.direita.chave
        )

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

def inserir(root, key):
    if root is None:
        return No(key)
    if key < root.chave:
        root.esquerda = inserir(root.esquerda, key)
    else:
        root.direita = inserir(root.direita, key)
    return root

def remover(root, key):
    # O número não existe ou árvore vazia
    if root is None:
        return None
    
    if key < root.chave:
        root.esquerda = remover(root.esquerda, key)
    else:
        root.direita = remover(root.direita, key)
        
    # Toda lógica de remoção
    if root.chave == key:
        if root.esquerda is None and root.direita is None:
            print("O valor a ser removido é uma folha")
            root = None
        elif root.esquerda is None:
            root = root.direita
        elif root.direita is None:
            root = root.esquerda
        else:
            aux = root.esquerda
            
            # Chega ao final da direita
            while aux.direita is not None:
                aux = aux.direita
            
            aux.chave, root.chave = root.chave, aux.chave
            
            root.esquerda = remover(root.esquerda, key)
    
    return root

def buscar(root, key):
    if root is None:
        return None  

    if key == root.chave:
        return root 

    if key < root.chave:
        return buscar(root.esquerda, key)
    else:
        return buscar(root.direita, key)



def pre_ordem(no):
    if no:
        print(no.chave, end=' ')
        pre_ordem(no.esquerda)
        pre_ordem(no.direita)

def em_ordem(no):
    if no:
        em_ordem(no.esquerda)
        print(no.chave, end=' ')
        em_ordem(no.direita)

def pos_ordem(no):
    if no:
        pos_ordem(no.esquerda)
        pos_ordem(no.direita)
        print(no.chave, end=' ')



arvore = ArvoreBinaria()
 [5, 6, 7, 4, 2, 1, 3, 9, 8, 10]

arvore.raiz = No(5)
inserir(arvore.raiz, 6)
inserir(arvore.raiz,7)
inserir(arvore.raiz, 4)
inserir(arvore.raiz, 2)
inserir(arvore.raiz, 1)
inserir(arvore.raiz, 3)
inserir(arvore.raiz, 9)
inserir(arvore.raiz, 8)
inserir(arvore.raiz, 10)

print("Árvore antes da remoção (em ordem):")
em_ordem(arvore.raiz)
print("\n")

remover(arvore.raiz, 6)

print("Árvore após a remoção de 6:")

print("Pré-ordem:")
pre_ordem(arvore.raiz)
print("\nEm ordem:")
em_ordem(arvore.raiz)
print("\nPós-ordem:")
pos_ordem(arvore.raiz)
print("\nValor Encontrado:", buscar(arvore.raiz,2))
print()
