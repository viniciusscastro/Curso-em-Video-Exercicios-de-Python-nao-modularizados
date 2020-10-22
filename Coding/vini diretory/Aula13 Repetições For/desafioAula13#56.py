mvelhoi=0
mvelhon=''
media=0
sm=0
mulheres=0
for c in range(1, 5):
    nome = str(input('qual seu nome?'))
    idade = int(input('qual a sua idade?'))
    sexo = int(input('digite:\n[1] se for mulher\n[2] se for homem\n'))
    sm += idade
    if c==1:
        mvelhon=nome
        mvelhoi=idade
    elif sexo==2 and idade>mvelhoi:
        mvelhon=nome
        mvelhoi=idade
    if sexo==1 and idade<20:
        mulheres += 1
media= sm/4

print('A media de idade do grupo é de {} enquanto que o homem mais velho é {}'
      ' com {} anos e no grupo ha {} mulheres com menos de 20 anos'.format(media, mvelhon, mvelhoi, mulheres))