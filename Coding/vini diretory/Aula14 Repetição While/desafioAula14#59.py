from time import sleep
c2=0
c=0
while c==0:
    n1 = float(input('digite o primeiro valor\n'))
    n2 = float(input('digite o segundo valor\n'))
    c=1
    while c2 == 0:
        sleep(3)
        e = int(input('selecione a operação que deseja realizar com os numeros {} e {}:\n'
              '[1] para somar\n[2] para multiplicar\n[3] para ver qual é o maior\n'
              '[4] para novos numeros\n[5] para sair do programa\n'.format(n1, n2)))
        if e == 1:
            print('a soma dos numeros é {}'.format(n1+n2))
        elif e == 2:
            print('a multiplicação entre eles é {}'.format(n1*n2))
        elif e == 3:
            if n1 > n2:
                print('o maior numero é: {}'.format(n1))
            elif n2 > n1:
                print('o maior numero é: {}'.format(n2))
        elif e == 4:
            print('ok repetiremos o processo!')
            c2 = 1
            c=0
        elif e == 5:
            c += 1
            c2 += 1
        else:
            print('opção invalida tente novamente')
print('processo finalizado')