produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
            'Estojo', 25,  'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila',
            120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('*=' * 20)
print('{:^38}'.format('LISTAGEM DE PREÇOS'))
print('*=' * 20)
for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<20}', end='')
    else:
        print(f'R$ {produtos[i]:>7.2f}')
