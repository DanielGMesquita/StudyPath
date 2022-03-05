# Desenhar um retângulo utilizando o caractere "#" de acordo com altura e largura

largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))
apoio = 1  # apoio para o laço de repetição que desenha a linha
apoioa = 1  # apoio para o laço de repetição que aninhado que fornece as colunas
while apoioa <= altura:
    while apoio <= largura:
        print('#', end='')
        apoio += 1
    print('')
    apoio = 1
    apoioa += 1