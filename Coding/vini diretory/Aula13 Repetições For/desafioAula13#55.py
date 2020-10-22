maior=0
menor=0
for c in range(1, 6):
    p=float(input('qual é o {} peso?'.format(c)))
    if c==1:
        maior=p
        menor=p
    if p>maior:
        maior=p
    if p<menor:
        menor=p
print('o maior numero é {} enquanto o menor é {}'.format(maior, menor))