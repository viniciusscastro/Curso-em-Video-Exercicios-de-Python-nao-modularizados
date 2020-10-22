sexo = ''
while sexo == '':
    p = str(input('digite seu sexo [M/F]')).strip().upper()#se ele digitar espaços desnecessarios eles serao retirados
    if p == 'M':
        sexo = p
    elif p == 'F':
        sexo = p
    else:
        print('Errou só é possivel escolher digitando com a letra "M" ou "F" tente novamente:')
if sexo == 'M':
    print('seu sexo é masculino')
else:
    print('seu sexo é feminino')
