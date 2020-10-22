def notas(*n, sit=False):
    """
    Função que analisa notas e situações de varios alunos
    :param n: uma ou mais notas dos alunos
    :param sit: valor opcional para mostrar situação do aluno
    :return: dicionario com varias informações sobre a situação da turma
    """
    r = dict()
    r['Total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >= 5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'Ruim'
    return r


resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)
