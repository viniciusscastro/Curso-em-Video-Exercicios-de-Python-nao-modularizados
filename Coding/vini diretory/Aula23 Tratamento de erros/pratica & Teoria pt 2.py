try:
    a = int(input('numerador: '))
    b = int(input('denominador: '))
    r = a/b

except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dadps que você digitou')
except ZeroDivisionError:
    print(f'Não é possivel dividir um numero por ZERO')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados!')
except Exception as error:
    print(f'Ouve um erro não previsto! ele esta relacionadoo com\n {error.__class__}')
else:
    print(f'A divisão {a}/{b} é igual a  {r:.2f}')
finally:
    print('volte sempre ^^! Muito obrigado')