#2. Escreva um algoritmo que leia a altura e o peso de uma pessoa e exiba o IMC dela (o IMC é dado por: peso altura2 )

#Exemplo:

#Qual o seu peso e m kil os? 80, 5

#Qual a sua alt ur a e m met r os? 1, 60

#Seu I MC é: 31, 25

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc= peso / altura**2
print('Seu peso é de {} kg, sua altura é de {} m. E o seu IMC é {:.2f}.'.format(peso,altura,imc))
input()# caso seja visulaizado pelo comando do idle.
print('Aluna: Danielle dos Santos Matias.')