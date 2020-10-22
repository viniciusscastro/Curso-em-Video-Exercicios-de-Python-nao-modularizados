from time import sleep
lista = []
c = 0
while True:
    if c==0:
        lista.append(int(input(f'digite o numero da {c} posição\n')))
        sleep(1)
        c += 1
        continuar = str(input('deseja continuar?[s/n]\n')).upper().strip()[0]
        sleep(1)
        if continuar == 'N':
            print('programa finalizado')
            break
    elif c > 0:
        lista.append(int(input(f'digite o numero da posição {c}\n')))
        if lista.count(lista[c]) > 1:
            print('esse numero ja existe na lista tente outro valor')
            lista.remove(lista[c])
            sleep(2)
        else:
            print(f'valor {lista[c]} armazenado na posição {c}')
            c += 1
            sleep(1)
            continuar = str(input('deseja continuar?[s/n]\n')).upper().strip()[0]
            if continuar == 'N':
                print('programa finalizado')
                break
print(f'foram digitados {c} eles são:')
lista.sort()
for s in lista:
    print(s, '...', end='')