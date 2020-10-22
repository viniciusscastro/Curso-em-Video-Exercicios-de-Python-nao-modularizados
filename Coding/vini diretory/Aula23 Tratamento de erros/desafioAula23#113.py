def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mErro!  Digite um numero inteiro valido.\033[m')
            continue
        else:
            return n
    return


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mErro!  Digite um numero inteiro valido.\033[m')
            continue
        else:
            return n
    return


n = leiaInt('Digite um numero:')
l = leiaFloat('Digite um numero real')
print(f'Voce acabou de digitar o numero {n} que é inteiro')
print(f'Você também digitou o numero {l} que é real')