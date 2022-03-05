import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0
    for traco in range(len(as_a)):  # percorre todos os traços linguísticos para comparar entre assinaturas
        soma = soma + abs(as_a[traco] - as_b[traco]) # calculo do valor absoluto da diferença entre os traços
    grau = soma/6 # grau de similaridade entre as assinaturas comparadas
    if grau < 0: # condicional para transformar número em positivo caso diferença seja negativa
        grau = grau * (-1)
    return grau

def calcula_assinatura(texto):
    """IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto."""
    frases = []  #lista para as frases
    palavras = []  #lista para as palavras
    tamanho_palavras = 0 #somatorio de caracteres das palavras
    caracteres_frases = 0 #somatorio de caracteres frases
    caracteres_sentencas = 0 #somatorio de caracteres sentenças
    sentencas = separa_sentencas(texto)  # primeiro separar as sentenças
    for sentenca in sentencas:
        caracteres_sentencas += len(sentenca)
        novas_frase = separa_frases(sentenca) #separando as frases de cada sentença
        for frs in novas_frase:#adiciona as frases separadas na lista de frases
            frases.append(frs)
    for frase in frases:
        caracteres_frases += len(frase) # totaliza os caracteres das frases
        novas_palavras = separa_palavras(frase) #separa as palavras de cada frase
        for palavra in novas_palavras:
            palavras.append(palavra) #adiciona as palavras separadas na lista de palavras
    for palavra in palavras:
        tamanho_palavras += len(palavra) #conta os caracteres de cada palavra separada

    wal_texto = tamanho_palavras / len(palavras)  # tamanho médio das palavras
    ttr_texto = n_palavras_diferentes(palavras)/len(palavras)  # número de palavras diferentes/total de palavras
    hlr_texto = n_palavras_unicas(palavras)/len(palavras) # palavras únicas/total de palavras
    sal_texto = caracteres_sentencas/len(sentencas)  # tamanho médio da sentença
    sac_texto = len(frases)/len(sentencas) # complexidade sent: total frases / total setenças
    pal_texto = caracteres_frases/len(frases) # tamanho médio das frases
    assinatura = [wal_texto, ttr_texto, hlr_texto, sal_texto, sac_texto, pal_texto]
    return assinatura

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    indice = [] # lista para armazenar o grau de semelhança das assinaturas
    for texto in textos:
        assinatura = calcula_assinatura(texto) # calcula a assinatura de cada texto
        indice.append(compara_assinatura(assinatura, ass_cp)) # adiciona na lista de indices o grau de semelhança das assinaturas
    menor = indice[0] # adiciona o primeiro indice como menor para parametro de comparação
    infectado = 1 # variável que define o texto infectado
    for i in range(1, len(indice)): # laço partindo do segundo elemento da lista, pois o primeiro já foi definido como primeiro parametro de comparação
        if menor > indice[i]:
            infectado = i
    return infectado

def main():
    ass_cp = le_assinatura() # recebe a assinatura parametro de um infectado com COH-PIAH
    textos = le_textos() # recebe os textos para comparação
    # Imprimir a avaliação dos textos e das assinaturas comparadas que define o infectado
    print('O autor do texto {} está infectado com COH-PIAH'.format(avalia_textos(textos, ass_cp)))

main()

