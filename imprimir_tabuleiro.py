def imprimir_tabuleiro_com_indices(tabuleiro):
    """Imprime o tabuleiro com índices para facilitar a visualização das posições."""
    tamanho = len(tabuleiro)
    print("Tabuleiro:")
    print("  " + "".join(f"{i:2}" for i in range(tamanho)))  # Imprime os índices das colunas
    for linha in range(tamanho):
        linha_tabuleiro = ['X' for _ in range(tamanho)]
        linha_tabuleiro[tabuleiro[linha]] = 'Q'
        print(f"{linha:2} " + " ".join(linha_tabuleiro))  # Imprime o índice da linha e o conteúdo da linha
    print()
