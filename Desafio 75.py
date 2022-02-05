valores = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'Você digitou os valores: {valores}', end='')
print(f'\nO valor 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O valor 3 está na posição {valores.index(3)+1}°.')
else:
    print('Nenhum valor 3 foi digitado.')
print(f'Os valores pares digitados foram: ', end='')
for c in valores:
    if c % 2 == 0:
        print(f'{c} ', end='')
