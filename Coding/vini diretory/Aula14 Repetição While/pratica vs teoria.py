#estrutura de repetição com teste logico = while
#estrutura de repetição com variavel de controle = for
#enquanto {teste logico ou condição}
#   comando...etc

#while {condição logica}
#exemplo na parte pratica:
#        c=1
#        while c<10:
#            print(c)
#            c+=1
#        print('fim')
n=1
par = impar = 0
while n != 0:
    n = int(input('digite um valor'))
    if n%2==0:
        par+=1
    else:
        impar+=1
print('voce digitou {} numeros parres e {} numeros impares'.format(par,impar))
