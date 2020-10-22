n=int(input('digite o numero que deseja o fatorial'))
c=n
if n == 0:
    f = 1
elif n == 1:
    f = 1
    c = 0
while c != 0:
    c -= 1
    if n == c+1:
        f = n*c
    elif c != 0:
        f = f*c
print('o fatorial de {} é :{}'.format(n, f))