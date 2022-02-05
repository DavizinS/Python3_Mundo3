""""
Exercício Python 080:
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""
num = []
for c in range(0, 5):
    n = int(input(f'Digite um valor: '))
    if c == 0 or n > num[-1]:  # Se for o primeiro valor, ou se n for maior que o primeiro valor.. Será o maior na lista
        num.append(n)
        print('Foi adicionado no final da lista')
    else:
        pos = 0  # Pegar a posição.
        while pos < len(num):  # Repita enquanto pos chegar no tamanho da lista
            if n <= num[pos]:  # Se n for menor que o n da posição
                num.insert(pos, n)  # o n novo irá pra lista.
                print(f'Foi adicionado na posição {pos}')
                break
            pos += 1
print(num)
# Fiz depois que aprendi..
num = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > num[-1]:
        num.append(n)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(num):
            if n <= num[posicao]:
                num.insert(posicao, n)
                print(f'Adicionado a posição {posicao} da lista...')
                break
            posicao += 1
print(num)
