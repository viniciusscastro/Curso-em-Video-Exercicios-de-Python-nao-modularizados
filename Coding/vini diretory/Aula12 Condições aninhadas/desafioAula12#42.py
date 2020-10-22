a = float(input('digite a primeira medida'))
b = float(input('digite a segunda medida'))
c = float(input('digite a terceira medida'))
if a < b +c and b < a+c and c< a+b:
    print('Os segmentos acima podem formar um triangulo')
    if a == b and a == c:
        print('o triangulo equilatero')
    if (a == b and a!=c) or (a == c and a!=b) or (b == c and b!=a):
        print('o triangulo isosceles')
    if a != b and a != c and c != b:
        print('o triangulo escaleno')
else:
    print('Os segmentos acima nao podem formar um triangulo')

