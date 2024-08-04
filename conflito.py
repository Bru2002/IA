def conflito(tabuleiro):
    """Conta o número de conflitos no tabuleiro."""
    conflitos = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if (tabuleiro[i] == tabuleiro[j] or
                abs(tabuleiro[i] - tabuleiro[j]) == abs(i - j)):
                conflitos += 1
    return conflitos