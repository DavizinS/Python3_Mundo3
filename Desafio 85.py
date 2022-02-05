"""
Exercício Python 085:
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""
numeros = []
p = []
i = []
for n in range(1, 8):
    numeros.append(int(input(f'Digite o {n}° número: ')))
    if numeros[0] == 0:
        print('\033[1;31m0 é NEUTRO, portanto será excluído da lista.\033[m')
        numeros.pop()
    else:
        if numeros[0] % 2 == 0:
            p.append(numeros[0])
            print('Adicionado para seção PAR.')
        elif numeros[0] % 2 == 1:
            i.append(numeros[0])
            print('Adicionado para seção IMPAR.')
    numeros.clear()
numeros.append(p)
numeros.append(i)
numeros.sort()
print('*=' * 30)
print('A lista de pares são: ', end='')
for c in numeros:
    if c[0] % 2 == 0:
        print(f'{sorted(c)}')
print('\nA lista de impares são: ', end='')
for c in numeros:
    if c[0] % 2 == 1:
        print(f'{sorted(c)}')

# Exercicio feito por Gustavo Guanabara Abaixo \/
num = [[], []]
valor = 0
for n in range(1, 7):
    valor = int(input(f'Digite o {n}° número: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('*=' * 30)
print(f'Os números pares digitados foram: {sorted(num[0])}')
print(f'Os números impares digitados foram: {sorted(num[1])}')
