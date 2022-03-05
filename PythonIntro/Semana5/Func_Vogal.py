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