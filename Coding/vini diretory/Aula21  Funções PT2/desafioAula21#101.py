def voto(ano):
    if 2020-ano < 18:
        return f'Negado Pois é menor de idade possui {2020-ano}'
    elif 2020-ano == 18:
        return 'opcional pois ira completar ou ja tem 18 anos'
    elif 2020-ano >= 68:
        return f'opcional pois ja atingiu a idade {2020-ano} superior ou igual a 68'
    else:
        return f'obrigatorio pois já é maior de idade possui {2020-ano}'

ano = int(input('digite o ano de nascimento:\n'))
voto(ano)
print(f'você tem voto {voto(ano)}')