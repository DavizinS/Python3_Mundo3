"""
Faça um programa que tenha uma lista chamada números e duas funções
chamadas sorteia() e somapar(). A primeira função vai sortear 5 números e vai coloca-los
dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares
sorteados pela função anterior
"""
from random import randint
from time import sleep


def sorteia(num):
    print(f'Sorteando 5 valores da lista: ', end='')
    sleep(1.5)
    for sortear in range(0, 5):
        num.append(randint(1, 10))
        print(f'{num[sortear]} ', end='', flush=True)
        sleep(0.5)
    print('PRONTO!')


def somapar(num):
    pares = 0
    for n in num:
        if n % 2 == 0:
            pares += n
    print(f'Somando os valores pares da lista {num}, temos: {pares}')


# Programa Principal
numeros = list()
sorteia(numeros)
somapar(numeros)
