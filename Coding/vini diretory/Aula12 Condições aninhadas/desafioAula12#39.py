s=int(input('se voce for:\n'
            'Mulher digite [1]\n'
            'Homem digite [2]\n'))
if s == 2:
    n = int(input('qual o ano de nascimento?'))

    if (2020-n)<18:
        print('você nasceu em {} ainda tem {} anos '
          'vai se alistar quando completar 18 anos faltam {} ano'.format(n, (2020-n), (18-(2020-n))))
    elif (2020-n)>18:
        print('você nasceu em {} tem {} anos já devia ou deve ter se alistado á {}'.format(n, (2020-n), ((2020-n)-18)))
    else:
        print('você nasceu em {} deve se alistar neste ano pois completara 18 anos'.format(n))
else:
    print('você nao necessita fazer alistamento obrigatorio')