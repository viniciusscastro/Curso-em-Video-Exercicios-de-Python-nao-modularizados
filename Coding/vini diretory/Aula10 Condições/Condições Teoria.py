#Condições simples e compostas
#
tempo=int(input('quantos anos tem seu carro?'))
if tempo<=3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')# note que os comandos que estiverem identados dentro do bloco do comando if/else seram executados
#de acordo com a condição
#
tempo=int(input('quantos anos tem seu carro?'))
print('carro novo' if tempo<=3 else 'carro velho')
#
#
#
#
#
#