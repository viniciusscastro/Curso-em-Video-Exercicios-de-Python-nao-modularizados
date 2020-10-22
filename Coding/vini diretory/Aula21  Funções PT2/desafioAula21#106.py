def ajuda(com):
    """
    consegue de maneira responsiva fornecer a funcionalidade da função digitada
    :param com: comando a ser colocado em help() para ver sua funcionalidade nos docfunctions
    :return:
    """
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('=-'*tam)
    print(f'   {msg}')
    print('-='*tam)


#programa Principal
comando = ''
while True:
    titulo('Sistema de Ajuda Pyhelp')
    comando = str(input('função ou biblioteca>'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Ate logo')