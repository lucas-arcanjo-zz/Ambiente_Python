    # Exercicio 5
# Faça um programa que leia um número Inteiro e mostre  na tela o seu sucessor e o seu antecessor.

n1 = int(input('Escreva um número: '))
n2 = n1+1
n3 = n1-1
print ('O Sucessor de {} é {}, e o seu antecessor é {}'.format(n1, n2, n3))

    # Exercicio 6
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n4 = int(input('Digite um número: '))
n5 = n4 * 2 
n6 = n4 * 3 
n7 = n4 **(1/2)
print ('O valor {} possui o dobro de {}, seu triplo de {},\ne sua raiz quadrada é {}'.format(n4, n5, n6, n7))

    #   Exercicio 7
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome = str(input('Digite o nome do aluno(a): '))
n8 = float(input('Digite a primeira nota: '))
n9 = float(input('Digite a segunda nota: '))
n10 = (n8 + n9) / 2

print ('O Aluno {} recebeu a média de {}'.format(nome, n10))

    #   Exercicio 8
# Escreva um programa que leia um valor em metros, e o exiba convertido em centímetros e milímetros.

n11 = int(input('Digite a quantidade de metros: '))
n12 = n11 * 100
n13 = n11 * 1000

print ('O valor de {} metros, convertido em centímetros é: {}\ne o valor convertido em milímetros é: {}'.format(n11, n12, n13))

    #   Exercicio 9
# Faça um programa que leia um número Inteiro qualquer e mostre na tela sua tabuada.

tabuada = int(input('Digite um número: '))
t0 = tabuada * 0
t1 = tabuada * 1
t2 = tabuada * 2
t3 = tabuada * 3
t4 = tabuada * 4
t5 = tabuada * 5
t6 = tabuada * 6
t7 = tabuada * 7 
t8 = tabuada * 8
t9 = tabuada * 9
t10 = tabuada * 10

print ('A tabuada de {} até 10 é:\n{} x 0 = {}\n{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {}'.format(tabuada, tabuada, t0, tabuada, t1, tabuada, t2, tabuada, t3, tabuada, t4, tabuada, t5, tabuada, t6, tabuada, t7, tabuada, t8, tabuada, t9, tabuada, t10))

    #   Exercicio 10
#  Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.  (Considerando o valor do dólar como US 1,00 = 3,27)

reais = int(input('Quantos reais possui?: '))
dolar = reais * 3.27

print ('O valor de {}, convertido em dolar, é {}'.format(reais, dolar))

    # Exercicio 11
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2.

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
soma = largura * altura
area = 2 * soma 

print ('A área possui {} metros quadrado, é necessário {} litros de tinta.'.format(soma, area))

    # Exercicio 12
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com desconto de 5% de desconto.

produto = float(input('Qual é o preço do produto?: '))
desconto = produto * 0.05
produto_desconto = produto - desconto

print ('Com desconto, o valor fica {}'.format(produto_desconto))

    # Exercicio 13
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário do(a) funcionário(a)?: '))
aumento = salario * 0.15
salario_novo = salario + aumento

print ('O aumento do(a) funcionário(a) subiu para {}'.format(salario_novo))

    # Exercicio 28 
    # Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
    # 		O programa deverá escrever na tela se o usuário venceu ou perdeu.

pensar = int(input('Descubra o número que estou pensando de 1 a 5: '))
if pensar == 3:
    print ('Parabéns, você descobriu o número!!')
else:
    print ('Você não acertou o número pensado!!')

    # Exericio 29 
    # Escreva um programa que leia a velocidade de um carro.
    # 	Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.	A multa vai custar R$7,00 por cada km acima do limite.

multa = int(input('Qual foi a velocidade do carro?: '))
calculo_multa = multa - 80 
valor_multa = calculo_multa * 7

if multa > 80:
    print ('Foi ultrapassado o limite de velocidade, você foi multado, o valor da multa é R$ {},00'.format(valor_multa))
else:
    print ('Velocidade conforme as normas')


    # Exercicio 30
    # Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
    
####################impar_ou_par = int(input('Digíte um número: ')
####################if impar_ou_par == x1:
# ##################print ('O número digitado é Impar!')
#####################else:
    #################print ('O númeor digitado é Par!')

    # Exercicio 31
    #  Desenvolva um programa que pergunte a distância de uma viagem de Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de 200Km e R$0,45 para viagens mais longas.
    
    # Exercicio 32
    #  Faça um programa que leia um ano qualquer e mostre-se ele é BISSEXTO.

    # Exercicio 33
    #  Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

    # Exercicio 34
    #  Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.	Para salários superiores a R$1.250,00, calcule um aumento de 10%.
    # 	Para os inferiores ou iguais, o aumento é de 15%.

    # Exercicio 35
    #  Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

    #==============================MUNDO 2==============================#

    #Desafio 036
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestação mensalm sabendo que ela não pode exceder 30% do salário ou entçaio o empréstimo será negado.

casa = float(input('Quanto é o valor da casa? '))
print ('R$ {} mil reias'.format(casa))
salario = float(input('Qual é o seu salário? '))
print ('R$ {},00'.format(salario))
anos = int (input('Quantos anos pretende pagar a casa? '))
print ('{} anos'.format(anos))
parcelas = casa / anos
valor_mensal = parcelas / 12
emprestismo = salario * 0.3 

print ('Para pagar a casa de {} mil reais em {} anos, as parcelas firam no valor de {}, o seu salário chega a {},00'.format(casa, anos, valor_mensal, salario))
if emprestismo > valor_mensal:
    print('Você possui empréstimo bancário !')
else:
    print('Imprestimo Negado')
    
#Desafio 037
#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 hexadecimal

#Desafio 038
#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - 0 primeiro valor é maior
# - 0 segundo valor é maior
# - Não existe valor maior, os dois são iguais

#Desafio 039
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.

#Seu programa também deverá mostrar o tempo que falta ou que passou o prazo.

#Desafio 040
#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

#Desafio 041
#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

#Desafio 042
#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# Equilátero: todos os lados iguais.
# Isósceles: dois lados iguais.
# Escaleno: todos os lados diferentes

#Desafio 043
#Desenvolva uma lógica de leia o peso e a altura de uma pessoa, calculce seu IMC e mostre seu status, de acordo com a tabela abaixo:

# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

#Desafio 044
#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

#Desafio 045
#Crie um programa que faça o computador jogar Jokenpô com você.

#Desafio 46
#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
from emoji import 
nome = str(input('Qual é o seu nome? '))
print ('{}, se prepare com a contagem dos fogos!!!'.format(nome))

for c in range(10,-1,-1):
    sleep(1.5)
    print(c)
print ('BUM, BUM, POOOW!')

##Desafio 047
#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for c in range (2, 51, 2):
    print(c, end=' ')   
print ('ACABOU')

#Desafio 057
#Faça um programa que leia o sexo de uma pessoa, mas só aceito os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.' 

#Desafio 058
#Melhore o jogo Desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

"""Desafio 059
Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multilpicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em casa caso."""
