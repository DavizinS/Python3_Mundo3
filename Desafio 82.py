"""
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso,
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""
lista = []
pares = []
impares = []
while True:
    num = lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
"""
Sistema de repetição para analisar os números da lista para verem se é PAR ou IMPAR..
Usando For enumare, estrutura do Para... (I - Enumerate, V - é o valor da lista). 
for i, v in enumerate(lista):
    if i % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)"""
"""
Sitema de repetição para analisar os numeros da lista e verem se são PAR OU IMPAR...
Usando While, estrutura do Enquanto..
cont = 0
while cont < len(lista):
    if lista[cont] % 2 == 0:
        pares.append(lista[cont])
    else:
        impares.append(lista[cont])
    cont += 1"""
for cont in range(0, len(lista)):
    if lista[cont] % 2 == 0:
        pares.append(lista[cont])
    else:
        impares.append(lista[cont])
print(f'A lista criada: {lista}')
print(f'A lista de par: {pares}')
print(f'A lista de impares: {impares}')
