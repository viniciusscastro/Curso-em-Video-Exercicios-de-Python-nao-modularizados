ano= int(input('qual é o ano de nascimento do atleta?'))
print(2020-ano)
if (2020 - ano) <= 9:
    print('categoria de Mirim pois esta abaixo ou esta com 9 anos')
elif (2020 - ano) <= 14:
    print('categoria Infantil pois esta acima de 9 mas nao alem de 14')
elif (2020-ano) <= 19:
    print('categoria junior pois esta com mais de 14 anos mas abaixo ou igual a 19')
elif (2020-ano) <=20:
    print(' categoria senior pois esta entre 19 e 20 anos')
elif (2020-ano) > 20:
    print('esta acima de 20 anos portanto ja é um master')