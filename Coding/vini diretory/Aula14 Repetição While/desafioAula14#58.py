from random import randint
from time import sleep
ad = 11
t = 0
numero = randint(0, 10)
while ad != numero:
    ad = int(input('qual numero vc acha que o computador pensou? '))
    if ad == numero:
        print('parabens vc acertou com {} tentativas o numero era {}'.format(t, numero))
    else:
        print('errou tente novamente!')
        t += 1
        if numero > ad:
            print('tente um numero maior')
        else:
            print('tente um numero menor')
