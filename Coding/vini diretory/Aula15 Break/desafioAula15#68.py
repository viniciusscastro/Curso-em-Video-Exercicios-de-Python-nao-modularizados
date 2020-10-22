from time import sleep
from random import randint
vc = 0
while True:
    n = int(input('digite um valor'))
    ip = str(input('impar ou par?[I/P]')).strip()[0].upper()
    pc = randint(1, 100)
    if (pc + n)%2 == 1 and ip == 'P':
        print(f'Computador digitou:{pc} e é impar\nvocê digitou:{n} e é par\n{pc}+{n} é {pc+n} logo impar\nvocê perdeu')
        break
    elif (pc + n)%2 ==1 and ip == 'I':
        print(f'Computador digitou:{pc} e é Par\nvocê digitou:{n} e é impar\n{pc}+{n} é {pc+n} logo impar\nvoce ganhou')
        vc += 1
    elif (pc + n)%2 == 0 and ip == 'P':
        print(f'Computador digitou:{pc} e é impar\nvocê:{n} e par\n{pc}+{n} é {pc+n} logo Par\nvoce ganhou')
        vc += 1
    elif (pc + n)%2 == 0 and ip == 'I':
        print(f'Computador digitou:{pc} e é Par\nvocê digitou:{n} e é impar\n{pc}+{n} é {pc + n} logo par\nvocê perdeu')
        break
    sleep(3)
print(f'Fim de jogo\n voce venceu {vc} vezes ')