def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não vota.'
    elif 16 <= idade <18 or idade >65:
        return f'Com {idade} anos: Voto Opcional.'
    else:
        return f'Com {idade} anos: Voto obrigatorio.'


nasc = str(input('Em que ano  voce nasceu'))
print(voto(nasc))
