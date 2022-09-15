#!/usr/bin/python
# coding: utf-8
def tuplaHelp():
	print 'Tuplas sao imutaveis:'
	tupla = (1, 2, 3, 4, 5) 
	print(type(tupla),tupla)
	tupla_2 = tuple([1, 2, 3, 4, 5])
	print(type(tupla_2),tupla_2)

def desempacotar():
	pacientes = [
             ('Alberto', 'Da Silva', 'M', (-23.5187, -43.5156)),
             ('Bernardo', 'Silva', 'M', (-20.5124, -39.3151)),
             ('Carla', 'Sousa', 'F', (-26.1234, -41.2121)),
             ('Darla', 'de Souza', 'F', (-29.2121, -29.2142))
             ]
	print('{:^25} | {:^10} | {:^10}'.format('Nome e sobrenome', 'Latitude', 'Longitude'))
	for nome, sobrenome, sexo, (latitude, longitude) in pacientes:
		print('{:<12} {:<12} | {:^10} | {:^10}'.format(nome, sobrenome, latitude, longitude))

def listaHelp():
	lista = [1, 2, 3, [1, 2, 3], (1, 2, 3), {'one': 1, 'two': 2}, 'ABEV3', lambda x: x + 2, range(10)]
	print('-' * 80)
	print(id(lista),lista,lista.count(10))
	for item in lista: 
		print(type(item),item)

	lista.append(6)  # Adiciona um elemento à última posição da lista
	lista.extend([7, 8, 9, 10]) # extende a lista a partir da ultima posicao com o argumento
	lista.insert(2, (2,0)) # insere no indice (primeiro argumento)
	lista.pop(0) #se nenhum argumento for passado, pop ultimo elemento
	lista.reverse()
#	lista.sort()
#	iteravel[inicio:fim:intervalo] # slicing: inicio <= i < fim; lista, tupla e string

	print('-' * 80)
	print(id(lista),lista,lista.count(10))
	for item in lista: 
		print(type(item),item)

	print('-' * 80)
#	lista2=lista.copy()  # Cria uma cópia rasa da lista; does not work both in python 2.x and python 3.x
	lista2=lista[:]
	print(id(lista),id(lista2),lista is lista2)

def moreTuplas():
	minha_tupla = (1, 2, 3, [1, 2, 3])
	print(id(minha_tupla),minha_tupla)
	minha_tupla[3].append('novo')
	print(id(minha_tupla[0]),id(minha_tupla[3][0]),minha_tupla)

def hashHelp():
#dic = {key: value}
#lists are not hashable, so cannot be used as key
	print('-' * 80)
	dict = {'John Smith': '521-1234', 'Lisa Smith': '521-8976', 'Sandra Dee': '521-9655'}
	for key,value in dict.items():
#		print(f'key: {key} = {hash(key)} value = {value}')
		print(hash(key),{key},{value})

def setHelp():
	myList = [1, 1, 1, 2, 2, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9, 9, 9] 
	mySet = set(myList)
	print('-' * 80)
	print(type(myList),myList)
# no repetitions in set, each set element has its hash; I cannot have lists inside sets
	print(type(mySet),mySet)
	mySet.pop()
	mySet2 = set(mySet)
	mySet2.remove(9)
	mySet2.add(90)
	print(type(mySet2),mySet2)
	mySet2.clear()
	print(type(mySet2),mySet2)
	myFrozenSet = frozenset(mySet)
	print(type(myFrozenSet),myFrozenSet)

def dictHelp():
	print('-' * 80)
	a = dict(one=1, two=2, three=3) # atribution
	b = {'one': 1, 'two': 2, 'three': 3} # conventional form
	c = dict(zip(['one', 'two', 'three'], [1, 2, 3])) # using zip function
	d = dict([('three', 3), ('one', 1), ('two', 2)]) # from tuples
	print(a == b == c == d) # order in dictionary doesn't mind
	for key, value in a.items(): 
            print(type(key),key,type(value),value)

# print 'Python Data Structs: contêineres básicos da linguagem temos: tuplas, listas, dicionários, conjuntos e conjuntos congelados.'

# 2.1 - Python - Tuplas
#tuplaHelp()
#desempacotar()

# 2.2 - Python - Listas
# 2.3 - Python - Slicing (fatiamento de sequências)
# listaHelp()

# 2.4 - Python - Aprofundando em listas e tuplas
# tuplas sao mais rapidas que listas
#moreTuplas()

# 2.5 - Python - Hashables, hash table e introdução a dicionários
#hashHelp()

# 2.6 - Python - Conjuntos (sets)
#setHelp()

# 2.7 - Python - Dicionários
dictHelp()

print('-' * 80)


