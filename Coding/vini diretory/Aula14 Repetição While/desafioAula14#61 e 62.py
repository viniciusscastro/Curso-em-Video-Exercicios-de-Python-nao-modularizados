n1 = int(input('digite o primeiro termo da PA'))
n = n1
r=int(input('digite a razão da PA'))
n10 = n1+(r*10)
c = 1
print('os 10 primeiros termos da PA são')
while n < n10:
    n = n1+(r*c)
    c += 1
    print(n-r, end=' ')
    if n==n10:
        resposta = str(input('\nquer mais termos [S/N]?\n')).strip().upper()
        if resposta == 'S':
            termos = int(input('quer mais quantos termos?\n'))
            if termos != 0:
                n10 = n1+(r*(c+termos-1))
            else:
                print('essa foi a contagem')
        elif resposta == 'N':
            print('essa foi a contagem')

