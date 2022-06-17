#!/usr/bin/env python
# coding: utf-8

# ## Desafio 1

# In[94]:


#determinar oq é o valor na variavel
number = 'asdf'


# In[80]:


if type(number)  is str:
    print('not a number')
elif number > 0:
    print('positivo')
elif number<0:
      print('negativo')
elif number == 0:
    print('0')
else:
    print('not a number')


# ## Desafio 2

# In[84]:


#intercalar valores da lista
valores = ['a','b','c','d','f']
numeros = [1,2,3,4,5]
intercalado = []

for i in range(5):
    intercalado.append(valores[i])
    intercalado.append(numeros[i])
intercalado


# ## Desafio 3

# In[92]:


# fazer o fatorial 
fatorial = int(input('digite o numero: '))
n = 1
valor = 1
while n <= fatorial:
    valor *= n
    n += 1


# In[93]:


valor


# # teste

# In[28]:


# numeros primos lista
# numeros primos são divididos por 1 por ele mesmo apenas
list = []
condicao = 0
for i in range(2,50):
    
    for j in range (2,i-1):
        if (i-1)%j == 0:
            condicao +=1
        
    if condicao == 0:
        list.append(i-1)
        
    condicao = 0
list


# In[50]:


#permutação do nome digitado
# ta funcionando mas não no jupiter
from itertools import permutations
import string
palavra = input('digite a palavra: ')
p = permutations(palavra)
list2 = []
for i in list(p):
    if i not in list2:
        list2.append(i)
list2


# In[10]:


lista = ['P','A','Y','A','T','A','H','O','N']
count = 0
for i in lista:
    if i == 'A':
        count+=1
    if count > 1 and i == 'A':
        lista.remove(i)
lista


# In[12]:


lista = []
for i in range(52):
    if i%2 !=0:
        lista.append(i)


# In[2]:


fx = lambda x:x*2+1

list(fx(x) for x in range(26))


# In[5]:


valores = [1,2,3,4,5]
chaves = ['a','b','c','d','e']
dict = {}
for i in range(5):
    dict[valores[i]] = chaves[i]
dict


# In[47]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'notebook')


# # Desafio Udemy 1

# In[42]:


# realizando o plot da circunferencia
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
a = 100
b = 100
r = 100
x = [i for i in range(2*r+1)]
y = []
func_y = lambda x:sqrt(((r**2) - (x-a)**2)) + b
func_y_neg = lambda x:-sqrt(((r**2) - (x-a)**2)) + b

y.extend(list(map(func_y,x)))
y.extend(list(map(func_y_neg,x)))
x.extend(x)
plt.plot(x,y)


# # o segundo desafio foi realizado no colab por problemas de import
# 

# In[70]:


data = pd.read_csv('/content/gdrive/MyDrive/Untitled folder/100.txt')


# In[ ]:


separate = data.Estado.value_counts()
a = separate[0]
print('A quantidade de Municípios no Estado de São Paulo é',a)


# In[ ]:


FRAME_SP = data[(data.Estado == 'SP')]
soma_part = FRAME_SP['Participação (%)'].sum()
print('A participação acumulada do Estado de SP é',soma_part,'%')


# # Exercicio 

# # 1

# In[63]:


def divide(frase):
    lista = frase.split(' ')
    return len(lista)

frase = input('digite a frase: ')
print(divide(frase))


# # 2

# In[80]:


def palavras_in_txt(arquivo):
    with open (arquivo_path) as f:
        string = f.read()
        f.close

    limpa = string.replace('\n','')
    separa =limpa.split(' ')
    return len(separa)
    


# In[82]:


arquivo_path = 'C:/Users/pedro/OneDrive/Documentos/100.txt'
numero  = palavras_in_txt(arquivo_path)
numero


# # 3

# In[86]:


def IMC(peso,altura):
    return peso/(altura**2)

print(IMC(float(input('diga o peso: ')),float(input('diga a altura: '))))


# # Desafio matlab 3D

# In[45]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')


# In[42]:


arquivo_path = 'C:/Users/pedro/OneDrive/Documentos/100.txt'
with open (arquivo_path) as f:
    string = f.readlines()
    f.close
lista = []
for i in range(len(string)):
    lista.append(string[i].split(','))

coordenadas = {'X':[],'Y':[],'Z':[]}
lista
for j in range(len(lista)):
    coordenadas['X'].append(lista[j][3])
    coordenadas['Y'].append(lista[j][4])
    coordenadas['Z'].append(lista[j][5])
    
x = coordenadas['X']
y = coordenadas['Y']
z = coordenadas['Z']


# In[63]:


ax.plot3D(coordenadas['X'],coordenadas['Y'],coordenadas['Z'])

