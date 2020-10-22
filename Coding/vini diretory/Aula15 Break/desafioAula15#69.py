from time import sleep
qhomens = qmulhers = qmaiores = 0
while True:
    idade = int(input('digite sua idade'))
    sexo= ''
    while sexo not in 'MF':
        sexo = str(input('digite seu sexo [M/F]')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('quer continuar?[S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
    if idade > 18 and (sexo == 'F' or sexo =='M'):
        qmaiores += 1
    if sexo == 'M':
        qhomens += 1
    if sexo == 'F' and idade < 20:
        qmulhers +=1
    print('aguarde estamos gerando o relatorio')
    sleep(2)
print(f'{qmaiores} maiores de idade\n{qhomens} homens cadastrados\n{qmulhers} mulheres com idade menor que 20 ')