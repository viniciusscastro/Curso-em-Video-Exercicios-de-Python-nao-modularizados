for c in range(0, 2):
    n = (int(input(f'digite o {c+1} valor')),
         int(input(f'digite o {c+1} valor')))
    if c == 0:
        tupla = n
    else:
        auxiliar = tupla + n
        del(tupla)
        tupla = auxiliar
        del(auxiliar)
    del(n)
print(tupla)
print(f'foram digitados "9" {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'o numero 3 foi digitado na posição {tupla.index(3)+1} pela primeira vez')
else:
    print('O valor 3 nao foi digitado em alguma posição')
for c in range(0, len(tupla)):
    if tupla[c] % 2 == 0:
        print(tupla[c], 'é par')