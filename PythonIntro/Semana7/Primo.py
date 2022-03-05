
def n_primos(x):
    a = 2
    p = 0
    c = 1
    cont = 0
    while a <= x:
        while c <= a:
            if a % c == 0:
                p += 1
                c += 1
            else:
                c += 1
        if p == 2:
            cont += 1
        p = 0
        c = 1
        a += 1
    return cont


n = int(input('Digite um número inteiro: '))
print(n_primos(n))
