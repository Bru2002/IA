import random
def gerar_aleatorio():
    """Gera uma configuração aleatória das 8 rainhas."""
    return [random.randint(0, 7) for _ in range(8)]