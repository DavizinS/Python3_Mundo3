"""
Desafio 099:

Faça um programa que tenha uma função chamada maior(), que receba vários parametros com
valores inteiros

Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep


def maior(* numeros):
    cont = mai = 0
    print('\nAnalisando os valores passados...')
    for v in numeros:
        print(f'{v} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            mai = v
        else:
            if v > mai:
                mai = v
        cont += 1
    print(f'Foram informado {cont} valores.')
    print(f'O maior valor foi {mai}.')


maior(1, 3, 5, 2, 0)
maior(3, 4, 8, 11)
maior(1, 2)
maior(6)
maior()
