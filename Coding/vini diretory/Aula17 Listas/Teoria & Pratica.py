from time import sleep
#listas []
#listas diferente de tuplas podem receber um valor diferente em sua cadeia de elementos
#quando ja definidas, alem disto podem tambem serem expandidas com o comando
#lista.append()
#há tambem a possibilidade de inserir um intem entre outros itens
#lista.insert('posição onde ira ser colocado o novo item','item que ocupara a posição')
#para apagar elementos vc pode utilizar os metodos
#del lanche[posiçao do item]
#ou
#lanche.pop(posição do item) 
#ou
#lanche.remove(item)
#quando um item é eliminado todos os outros são reposicionados
#lanche.pop() elimina o ultimo item
# valores = list(range(4, 11))
# valores.sort() #ordena os itens
# valores.sort(reverse=True) #ordena os itens reversamente
# len(valores)
#num = [2, 5, 9, 1]
#num[2] = 3
#num.append(7)
#num.sort(reverse=True)
#num.insert(2, 2)
#print(num)
#sleep(2)
#num.pop(2)
#print(num)
#print(f'Essa lista tem {len(num)} elementos')

#valores =[]
#valores.append(5)
#valores.append(9)
#valores.append(4)

#for c, v in enumerate(valores):
#    print(f'na posição {c} encontrei {v}')
valores = []
for cont in range(0, 5):
    valores.append(int(input('digite um valor')))

for c, v in enumerate(valores):
    print(f'foi encontrado na posição {c} o valor {v}')
copia = valores[:] #neste caso se cria uma copia
copia2 = valores # neste caso se cria uma ligação onde a edição de uma edita a outra


