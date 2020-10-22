#condições aninhadas são condições que nao são binarias e acabam tendo condições maiores que 2
#neste caso é necessario colocar uma estrutura condicional dentro de outra estrutura condicional
#
#            ___________________________
#            !  _______ponto_________  !
#            !  !      !   !        !  !
#            !  !      !   !        !  !
#            !  !      !   !        !  !
#            !  !      !   !        !  !
#            !  !______!   !________!  !
#            !_________CARRO___________!
#
#quando o carro quiser chegar ao ponto ele tera 3 opções
# exemplificadamente poderiamos representar a situação em codigos python da seguinte maneira
# if carro.esquerda():
#   carro.siga()
#   carro.direita()
#   carro.siga()
#   carro.direta()
#   carro.siga()
# elif carro.direita():
#   carro.siga()
#   carro.esquerda()
#   carro.siga()
#   carro.esquerda()
#   carro.siga()
# else:
#   carro.siga()

#outros exemplos da pratica são

nome=str(input('qual seu nome'))
if nome=='Gustavo':
    print('Que nome bonito')
elif nome=='Pedro' or nome=='maria' or nome== 'Paulo':
    print('Seu nome é bem popular no brasil')
elif nome in 'Ana Claudia Jessica Juliana': #quando colocada esta estrutura cada um dos nomes é uma opção isolada
    print('belo nome feminino')
else:
    print('seu nome é bem normal')
print('Tenha um bom dia, {}'.format(nome))