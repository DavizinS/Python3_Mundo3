"""
Exercício Python 079:
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
valores = []
cont = 0
while True:
    n = int(input(f'Digite o valor da posição {cont}:  '))
    if n not in valores:
        valores.append(n)
    else:
        print('Valor duplicado, não irei adicionar...')
        n = int(input(f'Tente novamente. Digite o valor da posição {cont}: '))
    cont += 1
    resp = str(input('Deseja continuar [S/N]? ')).strip()
    if resp not in 'Ss':
        break
print(f'Os valores foram: {sorted(valores)}')