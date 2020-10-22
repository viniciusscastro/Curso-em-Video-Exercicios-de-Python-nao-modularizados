n=float(input('digite um numero nao inteiro(com virgula):'))
from math import trunc
pi=trunc(n)
print('a porção inteira de {} é {}'.format(n,pi))
print('a porção inteira de {} é {}'.format(n,trunc(n)))