"""
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final,
mostre um boletim contendo a média de cada um
 e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
alunos = []
dados = []
while True:
    dados.append(str(input('Nome: ')))
    n1 = dados.append(float(input('Nota 1: ')))
    n2 = dados.append(float(input('Nota 2: ')))
    alunos.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar[S/N]? '))
    if resp in 'Nn':
        break
print('-=' * 30)
print('{:^50}'.format('BOLETIM ESCOLAR'))
print('-=' * 30)
print('N°|  NOME|    MEDIA')
for i, v in enumerate(alunos):
    print(f'{i:<4} {v[0]} {(v[1] + v[2]) / 2 :^15.2f}')
while True:
    print('*=' * 30)
    resp2 = int(input('Mostrar nota de qual aluno? (999 para finalizar): '))
    if resp2 == 999:
        print('Finalizando...')
        break
    if resp2 <= len(alunos) - 1:
        print(f'Notas de {alunos[resp2][0]}: {alunos[resp2][1]} e {alunos[resp2][2]}')
