import math

class MinHeap:
    def __init__(self):
        self.heap = []

    def _obter_indice_pai(self, indice_filho: int) -> int:
        if indice_filho > 0:
            return (indice_filho - 1) // 2
        else:
            return -1

    def _obter_indice_filho_esquerdo(self, indice_pai: int) -> int:
        return 2 * indice_pai + 1

    def _obter_indice_filho_direito(self, indice_pai: int) -> int:
        return 2 * indice_pai + 2

    def _tem_pai(self, indice: int) -> bool:
        return self._obter_indice_pai(indice) != -1

    def _tem_filho_esquerdo(self, indice: int) -> bool:
        return self._obter_indice_filho_esquerdo(indice) < len(self.heap)

    def _tem_filho_direito(self, indice: int) -> bool:
        return self._obter_indice_filho_direito(indice) < len(self.heap)

    def _trocar(self, indice1: int, indice2: int) -> None:
        self.heap[indice1], self.heap[indice2] = self.heap[indice2], self.heap[indice1]

    def _reorganizar_para_cima(self, indice_atual: int) -> None:
        while self._tem_pai(indice_atual) and self.heap[self._obter_indice_pai(indice_atual)] > self.heap[indice_atual]:
            self._trocar(self._obter_indice_pai(indice_atual), indice_atual)
            indice_atual = self._obter_indice_pai(indice_atual)

    def _reorganizar_para_baixo(self, indice_atual: int) -> None:
        while self._tem_filho_esquerdo(indice_atual):
            indice_filho_menor = self._obter_indice_filho_esquerdo(indice_atual)
            
            if self._tem_filho_direito(indice_atual):
                if self.heap[self._obter_indice_filho_direito(indice_atual)] < self.heap[indice_filho_menor]:
                    indice_filho_menor = self._obter_indice_filho_direito(indice_atual)

            if self.heap[indice_atual] < self.heap[indice_filho_menor]:
                break
            else:
                self._trocar(indice_atual, indice_filho_menor)
            indice_atual = indice_filho_menor

    def inserir(self, elemento: any) -> None:
        self.heap.append(elemento)
        self._reorganizar_para_cima(len(self.heap) - 1)

    def extrair_minimo(self) -> any:
        if not self.heap:
            raise IndexError("Heap está vazio. Não é possível extrair elemento.")
        
        if len(self.heap) == 1:
            return self.heap.pop()

        elemento_minimo = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._reorganizar_para_baixo(0)
        return elemento_minimo

    def consultar_minimo(self) -> any:
        if not self.heap:
            raise IndexError("Heap está vazio. Não há elemento para consultar.")
        return self.heap[0]

    def esta_vazio(self) -> bool:
        return len(self.heap) == 0

    def obter_tamanho(self) -> int:
        return len(self.heap)

    def imprimir_estrutura_heap(self) -> None:
        if not self.heap:
            print("Heap está vazio e não possui estrutura para imprimir.")
            return

        print("\n--- Estrutura do Heap (Representação Simples) ---")
        for indice in range(len(self.heap)):
            valor_no = self.heap[indice]
            
            valor_filho_esquerdo = "N/D"
            if self._tem_filho_esquerdo(indice):
                valor_filho_esquerdo = self.heap[self._obter_indice_filho_esquerdo(indice)]

            valor_filho_direito = "N/D"
            if self._tem_filho_direito(indice):
                valor_filho_direito = self.heap[self._obter_indice_filho_direito(indice)]
            
            print(f"Nó[{indice}]: {valor_no} (Filho Esquerdo: {valor_filho_esquerdo}, Filho Direito: {valor_filho_direito})")
        print("--------------------------------------------------")

if __name__ == "__main__":
    print("Iniciando demonstração do Heap de Mínimos...")
    min_heap_instancia = MinHeap()
    elementos_para_inserir = [10, 4, 15, 1, 9, 20, 5, 2]

    print("\n--- Operações de Inserção de Elementos ---")
    for elemento in elementos_para_inserir:
        print(f"Inserindo: {elemento}")
        min_heap_instancia.inserir(elemento)
        print(f"Estado interno do heap (lista): {min_heap_instancia.heap}")
        min_heap_instancia.imprimir_estrutura_heap()
        print("-" * 50)

    print("\n--- Consulta ao Elemento Mínimo (Raiz) ---")
    try:
        print(f"Elemento mínimo atual (raiz): {min_heap_instancia.consultar_minimo()}")
    except IndexError as e:
        print(e)
    print("-" * 50)

    print("\n--- Operações de Remoção do Elemento Mínimo ---")
    while not min_heap_instancia.esta_vazio():
        try:
            elemento_extraido = min_heap_instancia.extrair_minimo()
            print(f"Elemento removido (mínimo): {elemento_extraido}")
            print(f"Estado interno do heap (lista): {min_heap_instancia.heap}")
            if not min_heap_instancia.esta_vazio():
                min_heap_instancia.imprimir_estrutura_heap()
            else:
                print("Heap está agora vazio após remoção.")
            print("-" * 50)
        except IndexError as e:
            print(e)

    print("\n--- Demonstração de Casos Limite (Heap Vazio) ---")
    heap_vazio = MinHeap()
    print("Tentando operações em um heap recém-criado (vazio):")
    try:
        print(f"Tentando consultar em heap vazio: {heap_vazio.consultar_minimo()}")
    except IndexError as e:
        print(f"Erro ao consultar: {e}")
    try:
        print(f"Tentando remover em heap vazio: {heap_vazio.extrair_minimo()}")
    except IndexError as e:
        print(f"Erro ao remover: {e}")

    print("\nDemonstração do Heap de Mínimos Concluída.")
