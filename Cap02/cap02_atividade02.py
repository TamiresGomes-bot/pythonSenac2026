
"""Receber a entrada de dois valores  correspondentes aos lados de um retangulo em cm e realizar o calculo da area de um retangulo, multiplique o lado A pelo lado B
+ soma ; - subtração ; * multiplicação ; / divisão."""


import os
os.system('cls')


print ('Calculo da área do Retângulo')
num1 = input ('Informe o valor da base do retângulo: ')
num2 = input ('Informe o valor da altura do retângulo: ')

num1 = int (num1)
num2 = int (num2)
print('A área do retângulo com base', num1, 'e altura', num2, 'é igual a:', num1 * num2)

#segunda forma

lado_A = int(input('Informe a altura do retângulo: '))
lado_B = int(input('Informe a base do retângulo: '))
area = lado_A * lado_B
print ( 'A área do retângulo com lados: ', lado_A , 'e ', lado_B ,'é', area)


