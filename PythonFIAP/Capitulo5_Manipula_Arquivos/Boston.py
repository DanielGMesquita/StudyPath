#Análise do relatório de vôos e viagens do aeroporto de Boston com base nos relatórios econômicos oficiais

with open('economic-indicators.csv', 'r') as boston:
    total_voos = 0
    maior = 0
    total_passageiros = 0
    maior_media_diaria = 0
    ano_usuario = input('Qual ano deseja pesquisar?: ')
    #Retornar o total de voos do arquivo
    for linha in boston.readlines()[1:-1]:
        lista = linha.split(',')
        total_voos = total_voos + float(lista[3])
        #Retornar o mês/ano com maior trânsito no aeroporto
        if float(lista[2]) > float(maior):
            maior = lista[2]
            ano = lista[0]
            mes = lista[1]
        #Retorna o total de passageiros que transitaram no aeroporto no ano definido pelo usuário
        if ano_usuario == lista[0]:
            total_passageiros = total_passageiros + float(lista[2])
            #Retorna o mês com maior média de diária de hotéis
            if float(lista[5]) > float(maior_media_diaria):
                maior_media_diaria = lista[5]
                mes_maior_diaria = lista[1]
    print('O total de voos é {}'.format(total_voos))
    print('O mês/ano com maior trânsito no aeroporto foi {}/{}'.format(mes, ano))
    print('O total de passageiros que passaram no ano de {} é {} passageiros'.format(str(ano_usuario),
    str(total_passageiros)))
    print('O mês do ano {} com maior média diária de hotel foi {}'.format(ano_usuario, mes_maior_diaria))


