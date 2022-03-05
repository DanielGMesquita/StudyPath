#Recebe um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito
#com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".

n = input('Digite um número: ')
adj = False  #condição para encerramento
c = 1  #contador para iterações
d = n[0]  #variável de apoio para poder realizar comparação entre os itens da string
aux = 0  #auxiliar para definir a condição final

while c < len(n) and not adj:
    if d == n[c]:
        adj = True
        aux = 1
    d = n[c]
    c = c + 1
if aux == 1:
    print('sim')
else:
    print('não')