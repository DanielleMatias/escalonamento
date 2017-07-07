#4. Leia a idade de uma pessoa e diga se ele é menor maior ou idoso.
idade = int(input('Digite sua idade: '))
if idade < 18:
    print('Você tem {} anos por isso é de menor.'.format(idade))
elif (idade >= 18) and (idade <= 64):
    print('Você tem {} anos por isso é de maior.'.format(idade))
else:
    print('Você tem {} anos por isso  é considerado um idoso, mais con certeza essa é a melhor idade. '.format(idade))

input()# caso seja visulaizado pelo comando do idle
print('Aluna: Danielle dos Santos Matias.')