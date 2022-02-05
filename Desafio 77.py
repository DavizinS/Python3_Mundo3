palavras = ('Estou', 'Aprendendo', 'Python', 'Gustavo', 'Guanabara',
            'Curso', 'Muito', 'Bom', 'Recomendo', 'Cafe', 'Notebook',
            'Trabalho', 'Sacola')
for p in palavras:
    print(f'\nNa palavra {p.upper()}, temos ', end='')
    for letra in p:  # Criar uma variavel e repetição na var P, que está baseada em PALAVRAS
        if letra in 'AaEeIiOoUu':  # Se letra tiver as vogais
            print(f'{letra} ', end='')  # Escreva
