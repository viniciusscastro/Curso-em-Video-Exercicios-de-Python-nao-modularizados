n = int(input('escreva um numero inteiro para ser convertido:'))
escolha = int(input('escolha: \n[1] para converção em binario\n'
                    '[2] para converção em octal\n'
                    '[3] para converção hexadecimal\n\n'))
if escolha ==1:
    print('o numero {} em binario é {}'.format(n, bin(n)[2:]))

elif escolha == 2:
    print('o numero {} em octal é {}'.format(n, oct(n)[2:]))
elif escolha ==3:
    print('o  numero {} em hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('escolha indisponivel rode a aplicação novamente para fazer uma converção')