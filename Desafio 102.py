"""
Crie um programa que tenha uma função fatorial()
que receba dois parametros: o primeiro que indique o numero a calcular e o outro chamado show,
que será um valor lógico
(opcional) indicando se será mostrado ou não na tela o processo de
calculo fatorial
"""


def fatorial(num, show=False):
    cont = 1
    f = 1
    while cont <= num:
        if show:
            print(f'{cont}', end='')
            if cont > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= cont
        cont += 1
    return f'= {f}'


produto = int(input('Você deseja ver o fatorial de qual número? '))
print(fatorial(produto, True))
