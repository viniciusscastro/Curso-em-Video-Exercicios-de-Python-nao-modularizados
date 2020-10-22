lista = []
for c in range(0, 5):
    lista.append(int(input(f'digite um valor para a posição [{c}]')))
    if c == 0:
        maior = lista[c]
        posmaior = c
        menor = lista[c]
        posmenor = c
    elif lista[c] > maior:
        posmaior = c
        maior = lista[c]
    elif lista[c] < menor:
        posmenor = c
        menor = lista[c]
for s, v in enumerate(lista):
    print(f'na posição {s} foi encontrado {v}')
print(f'sendo o maior numero o {maior} na posição {posmaior} \ne o menor é  {menor} na posição ', posmenor)