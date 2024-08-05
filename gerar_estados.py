# Função para encontrar o índice do espaço vazio (0)
def encontrar_vazio(estado):
    return estado.index(0) 
# Função para gerar novos estados após um movimento
def gerar_estados(estado):
    indice_vazio = encontrar_vazio(estado)
    estados_possiveis = []

    # Movimento para cima
    if indice_vazio >= 3:
        novo_estado = estado[:]
        novo_estado[indice_vazio], novo_estado[indice_vazio - 3] = novo_estado[indice_vazio - 3], novo_estado[indice_vazio]
        estados_possiveis.append(novo_estado)

    # Movimento para baixo
    if indice_vazio <= 5:
        novo_estado = estado[:]
        novo_estado[indice_vazio], novo_estado[indice_vazio + 3] = novo_estado[indice_vazio + 3], novo_estado[indice_vazio]
        estados_possiveis.append(novo_estado)

    # Movimento para a esquerda
    if indice_vazio % 3 != 0:
        novo_estado = estado[:]
        novo_estado[indice_vazio], novo_estado[indice_vazio - 1] = novo_estado[indice_vazio - 1], novo_estado[indice_vazio]
        estados_possiveis.append(novo_estado)

    # Movimento para a direita
    if indice_vazio % 3 != 2:
        novo_estado = estado[:]
        novo_estado[indice_vazio], novo_estado[indice_vazio + 1] = novo_estado[indice_vazio + 1], novo_estado[indice_vazio]
        estados_possiveis.append(novo_estado)

    return estados_possiveis