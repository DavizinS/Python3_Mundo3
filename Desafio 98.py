"""
Faça um programa que tenha uma função chamada contador(),
que receba três parametros; inicio, fim e passo e realize a contagem

Seu programa tem que realizar três contagem, atraves da função criada

A) De 1 até 10, de 1 em 1
b) De 10, até 0, de 2 em 2
C) Uma conatgem personalizada.
"""
from time import sleep


def linha():
    print('-' * 30)


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contando de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
        linha()
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')
        linha()


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar...')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
linha()
contador(inicio, fim, passo)