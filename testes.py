#Desafio 036
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = int(input('Quanto é o valor da casa? '))
print ('R$ {} mil reias'.format(casa))
salario = int(input('Qual é o seu salário? '))
print ('R$ {},00'.format(salario))
anos = int (input('Quantos anos pretende pagar a casa? '))
print ('{} anos'.format(anos))
parcelas = casa / anos
valor_mensal = parcelas / 12
emprestismo = salario * 0.3 
print ('Para pagar a casa de {} mil reais em {} anos, as parcelas firam no valor de {}, o seu salário chega a {},00'.format(casa, anos, parcelas, salario))
if emprestismo > valor_mensal:
    print('Você possui empréstimo bancário !')
else:
    print('Imprestimo Negado')