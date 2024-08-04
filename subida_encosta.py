import random
import gerar_aleatorio
import conflito 

def subida_encosta_reinicio_aleatorio():
    """Implementa o algoritmo de subida de encosta com reinício aleatório e retorna a evolução das métricas e a melhor solução encontrada."""
    reinicios = 0
    evolucao = []  # Armazena a evolução das métricas
    tabuleiro = gerar_aleatorio.gerar_aleatorio()
    conflitos_atual = conflito.conflito(tabuleiro)
    
    while conflitos_atual > 0:
        melhor_tabuleiro = None
        melhor_conflito = conflitos_atual
        
        for i in range(8):
            for j in range(8):
                if tabuleiro[i] != j:
                    novo_tabuleiro = tabuleiro[:]
                    novo_tabuleiro[i] = j
                    conflitos_novo = conflito.conflito(novo_tabuleiro)
                    
                    if conflitos_novo < melhor_conflito:
                        melhor_tabuleiro = novo_tabuleiro
                        melhor_conflito = conflitos_novo
        
        if melhor_tabuleiro:
            tabuleiro = melhor_tabuleiro
            conflitos_atual = melhor_conflito
            # Registra a qualidade da solução
            evolucao.append((reinicios, conflitos_atual))
        else:
            # Reinício aleatório
            tabuleiro = gerar_aleatorio.gerar_aleatorio()
            conflitos_atual = conflito.conflito(tabuleiro)
            reinicios += 1
    
    return tabuleiro, evolucao, reinicios
