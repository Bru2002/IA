from collections import deque
import heapq
import time
import gerar_estados

# Implementação do algoritmo BFS
def bfs(estado_inicial):
    estado_objetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # estado objetivo
    fila = deque([(estado_inicial, [])])  # fila de tuplas (estado, caminho até o estado)

    visitados = set()
    visitados.add(tuple(estado_inicial))
    num_visitados = 0  # Contador de estados visitados

    start_time = time.time()  # Marca o início do tempo

    while fila:
        estado_atual, caminho = fila.popleft()
        num_visitados += 1  # Incrementa o contador de estados visitados

        if estado_atual == estado_objetivo:
            end_time = time.time()  # Marca o fim do tempo
            tempo_execucao = end_time - start_time
            return caminho, len(caminho), num_visitados, tempo_execucao  # Retorna caminho, número de estados testados e tempo de execução

        for proximo_estado in gerar_estados.gerar_estados(estado_atual):
            if tuple(proximo_estado) not in visitados:
                visitados.add(tuple(proximo_estado))
                fila.append((proximo_estado, caminho + [proximo_estado]))

    end_time = time.time()  # Marca o fim do tempo
    tempo_execucao = end_time - start_time
    return None, 0, num_visitados, tempo_execucao  # Se não encontrar solução