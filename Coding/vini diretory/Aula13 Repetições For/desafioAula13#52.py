n = int(input('digite um numero inteiro\n'))
tot=0
for c in range(1, n+1):
    if n%c==0:
        print('\033[33m', end='')
        tot+=1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c))
print('o numero {} foi divisivel {} vezes'.format(n, tot))
if tot==2:
    print('por isso ele é primo')
else:
    print('Por isso ele nao é primo')