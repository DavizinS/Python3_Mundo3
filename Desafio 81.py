"""
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar...[S/N]? '))
    if resp not in 'Ss':
        break
print(f'Foram digitados {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente é {lista}')
if 5 in lista:
    print('Foi encontrado o valor 5 na lista.')
else:
    print('Não foi encontrado o valor 5 na lista.')
