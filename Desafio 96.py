"""
Desafio 096:

Faça um programa que tenha um funçãp chamada área(), que
receba as dimensoes de um terreno retangular(Largura e comprimento) e
mostre a area do terreno.
"""


def area(lar, com):
    terreno = lar * com
    print(f'A área de um terreno {lar:.1f}x{com:.1f} é de {terreno:.1f}m²')


print('Controle de Terrenos')
print('-' * 30)
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg, comp)
