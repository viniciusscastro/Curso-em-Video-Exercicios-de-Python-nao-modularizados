def contador(inicio, fim, passo):
    if inicio < fim:
        print('-=' * 30)
        print(f'contagem de {inicio} ate {fim} de {passo} em {passo}')
        for c in range(inicio, fim+1, passo):
            print(c, end='...')
        print()
        print('-='*30)
    elif inicio > fim:
        print(f'contagem de {inicio} ate {fim} de {passo} em {passo}')
        passo *= -1
        for c in range(inicio, fim-1, passo):
            print(c, end='...')
        print()
        print('-=' * 30)
    else:
        print('não há como fazer a contagem')

contador(1, 10, 1)
contador(10, 0, 2)
print('agora é sua vez!')
i = int(input('digite o inicio da sua  contagem\n'))
f = int(input('digite o fim da sua contagem\n'))
p = int(input('digite o ritmo da sua contagem\n'))
contador(i, f, p)