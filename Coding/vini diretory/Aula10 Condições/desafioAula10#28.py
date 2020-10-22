from random import randint
numero= randint(0, 5)
ad=int(input('qual numero vc acha que o computador pensou'))
if ad==numero:
    print('parabens vc acertou')
else:
    print('errou')
    print('o certo era {}'.format(numero))