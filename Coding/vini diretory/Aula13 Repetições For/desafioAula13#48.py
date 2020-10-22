s=0
cont=0
for c in range(0, 501, 3):
    if (c%2)==1:
        s += c
        cont = cont+1
print('a soma dos numeros impares e multiplos de 3 entre 1 e 500 e {}'.format(s))
print('foram contados {} numeros'.format(cont))