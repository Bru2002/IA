from collections import deque
import heapq
import time
import gerar_estados
# Função de heurística (número de elementos fora do lugar) desconsidera o 0
# O 0 é ignorado porque não precisa ser movido 
# A função heuristica retorna a quantidade de peças fora do lugar, desconsiderando a peça representada pelo número 0. 
# Cada peça fora do lugar é considerada um erro que precisa ser corrigido para alcançar o estado objetivo.
def heuristica(estado, objetivo):
    #some 1 para resposta se o estado objetivo for diferente do estado atual dentro de um loop de posições encontradas
    # no tabuleiro / desconsiderando o 0, pois o 0 não se move. 
    return sum(1 for i in range(len(estado)) if estado[i] != objetivo[i] and estado[i] != 0)

# Implementação do algoritmo A*
def a_star(estado_inicial):
    estado_objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # estado objetivo
    # heap de tuplas (f, estado, caminho)
    fila = [(heuristica(estado_inicial, estado_objetivo), estado_inicial, [])]
    visitados = set()
    visitados.add(tuple(estado_inicial))
    estados_visitados = 0  # Contador de estados visitados

    while fila:
        _, estado_atual, caminho = heapq.heappop(fila)
        estados_visitados += 1  # Incrementa o contador de estados visitados

        if estado_atual == estado_objetivo:
            # Retorna caminho e número de estados testados
            return caminho, len(caminho),estados_visitados

        for proximo_estado in gerar_estados.gerar_estados(estado_atual):
            if tuple(proximo_estado) not in visitados:
                visitados.add(tuple(proximo_estado))
                novo_caminho = caminho + [proximo_estado]
                # No algoritmo A*, a heurística é usada para calcular o custo total estimado f, 
                # que é a soma do custo do caminho g até o estado atual e o custo estimado h para chegar ao objetivo. 
                # O valor de f é usado para determinar a prioridade dos estados na fila de prioridade (implementada com um heap).
                f = len(novo_caminho) + heuristica(proximo_estado, estado_objetivo)
                heapq.heappush(fila, (f, proximo_estado, novo_caminho))

    return None, 0 , estados_visitados  # Se não encontrar solução
