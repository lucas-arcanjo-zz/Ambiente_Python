#   AULA 6   
print ('Olá, Mundo!');

nome = input('Qual é o seu nome? ')
idade = input ('Qual a sua idade? ')
peso = input ('qual o sue peso? ')

print (nome, idade, peso);

#Exercício 1
nome = input ('Qual é o seu nome? ')
print ('Olá', (nome),', seja muito bem-vindo ! ')

#Exercício 2
dia = input('Dia = ')
mes = input('Mês = ')
ano = input ('Ano = ')
print ('Você nasceu no dia', (dia), 'de', (mes), 'de', (ano), '. Correto?')

#Exercício 03
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = int (n1+n2)
print ('O valor {} e {} soma {}'.format(n1, n2, soma))