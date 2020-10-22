n1 = float(input('qual a sua primeira nota?'))
n2 = float(input('qual a sua segunda nota?'))
media = (n1+n2)/2

if media>7:
    print('parabens você foi aprovado pois sua media foi {}'.format(media))
elif media >= 5 and media < 7:
    print('você esta de exame fara recuperação pois sua media é {}'.format(media))
else:
    print('você foi reprovado pois sua media é {}'.format(media))