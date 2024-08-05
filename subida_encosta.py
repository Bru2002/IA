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
                if tabuleiro[i] != j:#POS J =! Pos I
                    novo_tabuleiro = tabuleiro[:] #copia
                    novo_tabuleiro[i] = j #assume valor de j a pos i 
                    conflitos_novo = conflito.conflito(novo_tabuleiro)
                    
                    if conflitos_novo < melhor_conflito: #se conflito for menor que anterior segue
                        melhor_tabuleiro = novo_tabuleiro
                        melhor_conflito = conflitos_novo
        
        if melhor_tabuleiro: #existe um tab melhor?
            tabuleiro = melhor_tabuleiro #assume valor do tabuleiro melhor ao tabuleiro atual
            conflitos_atual = melhor_conflito #assume valor do conflito menor ao numero atual de conflito
            # Registra a qualidade da solução
            evolucao.append((reinicios, conflitos_atual)) # cria uma lista de evol. para apresentar a analise e testes volta ao for
        else:
            # Reinício aleatório se não existir melhor
            tabuleiro = gerar_aleatorio.gerar_aleatorio() 
            conflitos_atual = conflito.conflito(tabuleiro)
            reinicios += 1 # cont reinicia +1 volta ao for
    
    return tabuleiro, evolucao, reinicios
#O teste de mesa deve ser repetido para cada combinação de i e j,
#com a atualização do melhor_tabuleiro e melhor_conflito conforme necessário. 
#Este teste ajuda a verificar a lógica de encontrar o tabuleiro com menos conflitos.