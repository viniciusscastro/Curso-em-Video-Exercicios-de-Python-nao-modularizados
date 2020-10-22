import Moeda

p= float(input('digite o preço: R$ '))
print(f'A metade de {Moeda.moeda(p)} é {Moeda.metade(p)}')
print(f'O dobro de {Moeda.moeda(p)} é {Moeda.dobro(p)}')
print(f'Aumentando em 10% temos {Moeda.aumentar(p, 10)}')
print(f'Reduzindo em 13% temos {Moeda.diminuir(p, 13)}')