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