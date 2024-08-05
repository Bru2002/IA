Teste de mesa Tempera Simulada/ Revisão do código

     0 1  2  3  4  5  6  7
 0 Q X X X X X X X
 1 X X X X Q X X X
 2 X X X X X X X Q
 3 X X X X X Q X X
 4 X X Q X X X X X
 5 X X X X X X Q X
 6 X Q X X X X X X
 7 X X X Q X X X X

[0,4,7,5,2,6,1,3]

índice
[0,1,2,3,4,5,6,7]

SORTEIO (1 A 7)

j = 0
i = 1

j = 1
i = 0

[4,0,7,5,2,6,1,3]

j = 7
i = 3

j = 3
i = 7

[4,0,7,3,2,6,1,5]

j = 5
i = 2

j = 2
i = 5

[4,0,6,3,2,7,1,5]

…

1. Aceitação de Soluções Piores com Alta Temperatura
No início do processo, a temperatura é alta. Isso faz com que a função de aceitação probabilística permita a aceitação de soluções piores com uma probabilidade relativamente alta. A fórmula usada para essa aceitação é:
Probabilidade = math.exp((conflitos_atual - conflitos_novo) / temperatura)
    • Se conflitos_novo (o número de conflitos da nova solução) é maior que conflitos_atual (o número de conflitos da solução atual), a probabilidade de aceitar a nova solução ainda é calculada com base na fórmula exponencial. Com alta temperatura, essa probabilidade pode ser alta, o que significa que soluções piores ainda têm uma boa chance de serem aceitas.
2. Redução Gradual da Temperatura
A cada iteração, a temperatura é reduzida multiplicando-a por um fator de resfriamento, geralmente menor que 1 (por exemplo, 0.95). A redução gradual da temperatura faz com que a função de aceitação probabilística se torne mais seletiva:
temperatura *= fator_resfriamento
À medida que a temperatura diminui:
    • A diferença entre conflitos_atual e conflitos_novo tem um impacto maior na probabilidade de aceitação. Com uma temperatura mais baixa, a probabilidade de aceitar uma solução pior (ou seja, uma solução com mais conflitos) diminui.
3. Menor Aceitação de Soluções Piores
    • Quando a temperatura está baixa, a fórmula exponencial tende a se aproximar de 0 se conflitos_novo for muito maior que conflitos_atual. Isso significa que soluções piores são aceitas com menos frequência, e o algoritmo se torna mais seletivo, preferindo soluções que têm menos conflitos.
