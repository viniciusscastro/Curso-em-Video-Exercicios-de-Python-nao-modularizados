frase=input('digite uma frase').strip()
print('a letra A aparece {}'.format(frase.lower().count('a')))
print('o primeiro A aparece na posição {}'.format(frase.lower().find('a')+1))
print('a ultima letra A apareceu na posição {}'.format(frase.rfind('a')+1))
