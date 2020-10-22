dias=int(input('quantos dias alugados'))
km=float(input('quantos Km foram rodados'))
total=(60*dias)+(km*0.15)
print('você deve pagar um total de R${}'.format(total))
