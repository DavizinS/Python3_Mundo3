"""
Desafio 090:
Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
(Se a média for > 7 = APROVADO)
(Se for menos, REPROVADO.
"""
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Media: '))
if aluno['media'] > 7:
    print('Situação: \033[1;32mAPROVADO!\033[m')
elif 5 <= aluno['media'] < 7:
    print('Situação: \033[1;33mRECUPERAÇÃO\033[m')
else:
    print('Situação: \033[1;31mREPROVADO!\033[m')
for k, v in aluno.items():
    print(f'{k.title()}: {v}')
