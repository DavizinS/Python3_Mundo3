"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário
Incluindo o total de gols feitos durante o campeonato.
"""
jogador = dict()
pgols = dict()
gols = 0
lgol = list()
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(1, partidas+1):
    rgol = int(input(f'     Total de gols na {p}° Partida: '))
    lgol.append(rgol)
gols = sum(lgol)
jogador['gols'] = lgol
jogador['total'] = gols
print('*-' * 30)
print(jogador)
print('*-' * 30)
for c, v in jogador.items():
    print(f'O campo {c} tem valor {v}')
print('*-' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'==> Na {c+1}° partida, fez {jogador["gols"][c]}')
print(f'Foi um total de {gols} gols')
