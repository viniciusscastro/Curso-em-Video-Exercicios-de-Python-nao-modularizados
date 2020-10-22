def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
print('=-'*30)
name = str(input('Nome do jogador: '))
gol = str(input('Numero de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if name.strip() == '':
    ficha(gols=gol)
else:
    ficha(name, gol)

