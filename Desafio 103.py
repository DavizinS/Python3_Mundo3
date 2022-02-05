"""
Faça um programa que tenha uma função chamada ficha()
que receba dois parametros opcionais, o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não
tenha sido informado corretamente.
"""


def ficha(n, g):
    if len(n) == 0:
        n = '<desconhecido>'
    print(f'O jogador {n.title()} fez {g} gol(s) no campeonato.')


# Programa
nome = str(input('Nome do Jogador: ')).strip()
gols = str(input('Quantos gols ele fez? '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(nome, gols)
