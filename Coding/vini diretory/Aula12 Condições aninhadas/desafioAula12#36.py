v = float(input('qual o valor da casa?'))
s = float(input('qual o salario do comprador?'))
t = int(input('quantos anos ira demorar para pagar?'))
pm = v/(t*12)

if pm > (s*0.3):
    print('desculpe infelismente seu emprestimo não pode ser '
          'aprovado pois o valor mensal seria de {:.2f}'.format(pm))
elif pm<= (s*0.3):
    print('seu emprestimo foi aprovado com sucesso')
