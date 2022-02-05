"""
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = soma3 = mai2 = 0
for lin in range(0, 3):
    for c in range(0, 3):
        matriz[lin][c] = int(input(f'Informe o valor da posição {lin},{c}: '))
        if c == 0:
            mai2 = matriz[1][c]
        if matriz[lin][c] % 2 == 0:  # Se a matriz da linha for divisivel por 2
            somapar += matriz[lin][c]
        if matriz[lin][2]:  # Se matriz da coluna 3 então irá somar...
            soma3 += matriz[lin][2]
        if matriz[1][c] > mai2:  # Se matriz da linha 2 vai mostrar o maior valor...
            mai2 = matriz[1][lin]
for lin in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[lin][c]:^5}]', end='')
    print()
print(f'\nA soma dos valores PARES da Matriz é igual a: {somapar}')
print(f'A soma dos valores da 3° Coluna é igual a: {soma3}')
print(f'O maior valor da Segunda Linha é: {mai2}')
