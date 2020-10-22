import math
an= float(input('digite o angulo que deseja'))
seno= math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('o angulo {} possui: \nseno = {:.2f} \ncosseno = {:.2f} \ntangente = {:.2f}'.format(an,seno, cosseno,tangente))