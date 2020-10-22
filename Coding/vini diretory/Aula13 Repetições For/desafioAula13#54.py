menor=0
maior=0
for c in range(1, 8):
    n= int(input('qual a sua idade?'))
    if n>=18:
        maior += 1
    else:
        menor += 1
print('a quantia de maiores de idade é {} e de menores é {}'.format(maior, menor))
