"""
Desafio 095:
Aprimore o desafio 093 para que ele funcione com vários jogadores
incluindo um sistema de visualização de detalhe do aproveitamento de cada
jogador.
"""
jogadores = list()
jogador = dict()
listagol = list()
gols = 0
while True:
    jogador.clear()
    listagol.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    for gp in range(0, jogador['partidas']):
        listagol.append(int(input(f'{gp+1}° Partida, quantos gols? ')))
    jogador['gols'] = listagol[:]
    jogador['total'] = sum(listagol)
    jogadores.append(jogador.copy())
    resp = str(input('Quer continuar[S/N]? '))
    while resp not in 'SsNn':
        print('ERRO. TENTE NOVAMENTE, RESPONDA COM S OU N!')
        resp = str(input('Quer continuar[S/N]? '))
    if resp in 'Nn':
        print('\033[1;32mVocê concluiu os cadastro de jogadores...\033[m')
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(jogadores):
    print(f'{k:<3}', end='')
    for d in v.values():
          print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:
    escolha = int(input('Mostrar o resultado de qual jogador? (999 para parar):'))
    if escolha == 999:
        print('\033[1;31mVocê SAIU...\033[m')
        break
    if escolha >= len(jogadores):
        print(f'Não existe jogador com esse código {escolha}')
    else:
        print(f'== Levantamento do Jogador, {jogadores[escolha]["nome"]}')
        for cont in range(0, jogadores[escolha]["partidas"]):
            print(f'Na {cont+1}° partida: Fez {jogadores[escolha]["gols"][cont]} gol(s)')
print('<<< FIM >>>')
