quantia = soma = media = maior = menor = c = 0
while c != 1:
    r = str(input('quer digitar o {} numero?[s/n]'.format(quantia+1))).strip()[0].upper()
    if r == 'S':
        n = int(input('digite o numero que deseja armazenar'))
        soma += n
        quantia += 1
        if quantia == 1:
            maior = n
            menor = n
        elif n > maior:
            maior = n
        elif n < menor:
            menor = n
    elif r == 'N':
        c = 1
media = soma/quantia
print('foram digitados {} numeros a media entre eles é {} o maior numero é {} o menor é {}'.format(quantia, media, maior, menor))
