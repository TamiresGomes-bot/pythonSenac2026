"""
  Cap07 - Atividade 02
  Criar um Classe 

  Objetivos:
  Nesta atividade você vai criar uma objeto de classe, aprendendo sobre os metodos e propriedades e usar metodos especiais. Irá também aprender a consumir esta classe.

  Comandos utilizados:
  Classe, __init__, __str__, Propriedades e Metodos de uma classe
"""
from Cap07_atividade02_class import Recibo
from os import system, name
def limpartela():
 system('cls') if (name == 'nt') else system ('clear')

limpartela()
nome = input ('Informe o nome:  ')
dados = Recibo(nome)
v = float(input('Informe o valor: '))
d = input ('Informe a descrição: ')
dados.descricao(d) #sem a utilização de decoradores
dados.valor = v #com a utilização de decorador setter
limpartela()
  
print(dados)


