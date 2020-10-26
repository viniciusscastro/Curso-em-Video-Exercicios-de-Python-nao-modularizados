from time import sleep
#variaveis compostas: são divididas me tuplas, listas e dicionarios
#nestas aulas serão estudadas tuplas

# exemplo
# lanche = {conteudo} (lanche recebe amburguer)
# lanche = {amburguer}(desta vez substituindo amburguer com suco)
# desta forma o resultado anterior do primeiro lanche se perde pois é substituida para resolver isso
# utilizamos tuplas pois elas conseguem armazenar mais do que um unico valor
# quando armazenar mais de um valor nestas tuplas cada item armazenado sera identificado por indices
# similar aos vetores no C e java
# exemplificando isso digamos que:

# lanche = (amburguer , suco, pizza, pudim)

# se utilizarmos a instrução:

# print(lanche[2])

# ele ira imprimir na tela o resultado:

# pizza
# caso seja colocado:

# print(lanche[0:2]

# ele ira imprimir:

# amburguer , pizza (e nao ira contar o 3 termo que esta na posição 2)

# lanche[1:] = suco, pizza, pudim (do primeiro ao final)

# lanche[-1] = pudim (pois o termo -1 de uma lista é o ultimo da mesma

# len(lanche) = 4 pois ha 4 elementos armazenados na variavel composta lanche

# uma maneira de preencher uma variavel composta pode se fazer:

# for c in lanche:
#   print(c) (essa estrutura ira representar os 4 valores dentro da variavel

# outra caracteristica das tuplas é que são imutaveis o que sera explicado em breve

lanche = () #todas as tuplas são iniciadas com a atribuição de () como no exemplo ok

#tuplas = () -> listas = [] -> dicionarios = {}

lanche = ('hamburguer' , 'suco', 'Pizza', 'Pudim')
print(lanche[1])    #sera exibido o suco
sleep(1)
print(lanche[3])    #sera exibido o pudim
sleep(1)
print(lanche[-2])   #sera exibido a pizza
sleep(1)
print(lanche[1:3])  #sera exibido do elemento suco aoa pudim
sleep(1)
print(lanche[2:])   #sera exibido do elemento pizza ate pudim
sleep(1)
print(lanche[:2])   #sera exibido do elemento inicial ate o elemento 2
sleep(1)
print(lanche[-2:])  #sera exibido ele ira começar na pizza e ira ate o final pudim
sleep(1)
print(lanche[-3:])  #sera exibido ele ira do elemento suco ate o final
sleep(1)
print(lanche)       #sera exibido apresentara toda a tupla
sleep(1)
print('aguarde iremos iniciar o FOR')
sleep(2)
# para representar cada elemento é possivel fazer o seguinte codigo
for comida in lanche:
    print(f'eu vou comer {comida}')
    sleep(1)

print('iremos iniciar o outro FOR com RANGE(0, LEN(LANCHE) ')
sleep(2)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer{lanche[cont]} na posição {cont}')
    sleep(1)

print('iremos iniciar outro for com o enumerate')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
    sleep(1)

print('agora iremos ordenar a lista de lanches')
sleep(2)
print(sorted(lanche))
# caso precise juntar duas tuplas crie ambas e depois some-as
#exemplo:
print('iremos calcular agora')
print('a = (2, 5, 4)\n'
    'b = (5, 8, 1, 2)\n'
    'c = b+a')
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b+a #a ordem dos fatores importa sim
print(f'c = b+a={c}')
print(f'a quantia de elementos em c é {len(c)}')
print(f' a quantia de de 5 em c é {c.count(5)}')
print(f'o index de 8 é (a posição de 8 é {c.index(8)})')

#em python tuplas aceitam todos os tipo de dados
pessoa = ('gustavo', 39, 'm', 99.88)
del(pessoa[0])