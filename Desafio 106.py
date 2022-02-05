"""
Desafio 106:

Faça um mini sistema que utilize o interactive help do python.
O usuário vai digitar o comando e o manual vai aparecer. QUando o osuário digitar a palavra 'FIM',
o programa se encrrará.

OBS > Use cores.
"""
from time import sleep


def titulo(msg):
    tam = len(msg) + 4
    print('\033[1;32;40m~' * tam)
    print(f' {msg}')
    print('~' * tam)


def ajuda(com):
    help(com)


while True:
    titulo('SISTEMA DE AJUDA PYHELP')
    resp = str(input('\033[m\033[1;32mFunção ou Biblioteca > ')).strip()
    if resp not in 'FimFIMfim':
        titulo(f'Acessando o sistema de {resp}')
        sleep(1)
        print('\033[1;30;45m')
        ajuda(resp)
    else:
        print('Você Saiu...')
        break