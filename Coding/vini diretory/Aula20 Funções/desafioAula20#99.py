from time import sleep
def maior(*num):
    maior = 0
    print('analizando os valores passados...')
    for valor in num:
        print(f'[{valor}', end=']...')
        sleep(1)
        if num[0] == valor:
            maior = valor
        elif maior < valor:
            maior = valor
    print()
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor é {maior}')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(6)
maior()