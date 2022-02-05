"""
Exercício Python 086:
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Lista com 3 Listas dentros e 3 valores...

for L in range(0, 3):  # Repetição da linha
    for c in range(0, 3):  # Repetição da coluna
        matriz[L][c] = int(input(f'Digite o valor da posição {L},{c}: '))
print('*-' * 20)
for L in range(0, 3):  # Repetição para mostrar, linhas e colunas
    for c in range(0, 3):
        print(f'[{matriz[L][c]:^5}]', end='')  # Aqui mostra as lihas e as colunas
    print()
