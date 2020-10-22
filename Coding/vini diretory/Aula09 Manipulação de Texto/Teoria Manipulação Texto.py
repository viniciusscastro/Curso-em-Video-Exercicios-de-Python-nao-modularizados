#Manipulação de cadeia de textos
frase='curso em video python'#strings sao imutaveis a não ser que seja atribuido outro valor a ela
print(frase[9:13])#ele nao considera o caracter da posição 13 apenas para antes dele
print(frase[9:21])#por mais que nao exista caracter 21 ira ate o 20 e nao iria considerar o 21 mesmo que existisse
print(frase[9:21:2])#o ultimo siginifica que ira pular de dois em dois caracteres apartir do 9 caracter
print(frase[:5])# ele ira começar do caracter 0 e ira ate o 4
print(frase[15:])# ele ira do caracter 15 ate o final da string
print(frase[9::3])#neste caso ele ira começar do 9 ira ate o final e pulara de 3 em 3 caracteres

#analises de string

print(len(frase))#mostra o comprimento da string
print(frase.count('o'))#contara quantas letras o existem na frase
print(frase.count('o',0,13))#contara quantas letras 'o' existem entre o caracter 0 e 13 ignorando o 13 indo ate o 12
print(frase.find('deo'))# mostrara em que momento começou o evento DEO ou seja na posição 11
print(frase.find('android'))#ira indicar que nao ha essa string printando o valor -1
print('curso'in frase)

#Transformação

print(frase.replace('python','android'))#iria substituir os caracteres
frase.replace('android', 'python')#retornara ao valor anterior de string
print(frase.upper())#ira retornar frase em maiusculo
print(frase.lower())#ira retornar a string minuscula
print(frase.capitalize())# colocara todas as letras para minusculo enquanto a primeira letra fica maiuscula
print(frase.title())#ira colocar a primeira letra de todas as palavras da string em maiuscula
#quando pessoas ultilizam o espaço entre palavras sem necessidade com por exemplo
frase2='   aprenda python  '
print(frase2)
frase2.strip()#
frase2.rstrip()# faz com que os espaços excedente á direita serem removidos ou seja '   aprenda python'
frase2.lstrip()# remove excedentes na esquerda 'aprenda python  '
frase2.split()#o que é e como utilizar: ele divide a cadeia de caracteres caso tenha mais de uma palavra nela
# exemplificando no frase.split ele divide em 4 palavras em 4  listas diferentes
print('-'.join(frase))
