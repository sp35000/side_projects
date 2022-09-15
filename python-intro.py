#!/usr/bin/env python
# coding: utf-8

# ## Python: Conhecendo a Linguagem
# 
# 

# # O que é Programação?

# ## O que é um programa de computador?
# ## O que é um algoritmo?

# # Um pouco mais Sobre o Python

# ## O que programar? (aplicações)
# ## Aonde programar? (ambientes)
# ## Como instalar o interpretador? 

# # A linguagem ("Hello World")

# In[1]:


print("Hello World")


# #Tipos de Dados básicos

# In[2]:


print(type(2)) # O tipo do número 2 é int (número inteiro)
print(type(2.5)) # O tipo do número 2.5 é float (número decimal)
print(type(1+1j)) # O tipo do número 1 + 1j (j é o número imaginário) é complex
print(type("O termo 'termo' esta entre aspas\n")) # Sequencia de caracteres para armazenar texto
print(type(False)) # tipo booleano para Verdadeiro (True) e Falso (False)


# ## Variáveis
# 
# Uma variável não pode ter o nome comçado por números, evitem palavras-chave da linaguagem e caracateres especiais

# In[5]:


altura_do_guilherme = 1.90 # nome_da_variavel = valor
texto = "Hello world"
chovendo = True


# In[6]:


print(altura_do_guilherme, texto, chovendo)


# ## Operações básicas (e nem tão básicas)

# ### Com dados numéricos

# In[7]:


print(2.5+5j + 1) # o '+' é a soma usual
print(10 - 1) # o '-' é a subtração usual
print(2 * -2.5) # o '*' é a multiplicação usual
print(10 / 3) # o '/' é a divisão usual

print(4 ** -0.5) # o '**' é a potenciação
print(10 // 4 ) # o '//' é o quociente da divisão inteira
print(10 % 4) # o '%' é o resto da divisão inteiro


# ### Com dados texto

# In[8]:


anos = input("Digite sua idade: ")
frase = "Ola eu sou Guilherme e tenho " + anos  + " anos" # o '+' é a concatenação de strings
print(frase)
print("repete " * 2) # o '*' repete a string x vezes onde x é um número inteiro


# In[9]:


("oi " + "tudo bem ") * 4


# In[10]:


5 + "5" # não funciona


# ### Com booleanos

# In[11]:


False +  False# converte o True para 1 e o False para 0 e faz numericamente


# In[12]:


True + 4 


# In[13]:


# conversão de tipos de Dados

string = "34.5"
numero = float(string)
numero + 10


# In[14]:


a= 10
str(a)


# In[15]:


### Escreva uma sequência de operações em python que converta um valor em real para dólar
valor_em_real = float(input("Digite o valor em reais: "))
valor_em_dolar = valor_em_real / 5.62
saida = f'O valor é $ {valor_em_dolar:.2f} dolar'
print(saida) 
## Escreva uma sequência de operações em python que converta um valor em dólar para real


# In[16]:


## Exercicio Conversão de Celsius para Farenheit

##  C * 9/5  + 32 = F 


# In[21]:


#Marco
temperatura_Celsius = float(input("Digite a temperatura atual em Celsius: "))
temperatura_em_F = temperatura_Celsius * 9 / 5 + 32
saida = f'A temperatura em F é {temperatura_em_F:.2f} Farenheit'
print(saida) 


# In[27]:


valor_em_celsius = float(input("Digite o valor em Celsius: "))
valor_em_farenheit = valor_em_celsius * 9/5 + 32
saida = f'O valor é {valor_em_farenheit:.2f} ºF'
print(saida) 


# # Desvios condicionais

# if condicao:
#   codigo para executar quando a consiçãão for verdadeira
#   mais codigo
#   mais codigo
# outros códigos que não dependem da condição

# In[28]:


print('executa antes do if')
if True:
  print('Era verdadeira')
  print('Outro Texto dentro do if')
print('Imprimo independente do if')


# In[29]:


# Operadores de Comparação 

print("3 == 2:", 3 == 2) # '==' representa igualdade 
print('"texto" == "texto":', "texto" == "texto")
print('"2.34" == 2.34:', "2.34" == 2.34)
variavel = '5.78'
print("variavel == 5.78:", variavel == '5.78')

print("2 > 3:", 2 > 3) # '>' verifica se o número a esquerda do símbolo é maior que o da direita
print("2 > 2:", 2 > 2)
print("2 < 3:", 2 < 3) # '<' verifica se o número a esquerda do símbolo é menor que o da direita
print("2 < 2:", 2 < 2)

print("2 >= 3:", 2 >= 3) # '>=' verifica se o número a esquerda do símbolo é maior ou igual que o da direita
print("2 >= 2:", 2 >= 2)
print("2 <= 3:", 2 <= 3) # '<=' verifica se o número a esquerda do símbolo é menor ou igual que o da direita
print("2 <= 2:", 2 <= 2)

print("3 != 2:", 3 != 2) # '!=' verifica se os números são diferentes 
print("2 != 2:", 2 != 2) # '!=' verifica se os números são diferentes 


# In[ ]:


# a*x² + b*x + c = 0

# x² - x + 1 = 0 -> delta = -3 < 0
# x² +2x + 1 = 0 -> delta = 0
# x^2 - 4x = 0 - > delta = 16 > 0

# le os dados de entrada
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("digite o valor de c: "))


print(f"O problema que você quer resolver é: {a}x² + {b}x + {c} = 0")
# Calcula o Delta

delta = b * b - 4 * a * c
print(f"Delta é igual a: {delta:.3f}")

if delta > 0:
  x1 = (-b + delta ** 0.5)/(2 * a)
  x2 = (-b - delta ** 0.5)/(2 * a)
  print(f"O problema tem 2 soluções: {x1:.3f} e {x2:.3f}")

elif delta < 0:
  print("O problema não tem soluções reais")

else:
  x = (-b + delta ** 0.5)/(2 * a)
  print(f"O problema possui apenas uma solução: {x}")


# In[ ]:


##  Carro flex 

## se o valor etanol dor maior que 70% do valor do valor gasolina -> gasolina
## se o valor do etanol for menor ou igual a 70% do valor gasolina -> etanol


#gasolina, etanol = 4, 1 # etanol
#gasolina, etanol = 4, 3 # gasolina
#gasolina, etanol = 10, 7 # etanol
#gasolina, etanol = 10, 7.0000000001

gasolina = float(input("Informe o vlor da gasoolina: "))
etanol = float(input("Informe o valor do etanol: "))
coeficiente = etanol/ gasolina
if coeficiente > 0.7:
  print("Gasolina")
else:
  print("Etanol")


# ### Exercicio
# dada a tabela o IR, faça um programa que recebe o salário de um trabalhador e devolve o valor do imposto.
# 
# |Base de cálculo (R$)	|Alíquota (%)|
# --------------------- |-------------|
# |Abaixo de 1.903,99    | 0%  |
# |De 1.903,99 até 2.826,65|	7,5%	|
# |De 2.826,66 até 3.751,05|	15%	|
# |De 3.751,06 até 4.664,68|	22,5%	|
# |Acima de 4.664,68|	27,5%|

# In[ ]:


# Solução
salario = float(input("Digite seu salário mensal: "))
if salario < 1903.99:
  valor = 0
elif salario <= 2826.65:
  valor = salario * 0.075 
elif salario <= 3751.05:
  valor = salario * 0.15
elif salario <= 4664.68:
  valor = salario * 0.225
else:
  valor = salario * 0.275 
print(f"O valor a ser pago de IR é R${valor:.2f}")


# # Laços de repetição

# ## While (enquanto)

# while condição:
#   executa código para a condição verdadeira

# In[ ]:


numero = 1

while numero != 0:
  numero = int(input("Digite um número: "))
  print("voce digitou o numero", numero)
print('terminou')


# In[ ]:


numero = 0

while numero <= 10:
  print(numero, end=" ")
  numero = numero + 1


# In[ ]:


base = 2
expoente = 3

resultado = 1
while expoente > 0:
  resultado = resultado * base
  expoente = expoente - 1

print(resultado)


# In[30]:


## Le números o usuário até ele digitar o numero -1
## calcula a média dos números digitados


# ## For (para cada)

# In[31]:


teto = 0
for i in [5 , "texto", 2 , -1, 4.56, True]:
  if type(i) == int:
    a = i + 1
  print("a variável i vale:", i)
print(i)
print(a)


# # Coleções de dados

# ### Listas

# In[ ]:





# ## Dicionários

# In[ ]:





# ## Tuplas

# In[ ]:





# ## Muitas outras coleções!

# # Funções

# 
