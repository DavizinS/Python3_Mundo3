"""
Desafio 092:
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os(com idade) em um dicionário se por acaso a CTPS
for diferente de ZERO, o dicionário receberá também o ano de contratação e o
salário. calcule e acrescente, além da idade, com quantos anos a pessoa vai se
"""
from datetime import date
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
trabalhador['nasc'] = int(input('Ano de Nascimento: '))
idade = date.today().year - trabalhador['nasc']
print(idade)
trabalhador['nasc'] = trabalhador['idade'] = idade
del trabalhador['nasc']
trabalhador['ctps'] = int(input('Qual sua CTPS(Caso não tenha digite 0): '))
if trabalhador['ctps'] != 0:
    trabalhador['Contratação'] = int(input('Qual o ano de contratação: '))
    trabalhador['salario'] = float(input('Qual o salário: R$ '))
    trabalhador['Aposentadoria'] = trabalhador['idade'] + ((trabalhador['Contratação'] + 35) - date.today().year)
print('*+' * 30)
print('{:^50}'.format('INFO CIDADÃO'))
print('*+' * 30)
for c, v in trabalhador.items():
    print(f'{c}: {v}')
print('*+' * 30)
