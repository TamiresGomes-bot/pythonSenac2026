from os import system, name
system('cls') if (name=='nt') else system('clear')

"""
  Cap04 - Atividade 02
  MultiTabuada

  Objetivos:
  Nesta atividade você vai construir uma multitabuada de duas maneiras, na primeira usando for e na segunda usando for aninhado

  Comandos utilizados:
   Comandos for range
"""

print('\n*** MULTI TABUADA 1 ***')
borda = ''
for i in range (1,11):
    print(f'{i*1:>4}|{i*2:>4}|{i*3:>4}|{i*4:>4}|{i*5:>4}|{i*6:>4}|{i*7:>4}|{i*8:>4}|{i*9:>4}|{i*10:>4}')
    print(borda.center(48,"-"))

print('\n*** MULTI TABUADA 2 ***')
for i in range(1,11):
    linha = f'| {i:>3} |'
    for ii in range (2,11):
        linha += f'{i*ii:>3} |'
    print (linha)
    print(borda.center(50,"-"))
        