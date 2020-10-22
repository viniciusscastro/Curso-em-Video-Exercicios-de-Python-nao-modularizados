n=int(input('qual o primeiro termo da PA?\n'))
r=int(input('qual é a razão desta PA?\n'))
print('os 10 primeiros termos desta PA são:\n')
for c in range(n, n+(r*10), +r):
    print('- ', c, end=' -')