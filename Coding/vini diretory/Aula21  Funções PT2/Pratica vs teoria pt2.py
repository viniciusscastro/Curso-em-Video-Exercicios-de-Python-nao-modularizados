#parametros opcionais
def somar(a=0, b=0, c=0):
    s = a+b+c
    print(f'A soma dos valores {a}+{b}+{c} é {s}')

somar(3, 2, 5)
#quando os parametros são igualados a algum valor significa que agora eles são opcionais
somar(8, 9)
somar()