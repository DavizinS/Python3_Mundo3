"""
Desafio 83
"""
expr = str(input('Digite uma expressão: '))
pilha = []
for c in expr:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão VÁLIDA.')
else:
    print('Expressão INVÁLIDA.')
exp = str(input('Digite uma expressão: '))
pilha = []
for simb in exp:
    if simb == '(':  # Se tiver ( na expressao
        pilha.append('(')  # Vai adicionar ( na pilha
    elif simb == ')':  # Se tiver ) na expressao
        if len(pilha) > 0:  # Se a pilha tiver aberta ou seja com um (
            pilha.pop()  # Vai remover ultimo caractere, se tiver mais vai removendo um por um
        else:
            pilha.append(')')  # Se nao, coloca o ) na pilha
            break
if len(pilha) == 0:
    print('Expressão VÁLIDA.')
else:
    print('Expressão INVÁLIDA.')
