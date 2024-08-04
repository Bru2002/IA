import math
import random
import gerar_aleatorio
import conflito
import time

def tempera_simulada(max_iteracoes=100):
    """Implementa o algoritmo de tempera simulada e retorna a evolução das métricas e a melhor solução encontrada."""
    temperatura_inicial = 2000
    fator_resfriamento = 0.9
    temperatura = temperatura_inicial

    # Gera um tabuleiro inicial aleatório
    tabuleiro = gerar_aleatorio.gerar_aleatorio()
    #verifica conflitos
    conflitos_atual = conflito.conflito(tabuleiro)
    #inicia contagem de iterações sem melhoria
    iteracoes_sem_melhoria = 0
    evolucao = []  # Armazena a evolução das métricas ao passar da exec.
    #inicia contagem de todas iterações
    iteracoes = 0 

    start_time = time.time()
    
    while iteracoes < max_iteracoes:
        # Cria uma cópia do tabuleiro e faz uma troca aleatória / Cria uma nova lista com os mesmos elementos.
        novo_tabuleiro = tabuleiro[:]
        #sorteia os elementos que podem ser trocados de lugar
        #Range faz a contagem de possíveis alterações (0-7)
        #Random sorteia e atribui uma nova posição para i e j
        i, j = random.sample(range(len(tabuleiro)), 2)
        novo_tabuleiro[i], novo_tabuleiro[j] = novo_tabuleiro[j], novo_tabuleiro[i]
        
        conflitos_novo = conflito.conflito(novo_tabuleiro)
        
        # Verifica se o novo estado deve ser aceito/ Explicação mais complexa no relatório
        if conflitos_novo < conflitos_atual or random.random() < math.exp((conflitos_atual - conflitos_novo) / temperatura):
            tabuleiro = novo_tabuleiro
            conflitos_atual = conflitos_novo
            iteracoes_sem_melhoria = 0  # Reset a contagem de iterações sem melhoria
        else:
            iteracoes_sem_melhoria += 1
        
        # Resfria a temperatura
        temperatura *= fator_resfriamento
        
        # Registra a qualidade da solução
        evolucao.append((iteracoes, conflitos_atual))
        
        # Verifica se a solução ótima foi encontrada ou se atingiu o limite de iterações sem melhoria
        if conflitos_atual == 0 or iteracoes_sem_melhoria > 1000:  # Limite interno para evitar loops infinitos
            break
        
        iteracoes += 1  # Incrementa o contador de iterações
    
    end_time = time.time()
    tempo_execucao = end_time - start_time
    
    return tabuleiro, evolucao, iteracoes
