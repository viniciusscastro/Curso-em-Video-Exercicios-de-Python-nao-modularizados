p = float(input('qual é o peso KG?'))
h = float(input('qual a altura em metros ?'))

imc = p / h ** 2
if imc < 18.5:
    print('abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Morbida')
