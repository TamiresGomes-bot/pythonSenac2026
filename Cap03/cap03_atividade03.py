
from os import system, name
system('cls') if (name=='nt') else system('clear')

"""
  Cap03 - Atividade Extra
  Calcular IMC

  Objetivos:
  Nesta atividade você vai calcular o IMC a partir de um peso e uma 
  altura, usará a comando if para mostrar o resultado do calculo do IMC.
    Ex: IMC = 70 kg / (1,60 m x 1,60 m) = 70 kg / 2,56 m² = 27,3 
        IMC <18,5kg/m2 - baixo peso
        IMC >18,5 até 24,9kg/m2 - eutrofia (peso adequado)
        IMC ≥25 até 29,9kg/m2 - sobrepeso
        IMC >30,0kg/m2 até 34,9kg/m2 - obesidade grau 1
        IMC >35kg/m2 até 39,9kg/m2 - obesidade grau 2
        IMC > 40kg/m2 - obesidade extrema
  Comandos utilizados:
  Variáveis, if / elif / else
"""


print('*******CALCULADO DE IMC*****')

alturaCm = float(input ('Informe sua altura em cm: '))
peso = float(input('Informe seu peso: '))
imc = peso/alturaCm**2

print (f'Seu IMC é: {imc:.1f}')

if (imc <= 18.5 ):
    RESULTADO='baixo peso'

elif (imc < 25 ):
    RESULTADO='Eutrofia (peso adequado)'

elif (imc < 30 ):
    RESULTADO = 'Sobrepeso'

elif (imc < 35 ):
    RESULTADO = 'Obesidade grau I'

elif (imc < 40 ):
    RESULTADO = 'Obesidade grau II'

else:
    RESULTADO = 'Obesidade extrema'
print(RESULTADO)

peso_min = 18.5 * (alturaCm ** 2)
peso_max = 24.9 * (alturaCm ** 2)

print(f"Seu peso ideal fica entre {peso_min:.1f} kg e {peso_max:.1f} kg")





  

