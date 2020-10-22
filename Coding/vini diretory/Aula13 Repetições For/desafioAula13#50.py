s=0
for c in range(1, 7):
    n= int(input('digite um numero inteiro'))
    if n%2==0:
        s +=n
print('a soma dos numero pares que foram digitados é: {}'.format(s))