import os
os.system('cls')


#Funcão ler retorno a quantidade de caracteres de uma variavel

nomeCompleto = input ('Informe seu nome completo: ')
print ('1. Quantidade de caracteres: ' , len(nomeCompleto)) #Tamires Perpétua Figueredo Gomes

#.upper transforma um texto em maiúsculo
print ('2. Nome em maiúsculo: ' , nomeCompleto.upper()) 

#.lower transforma um texto em minúsculo
print ('3. Nome em maiúsculo: ' , nomeCompleto.lower()) 

#.title coloca a primeira letra de cada palavra em maiúsculo
print ('4. Nome em maiúsculo: ' , nomeCompleto.title()) 

#.capitalize coloca apenas a primeira letra da frase em maiúsculo
print ('5. Nome em maiúsculo: ' , nomeCompleto.capitalize()) 

#.Separar apenas o 1º nome - utilizar .find e utilizar pra buscar pelo 1º espaço.  
espaco = nomeCompleto.find(' ')
#print (espaco)
print ('6. Somente o primeiro nome: ', nomeCompleto.split()[0])
nome = nomeCompleto [0:espaco]

#Sobrenome = nomeCompleto [espaco+1:len(nomeCompleto)]
#print ('Somente o primeiro nome: ', nome)
#print ('Somente o segundo nome: ', Sobrenome)

#metodo replace para tirar todos os espaços em branco
print('7. Nome sem espaços: ', nomeCompleto.replace(' ',''))

#metodo isalpha para verificar se tem somente letras na palavra
somenteLetras = nomeCompleto.replace(' ','') #temos que tirar os espaços para verificar
print ('8. Tem somente Letras?: ', somenteLetras.isalpha())

#metodo isalnum para verificar se tem letras e numero na palavra
somenteLetras = nomeCompleto.replace(' ','') #temos que tirar os espaços para verificar
print ('9. É alfanumérico?Tem letras ou numeros: ', somenteLetras.isalnum())

#metodo split cria uma lista usando o espaço em branco como quebra 
#Exemplo ['Tamires', 'Perpetua', 'Figeuredo', 'Gomes']
print ('10. Quebrar o texto a cada espaço em branco: ', nomeCompleto.split(" "))

#metodo center para centralizar o texto em 80 colunas usando o *
print ('11. Centralizar o nome entre *: ')
print (nomeCompleto.center (80,"*"))














 

