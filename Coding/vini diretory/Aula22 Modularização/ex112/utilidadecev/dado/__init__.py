def leiaDinheiro(n):
    valido = False
    while True:
        entrada = str(input(n)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERRO: Preço invalido!\033[m')
        else:
            valido = True
            return float(entrada)
