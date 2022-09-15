#!/usr/bin/python
# coding: utf-8

def hello_world():
	print('Hello world')

def soma_dois_numeros(x, y):
	soma = x + y
	return soma

def divide_dois_numeros(x, y):
	divisao = x / y
	return divisao

def func_args(*args):
	print(args)
	for arg in args:
		print(arg)

def func_args_2(a, b, *variaveis):
	print(a)
	print(b)
	print(variaveis)

def func_kwargs(**kwargs): # any variable name, but ** is compulsory to pass dictionary as argument
	print(kwargs)

# 3.1 - Python - Introdução a funções
# 3.2 - Python - Escopo de funções
# a=hello_world()
b=soma_dois_numeros(3,2)
# print b

# 3.3 - Python - Funções anônimas (lambda functions)
# lambda
anonima = lambda x: x + 2
anonima_2 = lambda x, y: x + y 

#print(anonima(10))
#print(anonima_2(10,10))

# 3.4 - Python - *args e **kwargs
# 3.5 - Python - Parâmetros posicionais, nomeados, explicitamente nomeados e mais *args e **kwargs
#func_args(5, 3, 2, 10)
#func_args_2(5, 3, 2, 10)
#func_args(b=5, a=3, 2, 10)
#print(divide_dois_numeros(10,5))
#print(divide_dois_numeros(y=5,x=20))

dic = {'one': 1, 'two': 2}
func_kwargs(**dic)
