"""
Desafio 105:

Faça um programa que tenha uma função chamada notas() que pode receber várias notas de aluno
e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação Opcional

adicione também as docstrings da função.
"""


def notas(* pontos, sit=False):
    """
    => Função feita para analisar a nota dos alunos, media e situação da turma.
    :param pontos: Uma ou mais notas de alunos da turma(Pode colocar quantas notas quiserem!)
    :param sit: situação a partir da média da turma! Essa é opcional.
    :return: dicionário com várias informações sobre a turma.
    """
    doc = dict()
    mai = men = soma = cont = 0
    doc['total'] = len(pontos)
    for c in pontos:
        if cont == 0:
            men = c
        else:
            if c < men:
                men = c
        if c > mai:
            mai = c
        cont += 1
        soma += c
    doc['maior'] = mai
    doc['menor'] = men
    doc['media'] = soma / len(pontos)
    if sit:
        if doc['media'] < 4:
            doc['situação'] = 'RUIM'
        elif 3 < doc['media'] <= 6:
            doc['situação'] = 'RAZOAVEL'
        elif 6 > doc['media'] <= 8:
            doc['situação'] = 'BOA'
        else:
            doc['situação'] = 'MUITO BOA'
    return doc


resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)
help(notas)
