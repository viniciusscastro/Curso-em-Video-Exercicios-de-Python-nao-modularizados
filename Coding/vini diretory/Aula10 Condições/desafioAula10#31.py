d= float(input('qual a distancia percorrida no trajeto me KM?'))
if d>200:
    print('o valor sera de R${}'.format(d*0.45))
else:
    print('o valor sera de R${}'.format(d*0.5))