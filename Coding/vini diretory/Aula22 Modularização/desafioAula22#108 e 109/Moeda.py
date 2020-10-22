def aumentar(n, b):
    return moeda(n*((100+b)/100))


def diminuir(n, b):
    return moeda(n*((100-b)/100))


def dobro(n):
    return moeda(n*2)


def metade(n):
    return moeda(n/2)


def moeda(n):
    return f'R${n:.2f}'
