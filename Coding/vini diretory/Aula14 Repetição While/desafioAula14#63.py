#precisa de ajuda
n = int(input('ate qual termo quer ir na sequencia de fibonacci'))
t1=0
t2=1
if n == 1:
    print(t1)
elif n == 2 or n>2:
    print('{} -> {}'.format(t1, t2), end='')
    if n == 2:
        cont = n+1
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('->fim')