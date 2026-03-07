"""
  Cap07 - Atividade 01
  Criar um Classe 

  Objetivos:
  Nesta atividade você vai criar um objeto de classe, aprendendo sobre os metodos e 
  propriedades e como consumir esta classe.

  Comandos utilizados:
  Classe, Propriedades e Metodos de uma classe
"""

from Cap07.Calculadora.Cap07_atividade01_classe import Calculadora
valor01 = int(input('Informe o 1° valor: '))
valor02 = int (input('Informe o 2° valor: '))
calc = Calculadora(valor01,valor02)
print(f'Soma:{calc.soma()}')
print(f'Subtração:{calc.sub()}')
print(f'Multiplicação:{calc.mult()}')
print(f'Divisão:{calc.div()}')