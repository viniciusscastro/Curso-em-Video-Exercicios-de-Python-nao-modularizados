a = int(input('digite o primeiro numero'))
b = int(input('digite o segundo numero'))
c = int(input('digite o terceiro numero'))
menor=a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior = c

print('o maior numero é {} enquanto que o menor é {}'.format(maior,menor))