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