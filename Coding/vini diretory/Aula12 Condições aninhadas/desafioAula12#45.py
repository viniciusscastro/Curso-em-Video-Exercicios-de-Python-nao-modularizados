from random import randint
ppt=int(input('Bem vindo ao jogo pedra papel tesoura\n'
              'digite:\n'
              '[1] para pedra\n'
              '[2] para tesoura\n'
              '[3] para papel\n'))
computador= randint(1, 3)
print('Joken PO')

if ppt == computador:

    print('empate')
    if ppt == 1:
        print('pedra x pedra')
    if ppt == 2:
        print('tesoura x tesoura')
    if ppt == 3:
        print('papel x papel')

elif ppt == 1 and computador == 2:
    print('pedra x tesoura')
    print('você ganhou pois pedra ganha de tesoura')
elif ppt == 1 and computador == 3:
    print(' pedra x papel')
    print('você perdeu pois pedra perde de papel')
elif ppt == 2 and computador == 1:
    print('tesoura x pedra')
    print('você perdeu pois  tesoura perde de pedra')
elif ppt == 2 and computador == 3:
    print('tesoura x papel')
    print('você ganhou pois tesoura ganha de papel')
elif ppt == 3 and computador == 1:
    print('papel x pedra')
    print('voce ganhou pois papel ganha de pedra')
elif ppt == 3 and computador == 2:
    print('papel x pedra')
    print('voce perdeu pois papel perde de tesoura')
print('sua escolha {} \ncomputador {}'.format(ppt, computador))