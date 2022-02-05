"""
Desafio 101:

Crie um programa que tenha uma função chamada voto()
que vai receber como parametro, o ano de nascimento de uma pessoa
retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleiçoes
"""


def votar(anos):
    from datetime import date
    ano = date.today().year
    idade = ano - anos
    if idade < 16:
        return f'Com {idade} anos: Não VOTA'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


nasc = int(input('Em que ano você nasceu? '))
print(votar(nasc))
