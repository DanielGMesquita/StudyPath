def soma_hipotenusas(x):
    i = 1
    j = 1
    c = 1
    soma = 0
    apoio = 0
    while c <= x:
        while i < x:
            while j < x:
                if ((i ** 2) + (j ** 2)) == (c ** 2) and apoio != c ** 2:
                    apoio = c ** 2
                    soma += c
                    j += 1
                else:
                    j += 1
            i += 1
            j = 1
        i = 1
        c += 1
    return soma


n = int(input('Digite um número inteiro > 1: '))
print(soma_hipotenusas(n))