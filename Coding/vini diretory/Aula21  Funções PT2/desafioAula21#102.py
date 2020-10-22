def fatorial(num, show = False):
    if show == False:
        fator=1
        for c in range(num, 0, -1):
            fator *= c
        return fator
    else:
        fator = 1
        for c in range(num, 0, -1):
            fator *= c
            if c > 1:
                print(f'{c} x', end=' ')
            else:
                print(f'{c} = ', end= '')
        return fator

print('--'*30)
print(fatorial(5, True))