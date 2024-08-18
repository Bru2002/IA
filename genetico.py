import random
import gerar_aleatorio
import conflito

def gerar_populacao(tamanho):#Gera uma população inicial de 100 soluções.
    """Gera uma população inicial de soluções aleatórias."""
    return [gerar_aleatorio.gerar_aleatorio() for _ in range(tamanho)]

def selecionar(populacao):
    """Seleciona duas soluções para cruzamento usando roleta."""
    #A aptidão é inversamente proporcional ao número de conflitos. 
    # Se conflito.conflito(individual) é o número de conflitos para um indivíduo, então a aptidão é calculada como 1 / (conflito + 1). 
    # Adiciona-se 1 ao número de conflitos para evitar divisão por zero e para garantir 
    # que mesmo indivíduos com muitos conflitos tenham uma aptidão positiva.
    aptidoes = [1 / (conflito.conflito(individual) + 1) for individual in populacao]
    total = sum(aptidoes)#soma as aptidoes do grupo
    probabilidade = [aptidao / total for aptidao in aptidoes] # considera a aptidao inicial div pela total para cada individuo
    selecionados = random.choices(populacao, probabilidade, k=2) #seleciona  e retorna 2 com base na probabilidade
    return selecionados

def cruzar(pai1, pai2):
    """Aplica o cruzamento entre dois pais."""
    #sorteia 0-7
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
    populacao = gerar_populacao(220)
    evolucao = []  # Inicializa uma lista evolucao para armazenar a qualidade das soluções ao longo das gerações.
    geracoes = 0 #contador de gerações.
    
    while geracoes < max_geracoes: 
        populacao.sort(key=lambda ind: conflito.conflito(ind)) 
        #Ordena a população com base no número de conflitos de cada indivíduo, 
        #de forma que o indivíduo com menor número de conflitos (melhor solução) fique no início da lista.
        
        # Registra a qualidade da solução
        qualidade = conflito.conflito(populacao[0])
        evolucao.append((geracoes, qualidade))
        #efere-se ao primeiro indivíduo da lista populacao, 
        #que é o indivíduo com menor número de conflitos 
        #(ou seja, o melhor indivíduo da população após a ordenação).
        
        if qualidade == 0: #Se qualidade == 0, isso significa que a melhor solução na população tem zero conflitos, 
            return populacao[0], evolucao, geracoes
        
        nova_populacao = populacao[:10] #cria uma nova lista contendo os primeiros 10 indivíduos da lista populacao.
        #é inicializada com esses 10 melhores indivíduos, que serão os pais da próxima geração.
        
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
