f=str(input('digite uma frase que pode ser um palindromo')).strip().upper()# para tirar os espaços entre elas e deixar em miusculo
palavras= f.split() #separando as palavras tirando o espaço entre elas
junto = ''.join(palavras)#juntando todas as palavras das frases retirando seus espaços entre elas
inverso=''
for letra in range(len(junto)-1, -1 , -1):
    inverso += junto[letra]
if inverso==junto:
    print('a frase é um palindromo')
else:
    print('a frase nao é um palindromo')
