total = produtosmais = vbarato = 0
nbarato = ''
while True:
    nome = str(input('qual é o nome do produto')).strip()
    preço = float(input('qual o valor do produto?'))
    if total == 0:
        vbarato = preço
        nbarato = nome
    elif preço < vbarato:
        nbarato = nome
    if preço > 1000:
        produtosmais =+ 1
    total +=preço
    continuar = str(input('quer continuar?[S/N]')).upper().strip()[0]
    if continuar == 'S' or continuar == 'N':
        break
print(f'o total gasto foi de {total} o nome do produto mais barato é {nbarato} e haviam {produtosmais} produtos '
      f'que valiam mais que R$1000,00')
