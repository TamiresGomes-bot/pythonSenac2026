from os import system, name
system('cls') if (name=='nt') else system('clear')

"""
  Cap04 - Atividade 01
  Tabuada

  Objetivos:
  Nesta atividade você vai montar uma Tabuada usando a estrutura de Loop do For e range.

  Comandos utilizados:
  Comandos for e range
"""
print('****** Tabuada Simples ******')

numero = int(input ('Informe o multiplicador: '))
for i in range(1,11):
    print(f'{numero} x {i} = {numero * i } ')
print("----------------------------")

