# Calcular fatorial de um número definido pelo usuário

def fatorial(n):
    c = 1  # contador para suportar o laço de repetição
    fat = n  # valor inicial para dar suporte ao cálculo do fatorial
    if n == 0:
        fat = 1
    else:
        while c < n:
            fat = fat * (n - c)
            c = c + 1
    return fat

def numeroBinomial(n, k):
    return fatorial(n) / (fatorial(k)*(fatorial(n-k)))

def maximo(x, y, z):
    maior = max(x, y, z)
    return maior

def ePrimo(k):
    s = 0
    c = 1
    while c <= k:
        if k % c == 0:
            s = s + 1
            c = c + 1
        else:
            c = c + 1
    return s

def maior_primo(k):
    m = 1
    i = 0
    while m <= k:
        if ePrimo(m) == 2:
            i = m
            m = m + 1
        else:
            m = m + 1
    return i

def vogal(x):
    vogais = 'AEIOU'
    c = 0
    aux = False
    while c < len(vogais) and not aux:
        if x.upper() == vogais[c]:
            aux = True
        else:
            aux = False
        c = c + 1
    return aux
