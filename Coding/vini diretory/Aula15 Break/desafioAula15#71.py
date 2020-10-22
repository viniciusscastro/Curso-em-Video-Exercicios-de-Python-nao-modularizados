n50 = n20 = n10 = n1 = 0
n = int(input('qual sera o valor sacado'))
valortotal = n
while True:
    if n >= 50:
        n = n-50
        n50 += 1
    elif n >= 20:
        n = n-20
        n20 += 1
    elif n >= 10:
        n = n-10
        n10 += 1
    elif n >= 1:
        n = n-1
        n1 += 1
    else:
        break
print(f'seram entregues:')
if n50 != 0:
    print(f'{n50} notas de R$50,00')
if n20 != 0:
    print(f'{n20} notas de R$20,00')
if n10 != 0:
    print(f'{n10} notas de R$10,00')
if n1 != 0:
    print(f'{n1} notas de R$$1,00 ')
print(f'Para pagar um total de R${valortotal}')