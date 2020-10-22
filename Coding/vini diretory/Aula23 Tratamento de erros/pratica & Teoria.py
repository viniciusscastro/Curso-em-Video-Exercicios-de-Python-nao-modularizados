try:
    a = int(input('numerador: '))
    b = int(input('denominador: '))
    r = a/b

except Exception as erro:
    print(f'Problema encontrado foi:\n{erro.__class__}')
else:
    print(f'A divisão {a}/{b} é igual a  {r:.2f}')
finally:
    print('volte sempre ^^! Muito obrigado')