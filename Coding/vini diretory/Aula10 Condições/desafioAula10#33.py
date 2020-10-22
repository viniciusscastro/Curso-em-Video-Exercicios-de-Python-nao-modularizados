n1 = int(input('digite o primeiro numero'))
n2 = int(input('digite o segundo numero'))
n3 = int(input('digite o terceiro numero'))
if n1 > n2 and n1 > n3:
    m = n1
else:
    if n2 > n1 and n2 > n3:
        m = n2
    else:
        m = n3
if n1 < n2 and n1 < n3:
    me = n1
else:
    if n2 < n1 and n2 < n3:
        me = n2
    else:
        me = n3
print('o maior numero é {}, enquanto que o menor numero é {}'.format(m, me))
