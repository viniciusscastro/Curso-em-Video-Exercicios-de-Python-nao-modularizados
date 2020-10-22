nome=input('digite seu nome completo').strip()
dividido=nome.split()
print('seu primeiro nome é {}'.format(dividido[0]))
print('seu ultimo nome é {}'.format(dividido[len(dividido)-1]))