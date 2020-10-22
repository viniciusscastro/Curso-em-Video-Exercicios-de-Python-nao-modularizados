p = float(input('qual o valor do produto?'))
cp = int(input('escolha a condição de pagamento\n'
             '[1] para à vista dinheiro/cheque\n'
             '[2] para a vista no cartão \n'
             '[3] para em até 2x no cartão\n'
             '[4] para 3x ou mais no cartão\n'))
if cp == 1:
    print('o valor a ser pago em dinheiro/cheque a vista é {}'.format(cp*0.9))
elif cp == 2:
    print('o valor a ser pago no cartão a vista sera de {}'.format(cp*0.95))
elif cp == 3:
    print('o valor a ser pago em 2x no cartão sera de duas parcelas de {} totalizando'.format(cp/2, cp))
elif cp == 4:
    q = int(input('quantas parcelas serão?'))
    print('o valor total a ser pago para {} vezes no cartão sera {}\n'
          'as parcelas serão de {} no final'.format(q, p*1.2, ((p*1.2)/q)))
