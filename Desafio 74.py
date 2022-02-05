from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10))
print('Os números sorteados são: ', end='')
for c in numeros:
    print(f'{c} ', end='')
print(f'\nO menor número sorteado foi: {min(numeros)}')
print(f'O maior número sorteado foi: {max(numeros)}')
