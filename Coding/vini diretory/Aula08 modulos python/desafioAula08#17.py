from math import sqrt, pow
co = float(input('digite o comprimento do cateto oposto'))
ca = float(input('digite a medida do cateto adjacente'))
hi = sqrt(pow(co, 2) + pow(ca, 2))
print('a medida da hipotenusa deste triangulo é: {:.2f}'.format(hi))
