i = int(input('digite um numero entre 0 e 20\n'))
tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito',
       'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', ' quinze', 'dezesseis', 'dezessete', 'dezoito',
       'dezenove', 'vinte')
while True:
    if i > 20 or i < 0:
        i = int(input('tente novamente. Digite um numero entre 0 e 20\n'))
    else:
        print(f'voce digitou o numero {tupla[i]}')
        break