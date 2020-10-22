while True:
    n = int(input('digite um numero para ver a tabuada(digite um numero negativo para parar)'))
    if n < 0:
        break
    print('-=' * 20)
    for c in range(1, 11):
        print(f'{c}x{n}={c*n}')
    print('-=' * 20)
print('fim')