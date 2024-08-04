import time
import conflito
import subida_encosta
import tempera_simulada
import genetico
import imprimir_tabuleiro  # Função que imprime o tabuleiro de maneira fácil de verificar as posições das rainhas e conflitos

def testar_algoritmo(algoritmo, nome, *args):
    """Testa um algoritmo e imprime os resultados, incluindo métricas adicionais se aplicável."""
    print(f"Testando {nome}...")
    try:
        inicio = time.time()
        resultado, evolucao, metricas = algoritmo(*args)  # Recebe o resultado, evolução das métricas e métricas adicionais
        fim = time.time()
        
        tempo_execucao = fim - inicio
        conflitos = conflito.conflito(resultado)  # Recebe quantidade de conflitos
        
        # Imprime o nome do algoritmo e o tabuleiro encontrado
        print(f"{nome}:")
        imprimir_tabuleiro.imprimir_tabuleiro_com_indices(resultado)  # Chama função de impressão do tabuleiro
        print(f"Conflitos: {conflitos}")
        
        # Imprime evolução das métricas
        print("Evolução das métricas:")
        for etapa in evolucao:
            print(f"  Iteração/Reinício: {etapa[0]}, Conflitos: {etapa[1]}")
        
        # Imprime métricas adicionais se disponíveis
        if nome == "Tempera Simulada":
            print(f"Iterações realizadas: {metricas}")
        elif nome == "Subida de Encosta com Reinício Aleatório":
            print(f"Reinícios realizados: {metricas}")
        elif nome == "Algoritmo Genético":
            print(f"Gerações realizadas: {metricas}")
        
        print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
    except Exception as e:
        print(f"Erro ao testar {nome}: {e}")
    print("-" * 40)

# Testa os algoritmos sem limites definidos
testar_algoritmo(subida_encosta.subida_encosta_reinicio_aleatorio, "Subida de Encosta com Reinício Aleatório")
testar_algoritmo(tempera_simulada.tempera_simulada, "Tempera Simulada")
testar_algoritmo(genetico.algoritmo_genetico, "Algoritmo Genético")
