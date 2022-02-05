"""
Desafio 094:
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
os dados de cada pesoa em um dicionáro e todos os dicionários em uma lista.
No final mostre,
A) Quantas pessoas foram cadastradas (OK)
B) A média de idade do grupo (OK)
C) Uma lista com todas as mulheres (OK)
D) Uma lista com todas as pessoas com idade acima da média. (OK)
"""
pessoas = dict()
dados = list()
totidade = 0
media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: ')).title().strip()
    while True:
        pessoas['sexo'] = str(input('Sexo[M/F]: ')).upper().strip()[0]
        if pessoas['sexo'] in 'FfMm':
            break
        else:
            print('ERRO! Por favor responda com M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    dados.append(pessoas.copy())
    resp = str(input('Quer continuar[S/N]? ')).strip()
    while resp not in 'SsNn':
        resp = str(input('ERRO! Responda com S ou N! Quer continuar[S/N]? ')).strip()
    if resp in 'Nn':
        break
cont = 0
for v in dados:
    totidade += (v['idade'])
    cont += 1
media = totidade / cont
print('*-' * 30)
print(f'Total de pessoas cadastradas: {len(dados)}')
print(f'A média de idade do grupo é de: {media:5.2f} anos')
print('*-' * 30)
print('Lista de mulheres:')
for v in dados:
    if v['sexo'] in 'Ff':
        print(f'{v["nome"]}')
print('*-' * 30)
print('Lista das pessoas acima da média de idade: ')
for v in dados:
    if v['idade'] >= media:
        print(f'{v["nome"]}, sexo: [{v["sexo"]}], com {v["idade"]} anos.')
