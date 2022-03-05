def campeonato(): # executa um campeonato de 3 rodadas
    comp = 0
    user = 0
    c = 1
    while c <= 3:
        print('**** Rodada {} ****'.format(c))
        partida()
        comp += 1
        c += 1
    print('Placar: Você {} X {} Computador'.format(user, comp))

def partida(): # executa uma partida única
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    # Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida
    # com a frase "Você começa!"
    # Caso contrário, o computador toma a inciativa de começar o jogo, declarando "Computador começa!"
    if n % (m+1) != 0:
        print('Computador começa!\n')
        while n > 0:
            n -= computador_escolhe_jogada(n, m)
            print('Agora restam apenas {} peças no tabuleiro.\n'.format(n))
            if n == 0:
                print('Fim do jogo! O computador ganhou!\n')
            else:
                n -= usuario_escolhe_jogada(n, m)
                print('Agora restam apenas {} peças no tabuleiro.\n'.format(n))
    else:
        print('\nVocê começa!')
        while n > 0:
            n -= usuario_escolhe_jogada(n, m)
            print('Agora restam apenas {} peças no tabuleiro.'.format(n))
            n -= computador_escolhe_jogada(n, m)
            print('Agora restam apenas {} peças no tabuleiro.'.format(n))
            if n == 0:
                print('Fim do jogo! O computador ganhou!\n')

#Jogo do NIM
# Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada
# Objetivo do programa é garantir que seja executada a estratégia que apenas o computador ganhe


def computador_escolhe_jogada(n,m): # função que define a jogada do computador de acordo com a estratágia
    # Deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador.
    # Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.
    jogada = m
    for c in range(1, m):
        if (n-c) % (m+1) == 0:
            jogada = c
    if jogada == 1:
        print('\nComputador tirou uma peça.')
    else:
        print('\nComputador tirou {} peças.'.format(jogada))
    return jogada

def usuario_escolhe_jogada(n,m): # define a jogada do usuário
    jogada = 0
    if n > 0:
        jogada = int(input('Quantas peças você vai tirar? \n'))
        while jogada > m or jogada <= 0:
            print('Oops! Jogada inválida! Tente de novo.')
            jogada = int(input('Quantas peças você vai tirar? \n'))
        if jogada == 1:
            print('Você tirou uma peça')
        else:
            print('Você tirou {} peças.'.format(jogada))
    return jogada

print('Bem-vindo ao jogo do NIM! Escolha:')
escolha = int(input('Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato'))
if escolha == 1:
    print('\nVocê escolheu jogar uma partida isolada!\n')
    partida()
elif escolha == 2:
    print('\nVocê escolheu jogar um campeonato!\n')
    campeonato()
