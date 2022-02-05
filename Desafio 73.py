"""
Exercício Python 73:
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
"""
tabela = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Bragantino',
          'Corinthians', 'Fortaleza', 'Internacional', 'Fluminense',
          'América-MG', 'Ceará', 'Santos', 'Cuiabá', 'Athletico-PR', 'São Paulo',
          'Juventude', 'Atlético-GO', 'Bahia', 'Sport Recife', 'Grêmio', 'Chapecoense')
times = sorted(tabela)
chapeco = tabela.index('Chapecoense')+1
print('Classificação Seria A - Brasileirão\n')
print('{:~^20}'.format(''))  # Jeito diferente de manipulação de string
cont = 1
for c in tabela:  # Primeiro Jeito de mostrar as tuplas
    print(f'{cont}° {c}')
    cont += 1
print('\nOs 5 Primeiros Times.')
print('~' * 20)
for c in range(0, 5):  # Segundo jeito
    print(f'{c+1}° {tabela[c]}')
print('~' * 20)
print('\nOs Últimos 4 colocados.\n')
for c in range(16, 20):
    print(f'{c+1}° {tabela[c]}')
print('\nTimes em Ordem Alfabética.\n')
for c in range(0, 20):
    print(f'> {times[c]}')
print('\nChapecoense está na posição: ', end='')
print(f'{chapeco}°')
