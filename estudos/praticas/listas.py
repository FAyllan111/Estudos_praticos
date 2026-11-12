"""
Tarefa 1 — Criação e acesso (fácil)
Crie uma lista com 5 nomes de frutas. Imprima:

* A lista inteira
* O primeiro item
* O último item (usando índice negativo)

"""
#codigo
lista = ['maça','pera','abacaxi','uva','melao']

print(lista)

print(lista[0])
print(lista[-1])
"""
Tarefa 2 — Fatiamento (fácil)
Dada a lista numeros = [10, 20, 30, 40, 50, 60, 70, 80], imprima:

* Os 3 primeiros
* Os 3 últimos (usando fatiamento, não índice)
* Do index 2 ao 5 (inclusive o 5)
* A lista invertida (usando [::-1])
"""
#codigo

numeros = [10, 20, 30, 40, 50, 60, 70, 80]

print(numeros[0:3])
print(numeros[-3:]) 
print(numeros[2:6])
print(numeros[:-1])
"""
Tarefa 3 — Métodos (médio)
Comece com carrinho = ["arroz", "feijão", "macarrão"]. Faça em sequência:

* Adicione "óleo" no final
* Remova "feijão"
* Adicione "sal" na posição 1 (entre arroz e macarrão)
* Imprima o carrinho depois de cada operação
* Imprima quantos itens tem no final
"""
#codigo
carrinho = ["arroz", "feijão", "macarrão"]
print(carrinho)
carrinho.append("óleo")
print(carrinho)
carrinho.remove("feijão")
print(carrinho)
carrinho.insert(1,"sal")
print(carrinho)
print(len(carrinho))

"""
Tarefa 4 — Iteração (médio)
Dada notas = [7.5, 8.0, 6.0, 9.5, 5.5], use enumerate para imprimir cada nota no formato:

text
Aluno 1: 7.5
Aluno 2: 8.0
...
* Comece em 1, não em 0.
"""
#codigo
notas = [7.5, 8.0, 6.0, 9.5, 5.5]

enumerate(notas,0)

for i, numeros in enumerate(notas,start=1):
    print(f"aluno {i}: nota {numeros}")
#travei
"""
Tarefa 5 — List comprehension (médio-avançado)
Dada gastos = [120, 45, 300, 89, 210, 15, 500], crie em uma única linha (list comprehension):

* Uma lista só com os gastos maiores que 100
* Uma lista com cada gasto multiplicado por 1.1 (10% de acréscimo)
"""
#codigo
gastos = [120, 45, 300, 89, 210, 15, 500]

maiores_100 = [gasto for gasto in gastos if gasto > 100]
com_acrescimo = [gasto * 1.1 for gasto in gastos]
#travei

"""
P1 — Simples. Crie uma lista vazia chamada tarefas. Adicione "estudar", "treinar", "ler". Remova "treinar". Imprima a lista final e o total de itens.

"""
#codigo
lista2= []
lista2.append("estudar")
lista2.append("treinar")
lista2.append("ler")

print(lista2)

lista2.pop(1)

print(lista2)

"""
P2 — Mediana. Dada precos = [45, 120, 89, 200, 15, 300, 78], crie em uma única linha (comprehension) uma lista só com os preços entre 50 e 200 (inclusive). Depois imprima quantos itens tem essa lista.
"""
#codigo
precos = [45, 120, 89, 200, 15, 300, 78]

precos_50_a_200 =[preco for preco in precos if preco > 50 and preco < 200]
print(len(precos_50_a_200))


"""
P3 — Avançada. Dada meses = ["jan", "fev", "mar", "abr"], use enumerate (começando em 1) para imprimir no formato:
Mês 1: jan
Mês 2: fev
...
"""
#codigo 

meses = ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"]

for i, meses in enumerate(meses,1):
    print(f"Mês {i}: {meses}")