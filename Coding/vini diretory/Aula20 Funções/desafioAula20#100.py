from random import randint
from time import sleep

def sorteia(numero):
    print('Os numeros sorteados foram:')
    for c in range(0, 5):
        numero.append(randint(0, 100))
        print(numero[c], end='...')
        sleep(1)
    somaPar(numero)

def somaPar(lista):
    pares = 0
    print()
    print('a soma entre os numeros pares:')
    for c in lista:
        if c % 2 == 0:
            pares += c
            print(c, end='...')
            sleep(1)
    print()
    print(f'É igual à {pares}')

numeros = []
sorteia(numeros)