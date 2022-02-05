"""

Faça um programa que tenha uma função chamada escreva()
que receba um texto qualquer como parametro e mostre uma mensagem como tamanho adaptavel
Ex: Escreva('Ola, mundo!')
__________
Olá, Mundo
__________
"""


def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa Principal
escreva('Curso de Python')
escreva('Davi dos Santos')
escreva('CeV')
