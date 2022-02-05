"""
Exercício Python 078:
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
num = list()
maior = 0
menor = 0
for cont in range(0, 5):  # Loop de 5x para digitar os valores.
    num.append(int(input(f'Digite um valor na posição {cont}: ')))  # Aqui vai adicionar os valores, 5x.
    if cont == 0:  # Se for o primeiro valor
        menor = maior = num[cont]   # Oprimeirovalorvaireceber o menor valor(Apenas para comparar com os outros depois)
    else:  # Senao
        if num[cont] < menor:  # Se o valor for menor ou igual que o menor valor informado
            menor = num[cont]  # Então o valor seguinte recebe o menor valor.
        if num[cont] > maior:  # Se num for maior ou igual que o maior numero declarado..
            maior = num[cont]  # Então o maior valor passa pro valor informado.
print('*-' * 20)
print(f'Você digitou os valores {num}')
print(f'O maior valor informado foi {maior}, na posição: ', end='')
for c, v in enumerate(num):
    if v == maior:
        print(f'{c}...', end='')
print()
print(f'O menor valor informado foi {menor}, na posição: ', end='')
for c, v in enumerate(num):  # Explicação, foi criada duas var, 'C e V' enumemrate recebe C, e a lista recebe V
    if v == menor:
        print(f'{c}...', end='')
