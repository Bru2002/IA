from collections import deque
import heapq
import time
import a_star
import BFS

# Função para formatar a entrada
def formatar_entrada(string_entrada):
    return list(map(int, string_entrada.split()))

# Função para imprimir o tabuleiro formatado
def imprimir_tabuleiro(estado):
    for i in range(0, 9, 3):
        print(estado[i:i+3])

# Função principal
def principal():
    # Exemplo de entrada
    string_entrada = "1 2 3 4 5 0 6 7 8"
    estado_inicial = formatar_entrada(string_entrada)

    print("Estado inicial:")
    imprimir_tabuleiro(estado_inicial)

    # Escolha do algoritmo
    escolha = input("Escolha o algoritmo (1 para BFS, 2 para A*): ")

    if escolha == '1':
        # Usar BFS2
        caminho, num_movimentos, num_visitados, tempo_execucao = BFS.bfs(estado_inicial)
        if caminho:
            print("\nSolução encontrada em", num_movimentos, "movimentos:")
            for estado in caminho:
                imprimir_tabuleiro(estado)
                print()
            print(f"Número de estados visitados: {num_visitados}")
            print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
        else:
            print("\nNão foi encontrada uma solução.")
            print(f"Número de estados visitados: {num_visitados}")
            print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
    
    elif escolha == '2':
        # Usar A* com heurística de peças fora do lugar
        inicio = time.time()
        caminho, num_movimentos, num_estados_visitados = a_star.a_star(estado_inicial)
        fim = time.time()

        tempo_execucao = fim - inicio

        if caminho:
            print("\nSolução encontrada em", num_movimentos, "movimentos:")
            for estado in caminho:
                imprimir_tabuleiro(estado)
                print()
        else:
            print("\nNão foi encontrada uma solução.")
        
        print(f"Número de estados visitados: {num_estados_visitados}")
        print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
    
    else:
        print("Escolha inválida.")

if __name__ == "__main__":
    principal()
