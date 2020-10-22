s=float(input('QUAL É O SEU SALARIO?'))
if s>1250:
    print('seu salario é {} e sera aumentado para {}'.format(s, (s*1.1)))
else:
    print('seu salario é {} e sera aumentado para {}'.format(s, (s*1.15)))