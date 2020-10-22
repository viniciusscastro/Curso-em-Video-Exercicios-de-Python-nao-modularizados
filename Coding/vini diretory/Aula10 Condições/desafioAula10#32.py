ano= int(input('em que ano voce esta'))
if ano%4==0 and ano%100 or ano%400==0 :
    print('você esta em um ano bissexto')
else:
    print('voce nao esta em um ano bissexto')