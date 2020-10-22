from time import sleep
tabela = ('Athletico-PR', 'coritiba','internacional','botafogo','são paulo','goias',
          'corinthinas','bragantino-sp','atletico-go','palmeiras','santos','flamengo','fotaleza',
          'vasco da gama','gremio','sport recife','fluminense','ceara-sc','atletico-mg','bahia', 'chapecoence')
print('os 5 primeiros colocados são:')
sleep(2)
for a in range(0, 5):
    print(f'{tabela[a]} é o {a+1} colocado')
    sleep(1.5)
print('\nOs ultimos 4 colocados são')
sleep(2)
for b in range(16, 20):
    print(f'{tabela[b]} é o {b+1}')
    sleep(1.5)
print('\nos numeros em ordem alfabetica ficam:')
sleep(2)
print(sorted(tabela))
sleep(1)
print(f'\no time da chapecoence esta na posição {tabela.index("chapecoence")}')