import random
n1=input('qual é o nome do primeiro aluno')
n2=input('qual é o nome do segundo aluno')
n3=input('qual é o nome do terceiro aluno')
n4=input('qual é o nome do quarto aluno')
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))