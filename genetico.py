import random
import gerar_aleatorio
import conflito

def gerar_populacao(tamanho):
    """Gera uma população inicial de soluções aleatórias."""
    return [gerar_aleatorio.gerar_aleatorio() for _ in range(tamanho)]

def selecionar(populacao):
    """Seleciona duas soluções para cruzamento usando roleta."""
    aptidoes = [1 / (conflito.conflito(individual) + 1) for individual in populacao]
    total = sum(aptidoes)
    probabilidade = [aptidao / total for aptidao in aptidoes]
    
    selecionados = random.choices(populacao, probabilidade, k=2)
    return selecionados

def cruzar(pai1, pai2):
    """Aplica o cruzamento entre dois pais."""
    ponto = random.randint(0, 7)
    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]
    return filho1, filho2

def mutar(individuo):
    """Aplica a mutação em um indivíduo."""
    i, j = random.sample(range(8), 2)
    individuo[i], individuo[j] = individuo[j], individuo[i]
    return individuo

def algoritmo_genetico(max_geracoes=1000):
    """Implementa o algoritmo genético e retorna a evolução das métricas e a melhor solução encontrada."""
    populacao = gerar_populacao(100)
    evolucao = []  # Armazena a evolução das métricas
    geracoes = 0
    
    while geracoes < max_geracoes:
        populacao.sort(key=lambda ind: conflito.conflito(ind))
        
        # Registra a qualidade da solução
        qualidade = conflito.conflito(populacao[0])
        evolucao.append((geracoes, qualidade))
        
        if qualidade == 0:
            return populacao[0], evolucao, geracoes
        
        nova_populacao = populacao[:10]
        
        while len(nova_populacao) < 100:
            pai1, pai2 = selecionar(populacao)
            filho1, filho2 = cruzar(pai1, pai2)
            nova_populacao.append(mutar(filho1))
            nova_populacao.append(mutar(filho2))
        
        populacao = nova_populacao
        geracoes += 1
    
    # Retorna a melhor solução encontrada até o momento, mesmo que não seja ótima
    populacao.sort(key=lambda ind: conflito.conflito(ind))
    return populacao[0], evolucao, geracoes
