v=float(input('qual a velocidade que registrada?'))
if v>80:
    print('você foi multado')
    print('tera que pagar R${}'.format((v-80)*7))
else:
    print('parabens você seguiu a lei')
