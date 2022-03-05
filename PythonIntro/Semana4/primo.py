# Recebe um número inteiro positivo na entrada e verifique se é primo.
# Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

n = int(input('Digite um número: '))
c = 1  # contador para apoiar o laço de repetição
s = 0  # variável de apoio para contabilizar se o número possui apenas divisões entre 1 e ele mesmo

while c <= n:
    if n % c == 0:
        s = s + 1
        c = c + 1
    else:
        c = c + 1
if s == 2:
    print('primo')
else:
    print('não primo')