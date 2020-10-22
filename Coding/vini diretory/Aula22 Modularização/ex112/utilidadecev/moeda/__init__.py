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


def resumo(n, aumento, redução):
    print('-='*20)
    print('         RESUMO DO  VALOR')
    print('-='*20)
    print(f'preço analisado:   {moeda(n)}')
    print(f'Dobro do preço:    {dobro(n)}')
    print(f'Metade do preço:   {metade(n)}')
    print(f'80% de aumento:    {aumentar(n, 80)}')
    print(f'35% de desconto:   {diminuir(n, 35)} ')
    print('-='*20)
